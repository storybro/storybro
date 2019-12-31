import os

from storybro.models.model import Model
from storybro.utils import find_child_dirs


class ModelManager:
    def __init__(self, root_path):
        self.root_path = root_path
        for model in self.models.values():
            model.flatten()

    @property
    def models(self):
        models = dict()

        for model_name in find_child_dirs(self.root_path):
            model_path = os.path.join(self.root_path, model_name)
            models[model_name] = Model(model_path)

        return models

