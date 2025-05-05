import random
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

    def new_game(self):
        """Start a new game for user."""
        print("new game starting")
        self.reset_board()
    def new_game_with_points_reset(self):
        self.reset_board()
        self.player_1[1], self.player_2[1] = 0, 0

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
            return True
        else:
            print('spot is already taken, try again')
            return False

        # if self.check_winner(self.board):
        #     winner = self.player_1[0] if self.player_turn % 2 == 0 else self.player_2[0]
        #     return f'{winner} has won this round'
    def check_if_moves(self):
        """check if there are still moves"""
        for i in self.board:
            if ',' in i:
                return True
        return False

    def available_moves(self):
        move = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == ',':
                    move.append((i, j))
        return move


class easy_bot:
    def __init__(self, game: Tictactoe):
        self.game = game
    def start(self):
        while not self.game.check_winner(self.game.board)[0] and self.game.check_if_moves():
            print('current board: \n ')
            print(self.game.print_board())
            move = input(
                "what row, column would you like to play on (row, column), (row and column are in between 0 and 2: ")
            l = move.split(',')

            row = int(l[0])
            column = int(l[1])

            is_valid = self.game.player_move(row, column)
            while not is_valid:
                is_valid = input("what row, column would you like to play on (row, column), (row and column are in between 0 and 2: ")
            print('you have made a move, here is the board now \n')
            print(self.game.print_board())

            moves = self.game.available_moves()
            if self.game.check_winner(self.game.board)[0]:
                play = input("you have beat the robot! Type 2 to reset points and play again, 1 to play again, 0 to end game")
                while play != '1' and play != '0' and play != '2':
                    play = input('type 2 to play again and reset points, 1 to play again, 0 to quit')
                if play == '2':
                    self.game.new_game_with_points_reset()
                if play == '1':
                    self.game.reset_board()
                else:
                    self.game.end_game()
                    break
            elif not moves:
                t = input('It is a tie! type 0 to end game or 1 to reset board: ')
                while t != '1' and t != '0':
                    t = input("type 1 to play again, 0 to end game")
                if t == '0':
                    self.game.end_game()
                    break
                elif t == '1':
                    self.game.reset_board()
            else:
                print('Time for the easy bots move!')
                bot_move = random.choice(moves)
                self.game.player_move(bot_move[0], bot_move[1])
                print(f'the bot played on spot ({bot_move[0]}, {bot_move[1]}) \n')
                print(f"the board now looks like this: \n")
                print(self.game.print_board())

                if self.game.check_winner(self.game.board)[0]:
                    print('hahaha, you have lost to the easy bot!')
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
                        is_break = True
                        break
                    elif t == '1':
                        self.game.reset_board()





















def main():
    while True:
        player_or_bot = input('type 1 to play against a friend, 2 for a bot (easy mode), 3 for hard mode and 4 to watch two bots play ')
        if player_or_bot == '1':
            name1 = input("player1 name: ")
            name2 = input('player2 name: ')
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
                print("here is the current board")
                print(game.print_board())
                move = input("what row, column would you like to play on (row, column), (row and column are in between 0 and 2: ")
                l = move.split(',')
                row = int(l[0])
                column = int(l[1])
                game.player_move(row, column)
                is_over = game.check_winner(game.board)
                if is_over[0]:
                    print(f'The winner is {is_over[1]}')
                    print('current score:')
                    print(f'player 1 has {game.player_1[1]} points')
                    print(f'player 2 has {game.player_2[1]} points')
                    t = input('type 1 to play again, 2 to end game or 3 to reset points and play again')
                    if t == '1':
                        game.new_game()
                    elif t == '2':
                        game.end_game()
                        break
                    elif t == '3':
                        game.new_game_with_points_reset()

        if player_or_bot == '2':
            name = input('what is your name: ')
            bot = input('name your bot: ')
            game = Tictactoe(name, bot)
            bot = easy_bot(game)
            bot.start()


























if __name__ == "__main__":
  main()
