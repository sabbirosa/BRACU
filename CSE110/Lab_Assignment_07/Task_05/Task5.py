num_list = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]
sub_input = input()

if sub_input == "CSE110":
  sub = 1
elif sub_input == "PHY111":
  sub = 2
elif sub_input == "MAT110":
  sub = 3

for i in range(len(num_list)):
  max_index = i
  
  for j in range(i+1, len(num_list)):
    if num_list[j][sub] > num_list[max_index][sub]:
      max_index = j
  
  print(num_list[max_index][0])
  
  temp = num_list[i]
  num_list[i] = num_list[max_index]
  num_list[max_index] = temp