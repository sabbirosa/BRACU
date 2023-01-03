num_input = int(input())
num = num_input
lenght = 0
count = 0

while num != 0:
    num //= 10
    lenght += 1

while num_input != 0:
    digit = num_input // (10**(lenght-1))
    num_input %= (10**(lenght-1))
    lenght -= 1
    count += 1
    if num_input == 0:
        print(digit)
    else: 
        print(digit, end = ", ")