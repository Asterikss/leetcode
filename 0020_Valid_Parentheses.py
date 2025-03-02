class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    map = {")": "(", "}": "{", "]": "["}

    for b in s:
      if stack:
        if b in map.keys():
          if stack[-1] == map[b]:
            stack.pop()
          else:
            return False
        else:
          stack.append(b)
      else:
        if b in map.keys():
          return False
        stack.append(b)

    if stack:
      return False
    return True
