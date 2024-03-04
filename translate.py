from googletrans import Translator
from gtts import gTTS
import os

# Функция для перевода текста с русского на английский
def translate_text(input_text):
    translator = Translator()
    translated_text = translator.translate(input_text, src='ru', dest='en')
    return translated_text.text

# Функция для озвучивания текста на английском языке
def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

# Чтение текста из файла
input_file = "recognized_text.txt"
with open(input_file, "r", encoding="utf-8") as file:
    input_text = file.read()

# Перевод текста на английский
translated_text = translate_text(input_text)

# Сохранение переведенного текста в файл
translated_file = "translated_text.txt"
with open(translated_file, "w", encoding="utf-8") as file:
    file.write(translated_text)

# Озвучивание переведенного текста и сохранение аудиофайла
output_audio_file = "translated_audio.mp3"
text_to_speech(translated_text, output_audio_file)
print(f"Translated audio saved to {output_audio_file}")
