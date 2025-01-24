from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from functions import save_listening_time, enable_speech_recognition

class VoiceToTextApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("VTT.py")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #1b0f3a; color: #C8ACD6;")  # Цвет фона и текста

        # Поле ввода и метка
        self.label_title = QLabel("Enter listening time (in seconds):", self)
        self.label_title.setFont(QFont("Inria Sans", 20))
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setGeometry(200, 40, 400, 40)  # Расположим метку в верхней части экрана

        self.entry = QLineEdit(self)
        self.entry.setGeometry(245, 115, 310, 60)  # Позиция и размер поля ввода
        self.entry.setFont(QFont("Inria Sans", 16))
        self.entry.setPlaceholderText("Some number...")
        self.entry.setStyleSheet(
            "background-color: #331b54; color: #C8ACD6; border-radius: 15px; padding: 5px;"
        )

        # Кнопка сохранения
        self.btn_save = QPushButton("Save listening time", self)
        self.btn_save.setFont(QFont("Inria Sans", 20))
        self.btn_save.setStyleSheet(
            "background-color: #4c2b8e; color: #C8ACD6; border-radius: 10px;"
        )
        self.btn_save.setGeometry(250, 200, 300, 70)  # Позиция и размер кнопки
        self.btn_save.clicked.connect(lambda: save_listening_time(self.entry))

        # Разделительная линия
        self.separator = QLabel(self)
        self.separator.setFixedHeight(10)
        self.separator.setStyleSheet("background-color: #d7bde2;")
        self.separator.setGeometry(0, 300, 800, 2)  # Разделительная линия

        # Кнопка включения распознавания речи
        self.btn_enable = QPushButton("Enable speech recognition", self)
        self.btn_enable.setFont(QFont("Inria Sans", 20))
        self.btn_enable.setStyleSheet(
            "background-color: #4c2b8e; color: #C8ACD6; border-radius: 10px;"
        )
        self.btn_enable.setGeometry(225, 330, 350, 70)  # Позиция и размер кнопки
        self.btn_enable.clicked.connect(lambda: enable_speech_recognition(self.entry))

        # Инструкция
        self.label_instruction = QLabel(
            "(You can also enable speech recognition by pressing ctrl + f6)", self
        )
        self.label_instruction.setFont(QFont("Inria Sans", 10))
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_instruction.setGeometry(200, 400, 400, 30)  # Позиция и размер инструкции

        self.show()
