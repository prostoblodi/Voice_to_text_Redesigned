import sys
from PyQt6.QtWidgets import QApplication
from ui import VoiceToTextApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceToTextApp()
    window.show()
    sys.exit(app.exec())
