import random
import sys

import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class GuessTheNumberGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guess the Number")
        self.setMinimumWidth(200)
        self.setMinimumHeight(100)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        INSTALL_DIRECTORY = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(INSTALL_DIRECTORY, "icon.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.message_label = QLabel("Guess a number between 1 and 100:")
        self.input_line = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_guess)

        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        layout.addWidget(self.input_line)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_guess(self):
        guess = int(self.input_line.text())
        self.attempts += 1

        if guess == self.secret_number:
            self.message_label.setText(f"Congratulations! You guessed the number in {self.attempts} attempts.")
            self.input_line.setReadOnly(True)
            self.submit_button.setEnabled(False)
        elif guess < self.secret_number:
            self.message_label.setText("Too low! Try again.")
        else:
            self.message_label.setText("Too high! Try again.")


if __name__ == "__main__":
    app = QApplication([])
    game = GuessTheNumberGame()
    game.show()
    app.exec()
