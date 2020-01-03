import os
import shutil

from storybro.stories.story import Story
from storybro.utils import find_files


class DuplicateStoryError(Exception):
    def __init__(self, transcript_name):
        self.transcript_name = transcript_name


class StoryManager:
    def __init__(self, root_path):
        self.root_path = root_path
        os.makedirs(root_path, exist_ok=True)

    @property
    def stories(self):
        story_map = dict()

        for story_file in find_files(self.root_path):
            story_path = os.path.join(self.root_path, story_file)
            story_name = os.path.basename(story_file)
            story_map[story_name] = Story.load(story_path)

        return story_map

    def new_story(self, name):
        story = self.stories.get(name)

        if story:
            raise DuplicateStoryError(name)

        story_path = os.path.join(self.root_path, name)

        return Story(story_path)
