counter = 0
num_input = int(input())
sum = 0

while counter <= num_input:
  counter += 1
  if counter % 7 == 0:
    sum += counter
  
print(sum)