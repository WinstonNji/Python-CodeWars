def narcissistic( value ):
    sum = 0
​
    for number in list(str(value)):
      sum += int(number) ** len(list(str(value)))
​
    return sum == value