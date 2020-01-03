import json
import os
import uuid

from storybro.story.utils import split_first_sentence, cut_trailing_sentence, console_print


class Story:
    def __init__(
        self, story_start, context="", seed=None, game_state=None, upload_story=False
    ):
        self.story_start = story_start
        self.context = context
        self.rating = -1
        self.upload_story = upload_story

        # list of actions. First action is the prompt length should always equal that of story blocks
        self.actions = []

        # list of story blocks first story block follows prompt and is intro story
        self.results = []

        # Only needed in constrained/cached version
        self.seed = seed
        self.choices = []
        self.possible_action_results = None
        self.uuid = None

        if game_state is None:
            game_state = dict()
        self.game_state = game_state
        self.memory = 20

    def __del__(self):
        if self.upload_story:
            self.save_to_storage()
            console_print("Game saved.")
            console_print(
                "To load the game, type 'load' and enter the following ID: " + self.uuid
            )

    def init_from_dict(self, story_dict):
        self.story_start = story_dict["story_start"]
        self.seed = story_dict["seed"]
        self.actions = story_dict["actions"]
        self.results = story_dict["results"]
        self.choices = story_dict["choices"]
        self.possible_action_results = story_dict["possible_action_results"]
        self.game_state = story_dict["game_state"]
        self.context = story_dict["context"]
        self.uuid = story_dict["uuid"]

        if "rating" in story_dict.keys():
            self.rating = story_dict["rating"]
        else:
            self.rating = -1

    def initialize_from_json(self, json_string):
        story_dict = json.loads(json_string)
        self.init_from_dict(story_dict)

    def add_to_story(self, action, story_block):
        self.actions.append(action)
        self.results.append(story_block)

    def latest_result(self):

        mem_ind = self.memory
        if len(self.results) < 2:
            latest_result = self.story_start
        else:
            latest_result = self.context
        while mem_ind > 0:

            if len(self.results) >= mem_ind:
                latest_result += self.actions[-mem_ind] + self.results[-mem_ind]

            mem_ind -= 1

        return latest_result

    def __str__(self):
        story_list = [self.story_start]
        for i in range(len(self.results)):
            story_list.append("\n" + self.actions[i] + "\n")
            story_list.append("\n" + self.results[i])

        return "".join(story_list)

    def to_json(self):
        story_dict = {}
        story_dict["story_start"] = self.story_start
        story_dict["seed"] = self.seed
        story_dict["actions"] = self.actions
        story_dict["results"] = self.results
        story_dict["choices"] = self.choices
        story_dict["possible_action_results"] = self.possible_action_results
        story_dict["game_state"] = self.game_state
        story_dict["context"] = self.context
        story_dict["uuid"] = self.uuid
        story_dict["rating"] = self.rating

        return json.dumps(story_dict)

    def save_to_storage(self):
        print("Saving to storage has been disabled due to abuse of the cloud bucket. Save will now be stored locally.")

        self.uuid = str(uuid.uuid1())

        save_path = "./saved_stories/"

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        story_json = self.to_json()
        file_name = "story" + str(self.uuid) + ".json"
        f = open(os.path.join(save_path, file_name), "w")
        f.write(story_json)
        f.close()
        return self.uuid

    def load_from_storage(self, story_id):
        save_path = "./saved_stories/"

        if not os.path.exists(save_path):
            return "Error save not found."

        file_name = "story" + story_id + ".json"
        exists = os.path.isfile(os.path.join(save_path, file_name))
        if exists:
            with open(os.path.join(save_path, file_name), "r") as fp:
                game = json.load(fp)
                self.init_from_dict(game)
                return str(self)
        else:
            print("Save not found locally. Trying in the cloud bucket (only valid for saves before Dec 24 2019)")
            cmd = "gsutil cp gs://aidungeonstories/" + file_name + " " + save_path
            os.system(cmd)
            exists = os.path.isfile(os.path.join(save_path, file_name))


            if exists:
                with open(os.path.join(save_path, file_name), "r") as fp:
                    game = json.load(fp)
                self.init_from_dict(game)
                return str(self)
            else:
                return "Error save not found locally or in the cloud."

    def get_rating(self):
        while True:
            try:
                rating = input("Please rate the story quality from 1-10: ")
                rating_float = max(min(float(rating), 10), 1)
            except ValueError:
                print("Please return a valid number.")
            else:
                self.rating = rating_float
                return


class StoryManager:
    def __init__(self, generator):
        self.generator = generator
        self.story = None

    def start_new_story(
        self, story_prompt, context="", game_state=None, upload_story=False
    ):
        block = self.generator.generate(context + story_prompt)
        block = cut_trailing_sentence(block)
        self.story = Story(
            context + story_prompt + block,
            context=context,
            game_state=game_state,
            upload_story=upload_story,
        )
        return str(self.story)

    def load_new_story(self, story_id, upload_story=False):
        file_name = "story" + story_id + ".json"
        cmd = "gsutil cp gs://aidungeonstories/" + file_name + " ."
        os.system(cmd)
        exists = os.path.isfile(file_name)

        if not exists:
            return "Error save not found."

        with open(file_name, "r") as fp:
            game = json.load(fp)
        self.story = Story("", upload_story=upload_story)
        self.story.init_from_dict(game)
        return str(self.story)

    def load_story(self, story, from_json=False):
        if from_json:
            self.story = Story("")
            self.story.initialize_from_json(story)
        else:
            self.story = story
        return str(story)

    def json_story(self):
        return self.story.to_data()

    def story_context(self):
        return self.story.latest_result()


class UnconstrainedStoryManager(StoryManager):
    def act(self, action_choice):

        result = self.generate_result(action_choice)
        self.story.add_to_story(action_choice, result)
        return result

    def generate_result(self, action):
        block = self.generator.generate(self.story_context() + action)
        return block
