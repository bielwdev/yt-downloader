import yt_dlp

def ytdownloader(url):
    try:
        ydl_opts = {
            'merge_output_format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
            'concurrent_fragments': 8,
            'throttled-rate': 0,
            'external_downloader_args': ['-multi_thread', '-threads', '0'],
            'quiet': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print('Download completed.')
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

# Example usage
url = input('Enter the URL of the YouTube video: ')
ytdownloader(url)
