my_list = input()[1:-1].split(", ")

for i in range(len(my_list)):
  my_list[i] = int(my_list[i])

num1 = 0
num2 = 1
min_sum = my_list[num1] + my_list[num2]

for i in range(len(my_list) - 1):
  
  for j in range(i+1, len(my_list)):
    sum = my_list[i] + my_list[j]
    
    if abs(min_sum) > abs(sum):
      min_sum = sum
      num1 = my_list[i]
      num2 = my_list[j]

print("Two pairs which have the smallest sum =", num1, "and", num2)