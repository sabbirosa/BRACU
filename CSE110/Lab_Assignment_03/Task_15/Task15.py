str_input = input()
uppercase = True

for i in str_input:
  if "a" <= i <= "z" or "A" <= i <= "Z":
    if uppercase:
      print(i.upper(), end = "")
      uppercase = False
    else:
      print(i.lower(), end = "")
      uppercase = True
  else:
    print(i, end = "")

print()