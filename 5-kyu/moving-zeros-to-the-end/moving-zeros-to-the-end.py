def move_zeros(lst):
    zeros = []
    non_zeros = []
    for x in lst:
        if x == 0:
            zeros.append(x)
        else:
            non_zeros.append(x)
    lst[:] = non_zeros + zeros
    return lst