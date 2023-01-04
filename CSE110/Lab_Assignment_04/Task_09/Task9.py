str_input = input()
my_list = []
odd_list = []
temp = ''

for i in str_input:
    if i == ' ':
      my_list.append(temp)
      temp = ''
    else:
      temp += i
my_list.append(temp)

for i in range(len(my_list)):
  my_list[i] = int(my_list[i])
  if my_list[i] % 2 != 0:
    odd_list.append(my_list[i])
    

print("Original List:", my_list)
print("Modified List:", odd_list)