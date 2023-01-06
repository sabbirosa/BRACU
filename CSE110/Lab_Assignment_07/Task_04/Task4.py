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

#Selection Sort Descending Order
def selectionSortDes(my_list):
  
  for i in range(len(my_list)):
      max_index = i
      
      for j in range(i+1, len(my_list)):
          if my_list[max_index] < my_list[j]:
              max_index = j      
      
      temp = my_list[max_index]
      my_list[max_index] = my_list[i]
      my_list[i] = temp
  
  return my_list 

sitting_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]

even_list = []
odd_list = []
result_list = []

for i in range(len(sitting_list)):
  if i % 2 == 0:
    even_list.append(sitting_list[i])
  else:
    odd_list.append(sitting_list[i])

selectionSortAsc(even_list)
selectionSortDes(odd_list)

for i in range(len(even_list)):
  result_list.append(even_list[i])
  result_list.append(odd_list[i])

print(result_list)