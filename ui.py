from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
)
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
        self.setStyleSheet("background-color: #1b0f3a; color: #d7bde2;")

        # Поле ввода и метка
        self.label_title = QLabel("Enter listening time (in seconds):", self)
        self.label_title.setFont(QFont("Inria Sans", 20))
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.move(260, 90)

        self.entry = QLineEdit(self)

        self.entry.setFixedSize(225, 50)
        self.entry.actions()
        self.entry.setFont(QFont("Inria Sans", 16))
        self.entry.setPlaceholderText("Some number...")

        self.entry.setStyleSheet(
            "background-color: #331b54; color: #d7bde2; border-radius: 15px; padding: 5px;"
        )



        # Кнопка сохранения
        self.btn_save = QPushButton("Save listening time", self)
        self.btn_save.setFont(QFont("Inria Sans", 12))
        self.btn_save.setStyleSheet(
            "background-color: #4c2b8e; color: white; border-radius: 10px;"
        )
        self.btn_save.clicked.connect(lambda: save_listening_time(self.entry))

        # Разделительная линия
        self.separator = QLabel(self)
        self.separator.setFixedHeight(2)
        self.separator.setStyleSheet("background-color: #d7bde2;")

        # Кнопка включения распознавания речи
        self.btn_enable = QPushButton("Enable speech recognition", self)
        self.btn_enable.setFont(QFont("Inria Sans", 12))
        self.btn_enable.setStyleSheet(
            "background-color: #4c2b8e; color: white; border-radius: 10px;"
        )
        self.btn_enable.clicked.connect(lambda: enable_speech_recognition(self.entry))

        # Инструкция
        self.label_instruction = QLabel(
            "(You can also enable speech recognition by pressing ctrl + f6)", self
        )
        self.label_instruction.setFont(QFont("Inria Sans", 10))
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Макеты
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.label_title)
        main_layout.addWidget(self.entry)
        main_layout.addWidget(self.btn_save)
        main_layout.addWidget(self.separator)
        main_layout.addWidget(self.btn_enable)
        main_layout.addWidget(self.label_instruction)

        self.setLayout(main_layout)
