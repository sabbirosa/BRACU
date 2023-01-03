str_input = input()
split_chr = input()

for i in str_input:
    if i is split_chr:
        print()
        continue
    print(i, end = "")