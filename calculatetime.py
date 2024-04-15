from datetime import datetime, timedelta

# Function to get a valid time input from the user in 12-hour format
def get_valid_time_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_time = datetime.strptime(user_input, "%I:%M %p")
            return user_time
        except ValueError:
            print("Invalid time format. Please use hh:mm AM/PM.")

# Function to write total hours to a file
def write_total_hours_to_file(filename, date, total_hours,time1,time2):
    fixed_time =9.30
    t1=time1
    t2=time2
    time_difference = total_hours - fixed_time
    ans=round(time_difference,2)
    with open(filename, "a+") as file:
        file.write(f"======>> FOR THIS [{date.strftime('%Y-%m-%d')}] TOTAL TIME IS ATTEND BY YOU: {total_hours} hours <<=======\n")
        file.write(f"======>>[ CHECKIN TIME:-{t1} ]\n")
        file.write(f"======>>[ CHECKOUT TIME:-{t2} ]\n")
        if time_difference >= 1:
            file.write(f"------> TIME IS REMAIN FOR THIS DAY IS {ans} hours \n")
        else:
            file.write(f"------> TIME IS REMAIN FOR THIS DAY IS {ans} minite \n")
            
        
# Get the first time from the user
print("Enter the first time (hh:mm AM/PM):")
time1 = get_valid_time_input("")
# Get the second time from the user
print("Enter the second time (hh:mm AM/PM):")
time2 = get_valid_time_input("")

# Calculate the time difference in hours
time_difference = abs(time1 - time2)
total_hours = time_difference.total_seconds() / 3600

# Get the current date
current_date = datetime.now()

# Write total hours to a file with the current date
filename = "total_hours_2024.txt"
write_total_hours_to_file(filename, current_date, total_hours,time1,time2)

print(f"The total hours between the two times is: {total_hours} hours.")
print(f"Total hours for {current_date.strftime('%Y-%m-%d')} has been saved to {filename}.")
