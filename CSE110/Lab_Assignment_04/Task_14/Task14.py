str_input1 = input()
str_input2 = input()
list_1 = str_input1.split(", ")
list_2 = str_input2.split(", ")
list_3 = []

for i in list_1:
  if i in list_2:
    list_3.append(i)

print(list_3)