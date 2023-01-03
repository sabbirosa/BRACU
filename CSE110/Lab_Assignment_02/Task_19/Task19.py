column = int(input())
row = int(input())
count = 0

while count < column:
  for i in range(1, row+1):
    print(i, end = "")
  print()
  count += 1