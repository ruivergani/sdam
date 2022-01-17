# first version of phone algorithm

import math

OUNCE = 0.035271

phone1 = "Nokia 220"
phone2 = "Alcatel 1X"
phone3 = "Motorola Moto E6 Play"

g_phone1 = 86.5
g_phone2 = 130
g_phone3 = 140

oz_phone1 = g_phone1 * OUNCE
oz_phone2 = g_phone2 * OUNCE
oz_phone3 = g_phone3 * OUNCE

print(
    "Phone".ljust(22), "|",
    "Grams".rjust(6), "|",
    "Ounces".rjust(6),
    sep="")

print("=".center(36, "="))

print(
    phone1.ljust(22), "|",
    str(g_phone1).rjust(6), "|",
    str(round(oz_phone1,2)).rjust(6),
    sep="")
