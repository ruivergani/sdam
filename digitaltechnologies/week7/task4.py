import math


# radius
r = int(input("Type the radius: "))

area = (math.pi * (pow(r, 2)))
circumference = (2 * math.pi * r)

print("Area: {:.2f}" .format(area))
print("Circumference: {:.2f}" .format(circumference))
