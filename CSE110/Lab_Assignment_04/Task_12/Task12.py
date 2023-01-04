list_input = input()
my_list = []
largest_num = -99999

for i in list_input.split(", "):
  my_list.append(int(i))

for i in my_list:
  if i > largest_num:
    largest_num = i

my_list.remove(largest_num)
largest_num = -99999

for i in my_list:
  if i > largest_num:
    largest_num = i

print(largest_num)