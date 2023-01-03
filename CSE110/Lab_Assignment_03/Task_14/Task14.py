str_input = input()
num_input = int(input())

if num_input % 2 == 0:
    print(str_input * (num_input * 2))
else:    
    print(str_input * (num_input * 3))