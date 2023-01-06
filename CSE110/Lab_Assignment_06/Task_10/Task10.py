def make_square(a_tuple):
    start, end = a_tuple
    result = {}
    for i in range(start, end+1):
        result[i] = i**2
    return result

print(make_square((5, 9)))