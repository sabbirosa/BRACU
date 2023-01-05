dict_1 = {'A': [1, 2, 3, 5], 'b': ['1', '2', 0], "c": [4, 5, 6, 7, 9]}
counter = 0

for i in dict_1:
  for j in dict_1[i]:
    counter += 1

print(counter)