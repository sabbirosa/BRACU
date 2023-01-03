str_input = input()
input_num = int(input())

rev_str = str_input[:input_num+1][::-1]
rem_str = str_input[input_num+1:]

print(rev_str + rem_str)