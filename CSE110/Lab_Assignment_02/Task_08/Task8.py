counter = 0
odd_count = 0
sum = 0

while counter < 10:
  num_input = int(input())
  if num_input % 2 != 0:
    sum += num_input
    odd_count += 1
  counter += 1
print("The total of the odd numbers is", sum, "and their average is", sum/odd_count)