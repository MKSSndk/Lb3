import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Крестики-Нолики")
        self.setGeometry(100, 100, 300, 300)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.init_ui()
