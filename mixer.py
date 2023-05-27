import json

students = ["4618", "5222", "4058", "9022", "3292", "5474", "4834", "2190", "9763", "1249", "8952", "2895"]
time_slots = ["10:30 AM - 11:30 AM", "11:30 AM - 12:30 PM", "12:30 PM - 1:30 PM"]

schedule = []

for time_slot in time_slots:
    classes = []

    for i in range(3):
        class_name = input(f"Enter the name of class {i+1}: ")

        # Select four students for the class
        eligible_students = students[i*4:(i+1)*4]

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

# Convert the data to JSON
json_data = json.dumps(schedule, indent=4)

# Save the JSON data to a file
with open('schedule1.json', 'w') as file:
    file.write(json_data)

print("JSON data has been generated and saved to 'schedule.json'.")
