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



    def init_ui(self):
        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda _, r=row, c=col: self.make_move(r, c))
                self.grid_layout.addWidget(button, row, col)
                self.board[row][col] = button

    def make_move(self, row, col):
        button = self.board[row][col]
        if button.text() == "":
            button.setText(self.current_player)
            if self.check_winner():
                QMessageBox.information(self, "Победа", f"Игрок {self.current_player} выиграл!")
                self.reset_game()
            elif self.is_draw():
                QMessageBox.information(self, "Ничья", "Ничья!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Проверка строк и столбцов
        for i in range(3):
            if all(self.board[i][j].text() == self.current_player for j in range(3)):
                return True
            if all(self.board[j][i].text() == self.current_player for j in range(3)):
                return True

        # Проверка диагоналей
        if all(self.board[i][i].text() == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2 - i].text() == self.current_player for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(self.board[row][col].text() != "" for row in range(3) for col in range(3))

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col].setText("")
        self.current_player = "X"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
