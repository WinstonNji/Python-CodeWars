def square_digits(num):
    num_list = [str(int(n) ** 2) for n in str(num)]
    return int(''.join(num_list))
​