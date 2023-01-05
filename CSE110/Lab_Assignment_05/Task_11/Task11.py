str_input = input()
my_dict = {}
  
for i in str_input:
    if i in my_dict:
        my_dict[i] += 1
    elif i == " ":
      continue
    else:
        my_dict[i] = 1

print(my_dict)