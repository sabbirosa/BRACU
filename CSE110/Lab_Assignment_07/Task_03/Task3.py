my_list= [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

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

selectionSortDes(my_list)