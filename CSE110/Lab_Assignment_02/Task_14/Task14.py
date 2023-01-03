num_input = int(input())
counter = 0
divisor_count = 0

while counter <= num_input:
  counter += 1
  if num_input % counter == 0:
    if counter == num_input:
        print(counter) 
    else:
        print(counter, end = ", ")
    divisor_count += 1

print("Total", divisor_count, "divisors.")