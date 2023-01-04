list_input = input()
print("Original data:", list_input)

list_input = list_input.strip()

if list_input[0] == "[" and list_input[-1] == "]":
  list_input = list_input[1:-1]
  print("After removing square brackets:", list_input)
else:
  print("After removing square brackets:", list_input)

list_input = list_input.split(",")
print("Numbers in string format with extra white spaces:", list_input)

final_list = []

for i in list_input:
  final_list.append(int(i.strip()))

print("Final data (numbers in list format):", final_list)