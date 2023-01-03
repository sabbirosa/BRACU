str_input = input()

for i in str_input:
    if str_input.index(i) % 2 != 0:
        new_ord = ord(i) - 32
        print(chr(new_ord), end = "")