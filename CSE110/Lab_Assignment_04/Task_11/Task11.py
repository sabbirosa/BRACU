list_one = [1, 4, 3, 2, 5]
list_two = [8, 7, 6, 9]
res_ = False

for i in list_one:
  if i in list_two:
      res_ = True
      break
  else:
      res_ = False

print(res_)