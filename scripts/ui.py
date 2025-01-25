from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from scripts.functions import save_listening_time, enable_speech_recognition

class VoiceToTextApp(QWidget):
    def __init__(self):
        super().__init__()
        self.label_instruction = None
        self.btn_enable = None
        self.separator = None
        self.btn_save = None
        self.entry = None
        self.label_title = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("VTT.py")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #17153B; color: #C8ACD6;")  # Цвет фона и текста

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
            "background-color: #2E236C; color: #C8ACD6; border-radius: 15px; padding: 15px;"
        )

        # Кнопка сохранения
        self.btn_save = QPushButton("Save listening time", self)
        self.btn_save.setFont(QFont("Inria Sans", 20))
        self.btn_save.setStyleSheet(
            "background-color: #3D2F8C; color: #C8ACD6; border-radius: 20px;"
        )
        self.btn_save.setGeometry(250, 200, 300, 70)  # Позиция и размер кнопки
        self.btn_save.clicked.connect(lambda: save_listening_time(self.entry))

        # Прямая линия с округленными концами от (100, y) до (400, y)
        self.separator = QFrame(self)
        self.separator.setGeometry(150, 300, 450, 10)  # Начало на 100, конец на 400
        self.separator.setStyleSheet(
            "background-color: #C8ACD6; border-radius: 5px;"  # Цвет линии с округлыми концами
        )

        # Кнопка включения распознавания речи
        self.btn_enable = QPushButton("Enable speech recognition", self)
        self.btn_enable.setFont(QFont("Inria Sans", 20))
        self.btn_enable.setStyleSheet(
            "background-color: #3D2F8C; color: #C8ACD6; border-radius: 20px;"
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