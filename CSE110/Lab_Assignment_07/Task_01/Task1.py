my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

def bubbleSortAsc(my_list):
  for i in range(len(my_list)):
    
    for j in range(0, len(my_list) - i -1):
      
      if my_list[j] > my_list[j + 1]:
        temp = my_list[j]
        my_list[j] = my_list[j+1]
        my_list[j+1] = temp
  
  return my_list

print(bubbleSortAsc(my_list))