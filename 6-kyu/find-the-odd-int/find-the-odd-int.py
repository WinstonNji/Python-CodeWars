def find_it(seq):
    tracker = dict()
  
    for x in seq:
      if x in tracker:
        tracker[x] += 1
      else:
        tracker[x] = 1
​
    for k,v in tracker.items():
      if v % 2 != 0:
        return k