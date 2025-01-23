from PyQt6.QtWidgets import QLineEdit
from threading import Thread
from speech_recognition import Recognizer, Microphone

def save_listening_time(entry: QLineEdit):
    """
    Функция для сохранения времени прослушивания.
    """
    time = entry.text()
    if time.isdigit():
        print(f"Listening time saved: {time} seconds")
    else:
        print("Invalid input! Please enter a numeric value.")

def enable_speech_recognition(entry: QLineEdit):
    """
    Запускает процесс распознавания речи в отдельном потоке.
    """
    recognition_thread = Thread(target=start_speech_recognition, args=(entry,))
    recognition_thread.start()

def start_speech_recognition(entry: QLineEdit):
    """
    Распознавание речи с использованием библиотеки `speech_recognition`.
    """
    try:
        r = Recognizer()
        duration = int(entry.text())
        with Microphone() as source:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source)
            print(f"Listening for {duration} seconds...")
            audio = r.record(source, duration=duration)
            print("Recognizing speech...")
            text = r.recognize_google(audio, language="en")
            print(f"Recognized text: {text}")
    except ValueError:
        print("Please enter a valid number for listening time.")
    except Exception as e:
        print(f"Error during recognition: {e}")
