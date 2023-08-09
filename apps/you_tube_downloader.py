from pytube import YouTube
import random
import string
import os
import shutil

def download_audio(url, video_title, folder):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only(subtype='mp4')
    os.makedirs(folder, exist_ok=True)
    stream.download(output_path=folder, filename=f'{video_title}.mp3')


def download_video(url, video_title, folder):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').get_by_resolution('720p')
    os.makedirs(folder, exist_ok=True)
    stream.download(output_path=folder, filename=f'{video_title}.mp4')


def download(file, url, folder):
    try:
        video = YouTube(url)
        video_duration = video.length
        if video_duration > 3600:
            print("Відео занадто довге")
        else:
            video_author = video.author
            video_title = video.title
            
            text = f"*Автор відео: {video_author}*\n"
            text += f"*Назва відео: {video_title}*"
            
            try:
                if file == "video":
                    type_ = ".mp4"
                    download_video(url, video_title, folder)
                elif file == "audio":
                    type_ = ".mp3"
                    download_audio(url, video_title, folder)
                status = True
            except:
                try:
                    if type_ == ".mp3":
                        video_title = "audio"
                    else:
                        video_title = "video"
                        
                    if file == "video":
                        type_ = ".mp4"
                        download_video(url, video_title, folder)
                    elif file == "audio":
                        type_ = ".mp3"
                        download_audio(url, video_title, folder)
                    
                    status = True
                except:
                    video_title = ""
                    status = False
                    text = ""
    except Exception as e:
        video_title = ""
        status = False
        text = str(e)
    
    return video_title, status, text