import re


def file_cleanup(file):
    dirs = {}
    is_dir = False
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("$"):
                parts = line.strip().split(" ")
                cmd = parts[1]

                if cmd == "cd":
                    dir_name = parts[2]
                    dirs[dir_name] = {}
                    is_dir = True
                    dir_dict = {}
                if cmd == "ls":
                    continue
            elif re.search(r'^\d[^\s]+', line):
                file_size_re = re.search(r'^\d[^\s]+', line)
                file_size = file_size_re.group()
                file_name_r = re.search(r'(?<=\s)[\w+\.+]+', line)
                file_name = file_name_r.group()
                print(file_size)
                print(file_name)
                dirs[dir_name][file_name] = int(file_size)
            elif line.startswith("dir"):
                inside_dir = line.strip().split(' ')[1]
                dirs[inside_dir] = {}
    print(dirs)


                # file_dir[file_name] = file_size


print(file_cleanup('test-input.txt'))
