hours = int(input())

if hours < 0:
    print("Hour cannot be negative")
elif hours > 168:
    print("Impossible to work more than 168 hours weekly")
elif hours <= 40:
    salary = hours*200
    print(salary)
else:
    extra_hours = hours - 40
    salary = (hours-extra_hours)*200 + (extra_hours*300)
    print(salary)