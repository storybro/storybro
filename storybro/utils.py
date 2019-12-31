import os


def find_files(path):
    for d, dirs, files in os.walk(path):
        for f in files:
            yield os.path.join(d, f)


def find_dirs(path):
    for d, dirs, files in os.walk(path):
        for path in dirs:
            yield os.path.join(d, path)


def find_child_dirs(path):
    try:
        return next(os.walk(path))[1]
    except StopIteration:
        return []
