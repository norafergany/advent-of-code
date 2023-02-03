# Thanks to https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day07p1.py for this solution
def create_file_system(file):
    cwd = root = {}
    stack = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line[0] == "$":
                cmd_list = line.split(" ")
                cmd = cmd_list[1]
                if cmd == "cd":

                    curr_dir = cmd_list[2]
                    if curr_dir == "/":
                        cwd = root
                        stack = []
                    elif curr_dir == "..":
                        cwd = stack.pop()
                    else:
                        if curr_dir not in cwd:
                            cwd[curr_dir] = {}
                        stack.append(cwd)
                        cwd = cwd[curr_dir]
            else:
                x, y = line.split()
                if x == "dir":
                    if y not in cwd:
                        cwd[y] = {}
                else:
                    cwd[y] = int(x)
        return root


root = create_file_system('test-input.txt')
print(root)


def calc_sizes(dir=root):
    size = 0
    total_size = 0
    if type(dir) == int:
        return dir, 0
    for child in dir.values():
        s, t = calc_sizes(child)
        size += s
        total_size += t
    if size <= 100000:
        total_size += size
    return size, total_size


print(calc_sizes(root))

def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

print(size(root))
# def delete_size(dir=root):
#     size = 0
#     total_size = 0
#     sizes = {}
#     if type(dir) == int:
#         return dir
#     for key, child in dir.items():
#         s = delete_size(child)
#         print(size)
#         print(s)
#         size += s
#         # total_size += t
#     sizes[key] = size
#
#     return sizes
#
#
# print(delete_size(root))
