import os
import tempfile
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment

# Путь к видеофайлу
video_path = "video.mp4"

# Загрузка видеофайла
video_clip = mp.VideoFileClip(video_path)

# Извлечение аудиодорожки из видео
audio_path = os.path.join(tempfile.gettempdir(), "temp_audio.wav")
video_clip.audio.write_audiofile(audio_path, fps=44100)

# Инициализация объекта recognizer
recognizer = sr.Recognizer()

# Функция для распознавания речи в аудиофайле
def recognize_speech(audio_data):
    try:
        text = recognizer.recognize_google(audio_data, language="ru-RU")
        return text
    except Exception as e:
        print(f"Recognition error: {e}")
        return None

# Функция для сохранения текста в текстовом файле
def save_text_to_file(text, file_path):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + '\n')

# Разделение аудиофайла на 10 частей и распознавание каждой части
output_file_path = "recognized_text.txt"
audio = AudioSegment.from_wav(audio_path)
duration = len(audio)
segment_duration = duration // 10

for i in range(10):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    audio_segment = audio[start_time:end_time]
    audio_segment.export(os.path.join(tempfile.gettempdir(), "temp_segment.wav"), format="wav")
    with sr.AudioFile(os.path.join(tempfile.gettempdir(), "temp_segment.wav")) as source:
        audio_data = recognizer.record(source)
        text = recognize_speech(audio_data)
        if text:
            print(f"Segment {i + 1} recognition successful:")
            print(text)
            save_text_to_file(text, output_file_path)
        else:
            print(f"Segment {i + 1} recognition failed.")

print(f"Всё збс, сохранил все здесь - {output_file_path}")
