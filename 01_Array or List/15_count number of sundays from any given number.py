


# Start counting from the next day
def sunday_count_v3(arr,start_day,n):
    
    index = (arr.index(start_day.lower()) + 1) % 7
    count = 0
    for day in range(n):
        if arr[(index + day) % 7] == "sun":
            count += 1

    return count
    
arr = ["sun","mon","tue","wed","thu","fri","sat"]
print(sunday_count_v3(arr, "mon" , 13))


# or dificult to understand

days_index = {
    "sun": 0,
    "mon": 1,
    "tues": 2,
    "wednes": 3,
    "thurs": 4,
    "fri": 5,
    "satur": 6
}

start_day = input("Enter start day: ").strip().lower()
total_days = int(input("Enter total days: "))

start_index = days_index[start_day]

if start_index == 0:
    days_to_first_sunday = 7  # Skip first day if it’s Sunday
else:
    days_to_first_sunday = 7 - start_index


sundays = 0

# Check if the first Sunday falls within the total days
if days_to_first_sunday <= total_days:
    sundays = 1  # Count first Sunday

    remaining_days = total_days - days_to_first_sunday
    sundays += remaining_days // 7  # Count remaining Sundays every 7 days

print("Total Sundays:", sundays)