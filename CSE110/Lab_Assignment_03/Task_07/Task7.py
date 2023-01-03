str_input = input()

for i in range(len(str_input)):
    ascii_value = ord(str_input[i])
    if ascii_value < 122:
        new_char = chr(ascii_value + 1)
    else:
        new_char = chr(97)
    print(new_char, end = "")