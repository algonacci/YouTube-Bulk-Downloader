from pytube import YouTube
import os

def download_video(url, output_path, index):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_extension = stream.mime_type.split("/")[-1]
        filename = f"{index:02d}_{yt.title}.{file_extension}"
        filepath = os.path.join(output_path, filename)
        print(f"Downloading video {index:02d}: {yt.title}")
        stream.download(output_path, filename=filename)
        print(f"Download of '{yt.title}' completed successfully.")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_videos_from_file(file_path, output_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for index, url in enumerate(urls, start=1):
            url = url.strip()
            if url:
                download_video(url, output_path, index)

if __name__ == "__main__":
    file_path = "video_urls.txt"
    output_path = "./videos/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    download_videos_from_file(file_path, output_path)
