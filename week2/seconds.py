#seconds exercise

seconds = int(input("Type seconds: "))

#calculations

hours = int((seconds / 3600))
minutes = int((((seconds % 3600) / 3600) * 60))
seconds_result = (seconds - ((hours * 3600) + (minutes * 60)))
print("\n{:<10}{:<15}{:<15}{:<20}" .format("Input", "Hours", "Minutes", "Seconds"))
print("{:<10.0f}{:<15.0f}{:<15.0f}{:<20.0f}" .format(seconds, hours, minutes, seconds_result))