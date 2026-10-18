import subprocess
from pathlib import Path
from django.conf import settings

from .models import Video

def process_video(video_id):
    video=Video.objects.get(id=video_id)

    if not video.video_file:
        raise ValueError("This video has no uploaded file.")

    video.status= "processing"
    video.save(update_fields=["status"])

    output_dir = (
        Path(settings.MEDIA_ROOT) / "hls" / str(video.id)
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    playlist_path = output_dir / "index.m3u8"
    segment_pattern = output_dir / "segment_%03d.ts"

    command = [
        "ffmpeg",
        "-y",
        "-i", video.video_file.path,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-hls_time", "6",
        "-hls_playlist_type", "vod",
        "-hls_segment_filename", str(segment_pattern),
        str(playlist_path),
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True,)
        video.hls_playlist = ( f"hls/{video.id}/index.m3u8")
        video.status = "ready"
        video.save(update_fields=["hls_playlist", "status"])

    except (subprocess.CalledProcessError, OSError):
        video.status = "failed"
        video.save(update_fields=["status"])
        raise
    
