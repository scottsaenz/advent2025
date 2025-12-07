import csv


def inv_cov(row):
    row = row.replace("L", "-").replace("R", "")
    return int(row)


with open("Day_1/input.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    numbers = [inv_cov(row[0]) for row in data]

num_zeros = 0
pointer = 50

for num in numbers:
    if num == 0:
        continue

    prev_pointer = pointer
    pointer += num

    full_rotations = abs(num) // 100
    num_zeros += full_rotations

    start = prev_pointer % 100
    end = pointer % 100

    if num > 0:
        if end <= start and start != 0:
            num_zeros += 1
        elif end == 0:
            num_zeros += 1
    else:
        if end >= start and start != 0:
            num_zeros += 1
        elif end == 0:
            num_zeros += 1

print(num_zeros)
