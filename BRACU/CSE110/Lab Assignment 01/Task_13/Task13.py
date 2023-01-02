mark  = int(input())

if mark >= 0 and mark <= 100:
    if mark >= 90:
        print("A")
    elif mark >= 80:
        print("B")
    elif mark >= 70:
        print("C")
    elif mark >= 60:
        print("D")
    elif mark >= 50:
        print("E")
    else:
        print("F")

else:
    print("Wrong mark")