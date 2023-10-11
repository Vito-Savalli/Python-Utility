import os
import subprocess

def convert_mov_to_webm(file_path, output_path):
    # Command for conversion using ffmpeg
    command = [
        'ffmpeg',
        '-i', file_path,
        '-c:v', 'libvpx-vp9',
        '-b:v', '1M',
        '-c:a', 'libopus',
        '-b:a', '100K',
        output_path
    ]

    subprocess.run(command, check=True)

def main():
    # Path to the files on your desktop
    desktop_path = os.path.expanduser('~/Desktop')
    
    # List all the files on the desktop
    files_on_desktop = os.listdir(desktop_path)

    # Filter for .mov and .mp4 files
    mov_and_mp4_files = [f for f in files_on_desktop if f.endswith('.mov') or f.endswith('.mp4')]

    if not mov_and_mp4_files:
        print("No .mov or .mp4 files found on the desktop.")
        return

    for file_name in mov_and_mp4_files:
        file_path = os.path.join(desktop_path, file_name)
        output_path = os.path.join(desktop_path, f"{os.path.splitext(file_name)[0]}.webm")
        convert_mov_to_webm(file_path, output_path)
        print(f"Conversion complete for {file_name}! File saved at: {output_path}")

if __name__ == "__main__":
    main()
