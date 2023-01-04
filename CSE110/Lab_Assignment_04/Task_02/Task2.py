list_input = input()[1:-1]
my_list = []

for i in list_input.split(", "):
  my_list.append(int(i))

if len(my_list) >= 4:
    print(my_list[2:-2])
else:
    print("Not Possible")