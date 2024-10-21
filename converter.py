from moviepy.editor import VideoFileClip


def convert_to_webm(input_video_path, output_video_path):
    try:
        # Load the video file
        video = VideoFileClip(input_video_path)

        # Write the video file to the specified output path in WEBM format
        video.write_videofile(output_video_path, codec='libvpx')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the video is closed if it was successfully opened
        if 'video' in locals():
            video.close()


# Example usage
input_video_path = r'C:\Users\niraz\PycharmProjects\image_watermark\video2.mp4'
output_video_path = r'C:\Users\niraz\PycharmProjects\image_watermark\output_video.webm'

convert_to_webm(input_video_path, output_video_path)

