import cmd2
import random
from storybro.cli.config import Config

class PromptCreator(cmd2.Cmd):
    """A simple cmd2 application."""

    def __init__(self, config):
        super().__init__()

        self.current_prompt = ""
        self.allow_ansi = "Terminal"
        self.config: Config = config

        self.setting = ""
        self.character = ""
        self.name = ""
        self.rules = {}
        self.prompt_rolled = ""
        

    def get_prompt(self):
        self.poutput("Welcome to the Prompt Creator. To begin, use /random to randomise the prompt or use /setting to pick a setting. ")

        self.poutput("Use /print to print the current prompt if one exists, or just type text to create a custom prompt.")

        self.cmdloop()

        return self.final_prompt

    @property
    def prompt(self):
        return f">   "

    def random_name(self):
        if self.setting == "" or 'character_name' not in self.rules:
            return "<NAME>"

        return random.choice(self.rules['character_name'])

    @property
    def final_prompt(self):
        manager = self.config.grammar_manager

        if self.name == "":
            self.name = self.random_name()

        if self.prompt_rolled == "":
            prompt = self.current_prompt.replace("<NAME>", self.name)
            self.prompt_rolled = manager.apply_grammar(prompt, self.rules, False)

        return self.prompt_rolled

    def _input_line_to_statement(self, line: str) -> cmd2.Statement:
        line = line.strip()

        if line == "eof":
            line = "quit"
        elif line == "":
            line = ""
        elif not line.startswith("/"):
            line = f"custom {line}"
        else:
           line = line[1:]

        return super()._input_line_to_statement(line)

    def roll_character(self):
        manager = self.config.grammar_manager
        
        context = manager.generate(self.setting, self.character, "context")
        story = manager.generate(self.setting, self.character, "prompt")

        self.current_prompt = f"{context}\n{story}"
        self.prompt_rolled = ""

    def print_settings(self, settings):
        self.poutput("Available settings:")

        for setting in settings:
            self.poutput(f"- {setting}")

    def print_characters(self):
        if self.setting == "" or 'characters' not in self.rules:
            return

        self.poutput("Available characters:")

        for character in self.rules['characters']:
            self.poutput(f"- {character}")

    def do_custom(self, input_text: str):
        if not self.current_prompt == "":
            self.poutput("This will reset the current prompt.")
            if not self.read_input("To confirm, type 'yes': ") == "yes":
                return

        self.current_prompt = input_text
        self.prompt_rolled = ""
        self.do_print()

    def do_print(self, args = ""):
        if self.current_prompt == "":
            self.poutput("The prompt is currently blank")
            return 

        self.poutput(f"The current prompt is:\n\n {self.final_prompt}\n")

    def do_name(self, name):
        if not self.name == "" and name == "":
            self.poutput(f"Current Name: {self.name}")
            return 

        self.name = name
        self.do_print()

    def do_setting(self, setting):
        grammars = self.config.grammar_manager.grammars
        if setting == "":
            if not self.setting == "":
                self.poutput(f"Currently selected setting: {self.setting}")
                
            self.print_settings(grammars)
        elif setting not in grammars:
            self.poutput("Invalid setting")
            self.print_settings(grammars)
        else:
            self.poutput(f"Switching to {setting} setting")
            self.setting = setting
            self.character = ""
            self.prompt_rolled = ""
            self.rules = self.config.grammar_manager.load_rules(setting)
            self.poutput(f"Loaded setting. Select a character with /character")
            self.print_characters()

    def do_character(self, character):
        if self.setting == "" or 'characters' not in self.rules:
            self.poutput("Please select a valid setting!")
            return

        if character == "":
            if not self.character == "":
                self.poutput(f"Currently selected character: {self.character}")
        else:
            self.character = character
            self.roll_character()
            self.do_print()
            self.poutput(f"You may want to name your character with /name. Don't like the start? Try /regen")

    def do_random(self, args):
        self.poutput("This will reset all customisations.")
        if not self.read_input("To confirm, type 'yes': ") == "yes":
            return

        self.name = ""
        self.setting = random.choice(self.config.grammar_manager.grammars)
        self.rules = self.config.grammar_manager.load_rules(self.setting)

        self.character = random.choice(self.rules['characters'])

        self.roll_character()
        self.do_print()

    def do_regen(self, args):
        self.poutput("Are you sure you want to regen the character?")
        if not self.read_input("To confirm, type 'yes': ") == "yes":
            return

        self.roll_character()
        self.do_print()

    def do_reroll(self, args):
        self.poutput("Are you sure you want to reset tracery replacements (only useful in custom prompts)?")
        if not self.read_input("To confirm, type 'yes': ") == "yes":
            return

        self.prompt_rolled = ""
        self.do_print()
