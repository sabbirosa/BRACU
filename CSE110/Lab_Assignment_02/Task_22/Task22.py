num_input = int(input())
output = ""

while num_input: 
    digit = num_input % 2
    output += str(digit)
    num_input //= 2

print(output[::-1])