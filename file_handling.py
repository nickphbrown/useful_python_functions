from os import path

def create_file(file_name):
    """create directories and file given a file path as a string"""
    directory = path.dirname(filename)
    if directory and not path.exists(directory):
        makedirs(directory)
    with open(filename, "w") as file:
        pass
