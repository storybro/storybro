import json


class Block:

    def __init__(self, text, attrs=None):
        self.text = text
        self.attrs = attrs or dict()

    def to_data(self) -> dict:
        return {
            'text': self.text,
            'attrs': self.attrs
        }

    @staticmethod
    def from_data(data: dict):
        return Block(data['text'], data['attrs'])
