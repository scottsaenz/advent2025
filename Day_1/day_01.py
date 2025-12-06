import csv

def inv_cov(row):
    row = row.replace('L','-').replace('R','')
    return int(row)


with open('Day_1/input.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    numbers = [inv_cov(row[0]) for row in data]

num_zeros = 0
pointer = 50
for num in numbers:
    pointer += num
    if pointer % 100 == 0:
        num_zeros += 1

print(num_zeros)