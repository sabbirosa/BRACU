# a) 24, 18, 12, 6, 0, -6
counter = 24

while counter >= -6:

    if counter == -6:
        print(counter) 
    else:
        print(counter, end = ", ") 
     
    counter = counter - 6 

# b) -10, -5, 0, 5, 10, 15, 20
for counter in range(-10, 21, 5):
    if counter == 20:
        print(counter) 
    else:
        print(counter, end = ", ")

# c) 18, 27, 36, 45, 54, 63
counter = 18

for counter in range(18, 64, 9):
    if counter == 63:
        print(counter) 
    else:
        print(counter, end = ", ")

# d) 18, -27, 36, -45, 54, -63
for counter in range(18, 64, 9):
    if counter % 2 != 0:
      if counter == 63:
          print("-" + str(counter)) 
      else:
          print("-" + str(counter), end = ", ")
    else:
      if counter == 63:
          print(counter) 
      else:
          print(counter, end = ", ")