str_input = input()
new_str = ""
previous_str = ""
  
for i in str_input:
  if i == previous_str:
      continue
  else:
      new_str += i
      previous_str = i

print(new_str)