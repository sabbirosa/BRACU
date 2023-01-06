def two_max(a_list):
    result = []
    counter = 0
    for i in a_list:
        if result.count(i) < 2:
            result.append(i)
        else:
            counter += 1
    print("Removed:", counter)
    return result

two_max([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])