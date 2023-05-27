import json

students = ["4618", "5222", "4058", "9022", "3292", "5474", "4834", "2190", "9763", "1249", "8952", "2895"]
time_slots = ["10:30 AM - 11:30 AM", "11:30 AM - 12:30 PM", "12:30 PM - 1:30 PM"]

schedule = []

class_names = []
for _ in range(3):
    class_name = input("Enter the name of the class: ")
    class_names.append(class_name)

class_index = 0
for _ in range(3):
    classes = []

    for _ in range(3):
        class_name = class_names[class_index]

        # Select four students for the class
        eligible_students = students[:4]
        students = students[4:]

        class_info = {
            "className": class_name,
            "eligibleRollNumbers": eligible_students
        }
        classes.append(class_info)

        class_index = (class_index + 1) % 3

    time_slot_info = {
        "time": time_slots.pop(0),
        "classes": classes
    }
    schedule.append(time_slot_info)

# Convert the data to JSON
json_data = json.dumps(schedule, indent=4)

# Save the JSON data to a file
with open('schedule.json', 'w') as file:
    file.write(json_data)

print("JSON data has been generated and saved to 'schedule.json'.")
