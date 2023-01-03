num_input = int(input()) 
 
while num_input: 
    digit = num_input % 10
    num_input //= 10
    if num_input == 0:
      print(digit)
    else: 
      print(digit, end = ", ")