import csv

with open('/Users/scottsaenz/Projects/Advent2025/Day_2/input.txt') as f:
    reader = csv.reader(f,delimiter=',')
    data = list(reader)[0]

# split each element into min max of a range
ranges = [tuple(map(int, item.split('-'))) for item in data]

# get products of the range of length for the min/max of each range
def get_products(str_len):
    products = []
    for r in range(str_len):
        if r < 1:
            continue
        if str_len % r == 0:
            products.append(r)
    return products

def generate_patterns(num_length):
    """
    
    """
    return range(10**(num_length - 1), 10**num_length)

# create set of invalid patterns within range
def invalid_patterns(min_val, max_val):
    invalids = set()
    len_min_val = len(str(min_val))
    len_max_val = len(str(max_val))
    for current_len in range(len_min_val, len_max_val + 1):
        pattern_lengths = get_products(current_len)
        # for each pattern length, create a pattern of digits
        for pattern_length in pattern_lengths:
            patterns = generate_patterns(pattern_length)
            if current_len % pattern_length == 0:
                multiple = current_len // pattern_length

                # create a range of numbers that are multiples of the pattern
                for pattern in patterns:
                    str_pattern = str(pattern)
                    full_pattern = str_pattern * multiple
                    num_pattern = int(full_pattern)
                    if num_pattern >= min_val and num_pattern <= max_val:
                        invalids.add(num_pattern)
    

    return invalids

final_invalids = set()

for r in ranges:
    min_val, max_val = r
    invalids = invalid_patterns(min_val, max_val)
    final_invalids = final_invalids.union(invalids)



final_invalids_list = list(final_invalids)
final_invalids_list.sort()
print(sum(final_invalids))
print('done')


# expected 1227775554 
# got 1227774445
# try number 2 
# 1227776664

# too high 19058204438