import os
import csv


fresh = []
valid_ids = set()
fresh_id_section = False
total_fresh=0
inventory_ids = []
total_fresh_after=0
fresh_removal = []
fresh_new = []
removed_items = []
valid_ids_after = set()

def split_range(valid_range: str):
    min, max = valid_range.split('-')
    return int(min), int(max)

def check_id(id):
    global total_fresh
    for item in fresh:
        if id >= item[0] and id <= item[1]:
            total_fresh += 1
            valid_ids.add(id)
            return
        else:
            continue

with open('good_ids.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        if len(row) == 0:
            fresh_id_section = True
        if len(row) > 0 and not fresh_id_section:
            new_min,new_max = split_range(row[0])
            fresh.append([new_min, new_max])
        elif len(row) > 0:
            fresh_id = int(row[0])
            check_id(fresh_id)
            inventory_ids.append(fresh_id)

def optimize_fresh():
    fresh.sort(key=lambda x: (x[0], x[1]))
    merged = []
    for current in fresh:
        if not merged or current[0] > merged[-1][1] + 1:
            merged.append(current[:])
        else:
            merged[-1][1] = max(merged[-1][1], current[1])
    fresh.clear()
    fresh.extend(merged)

optimize_fresh()

total_valid = 0
for item in fresh:
    total_valid += item[1] - item[0] + 1

print(total_valid) 