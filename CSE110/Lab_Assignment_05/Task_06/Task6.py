given_tuple = (10, 20, 30, 40, 50, 60)
new_list = []

for i in range(1, len(given_tuple)+1):
  new_list.append(given_tuple[-i])

print(tuple(new_list))