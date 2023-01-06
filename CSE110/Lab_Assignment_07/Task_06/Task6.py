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
  
my_list = [4, 2, 3, 1, 6, 5]
copy_list = my_list.copy()
selectionSortAsc(my_list)
count = 0

for i in range(len(copy_list)):
  if copy_list[i] != my_list[i]:
    count += 1

print(count)