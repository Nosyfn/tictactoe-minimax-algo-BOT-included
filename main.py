
class Tictactoe:
    board: list[list[str]]
    player_1: list
    player_2: list

    def __init__(self, p1: str, p2: str):
        self.board = [[',', ',', ','], [',', ',', ','], [',', ',', ',']]
        self.player_1 = [p1, 0]
        self.player_2 = [p2, 0]
        self.player_turn = 0
        # if self.player_move is even, it is player 1 turn so use X, else 0


    def print_board(self, board):
        result = ""
        for row in board:
            result += '|'.join(row) + '\n'
        return result

    def check_winner(self, board):
        """Return True and player who won, else False and None"""
        # i just hard coded this part because we know its 3 by 3
        p1_win, p2_win = "XXX", "OOO"
        for row in board:
            word = ''.join(row)
            if word == p1_win:
                self.player_1[1] += 1
                return True, self.player_1[0]
            if word == p2_win:
                self.player_2[1] += 1
                return True, self.player_2[0]
        diagonal1 =  board[0][0] + board[1][1] + board[2][2]
        diagonal2 = board[2][2] + board[1][1] + board[0][0]
        if diagonal1 == p1_win or diagonal2 == p1_win:
            self.player_1[1] += 1
            return True, self.player_1[0]
        if diagonal2 == p2_win or diagonal1 == p2_win:
            self.player_2[1] += 1
            return True, self.player_2[0]
        columns = [board[0][0] + board[1][0] + board[2][0],
                   board[0][1] + board[1][1] + board[2][1],
                   board[0][2] + board[1][2] + board[2][2]]
        if p1_win in columns:
            self.player_1[1] += 1
            return True, self.player_1[0]
        if p2_win in columns:
            self.player_2[1] += 1
            return True, self.player_2[0]
        return False, None

    def reset_board(self):
        """Reset the board."""
        self.board = [[',', ',', ','], [',', ',', ','], [',', ',', ',']]

    def new_game(self):
        """Start a new game for user."""
        print("new game starting")
        self.reset_board()
    def new_game_with_points_reset(self):
        self.reset_board()
        self.player_1[1], self.player_2[2] = 0, 0

    def end_game(self):
        """Return the winner and amount of points each team has."""
        if self.p2_score == self.p1_score:
            return f'No winner! player 1 had {self.p1_score} points and player 2 had {self.p2_score} points'

        winner = self.player_1 if self.player_1[1] > self.player_2[1] else self.player_2
        second = self.player_1 if winner == self.player_2 else self.player_2

        return f'The winner is {winner} with {winner[1]} points, beating {second} with {second[1]} points'


    def player_move(self, row, column):
        """Take user input for move and update board"""

        if self.board[row][column] == ",":
            self.board[row][column] = "X" if self.player_turn % 2 == 0 else '0'
            self.player_turn += 1
        else:
            print('spot is already taken, try again')

        # if self.check_winner(self.board):
        #     winner = self.player_1[0] if self.player_turn % 2 == 0 else self.player_2[0]
        #     return f'{winner} has won this round'

def main():
    while True:
        player_or_bot = input('type 1 to play against a friend or 2 for a bot: ')
        if player_or_bot == '1':
            name1 = input("player1 name: ")
            name2 = input('player2 name: ')
            game = Tictactoe(name1, name2)
            while True:
                print("here is the current board")
                print(game.print_board(game.board))
                move = input("what row, column would you like to play on (row, column), (row and column are in between 0 and 2: ")
                l = move.split()
                row = int(l[0])
                column = int(l[1])
                game.player_move(row, column)
                is_over = game.check_winner(game.board)
                if is_over[0]:
                    print(f'The winner is {is_over[1]}')
                    print('current score:')
                    print(f'player 1 has {game.player_1[1]} points')
                    print(f'player 2 has {game.player_2[1]} points')
                    t = input('type 1 to play again, 2 to exit player vs player mode or 3 to reset points')
                    if t == '1':
                        game.new_game()
                        continue
                    elif t == '2':
                        break
                    elif t == '3':
                        game.new_game_with_points_reset()


        if player_or_bot == '2':
            pass























if __name__ == "__main__":
  main()
