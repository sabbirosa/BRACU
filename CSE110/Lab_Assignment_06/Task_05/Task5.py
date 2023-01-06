#Task5 #Done
age = int(input())
salary = int(input())
designation = input()

def calculate_tax(age, salary, designation):
    if age < 18 or designation == "President".casefold() or salary < 10000:
        tax = 0
    else:
        if 10000 <= salary <= 20000:
            tax = salary * 0.05
        else:
            tax = salary * 0.10
    
    return tax

print(calculate_tax(age, salary, designation))