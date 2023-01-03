num_input = int(input())
counter = 0
divisor_count = 0

while counter <= num_input:
  counter += 1
  if num_input % counter == 0:
    divisor_count += 1

if divisor_count == 2:
  print(num_input, "is a prime number")
else:
  print(num_input, "is not a prime number")