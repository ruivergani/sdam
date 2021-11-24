import math

ages = [10, 18, 21, 15, 17]
last_checked = [1998, 2020, 2015, 2018, 2019]

# return an iterator with function applied to every element of one or more iterable
actual_age = map(
    lambda age, year: (2021 - year) + age,  # function (lambda arguments:expressions)
    ages, last_checked  # iterable (lists)
    )
# the age and year will go through the array (same way as item), they are control variables.

actual_age = list(actual_age)
print(actual_age)