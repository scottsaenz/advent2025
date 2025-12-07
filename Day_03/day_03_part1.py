import csv

with open("Day_03/input.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

init_list = []
for datum in data:
    init_list.append(datum[0])

print("temp")
batt_voltages = []

for battery in init_list:
    first_digit = int(battery[0])
    second_digit = int(battery[1])
    second_starting_point = 1
    for slot in range(1, len(battery) - 1):
        if int(battery[slot]) > first_digit:
            first_digit = int(battery[slot])
            second_digit = int(battery[slot + 1])
            second_starting_point = slot + 1

    for slot in range(second_starting_point, len(battery)):
        if int(battery[slot]) > second_digit:
            second_digit = int(battery[slot])

    batt_voltage = int(str(first_digit) + str(second_digit))
    batt_voltages.append(batt_voltage)

total_voltage = sum(batt_voltages)
print(total_voltage)
