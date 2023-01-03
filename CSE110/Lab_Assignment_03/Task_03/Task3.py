str_input = input()
binary = True

for i in str_input:
  if i not in "01":
    binary = False
    break

if binary:
  print("Binary Number")
else:
  print("Not a Binary Number")