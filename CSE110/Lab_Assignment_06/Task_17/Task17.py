def remove_odd(nums):
  evens = []

  for i in nums:
    if i % 2 == 0:
      evens += [i]
      
  print(evens)

remove_odd([11, 2, 3, 4, 5, 2, 0, 5, 3])