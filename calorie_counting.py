def count_calories(file):
    max_cal = 0
    curr_sum = 0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                # line = num
                curr_sum += int(line)
            if not line.strip():
                max_cal = max(max_cal, curr_sum)
                curr_sum = 0
            if line == lines[-1] and not line.strip():
                curr_sum += int(line)
                max_cal = max(max_cal, curr_sum)
    return max_cal


print(count_calories('input.txt'))

"""
if you had all sums in array, \\

50 83 64 23 08 65 268 964

get the first 3 nums, then compare each num to all the other nums
"""