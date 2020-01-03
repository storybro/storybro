import json
from typing import Set, List, Dict

from storybro.stories.block import Block
from storybro.story.utils import parse_slice


class Story:

    def __init__(self, path: str):
        self.path: str = path
        self.blocks: List[Block] = []
        self.attrs: Dict = {}

    def save(self):
        with open(self.path, 'w') as fobj:
            data = self.to_data()
            json.dump(data, fobj)

    @classmethod
    def load(cls, path):
        with open(path, 'r') as fobj:
            data = json.load(fobj)
        return cls.from_data(path, data)

    def to_data(self):
        return {
            'attrs': self.attrs,
            'blocks': [b.to_data() for b in self.blocks],
        }

    @classmethod
    def from_data(cls, path, data):
        story = cls(path)
        story.attrs = data["attrs"]
        story.blocks = [Block.from_data(d) for d in data["blocks"]]
        return story

    def filter_blocks(self, first_n=None, last_n=None, range=None):
        filtered = set([])

        if range and ":" in range:
            slice_obj: slice = parse_slice(range, bump_stop=True)
            filtered = filtered | set(self.blocks[slice_obj])

        if last_n:
            filtered = filtered | set(self.blocks[-last_n:])

        if first_n:
            filtered = filtered | set(self.blocks[:first_n])

        if not range and not last_n and not first_n:
            filtered = self.blocks

        return filtered


    def render_transcript(self, latest_n: int, specific_blocks: Set[int] = None):
        indices = specific_blocks or set([])

        total = len(self.blocks)

        if total == 0:
            return ""

        index = 0

        while index < total:
            if index in indices:
                index += 1
                continue

            if index > total - latest_n:
                indices.add(index)

            index += 1

        transcript = ""

        for index in sorted(indices):
            transcript += self.blocks[index]

        return transcript
