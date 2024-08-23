import os
import imageio.v2 as imageio

EF = "Euler's Forward"
EB = "Euler's Backward"
RK4 = "Runge-Kutta 4"

method = RK4
varied = "Varied b"
const = "a=0.5"

# Define the base path using relative paths
base_path = os.path.join('..', '..', '..', 'Graphs', 'Stability Regions', 'Videos')

# Define the frames directory and the output video path using relative paths
frames_dir = os.path.join(base_path, varied, method, const, 'frames')
output_video_path = os.path.join(base_path, varied, method, const, 'video.mp4')

# Ensure the frames directory exists
if not os.path.exists(frames_dir):
    raise ValueError(f"The frames directory {frames_dir} does not exist.")

# Create the video writer
with imageio.get_writer(output_video_path, fps=30) as writer:
    # Iterate through the frames in the directory
    for frame_number in sorted(os.listdir(frames_dir)):
        # Construct the full path to the frame
        frame_path = os.path.join(frames_dir, frame_number)
        # Read and append the frame to the video
        image = imageio.imread(frame_path)
        writer.append_data(image)

print(f"Video created successfully at {output_video_path}")
