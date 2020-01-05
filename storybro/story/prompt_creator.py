import cmd2
from storybro.cli.config import Config

class PromptCreator(cmd2.Cmd):
    """A simple cmd2 application."""

    def __init__(self, config):
        super().__init__()

        self.current_prompt = ""
        self.allow_ansi = "Terminal"
        self.config: Config = config
        

    def get_prompt(self):
        self.poutput("Welcome to the Prompt Creator. To begin, use /random to randomise the prompt or use /setting to pick a setting. ")

        self.poutput("Use /print to print the current prompt if one exists, or just type text to create a custom prompt.")

        self.cmdloop()

        return self.current_prompt


    @property
    def prompt(self):
        return f">   "


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

    def do_custom(self, input_text: str):
        self.current_prompt = input_text
        self.poutput(f"The current prompt is now: {self.current_prompt}")

    def do_print(self, args):
        if self.current_prompt == "":
            self.poutput("The prompt is currently blank")
            return 

        self.poutput(f"The current prompt is: {self.current_prompt}")