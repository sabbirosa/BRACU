str_input = input()

str_1 = str_input.split(", ")[0]
str_2 = str_input.split(", ")[1]

if len(str_1) > len(str_2):
    for i in range(len(str_2)):
        print(str_1[i]+str_2[i], end = "")
    print(str_1[len(str_2):])

elif len(str_2) > len(str_1):
    for i in range(len(str_1)):
        print(str_1[i]+str_2[i], end = "")
    print(str_2[len(str_1):])

else:
    for i in range(len(str_2)):
        print(str_1[i]+str_2[i], end = "")
    print(str_1[len(str_2):])