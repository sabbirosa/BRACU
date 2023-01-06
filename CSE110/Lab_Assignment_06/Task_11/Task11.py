def rem_duplicate(a_tuple):
    result = []
    for i in a_tuple:
        if i not in result:
            result.append(i)
    return tuple(result)

print(rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2])))