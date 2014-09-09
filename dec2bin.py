def dec2bin(num):
  list = []
  while num >= 1:
    if num % 2 == 1:
      list.insert(0, 1)
      num = num - 1
      num = num/2
    else:
      list.insert(0, 0)
      num = num/2
  print list