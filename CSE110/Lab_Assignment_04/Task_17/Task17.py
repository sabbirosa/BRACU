list_input = input().strip()
my_list = []
mod_list = []

for i in list_input.split(", "):
  my_list.append(int(i.strip()))

for i in my_list:
  if i not in mod_list:
    mod_list.append(i)

print("Given numbers in list:", my_list)
print("List without any dupliacte values:", mod_list)