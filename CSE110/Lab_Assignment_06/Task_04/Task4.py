def case_counter(string):
    upper_count = 0
    lower_count = 0

    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
        else:
            continue

    print("No. of Uppercase characters:", upper_count)
    print("No. of Uppercase characters:", lower_count)

case_counter('The quick Sand Man')