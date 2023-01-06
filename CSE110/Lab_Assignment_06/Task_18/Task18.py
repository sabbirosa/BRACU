def div_check(starting_value, ending_value, first_divisor, second_divisor):
  sum_ = 0

  for i in range(starting_value, ending_value):
    if i % first_divisor == 0 and i % second_divisor == 0:
      continue
    if i % first_divisor == 0 or i % second_divisor == 0:
      sum_ += i

  print(sum_)

starting_value = int(input())
ending_value = int(input())
first_divisor = int(input())
second_divisor = int(input())

div_check(starting_value, ending_value, first_divisor, second_divisor)