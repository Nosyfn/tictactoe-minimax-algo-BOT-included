class board:

  board: list[list[str]]
  player_1: str
  player_2: str
  p1_score: int
  p2_score: int
  def __init__(self, board=[[',', ',', ','], [',', ',', ','], [',', ',', ',']], p1: str, p2: str):
    self.board = board
    self.player_1 = p1
    
    self.player_2 = p2
    self.p1_score = 0
    self.p2_score = 0
  def print_board(self, board):
    result = ""
    for row in board: 
      result += '|'.join(row) + /n
    return result
  
