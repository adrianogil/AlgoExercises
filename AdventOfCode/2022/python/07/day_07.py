

def find_size(dir_tree, full_path, size_by_path):
    current_dir = dir_tree
    for folder in full_path:
        current_dir = current_dir[folder]
    
    total_size = 0

    for node in current_dir:
        if node == "type":
            continue
        if current_dir[node]['type'] == 'dir':
            total_size += find_size(dir_tree, full_path+[node], size_by_path)
        else:
            total_size += current_dir[node]['size']
    size_by_path["/" + "/".join(full_path[1:])] = total_size

    return total_size


def get_directory_size_sum(lines):

    dir_tree = {
        "/": {}
    }
    full_path = []
    current_dir = dir_tree["/"]

    parse_ls = False

    for line in lines:
        line = line.strip()
        if parse_ls:
            if line.startswith("$"):
                parse_ls = False
            else:
                ls_line = line.split(" ")
                if ls_line[0] == "dir":
                    dir_name = ls_line[1]
                    if dir_name not in current_dir:
                        current_dir[dir_name] = {'type': 'dir'}
                else:
                    current_dir[ls_line[1]] = { 
                        'type': 'file',
                        'size': int(ls_line[0])
                    }
        if line.startswith("$ cd "):
            target_dir = line[5:]
            if target_dir == "/":
                full_path = []
                current_dir = dir_tree["/"]
            elif target_dir == "..":
                full_path = full_path[:-1]
                current_dir = dir_tree['/']
                for d in full_path:
                    current_dir = current_dir[d]
            else:
                full_path += [target_dir]
                if target_dir not in current_dir:
                    current_dir[target_dir] = {'type': 'dir'}
                current_dir = current_dir[target_dir]
        elif line.startswith("$ ls"):
            parse_ls = True
            
    # print(dir_tree)

    size_by_path = {}
    total_size = find_size(dir_tree, ['/'], size_by_path)

    # print(size_by_path)

    max_size = 100000
    total_size = 0

    for path in size_by_path:
        if size_by_path[path] <= max_size:
            total_size += size_by_path[path]

    return total_size


if __name__ == '__main__':
    import sys
    
    test_mode = False
    if '-test' in sys.argv:
        test_mode = True
        target_file = "test_input.txt"
    else:
        target_file = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

    with open(target_file, 'r') as file_handler:
        lines = file_handler.readlines()

    result = get_directory_size_sum(lines)

    if test_mode:
        print("Got", result)
        assert result == 95437
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

