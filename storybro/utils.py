import os
import sys

from distutils.util import strtobool


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


def yes_no(question):
    sys.stdout.write('%s [y/n]\n' % question)
    while True:
        try:
            return strtobool(input().lower())
        except ValueError:
            sys.stdout.write('Please respond with \'y\' or \'n\'.\n')
