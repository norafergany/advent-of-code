def count_calories(file):
    calorie_sums = []
    curr_sum = 0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                curr_sum += int(line)
            if not line.strip():
                calorie_sums.append(curr_sum)
                curr_sum = 0
            if line == lines[-1] and not line.strip():
                curr_sum += int(line)
                calorie_sums.append(curr_sum)

    top_cal_sums = sorted(calorie_sums, reverse=True)

    top_three_sums = (top_cal_sums[0]) + (top_cal_sums[1]) + (top_cal_sums[2])

    print(f'The total calories from the top 3 elves is: {top_three_sums}')

    print(f'The total calories from the top elf is: {top_cal_sums[0]}')


def main():
    count_calories('day_1/files/input.txt')


if __name__ == "__main__":
    main()
