import os
import shutil

def models_at_path(path):
    try:
        return next(os.walk(path))[1]
    except StopIteration:
        return []

def find_files(path):
    for d, dirs, files in os.walk(path):
        for f in files:
            yield os.path.join(d, f)

def find_dirs(path):
    for d, dirs, files in os.walk(path):
        for path in dirs:
            yield os.path.join(d, path)

def flatten_model(path):
    for filename in find_files(path):
        shutil.move(filename, path)
    for dirname in find_dirs(path):
        shutil.rmtree(dirname)
