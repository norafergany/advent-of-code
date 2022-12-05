def part_1(file):
    full_overlap = 0
    with open(file) as f:
        lines = f.readlines()

        for line in lines:
            elves = line.split(',')
            elf_1 = elves[0].split('-')
            elf_2 = elves[1].split('-')
            first_start = int(elf_1[0])
            first_end = int(elf_1[1])
            second_start = int(elf_2[0])
            second_end = int(elf_2[1])

            if first_start > second_start:
                if second_end >= first_end:
                    full_overlap += 1

            elif second_start > first_start:
                if first_end >= second_end:
                    full_overlap += 1

            elif first_start == second_start:
                full_overlap += 1

        return full_overlap


print(part_1('input.txt'))


def part_2(file):
    overlap = 0
    with open(file) as f:
        lines = f.readlines()

        for line in lines:
            elves = line.split(',')
            elf_1 = elves[0].split('-')
            elf_2 = elves[1].split('-')
            first_start = int(elf_1[0])
            first_end = int(elf_1[1])
            second_start = int(elf_2[0])
            second_end = int(elf_2[1])

            if first_start > second_start:
                if second_end >= first_start:
                    overlap += 1

            elif second_start > first_start:
                if first_end >= second_start:
                    overlap += 1

            else:

                overlap += 1

        return overlap


print(part_2('input.txt'))
