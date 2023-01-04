my_list = []
for i in range(5):
    num_input = int(input())
    my_list.append(num_input)

print("Input data:", my_list)
print("Printing values from the list in reverse order:")

for i in range(1, len(my_list)+1):
  print(my_list[-i])