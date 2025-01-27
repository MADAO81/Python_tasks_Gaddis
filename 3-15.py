seconds= int(input("Enter the quantity of seconds:"))
minutes = 0
hours = 0
days = 0
seconds_per_minute = 60
seconds_per_hour = 3600
seconds_per_day = 86400

if seconds >=60:
    days = seconds // seconds_per_day
    hours = (seconds % seconds_per_day) // seconds_per_hour
    minutes = (seconds % seconds_per_hour) // seconds_per_minute
    seconds = seconds % seconds_per_minute
    print(days,"days", hours,"hours",minutes,"minutes",seconds,"seconds")
else:
    print(days,"days", hours,"hours",minutes,"minutes",seconds,"seconds")
    