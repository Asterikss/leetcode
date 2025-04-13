from typing import List


class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    def find_word(i, j, n_character) -> bool:
      visited.add((i, j))
      if n_character == len_word:
        return True

      if (
        i < n_rows
        and board[i + 1][j] == word[n_character]
        and (i + 1, j) not in visited
      ):
        if find_word(i + 1, j, n_character + 1):
          return True

      if i > 0 and board[i - 1][j] == word[n_character] and (i - 1, j) not in visited:
        if find_word(i - 1, j, n_character + 1):
          return True

      if (
        j < n_columns
        and board[i][j + 1] == word[n_character]
        and (i, j + 1) not in visited
      ):
        if find_word(i, j + 1, n_character + 1):
          return True

      if j > 0 and board[i][j - 1] == word[n_character] and (i, j - 1) not in visited:
        if find_word(i, j - 1, n_character + 1):
          return True

      visited.remove((i, j))
      return False

    len_word = len(word)
    n_rows = len(board) - 1
    n_columns = len(board[0]) - 1
    first_letter = word[0]
    visited = set()
    for i, row in enumerate(board):
      for j, letter in enumerate(row):
        if letter == first_letter:
          if find_word(i, j, 1):
            return True
    return False

  # Ver1 without visited.remove at the end, and with visited.copy instead
  def exist2(self, board: List[List[str]], word: str) -> bool:
    def find_word(i, j, n_character, visited) -> bool:
      visited.add((i, j))
      if n_character == len_word:
        return True

      # [["A","B","C","E"],
      #  ["S","F","E","S"],
      #  ["A","D","E","E"]] ABCESEEEFS
      if (
        i < n_rows
        and board[i + 1][j] == word[n_character]
        and (i + 1, j) not in visited
      ):
        if find_word(i + 1, j, n_character + 1, visited.copy()):
          return True

      if i > 0 and board[i - 1][j] == word[n_character] and (i - 1, j) not in visited:
        if find_word(i - 1, j, n_character + 1, visited.copy()):
          return True

      if (
        j < n_columns
        and board[i][j + 1] == word[n_character]
        and (i, j + 1) not in visited
      ):
        if find_word(i, j + 1, n_character + 1, visited.copy()):
          return True

      if j > 0 and board[i][j - 1] == word[n_character] and (i, j - 1) not in visited:
        if find_word(i, j - 1, n_character + 1, visited.copy()):
          return True

      return False

    len_word = len(word)
    n_rows = len(board) - 1
    n_columns = len(board[0]) - 1
    first_letter = word[0]
    for i, row in enumerate(board):
      for j, letter in enumerate(row):
        if letter == first_letter:
          if find_word(i, j, 1, set()):
            return True
    return False
