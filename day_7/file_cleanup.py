import re

"""
build a dict maps each directory to file contents
build dict that maps each directory to its parent

simple_dirs dict: dirs & their children 1 level (child dirs but not their children)
when you cd to a folder initiate empty dict curr_dir_contents, add filenames to filesizes, dirs map to file_size -1
add that dict to the simple_dirs dict
when you iterate through to sum total, if you find dir with filesize -1, get that dirs contents also, 
and keep going till there aren't any dirs left 


add child dirs and files to root dir, with dirs having a file size of -1 (make sure not to add these to the total)
when you enter another directory, create an empty dict for it
add it to the dirs directory with child dirs and file





"""


def file_cleanup(file):
    simple_dirs = {}
    parents = {}
    parent_child = {}
    dir_sizes = {}
    with open(file) as f:

        lines = f.readlines()
        i = 0
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith("$"):
                cmd_line = line.strip().split(" ")
                cmd = cmd_line[1]

                if cmd == "cd":

                    # curr_dir = parts[2]
                    # TODO parents
                    if cmd_line[2] == "..":
                        # print(i)
                        # print(curr_dir)
                        curr_dir = parents[curr_dir]
                        # print(curr_dir)
                    else:
                        curr_dir = cmd_line[2]
                    if curr_dir not in simple_dirs:
                        curr_dir_dict = {}

                        simple_dirs[curr_dir] = curr_dir_dict
                    # is_dir = True
                    # dir_dict = {}

                if cmd == "ls":
                    continue
            elif line.startswith("dir"):
                dir_child = line.strip().split(' ')[1]
                # print(dir_child)
                curr_dir_dict[dir_child] = -1
                # if dir_child not in dirs:
                #     new_dir_dict = {}
                #     dirs[curr_dir] = new_dir_dict
                parents[dir_child] = curr_dir
                # dirs[curr_dir] =
                # print(i, dirs)

            elif re.search(r'^\d[^\s]+', line):
                file_size_re = re.search(r'^\d[^\s]+', line)
                file_size = file_size_re.group()
                file_name_r = re.search(r'(?<=\s)[\w+\.+]+', line)
                file_name = file_name_r.group()
                # print(file_size)
                # print(file_name)
                curr_dir_dict[file_name] = int(file_size)
                simple_dirs[curr_dir] = curr_dir_dict
                # if curr_dir in dirs:
                #     dirs[curr_dir][file_name] = int(file_size)
                # else:
                #     parent_key = parents[curr_dir]
                #     dirs[parent_key] = dirs[curr_dir]
    print(simple_dirs)
    print(parents)

    for folder, contents in simple_dirs.items():
        print("item ", contents)

        # print(contents.values())
        dir_sizes[folder] = 0
        for f_name, item in contents.items():
            if folder != "/":

                if item != -1:
                    print("file")
                    dir_sizes[folder] += item
                    print(dir_sizes[folder])

    for child, parent in parents.items():
        if parent != "/":
            dir_sizes[parent] += dir_sizes[child]
    
    for folder, contents in simple_dirs.items():
        # print("item ", contents)

        # print(contents.values())
        # dir_sizes[folder] = 0
        for f_name, item in contents.items():
            if folder != "/":

                if item == -1:
                    print(f_name, " file", dir_sizes[f_name])
                    dir_sizes[folder] += dir_sizes[f_name]
                    print(dir_sizes[folder])
                # else:
                #     print("dir")
                #     if f_name in dir_sizes:
                #         dir_sizes[folder] += dir_sizes[f_name]
    # print(dir_sizes)
    for child, parent in parents.items():
        if parent != "/":
            dir_sizes[parent] += dir_sizes[child]

    total_sum = 0
    for size in dir_sizes.values():
        if size <= 100000:
            print(size)
            total_sum += size

    print(dir_sizes)

    print(total_sum)

    # simple_dirs[item]
    # for k, v in contents:
    #     print(k, v)


# def file_cleanup(file):
#
#     dirs = {}
#     is_dir = False
#     parents = {}
#     with open(file) as f:
#         lines = f.readlines()
#         i = 0
#         for i in range(len(lines)):
#             line = lines[i]
#             inside_dirs = {}
#             if i == 0:
#                 curr_dir = line.strip().split(" ")[2]
#                 print("0 ", curr_dir)
#                 inside_dir = line.strip().split(" ")[2]
#                 parents[None] = curr_dir
#                 dirs[curr_dir] = {}
#                 dir_dict = {}
#             if line.startswith("$") and i != 0:
#                 parts = line.strip().split(" ")
#                 cmd = parts[1]
#
#                 if cmd == "cd":
#
#                     # curr_dir = parts[2]
#                     if parts[2] == "..":
#                         print(i)
#                         print(curr_dir)
#                         curr_dir = parents[curr_dir]
#                         print(curr_dir)
#                     else:
#                         curr_dir = parts[2]
#                     if curr_dir not in dirs:
#
#                         dirs[curr_dir] = {}
#                     is_dir = True
#                     dir_dict = {}
#
#                 if cmd == "ls":
#                     continue
#             elif line.startswith("dir"):
#                 inside_dir = line.strip().split(' ')[1]
#                 print(inside_dir)
#                 if inside_dir not in dirs:
#                     new_dir_dict = {}
#                     dirs[curr_dir] = new_dir_dict
#                 parents[inside_dir] = curr_dir
#                 # dirs[curr_dir] =
#                 print(i, dirs)
#
#             elif re.search(r'^\d[^\s]+', line):
#                 file_size_re = re.search(r'^\d[^\s]+', line)
#                 file_size = file_size_re.group()
#                 file_name_r = re.search(r'(?<=\s)[\w+\.+]+', line)
#                 file_name = file_name_r.group()
#                 # print(file_size)
#                 # print(file_name)
#                 if curr_dir in dirs:
#                     dirs[curr_dir][file_name] = int(file_size)
#                 else:
#                     parent_key = parents[curr_dir]
#                     dirs[parent_key] = dirs[curr_dir]
#                 print(dirs)
#
#     print(dirs)
#     print(parents)
#
#
#                 # file_dir[file_name] = file_size
# def find_parents(d, child_key):


print(file_cleanup('input.txt'))
