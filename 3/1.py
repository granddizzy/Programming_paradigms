class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        print("  1   2   3")  # Заголовок для столбцов
        for i, row in enumerate(self.board):
            print(f"{i + 1} " + " | ".join(row))  # Добавляем номер строки
            if i < 2:  # Разделители только между строками
                print("  " + "-" * 9)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def is_draw(self):
        # функция all принимает генератор который выдает заполнена клетка или нет, и проверяет что все истина
        return all(cell != " " for row in self.board for cell in row)

    def make_move(self, row, col):
        self.board[row][col] = self.current_player

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        self.print_board()  # Вывод начальной доски
        while True:
            print(f"Ходит игрок {self.current_player}.")
            row, col = None, None

            # Проверяем ввод пользователя
            while True:
                user_input = input("Введите строку и столбец через пробел (1-3) или 'exit' для выхода: ")
                if user_input.lower() == "exit":
                    print("Выход из игры...")
                    return  # Завершаем игру

                try:
                    # Проверка: ввод двух чисел через пробел
                    row, col = map(int, user_input.split())
                except ValueError:
                    print("Некорректный ввод! Убедитесь, что вы ввели два числа через пробел.")
                    continue

                # Проверка: диапазон значений
                if not (1 <= row <= 3 and 1 <= col <= 3):
                    print("Координаты вне диапазона! Введите числа от 1 до 3.")
                    continue

                # Преобразуем координаты к 0-индексации
                row -= 1
                col -= 1

                # Проверка: клетка не занята
                if self.board[row][col] != " ":
                    print("Эта клетка уже занята! Попробуйте снова.")
                    continue

                break

            # Совершаем ход
            self.make_move(row, col)
            self.print_board()  # Печать доски после хода

            # Проверка на победу или ничью
            winner = self.check_winner()
            if winner:
                print(f"Игрок {winner} победил!")
                break

            if self.is_draw():
                print("Ничья!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
