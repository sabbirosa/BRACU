def print_string(string):
  char_dict = {}
  msg = "PSG will win the Champions League this season"

  for i in string.lower():
    if 'a' <= i <= 'j':
      if i not in char_dict:
        char_dict[i] = 1
      else:
        char_dict[i] += 1
    
  if len(char_dict) == 10:
    for i in range(5):
      print(msg)
    return
  else:
    for i in range(6):
      print(msg)
    return
  
  
string_input = input()
print_string(string_input)