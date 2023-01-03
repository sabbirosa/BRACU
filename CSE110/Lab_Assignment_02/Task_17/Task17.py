input_amount = int(input())
counter = 0
highest_num = 0
lowest_num = 0
total_num = 0

while counter < input_amount:
  counter += 1
  num_input = int(input())
  if num_input > highest_num:
    highest_num = num_input
  if num_input < lowest_num:
    lowest_num = num_input
  total_num += num_input

print("Maximum:", highest_num)    
print("Minimum:", lowest_num)    
print("Average:", total_num/input_amount)    