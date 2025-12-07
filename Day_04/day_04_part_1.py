import csv

with open("Day_04/input.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

# remove list from list of lists
data = [item for sublist in data for item in sublist]

print("read data")

x = len(data[0])
y = len(data)


access = 0
valid_rolls = []

range_x = range(x)
range_y = range(y)

for i in range_x:
    for j in range_y:
        if data[i][j] == ".":
            continue
        if i > 0:
            start_x = i - 1
        else:
            start_x = i
        if i < x - 1:
            end_x = i + 1
        else:
            end_x = i
        if j > 0:
            start_y = j - 1
        else:
            start_y = j
        if j < y - 1:
            end_y = j + 1
        else:
            end_y = j
        sub_x = 0
        sub_y = 0
        count_rolls = 0
        for x_eval in range(start_x, end_x + 1):
            for y_eval in range(start_y, end_y + 1):
                if x_eval == i and y_eval == j:
                    continue
                if data[x_eval][y_eval] == "@":
                    count_rolls += 1

        if count_rolls < 4:
            access += 1
            valid_rolls.append((i, j))
print(access)
