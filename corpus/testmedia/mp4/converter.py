# Convert mp4 to yuv

import os

def convert_to_yuv(input_file, output_file):
    command = f"ffmpeg -i {input_file} -c:v rawvideo -pixel_format yuv420p {output_file}"
    os.system(command)

def batch_convert_to_yuv(input_dir, output_dir):
    print(f"batch_convert_to_yuv({input_dir}, {output_dir})")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace(".mp4", ".yuv"))
            convert_to_yuv(input_file, output_file)

if __name__ == "__main__":
    input_dir = "."
    output_dir = "../"
    batch_convert_to_yuv(input_dir, output_dir)
