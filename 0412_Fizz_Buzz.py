for i in range(1, 101):
  print("FIZZ" * (i % 3 < 1) + "BUZZ" * (i % 5 < 1) or i)
