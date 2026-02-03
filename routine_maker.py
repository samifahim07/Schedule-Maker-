

routine = {}

week_days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

days = int(input("How many days you want to plan? (1-7): "))

if days < 1 or days > 7:
    print("Invalid number of days!")
    exit()
for i in range(days):
    routine[week_days[i]] = {}

# Add tasks
while True:
    print("\n--- ADD A TASK ---")
    print("Days Available:")
    for d in routine:
        print(d)
    
    day_choice = input("Choose a day: ")
    if day_choice not in routine:
        print("Invalid day!")
        continue

    time = input("Enter the time (HH:MM): ")
    if time in routine[day_choice]:
        print("You already have something at that time!")
        continue

    task = input("Enter your task: ")
    routine[day_choice][time] = task

    again = input("Do you want to add another task? (y/n): ").lower()
    if again != 'y':
        break

# Show routine
print("\nYour Routine:")
for day in routine:
    print(day + ":")
    for time in routine[day]:
        print(time + " -> " + routine[day][time])
