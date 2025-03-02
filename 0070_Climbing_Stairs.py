class Solution1:
  # 3
  # * _ _ _
  def climbStairs(self, n: int) -> int:
    buffer1, buffer2 = 1, 1  # or buffer1, buffer2 = 1, 0

    for _ in range(n - 1):  # or for _ in range(n)
      print(buffer1)
      print(buffer2)
      tmp = buffer1
      buffer1 = buffer1 + buffer2
      buffer2 = tmp
      print(buffer1)
      print(buffer2)

    return buffer1


# Works, but takes too much time
class Solution2:
  # 3
  #  2   1
  #  1 0  ret 1
  # r1   r1
  def climbStairs(self, n: int) -> int:
    if n > 1:
      return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    else:
      return 1

  def climbStairs2(self, n: int) -> int:
    counter = 0

    def abc(i: int):
      nonlocal counter
      if i == n:
        counter += 1

      if i + 1 <= n:
        # print(i, counter)
        # counter += 1
        abc(i + 1)
      if i + 2 <= n:
        # print(i, counter)
        # counter += 1
        abc(i + 2)

    abc(0)
    return counter
