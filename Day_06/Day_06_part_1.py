import csv
import numpy as np

with open('Day_06/input.csv') as f:
    reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
    data = [list(row) for row in reader]

# Convert all rows except the last to integers
data_numbers = [[int(item) for item in row if item] for row in data[:-1]]
data_operators = data[-1]

arr = np.array(data_numbers)
# transpose the array
arr = arr.T
print('done')

grand_total = 0 

for i in range(arr.shape[0]):
    if data_operators[i] == '*':
        total = np.prod(arr[i])
    else:
        total = np.sum(arr[i])
    grand_total += total

print(grand_total)
