import cv2
import os

def extract_frames(video_path, output_dir, frame_interval=1):
    """
    Extract frames from a video and save them as JPG images.
    
    Parameters:
    video_path (str): Path to the video file
    output_dir (str): Directory to save the extracted frames
    frame_interval (int): Extract a frame every 'frame_interval' frames
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return
    
    # Get video information
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    
    print(f"Video has {frame_count} frames at {fps} fps")
    
    # Read and save frames
    frame_number = 0
    saved_count = 0
    
    while True:
        # Read the next frame
        success, frame = video.read()
        
        if not success:
            # End of video
            break
        
        # Save frame at specified intervals
        if frame_number % frame_interval == 0:
            frame_filename = os.path.join(output_dir, f"frame_{saved_count:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1
            
            if saved_count % 100 == 0:
                print(f"Saved {saved_count} frames")
        
        frame_number += 1
    
    # Release the video file
    video.release()     
    
    print(f"Completed! Total frames saved: {saved_count}")

# Example usage
if __name__ == "__main__":
    video_path = r"C:\Users\karti\Downloads\10mm-08-04-25\20250408_031646.mp4"  # Replace with your video path
    output_dir = r'C:\Users\karti\Downloads\10mm-08-04-25\extracted_frames_4'        # Replace with your desired output directory
    extract_frames(video_path, output_dir, frame_interval=10)  # Extract 1 frame per second for a 24fps video 