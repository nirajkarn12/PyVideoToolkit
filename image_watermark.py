from pyffmpeg import FFmpeg


ff = FFmpeg()

# Define input video, watermark image, and output video paths
input_video = r'C:\Users\niraz\PycharmProjects\image_watermark\video2.mp4'
watermark_image = r'C:\Users\niraz\PycharmProjects\image_watermark\miracle.png'
output_video = r'C:\Users\niraz\PycharmProjects\image_watermark\output.mp4'

overlay_position = "(W-w)/2:(H-h)/2"


options_result = ff.options(
    f'-y -i "{input_video}" -i "{watermark_image}" -filter_complex "overlay={overlay_position}" "{output_video}"'
)


if options_result:
    print("Watermark applied successfully.")
else:
    print("Error applying options.")
