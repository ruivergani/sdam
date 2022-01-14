# cans of paint exercise without user input

import math

can_diameter = 15
can_height = 30
can_raio = float(can_diameter / 2)
can_volume = math.ceil((3.14 * (can_raio * can_raio) * can_height))
box_volume = math.ceil(60 * 30 * 35)

area_paint = (140 * 3.4)  # m2 (30 * 3.4) + (30 * 3.4) + (60 * 3.4) + (60 * 3.4)
can_cover_measurement = 5.1  # m2
can_required = (area_paint / can_cover_measurement)

can_per_box = int((box_volume / can_volume))
print("\nVolume of a can: {} cm³" .format(can_volume))
print("Volume of a box: {} cm³" .format(box_volume))
print("Quantity of cans I can fit in 1 box: {} cans" .format(can_per_box))


amount_full_boxes = int((can_required / can_per_box))
total_cans_in_box = (can_per_box * amount_full_boxes)
remaining_cans = math.ceil((can_required - total_cans_in_box))

print("\n=====================================")
print("\nNumber of cans required: {}" .format(math.ceil(can_required)))  # (integer division area / cover of the pain)
print("Number of cans in box: {}" .format(can_per_box))  # volume of box / volume of can (integer)
print("Number of full boxes: {}" .format(amount_full_boxes))  # total can required / can per box = quantity of full boxes needed (integer)
print("Cans not packed in boxes: {}" .format(remaining_cans))  # can required - total quantity of cans in boxes (round up the value)

