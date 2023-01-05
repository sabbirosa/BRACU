num_input = int(input())
given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
counter = 0

for i in given_tuple:
  if i == num_input:
    counter += 1

print(num_input, "appears", counter, "times in the tuple")