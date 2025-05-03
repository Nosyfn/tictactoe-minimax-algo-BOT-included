class Tictactoe:
    board: list[list[str]]
    player_1: str
    player_2: str
    p1_score: int
    p2_score: int
    def __init__(self, p1: str, p2: str):
      self.board = [[',', ',', ','], [',', ',', ','], [',', ',', ',']]
      self.player_1 = p1
      self.player_2 = p2
      self.p1_score = 0
      self.p2_score = 0

    def print_board(self, board):
      result = ""
      for row in board:
        result += '|'.join(row) + '\n'
      return result

    def check_winner(self, board):
      "return True if winner is found, else False, winner is 3 in a row, update scores"

    def reset_board(self):
      "reset the board"

    def new_game(self):
      "start a new game for user"

    def end_game(self):
      "return the winner and ampount of points each team has. maybe return a percentage of how much they won"

    def play(self):
    """ take user input for which row,column they want to play at and mutate board
    check if they are allowed to play there"""



if __name__ == "__main__":
  t = Tictactoe('p1', 'p2')
  print(t.print_board(t.board))
