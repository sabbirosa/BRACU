count = int(input())
sum = 0

for count in range(1, count+1):
  if count % 2 == 0:
    count = -count**2
  else:
    count = count**2
  sum += count

print(sum)