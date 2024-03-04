import moviepy.editor as mp

# Пути к оригинальному видео и аудиодорожке
video_path = "video.mp4"
audio_path = "translated_audio.mp3"

# Загрузка оригинального видео и аудиодорожки
video_clip = mp.VideoFileClip(video_path)
audio_clip = mp.AudioFileClip(audio_path)

# Настройка громкости аудиодорожки
audio_clip = audio_clip.volumex(1.0)  # Громкость аудиодорожки 100%
video_clip = video_clip.volumex(0.3)   # Громкость оригинального видео 30%

# Наложение аудиодорожки на видео
final_clip = video_clip.set_audio(audio_clip)

# Сохранение видео с аудиодорожкой
output_path = "final_video.mp4"
final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
print(f"Final video saved to {output_path}")
