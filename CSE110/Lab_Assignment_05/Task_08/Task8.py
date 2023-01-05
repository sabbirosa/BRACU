my_dict = input()[1:-1]
sum = 0
i_count = 0

for i in my_dict.split(", "):
  i_count += 1
  sum += int(i.split(":")[1])

print("Average is", sum//i_count)