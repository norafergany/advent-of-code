import functools
import re
from collections import defaultdict


def supply_stack(file):
    with open(file) as f:
        lines = f.read()

        # Assign the rows and instructions to different arrays
        rows, steps = lines.split('\n\n')

        # Array: crates grouped by level across all the stacks
        # ['    [D]', '[N] [C]', '[Z] [M] [P]']
        rows = rows.split('\n')
        steps = steps.strip().split('\n')
        labels = rows.pop(-1).strip()

        stacks = defaultdict(list)

        # For each set of crates in a level
        for stack in rows:
            for i, crate in enumerate(stack[1::4]):
                if crate != " ":
                    stacks[i + 1].append(crate)

        instructions = defaultdict(list)

        for i, step in enumerate(steps):
            array = re.findall(r'[0-9]+', step)
            instructions[i] = [int(x) for x in array]

        for i in instructions:
            num = instructions.get(i)[0]
            from_stack = instructions.get(i)[1]
            to_stack = instructions.get(i)[2]
            moved_crates = (stacks[from_stack][:num])
            moved_crates.reverse()

            del stacks[from_stack][:num]

            stacks[to_stack] = moved_crates + stacks[to_stack]

        top_crates = ''
        for i in range(len(stacks)):
            top_crate = stacks.get(i + 1)[0]
            top_crates += top_crate
        print(top_crates)


supply_stack('input.txt')
