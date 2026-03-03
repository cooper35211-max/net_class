
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("PyQt6 Test")
    window.setGeometry(100, 100, 280, 100) # x, y, width, height

    label = QLabel("Hello, PyQt6!", parent=window)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setGeometry(0, 0, 280, 100) # Make label fill the window

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
