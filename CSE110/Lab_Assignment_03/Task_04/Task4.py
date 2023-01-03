str_input = input()
length = len(str_input)

if length < 4:
    if "er" in str_input:
        str_input = str_input[:-2]
        print(str_input+"est")
    else:
        print(str_input)

elif "est" in str_input:
    print(str_input)
    
elif "er" in str_input:
    str_input = str_input[:-2]
    print(str_input+"est")

elif length > 3:
    print(str_input+"er")