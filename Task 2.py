import math

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                self.current_winner = player
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                self.current_winner = player
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            self.current_winner = player
            return True
        return False

    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == " "]

    def minimax(self, is_maximizing):
        if self.current_winner == "O":
            return 1
        if self.current_winner == "X":
            return -1
        if not self.get_empty_cells():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = "O"
                score = self.minimax(False)
                self.board[row][col] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = "X"
                score = self.minimax(True)
                self.board[row][col] = " "
                best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for row, col in self.get_empty_cells():
            self.board[row][col] = "O"
            score = self.minimax(False)
            self.board[row][col] = " "
            if score > best_score:
                best_score = score
                move = (row, col)
        return move

    def player_move(self):
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column: 1-3 1-3): ").split())
                row, col = row - 1, col - 1
                if (row, col) in self.get_empty_cells():
                    return row, col
                else:
                    print("The cell is already occupied. Give it another go.")
            except ValueError:
                print("The input is invalid. Kindly provide two digits from 1 to 3.")

    def play_game(self):
        print("Greetings from Tic-Tac-Toe!")
        self.print_board()

        for turn in range(9):
            if turn % 2 == 0:
                print("It's your turn!")
                row, col = self.player_move()
                self.board[row][col] = "X"
            else:
                print("Time for AI!")
                row, col = self.best_move()
                self.board[row][col] = "O"
            self.print_board()
            if self.check_winner("X"):
                print("Well done! You're the winner!")
                return
            if self.check_winner("O"):
                print("AI triumphs! I hope you have more success the next time.")
                return

        print("The score is tied!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
