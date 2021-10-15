# distance calculator algorithm

print("\nWelcome to the Distance Calculator algorithm")

u = float(input("Initial velocity (m/s): "))
a = float(input("Acceleration (m/s²): "))
t = float(input("Time taken (s): "))


# calculations
x = (u * t)
y = pow(t, 2)
z = (0.5 * a * y)
result = (u + z)

print("Distance calculator: {:.0f}m²" .format(result))