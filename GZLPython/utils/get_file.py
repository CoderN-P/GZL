def get_file(path) -> str:
    file = open(path, 'r')
    file_string = file.readlines()
    file.close()
    return ''.join(file_string)