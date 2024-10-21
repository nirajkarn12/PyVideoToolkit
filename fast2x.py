from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

def fast_video(video_path, output_path, factor=2.0):
    video = VideoFileClip(video_path)
    fast_video = video.fx(vfx.speedx, factor)
    fast_video.write_videofile(output_path)
    video.close()


# Path to the input video and output videos
video_path = "video2.mp4"
output_path_fast = "fast_path.mp4"

# Apply  fast motion effects
fast_video(video_path, output_path_fast, factor=2.0)  
