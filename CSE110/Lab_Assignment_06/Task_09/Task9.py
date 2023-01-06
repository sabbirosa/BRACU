import math


def area_circumference_generator(radius):
    result = (math.pi * radius**2, 2 * math.pi * radius)
    return result

result = area_circumference_generator(1)
print(result)

area, circumference = result
print("Area of the circle is", area, "and circumference is", circumference)