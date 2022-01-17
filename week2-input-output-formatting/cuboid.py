# cuboid algorithm

width = int(input("Type the width (m): "))
height = int(input("Type the height (m): "))
length = int(input("Type the length (m): "))

# calculate surface area:

volume_cuboid = (width * height * length)
surface_area = 2 * ((width * length) + (width * height) + (length * height))

print("\nSurface area: {} m²" .format(surface_area))
print("Volume area: {} m³ " .format(volume_cuboid))
