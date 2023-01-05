list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]

a_list = []
b_list = []
c_list = []

for i in list_1:
  k, v = i
  if k == "a":
    a_list.append(v)
  elif k == "b":
    b_list.append(v)
  else:
    c_list.append(v)
  
my_dict = {'a': a_list, 'b': b_list, 'c': c_list}
print(my_dict)