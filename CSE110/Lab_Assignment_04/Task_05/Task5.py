my_list = ["hey", "there", "", "what's", "", "up", "", "?"]
mod_list = []

for i in my_list:
  if i == "":
    continue
  else:
    mod_list.append(i)

print("Original List:", my_list)
print("Modified List:", mod_list)