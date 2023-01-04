str_input = input()
my_list = []
mod_list = []

for i in str_input.split(", "):
  my_list.append(int(i))
  if int(i) not in mod_list:
    mod_list.append(int(i))

print("Original list:", my_list)
print("Modified list:", mod_list)