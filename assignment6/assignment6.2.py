seconds = int(input("Enter seconds: "))

days = seconds // (24 * 60 * 60)
seconds_left = seconds % (24 * 60 * 60)

hours = seconds_left // (60 * 60)
seconds_left = seconds_left % (60 * 60)

minutes = seconds_left // 60
seconds_left = seconds_left % 60

if days == 1:
    day_word = "day"
else:
    day_word = "days"

print(str(days) + " " + day_word + ", " + str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds_left).zfill(2))