from typing import Dict


class WordDictionary:
  def __init__(self):
    self.children = {}

  def addWord(self, word: str) -> None:
    curr_node = self.children
    for c in word:
      if c not in curr_node:
        curr_node[c] = {}
      curr_node = curr_node[c]
    curr_node[-1] = True

  def search(self, word: str) -> bool:
    len_word = len(word)

    def dfs(idx: int, node: Dict):
      if idx == len_word:
        return -1 in node

      curr_char = word[idx]
      if curr_char == ".":
        for next_node in node.values():
          if isinstance(next_node, dict) and dfs(idx + 1, next_node):  # important if
            return True
      else:
        if curr_char not in node:
          return False
        return dfs(idx + 1, node[curr_char])  # "if" not needed - it's a straight path

      return False

    return dfs(0, self.children)
