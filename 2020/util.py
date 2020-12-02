def file_to_list(file):
    list = []
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            list.append(line.replace('\n', ''))

    return list
