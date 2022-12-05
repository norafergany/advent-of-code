def create_priority_map():
    priority_points = {

    }

    lowercase_start = 97
    uppercase_start = 65
    for j in range(1, 27):
        priority_points[chr(lowercase_start)] = j
        lowercase_start += 1
    for j in range(27, 53):
        priority_points[chr(uppercase_start)] = j
        uppercase_start += 1

    return priority_points


def part_1(file):
    total_sum = 0
    priority_points = create_priority_map()
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            midpt = len(line) // 2
            part_1_items = set(line[0:midpt])
            part_2_items = set(line[midpt:len(line)])

            misplaced = part_1_items.intersection(part_2_items)
            item = next(iter(misplaced))
            total_sum += priority_points.get(item)

    return total_sum


print(part_1('input.txt'))


def part_2(file):
    total_sum = 0
    priority_points = create_priority_map()

    with open(file) as f:
        lines = f.readlines()

        for i in range(0, len(lines), 3):
            line_1 = lines[i].strip()
            line_2 = lines[i + 1].strip()
            line_3 = lines[i + 2].strip()
            elf_1_items = set(line_1)
            elf_2_items = set(line_2)
            elf_3_items = set(line_3)

            badge = elf_1_items.intersection(elf_2_items, elf_3_items)
            item = next(iter(badge))
            total_sum += priority_points.get(item)

    return total_sum


print(part_2('input.txt'))
