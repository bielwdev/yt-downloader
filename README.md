# YouTube Video Downloader Script

This personal repository is designed for downloading YouTube videos at the highest available resolution. It combines both audio and video into a single MP4 file using the `yt_dlp` library.

## Requirements

- Python 3.x
- Python Libraries: `yt_dlp`
- FFmpeg (version 7.x.x or higher is highly recommended for 4K video support)

## Installation

1. **Install Dependencies**:

   You can install the dependencies using `pip`:

   ```bash
   pip install yt-dlp
   ```

   **Note**: Ensure that `ffmpeg` is installed on your system. Follow the instructions on [FFmpeg - Official Website](https://ffmpeg.org/download.html) to install it. It is highly recommended to use FFmpeg version 7.x.x or higher for better support, including 4K video downloads.

2. **Install `ffmpeg`**:

   **On Windows**:

   1. Go to the [FFmpeg download page](https://ffmpeg.org/download.html).
   2. Click on “Windows” and then on “Windows builds by BtbN”.
   3. Download the latest ZIP file.
   4. Extract the ZIP file to a directory, e.g., `C:\ffmpeg`.
   5. Add the `bin` directory path (e.g., `C:\ffmpeg\bin`) to your system PATH:
      - Right-click on “This PC” or “My Computer” and select “Properties”.
      - Click on “Advanced system settings” and then on “Environment Variables”.
      - In the “System variables” section, find the `Path` variable and click “Edit”.
      - Add the path to the `bin` folder of `ffmpeg` (e.g., `C:\ffmpeg\bin`) and click “OK”.

   **On Linux**:

   1. Open a terminal.
   2. Update your system repositories and install `ffmpeg` with the following command:

      ```bash
      sudo apt update
      sudo apt install ffmpeg
      ```

   3. Verify that `ffmpeg` was installed correctly by running:

      ```bash
      ffmpeg -version
      ```

3. **Clone the Repository**:

   Clone the repository containing the script from GitHub:

   ```bash
   git clone https://github.com/bielwdev/yt-downloader.git
   ```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the `ytdownloader.py` file is located.
3. Run the script with the command:

   ```bash
   python ytdownloader.py
   ```

4. When prompted, enter the URL of the YouTube video you want to download and press Enter.

The script will download the video in max resolution available and the audio in MP4 format, combine both using `ffmpeg`, and save the result in the same directory with the video title as the filename.

## Notes

- `ffmpeg` must be correctly installed and configured on your system for the script to work. Ensure that the `ffmpeg` executable is in your PATH.
- It is highly recommended to use FFmpeg version 7.x.x or higher to support 4K video downloads.
- The resulting file name will be based on the video title, with special characters replaced to avoid file naming issues.

---
