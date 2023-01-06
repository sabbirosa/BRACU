#Selection Sort Ascending Order
def selectionSortAsc(my_list):
  
  for i in range(len(my_list)):
      min_index = i
      
      for j in range(i+1, len(my_list)):
          if my_list[min_index] > my_list[j]:
              min_index = j      
      
      temp = my_list[min_index]
      my_list[min_index] = my_list[i]
      my_list[i] = temp
  
  return my_list 
  
list_one = input()[1:-1].split(", ")

for i in range(len(list_one)):
  list_one[i] = int(list_one[i])

list_two = input()[1:-1].split(", ")

for i in range(len(list_two)):
  list_two[i] = int(list_two[i])

my_list = selectionSortAsc(list_one + list_two)

for i in range(len(my_list)):
  if len(my_list) % 2 == 0:
    med = (my_list[(len(my_list) // 2)] + my_list[(len(my_list) // 2)-1])/2
  else:
    med = my_list[len(my_list) // 2]

print("Sorted list =", my_list)
print("Median =", med)