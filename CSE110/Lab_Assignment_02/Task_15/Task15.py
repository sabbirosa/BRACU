num_input = int(input())
counter = 0
sum = 0

while counter <= num_input:
  counter += 1
  if num_input % counter == 0:
    sum += counter

sum -= num_input

if sum == num_input:
  print(num_input, "is a perfect number")
else:
  print(num_input, "is not a perfect number")