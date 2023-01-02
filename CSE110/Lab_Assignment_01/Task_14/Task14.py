tem_fer  = int(input())

tem_cel = int(((tem_fer) - 32) * 0.56)
print(tem_cel, "degrees C")

if tem_cel < 20:
    print("Winter")
elif tem_cel >= 20 and tem_cel < 25:
    print("Autumn")
elif tem_cel >= 25 and tem_cel < 30:
    print("Spring")
else:
    print("Summer")