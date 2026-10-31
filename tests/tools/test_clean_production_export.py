"""Real offline render/export coverage for the clean production contract.

Detects injected overlays, appended promotional metadata, lost attribution,
and export-time media changes. No provider calls or fabricated MP4 files.
"""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from schemas.artifacts import validate_artifact
from tools.audio.audio_mixer import AudioMixer
from tools.publishers.export_bundle import ExportBundle
from tools.video.video_compose import VideoCompose


pytestmark = pytest.mark.skipif(
    not shutil.which("ffmpeg") or not shutil.which("ffprobe"),
    reason="ffmpeg and ffprobe are required for the offline production test",
)


def _run(*args: str) -> bytes:
    return subprocess.run(
        args, check=True, capture_output=True, timeout=30,
    ).stdout


@pytest.fixture(scope="module")
def local_render(tmp_path_factory):
    project = tmp_path_factory.mktemp("clean-production")
    assets = project / "assets"
    assets.mkdir()
    source = assets / "source.mp4"
    speech = assets / "speech.wav"
    music = assets / "music.wav"
    _run(
        "ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
        "color=c=teal:s=320x180:d=2:r=30", "-c:v", "libx264",
        "-pix_fmt", "yuv420p", str(source),
    )
    for path, frequency in ((speech, 440), (music, 220)):
        _run(
            "ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
            f"sine=frequency={frequency}:duration=2", str(path),
        )

    mixed = AudioMixer().execute({
        "operation": "full_mix",
        "tracks": [
            {"path": str(speech), "role": "speech"},
            {"path": str(music), "role": "music"},
        ],
        "ducking": {"enabled": True},
        "normalize": False,
        "target_duration": 2,
        "output_path": str(assets / "mix.wav"),
    })
    assert mixed.success, mixed.error

    final = project / "renders" / "final.mp4"
    rendered = VideoCompose().execute({
        "operation": "compose",
        "edit_decisions": {
            "version": "1.0",
            "render_runtime": "ffmpeg",
            "cuts": [{
                "id": "c1", "source": str(source),
                "in_seconds": 0, "out_seconds": 2,
            }],
            "metadata": {"compose_target": {"width": 320, "height": 180}},
        },
        "audio_path": str(assets / "mix.wav"),
        "output_path": str(final),
        "preset": "ultrafast",
    })
    assert rendered.success, rendered.error
    assert final.is_file()
    return final


@pytest.mark.parametrize("description", [
    "A lesson about how light scatters in the atmosphere.",
    "A lesson about light. Required credit: Example Author, CC BY 4.0, "
    "https://creativecommons.org/licenses/by/4.0/",
])
def test_local_render_and_export_preserve_only_requested_content(
    local_render, tmp_path, description,
):
    result = ExportBundle().execute({
        "video_path": str(local_render),
        "title": "How Light Scatters",
        "description": description,
        "export_dir": str(tmp_path / "exports"),
        "chapters": [{"start_seconds": 0, "title": "Light and air"}],
    })
    assert result.success, result.error
    validate_artifact("publish_log", result.data["publish_log"])
    root = Path(result.data["export_path"])
    exported = root / "video" / "output.mp4"
    assert exported.read_bytes() == local_render.read_bytes()

    # Exact output contract catches any appended CTA/URL while retaining
    # an explicitly supplied legal attribution link without filtering it.
    metadata = json.loads((root / "metadata" / "metadata.json").read_text())
    assert metadata == {
        "title": "How Light Scatters",
        "description": description,
        "tags": [], "hashtags": [],
        "chapters": [{"start_seconds": 0, "title": "Light and air"}],
    }
    assert (root / "metadata" / "description.txt").read_text() == (
        description + "\n\n0:00 - Light and air\n"
    )
    entry = result.data["publish_log"]["entries"][0]
    assert entry["metadata_used"]["description"] == description
    assert not entry.get("url")

    probe = json.loads(_run(
        "ffprobe", "-v", "error", "-show_streams", "-show_format",
        "-of", "json", str(exported),
    ))
    assert {stream["codec_type"] for stream in probe["streams"]} == {"video", "audio"}
    assert float(probe["format"]["duration"]) == pytest.approx(2, abs=0.1)
    assert "http" not in json.dumps(probe).lower()

    # Decode every frame: the approved source is solid teal. Any automatic
    # logo, text banner, intro, or end card would change these pixels.
    frames = _run(
        "ffmpeg", "-v", "error", "-xerror", "-i", str(exported),
        "-map", "0:v:0", "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1",
    )
    frame_size = 320 * 180 * 3
    assert len(frames) % frame_size == 0
    # Audio muxing can retain one extra frame at the AAC packet boundary.
    assert len(frames) // frame_size == pytest.approx(60, abs=1)
    for channel, expected in enumerate((0, 128, 128)):
        values = frames[channel::3]
        assert max(values) - min(values) <= 4
        assert sum(values) / len(values) == pytest.approx(expected, abs=5)
    _run("ffmpeg", "-v", "error", "-xerror", "-i", str(exported), "-f", "null", "-")
