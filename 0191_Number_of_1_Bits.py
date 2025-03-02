def hammingWeight(n: int):
  ret_counter = 0
  i = 0
  while n:
    ret_counter += n % 2
    n = n >> 1
    i += 1

  print("times", i)
  return ret_counter


def hammingWeight2(n: int):
  ret_counter = 0
  i = 0
  while n:
    n = n & (n - 1)
    ret_counter += 1
    i += 1

  print("times", i)
  return ret_counter


def hammingWeight3(n: int) -> int:
  m = n
  ret_counter = 0
  # n = 11 - 8 = 3 - 2 = 1
  # m
  while m > 0:
    if helper_function(m):
      ret_counter += 1
      n -= m
      m = n
    else:
      m -= 1

  return ret_counter


def helper_function(n: int) -> bool:
  if n == 1:
    return True

  if n % 2 != 0:
    return False

  while n != 0:
    n = n // 2
    if n == 1:
      return True
    if n % 2 != 0:
      return False

  return False  # if zero


# print(11, hammingWeight(11))
# print(128, helper_function(128))
# print(128, hammingWeight(128))
# print(2147483645, hammingWeight(2147483645))
print(11, hammingWeight(11))
print(128, hammingWeight(128))
print("--------")
print(11, hammingWeight2(11))
print(128, hammingWeight2(128))
