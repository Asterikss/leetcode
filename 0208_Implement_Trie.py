class PrefixTree:
  def __init__(self):
    self.children = {}

  def insert(self, word: str) -> None:
    curr_node = self.children
    for c in word:
      if c not in curr_node:
        curr_node[c] = {}
      curr_node = curr_node[c]
    curr_node[-1] = True  # A class wrapper with is_end field can be used instead

  def search(self, word: str) -> bool:
    curr_node = self.children
    for c in word:
      if c not in curr_node:
        return False
      curr_node = curr_node[c]
    return -1 in curr_node

  def startsWith(self, prefix: str) -> bool:
    curr_node = self.children
    for c in prefix:
      if c not in curr_node:
        return False
      curr_node = curr_node[c]
    return True
