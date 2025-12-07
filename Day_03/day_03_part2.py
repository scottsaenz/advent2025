import csv


def find_max_n_digits(battery, n):
    """
    Find n digits from battery string where each digit is the maximum
    possible from its starting position onward, with each subsequent digit
    starting after the previous one.
    """
    if n > len(battery):
        return int(battery)

    digits = []
    start_pos = 0

    for digit_num in range(n):
        # How many positions do we need to reserve for remaining digits?
        remaining_digits = n - digit_num - 1
        # Search up to the point where we can still fit remaining digits
        search_end = len(battery) - remaining_digits

        max_digit = int(battery[start_pos])
        max_pos = start_pos

        for pos in range(start_pos, search_end):
            if int(battery[pos]) > max_digit:
                max_digit = int(battery[pos])
                max_pos = pos

        digits.append(str(max_digit))
        start_pos = max_pos + 1

    return int("".join(digits))


with open("Day_03/input.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

init_list = []
for datum in data:
    init_list.append(datum[0])

# Change n to whatever you need
n = 12  # Number of digits to extract
batt_voltages = []

for battery in init_list:
    batt_voltage = find_max_n_digits(battery, n)
    batt_voltages.append(batt_voltage)

total_voltage = sum(batt_voltages)
print(total_voltage)
