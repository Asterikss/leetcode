from enum import Enum, auto
from typing import List


class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    class Direction(Enum):
      Up = auto()
      Right = auto()
      Down = auto()
      Left = auto()

    def get_updated_cords(direction: Direction, x: int, y: int):
      if direction == Direction.Up:
        return x - 1, y
      if direction == Direction.Down:
        return x + 1, y
      if direction == Direction.Left:
        return x, y - 1
      if direction == Direction.Right:
        return x, y + 1

    def turn_right(direction: Direction) -> Direction:
      return Direction(direction.value % 4 + 1)

    def turn_right2(direction: Direction) -> Direction:
      if direction == Direction.Up:
        return Direction.Right
      elif direction == Direction.Right:
        return Direction.Down
      elif direction == Direction.Down:
        return Direction.Left
      elif direction == Direction.Left:
        return Direction.Up

    N_ROWS = len(matrix)
    N_COLS = len(matrix[0])
    visited = set()
    curr_row, curr_col = 0, 0
    visited.add((curr_row, curr_col))
    sequence = [matrix[0][0]]
    turned = False
    direction = Direction.Right

    while True:
      x, y = get_updated_cords(direction, curr_row, curr_col)
      if (x, y) in visited or x < 0 or x >= N_ROWS or y < 0 or y >= N_COLS:
        direction = turn_right(direction)
        if turned == True:
          break
        turned = True
        continue
      turned = False
      curr_row, curr_col = x, y
      sequence.append(matrix[x][y])
      visited.add((x, y))

    return sequence
