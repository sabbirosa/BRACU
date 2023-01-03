num_input = int(input())
counter = 2
n1 = 0
n2 = 1

print(n1, n2, end = " ")

for counter in range(2, num_input):
    n = n1 + n2
    if n > num_input:
      break
    print(n, end = " ")
    n1 = n2
    n2 = n