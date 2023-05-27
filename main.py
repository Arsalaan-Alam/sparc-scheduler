# code to convert manual input of classes and students into JSON structure.
import json

schedule = []

while True:
    time = input("Enter the time slot (e.g., 10:30 AM - 11:30 AM) or type 'done' to finish: ")
    if time.lower() == 'done':
        break

    classes = []
    while True:
        class_name = input("Enter the class name or type 'done' to finish: ")
        if class_name.lower() == 'done':
            break

        roll_numbers = []
        while True:
            roll_number = input("Enter an eligible roll number or type 'done' to finish: ")
            if roll_number.lower() == 'done':
                break
            roll_numbers.append(roll_number)

        class_info = {
            "className": class_name,
            "eligibleRollNumbers": roll_numbers
        }
        classes.append(class_info)

    time_slot = {
        "time": time,
        "classes": classes
    }
    schedule.append(time_slot)

# Convert the data to JSON
json_data = json.dumps(schedule, indent=4)

# Save the JSON data to a file
with open('schedule.json', 'w') as file:
    file.write(json_data)

print("JSON data has been generated and saved to 'schedule.json'.")
