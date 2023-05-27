import random
import json

class_names = []
time_slots = ["10:30 AM - 11:30 AM", "11:30 AM - 12:30 PM", "12:30 PM - 1:30 PM"]
students = ["4618", "5222", "4058", "9022", "3292", "5474", "4834", "2190", "9763", "1249", "8952", "2895"]

# Prompt for class names
for i in range(3):
    class_name = input(f"Enter the name of class {i+1}: ")
    class_names.append(class_name)

schedule = []

# Create the schedule for each time slot
for time_slot in time_slots:
    classes = []

    # Assign students to classes
    for class_name in class_names:
        if len(students) < 4:
            print("Error: Insufficient number of students available.")
            exit(1)

        eligible_students = random.sample(students, 4)
        students = [student for student in students if student not in eligible_students]

        class_info = {
            "className": class_name,
            "eligibleRollNumbers": eligible_students
        }
        classes.append(class_info)

    time_slot_info = {
        "time": time_slot,
        "classes": classes
    }
    schedule.append(time_slot_info)

# Repeat the schedule for 2 more times
for i in range(2):
    schedule.extend(schedule)

# Convert the data to JSON
json_data = json.dumps(schedule, indent=4)

# Save the JSON data to a file
with open('schedule.json', 'w') as file:
    file.write(json_data)

print("JSON data has been generated and saved to 'schedule.json'.")
