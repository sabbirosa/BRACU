num_input = int(input()) 
counter = 0
sum = 0

while num_input: 
    digit = num_input % 10
    num_input //= 10
    sum += digit*(2**counter)
    counter += 1

print(sum)