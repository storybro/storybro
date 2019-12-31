import json


class Transcript:

    def __init__(self, path):
        self.path = path
        self.context = ""
        self.blocks = []


    def toJSON(self):
        with open(self.path, 'w') as fobj:
            data = json.dump(self, fobj)

    @staticmethod
    def fromJSON(path):
        script = Transcript(path)
        with open(path, 'r') as fobj:
            data = json.load(fobj)
            script.context = data.context
            script.blocks = data.blocks

        return script
