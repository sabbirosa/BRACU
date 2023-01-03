counter = 0
sum = 0

while counter <= 600:
  counter += 1
  if counter % 7 == 0 and counter % 9 == 0:
    sum += counter

print(sum)