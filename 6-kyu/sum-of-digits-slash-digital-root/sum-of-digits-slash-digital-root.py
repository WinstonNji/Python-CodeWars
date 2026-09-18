def digital_root(n):
  if len(str(n)) == 1:
    return n
  
  total = sum([int(num) for num in list(str(n))])
  return digital_root(total)