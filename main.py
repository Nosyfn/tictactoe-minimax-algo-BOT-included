import random


class Tictactoe:
    """A Python implementation of Tic-Tac-Toe."""

    board: list[list[str]]
    player_1: list
    player_2: list

    def __init__(self, p1: str, p2: str):
        self.board = [[',', ',', ','], [',', ',', ','], [',', ',', ',']]
        self.player_1 = [p1, 0]
        self.player_2 = [p2, 0]
        self.player_turn = 0
        # if self.player_move is even, it is player 1 turn so use X, else 0

    def print_board(self):
        result = ""
        for row in self.board:
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
        self.player_turn = 0

    def new_game(self):
        """Start a new game for user."""

        # Comment: I updated the points for both players to 0 & combined this with new_game_with_points_reset b/c
        # it was pretty much the same.

        print("STARTING A NEW GAME!")
        self.reset_board()
        self.player_turn = 0

    def new_game_with_points_reset(self):
        """Start a new game, while resetting all player points to 0."""
        self.reset_board()
        self.player_1[1], self.player_2[1] = 0, 0
        self.player_turn = 0

    def end_game(self):
        """Return the winner and amount of points each team has."""
        if self.player_2[1] == self.player_1[1]:
            return f'Both players have {self.player_1[1]} points, hence it\'s a TIE!'

        winner = self.player_1 if self.player_1[1] > self.player_2[1] else self.player_2
        second = self.player_1 if winner == self.player_2 else self.player_2

        return f'The winner after all rounds played is {winner[0]} with {winner[1]} points, beating {second[0]} with {second[1]} points!'

    def player_move(self, row, column):
        """Take user input for move and update board"""
        if not (0 <= row <= 2 and 0 <= column <= 2):
            print("That move is not possible, try again!")
            return False

        if self.board[row][column] == ",":

            if self.player_turn % 2 == 0:
                self.board[row][column] = "X"
            else:
                self.board[row][column] = "O"

            self.player_turn += 1

            return True
        else:
            print('This spot is already taken!')

            return False

    def check_if_moves(self):
        """check if there are still moves"""
        for i in self.board:
            if ',' in i:
                return True
        return False

    def available_moves(self):
        """ Return a list of the remaining spaces on the board, in the form (row, column).

        Note: Columns & rows both start at index 0
        """
        move = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == ',':
                    move.append((i, j))
        return move


class EasyBot:
    """Implementing the EASY bot for the Tic-Tac-Toe game."""

    def __init__(self, game: Tictactoe):
        self.game = game

    def start(self):
        """Instructions for starting the game."""

        while not self.game.check_winner(self.game.board)[0] and self.game.check_if_moves():
            print('Current Board: \n ')
            print(self.game.print_board())

            row = int(input("Row? (between 0 and 2)"))
            column = int(input("Column? (between 0 and 2)"))
            is_valid = self.game.player_move(row, column)

            # Why doesn't this have a function call after it?
            # ok fixed.
            while not is_valid:
                row = int(input("Row? (between 0 and 2)"))
                column = int(input("Column? (between 0 and 2)"))
                is_valid = self.game.player_move(row, column)

            print('Here is the board after your new move: \n')
            print(self.game.print_board())

            moves = self.game.available_moves()

            if self.game.check_winner(self.game.board)[0]:
                play = input("YOU WON! Type...\n- 1 to play again\n- 2 to exit\n- 3 to reset points & play again")

                while play != '1' and play != '2' and play != '3':
                    play = input('- type 1 to play again\n- 2 to exit\n- 3 to reset points and play again' )
                if play == '3':
                    self.game.new_game_with_points_reset()
                elif play == '1':
                    self.game.reset_board()
                else:
                    print(self.game.end_game())
                    break

            elif not moves:
                t = input('It is a tie! \nType 0 to end game or 1 to reset board: ')
                while t != '1' and t != '0':
                    t = input("type 1 to play again, 0 to end game")
                if t == '0':
                    self.game.end_game()
                    break
                elif t == '1':
                    self.game.reset_board()
            else:

                print('Time for the easy bot\'s move!')
                bot_move = random.choice(moves)
                self.game.player_move(bot_move[0], bot_move[1])
                print(f'The bot played on position ({bot_move[0]}, {bot_move[1]}) \n')
                print("Updated Board: \n")
                print(self.game.print_board())

                if self.game.check_winner(self.game.board)[0]:
                    print('YOU LOST!')

                    play = input('type 0 to end game, 1 to play again, 2 to reset points')

                    while play != '1' and play != '0' and play != '2':
                        play = input('type 2 to play again and reset points, 1 to play again, 0 to quit')
                    if play == '2':
                        self.game.new_game_with_points_reset()
                    if play == '1':
                        self.game.reset_board()
                    else:
                        self.game.end_game()
                        return

                elif not moves:
                    t = input('It is a tie! type 0 to end game or 1 to reset board: ')

                    while t != '1' and t != '0':
                        t = input("type 1 to play again, 0 to end game")
                    if t == '0':
                        self.game.end_game()
                        break
                    elif t == '1':
                        self.game.reset_board()


def main():
    """Main class for the Tic-Tac-Toe game."""

    while True:
        player_or_bot = input('TYPE...\n- 1 to play a FRIEND\n- 2 to play an EASY bot\n- 3 to play a HARD bot\n- 4 to '
                              'WATCH two bots play')

        if player_or_bot == '1':
            name1 = input("Player 1's name: ")
            name2 = input('Player 2\'s name: ')
            game = Tictactoe(name1, name2)

            while True:
                if not game.available_moves():
                    play = input('type 1 to play again, 0 to quit')
                    while play != '1' or play != '0':
                        play = input('type 1 to play again, 0 to quit')
                    if play == '1':
                        game.reset_board()
                    else:
                        game.end_game()
                        break

                print("Current Board:")
                print(game.print_board())

                row = int(input("Row? (between 0 and 2)"))
                column = int(input("Column? (between 0 and 2)"))
                game.player_move(row, column)

                is_over = game.check_winner(game.board)

                if is_over[0]:
                    print(f'The winner is {is_over[1]}')
                    print('Current score:')
                    print(f'Player 1 has {game.player_1[1]} points')
                    print(f'Player 2 has {game.player_2[1]} points \n')

                    t = input('TYPE...\n- 1 to play again\n- 2 to exit\n- 3 to reset points & play again')
                    if t == '1':
                        game.new_game()
                    elif t == '2':
                        game.end_game()
                        break
                    elif t == '3':
                        game.new_game_with_points_reset()

        elif player_or_bot == '2':
            name = input('What is your name?: ')
            bot = input('Name your bot: ')
            game = Tictactoe(name, bot)
            bot = EasyBot(game)
            bot.start()
        elif player_or_bot == '3':
            pass


if __name__ == "__main__":
    main()
