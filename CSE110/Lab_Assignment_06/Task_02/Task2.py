def fibonacci(num):
    n1, n2 = 0, 1

    print(n1, n2, end = " ")
    for i in range(num):
        n = n1 + n2
        if n <= num:
          print(n, end = " ")
        n1 = n2
        n2 = n

fibonacci(10)