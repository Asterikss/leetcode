from typing import List


class Trie:
  def __init__(self):
    self.children = {}

  def add_word(self, word: str):
    curr_node = self.children
    for w in word:
      if w not in curr_node:
        curr_node[w] = {}
      curr_node = curr_node[w]
    curr_node[-1] = False


class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    ret = []
    len_rows = len(board)
    len_cols = len(board[0])

    trie = Trie()
    for word in words:
      trie.add_word(word)

    def dfs(i: int, j: int, children: dict, path: str):
      visited.add((i, j))
      if -1 in children and not children[-1]:
        children[-1] = True
        ret.append(path)

      if i > 0 and board[i - 1][j] in children and (i - 1, j) not in visited:
        dfs(i - 1, j, children[board[i - 1][j]], path + board[i - 1][j])
      if i < len_rows - 1 and board[i + 1][j] in children and (i + 1, j) not in visited:
        dfs(i + 1, j, children[board[i + 1][j]], path + board[i + 1][j])
      if j > 0 and board[i][j - 1] in children and (i, j - 1) not in visited:
        dfs(i, j - 1, children[board[i][j - 1]], path + board[i][j - 1])
      if j < len_cols - 1 and board[i][j + 1] in children and (i, j + 1) not in visited:
        dfs(i, j + 1, children[board[i][j + 1]], path + board[i][j + 1])

      visited.remove((i, j))

    for i, row in enumerate(board):
      for j in range(len(row)):
        if board[i][j] in trie.children:
          visited = set()
          dfs(i, j, trie.children[board[i][j]], board[i][j])

    return ret

  def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
    ret = []
    len_rows = len(board)
    len_cols = len(board[0])

    def dfs(idx: int, i: int, j: int):
      visited.add((i, j))
      if idx == len(word):
        return True

      next_ch = word[idx]

      # up
      if i > 0 and board[i - 1][j] == next_ch and (i - 1, j) not in visited:
        if dfs(idx + 1, i - 1, j):
          return True
      # down
      if i < len_rows - 1 and board[i + 1][j] == next_ch and (i + 1, j) not in visited:
        if dfs(idx + 1, i + 1, j):
          return True
      # left
      if j > 0 and board[i][j - 1] == next_ch and (i, j - 1) not in visited:
        if dfs(idx + 1, i, j - 1):
          return True
      # right
      if j < len_cols - 1 and board[i][j + 1] == next_ch and (i, j + 1) not in visited:
        if dfs(idx + 1, i, j + 1):
          return True

      visited.remove((i, j))
      return False

    for word in words:
      found = False
      visited = set()

      for i, row in enumerate(board):
        for j in range(len(row)):
          if not found and board[i][j] == word[0] and dfs(1, i, j):
            ret.append(word)
            found = True

    return ret
