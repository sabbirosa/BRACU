list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
new_list = []

for i in list_one:
  if int(i) % 2 == 0:
    new_list.append(i)

for i in list_two:
  if int(i) % 2 == 0:
    new_list.append(i)

print(new_list)