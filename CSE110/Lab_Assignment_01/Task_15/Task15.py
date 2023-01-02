distance  = int(input())
time  = int(input())

velocity = (distance/1000)/(time/3600)
print(velocity, "km/h")

if velocity < 60:
    print("Too slow. Needs more changes")
elif velocity >= 60 and velocity < 90:
    print("Velocity is okay. The car is ready!")
else:
    print("Too fast. Only a few changes should suffice.")