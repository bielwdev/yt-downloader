from pytube import YouTube
import os

def download_video_1080p(url):
    try:
        yt = YouTube(url)
        title = yt.title
        sanitized_title = title.replace(" ", "_").replace("/", "_").replace("|", "").replace("ã", "a")

        video_stream = yt.streams.filter(res="1080p", file_extension='mp4', progressive=False).first()
        
        if not video_stream:
            print("Stream de vídeo em 1080p não disponível.")
            return None

        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()

        if not audio_stream:
            print("Stream de áudio não disponível.")
            return None

        video_path = video_stream.download(filename=f'{sanitized_title}_video.mp4')
        audio_path = audio_stream.download(filename=f'{sanitized_title}_audio.mp4')

        output_path = f'{sanitized_title}.mp4'

        ffmpeg_cmd = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{output_path}"'

        os.system(ffmpeg_cmd)

        os.remove(video_path)
        os.remove(audio_path)

        print(f'Download concluído: {title}')
        return "1080p"
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        return None

if __name__ == "__main__":
    url = input('Digite a URL do vídeo do YouTube: ')
    resolution = download_video_1080p(url)

    if resolution:
        print(f'O vídeo foi baixado na resolução {resolution}.')
