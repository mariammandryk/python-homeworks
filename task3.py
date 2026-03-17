# Ask the user to enter the number of minutes
minutes = int(input("Enter the number of minutes: "))

# Calculate hours and remaining minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# Print the result
print(hours, "hours", remaining_minutes, "minutes")