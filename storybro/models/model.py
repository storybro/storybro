import os
import shutil

from storybro.utils import find_files, find_dirs


class Model:

    def __init__(self, root_path):
        self.root_path = root_path

    def filename_for(self, filename):
        return os.path.join(self.root_path, filename)

    def flatten(self):
        for filename in find_files(self.root_path):
            if os.path.dirname(filename) != self.root_path:
                shutil.move(filename, self.root_path)
        for dirname in find_dirs(self.root_path):
            shutil.rmtree(dirname)

    @property
    def name(self):
        return os.path.basename(self.root_path)
