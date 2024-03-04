import os
import tempfile
import moviepy.editor as mp
from gtts import gTTS

# Функция для синтеза речи с настройками параметров
def synthesize_speech(text, filename):
    try:
        tts = gTTS(text=text, lang='en')
        temp_audio_path = os.path.join(tempfile.gettempdir(), filename)
        tts.save(temp_audio_path)
        return temp_audio_path
    except Exception as e:
        print(f"Speech synthesis error: {e}")
        return None

# Функция для дублирования видеоконтента с озвучкой
def duplicate_video(video_path, audio_path):
    try:
        # Загрузка видеофайла
        video_clip = mp.VideoFileClip(video_path)

        # Загрузка аудиофайла
        audio_clip = mp.AudioFileClip(audio_path)

        # Наложение аудио на видео и сохранение результата
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile('duplicated_video.mp4', codec='libx264', audio_codec='aac')
    except Exception as e:
        print(f"Duplication error: {e}")

# Путь к видеофайлу
video_path = "video_1.mp4"

# Текст для синтеза
text = "This is a sample text for synthesis."

# Синтез речи с настройками параметров
audio_path = synthesize_speech(text, "temp_voice.mp3")

if audio_path:
    print("Speech synthesis successful.")

    # Дублирование видео с озвучкой
    duplicate_video(video_path, audio_path)
