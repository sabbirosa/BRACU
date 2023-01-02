cgpa  = float(input())
credits  = int(input())

if cgpa <= 4:
    if cgpa >= 3.8 and credits >= 30:
        if cgpa == 4:
            print("The student is eligible for a waiver of 100 percent.")
        elif cgpa >= 3.95 and cgpa <= 3.99:
            print("The student is eligible for a waiver of 75 percent.")
        elif cgpa >= 3.9 and cgpa <= 3.94:
            print("The student is eligible for a waiver of 50 percent.")
        else:
            print("The student is eligible for a waiver of 25 percent.")       
    else:
        print("The students is not eligible for a waiver")
else:
    print("CGPA can't be greater than 4")