list_input = input()
my_list = list_input.split(", ")
largest_num = int(my_list[0])
index_num = 0

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

for i in range(1, len(my_list)):
    if my_list[i] > largest_num:
        largest_num = my_list[i]
        index_num = i

print("My list:", my_list)
print("Largest number in the list is", largest_num, "which was found at index", index_num)