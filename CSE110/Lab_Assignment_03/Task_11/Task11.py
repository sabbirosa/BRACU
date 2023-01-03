str_input = input()
letter_input = input()

if letter_input in str_input:
    for i in str_input:
        if i is letter_input:
            continue
        else:
            print(i, end = "")

elif len(str_input) > 3:
    print(str_input[slice(1, len(str_input)-1)])

else:
    print(str_input)