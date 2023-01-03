start = int(input())
end = int(input())
prime_numbers = []
perfect_numbers = []

for num in range(start, end+1):

  #Code for Perfect Number
  counter = 0
  sum = 0

  while counter <= num:
    counter += 1
    if num % counter == 0:
      sum += counter

  sum -= num

  if sum == num:
    perfect_numbers.append(str(num))

  #Code for Perfect Number
  counter = 0
  divisor_count = 0

  while counter <= num:
    counter += 1
    if num % counter == 0:
      divisor_count += 1

  if divisor_count == 2:
    prime_numbers.append(str(num))
  
print(f"Between {start} and {end},")
print(f"Found {len(prime_numbers)} prime numbers")
print(f"Found {len(perfect_numbers)} perfect number")
print(f"Prime numbers: {', '.join(prime_numbers)}")
print(f"Perfect number: {', '.join(perfect_numbers)}")