input_s = int(input())

if input_s < 100:
    value_L = 3000 - (125*(input_s**2))
    print(value_L)
else:
    value_L = 12000 / (4+(input_s**2)/14900)
    print(value_L)