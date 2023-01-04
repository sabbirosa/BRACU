list_input = input()
my_list = []
largest_num = -99999
smallest_num = 99999

for i in list_input.split(", "):
  my_list.append(int(i))

for i in my_list:
  if i > largest_num:
    largest_num = i
  if i < smallest_num:
    smallest_num = i

small_index = my_list.index(smallest_num)
large_index = my_list.index(largest_num)

print("Smallest number in the list is", smallest_num, "which was found at index", small_index)
print("Largest number in the list is", largest_num, "which was found at index", large_index)