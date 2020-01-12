import json
import os
import os.path

from importlib_resources import read_text, path

import tracery
from tracery.modifiers import base_english
from storybro.utils import find_files

class GrammarManager:
    def __init__(self, root_path):
        self.root_path = root_path
        os.makedirs(root_path, exist_ok=True)

        if not os.listdir(self.root_path):
            self.install_defaults()
    

    def install_defaults(self):
        with self.open_default("fantasy") as file:
            self.write_file("fantasy", file.read())

        with self.open_default("apocalyptic") as file:
            self.write_file("apocalyptic", file.read())

    @property
    def grammars(self):
        grammars = []

        for file_path in find_files(self.root_path):
            name = os.path.basename(file_path)
            grammars.append(name.replace('.json', ''))

        return grammars


    def open_default(self, name):
        with path('storybro.data.grammars', f"{name}.json") as grammar_path:
            return open(grammar_path, 'r')
        

    def write_file(self, name, text):
        path = os.path.join(self.root_path, f"{name}.json")

        with open(path, 'w') as fobj:
            fobj.write(text)


    def apply_grammar(self, text, rules, as_key):
        grammar = tracery.Grammar(rules)
        grammar.add_modifiers(base_english)
        return grammar.flatten("#{}#".format(text) if as_key else text)


    def load_rules(self, grammar_file):
        path = os.path.join(self.root_path, f"{grammar_file}.json")

        with open(path, 'r') as fobj:
            return json.load(fobj)


    def generate(self, grammar_file, character_type, key):
        """
        Provides a randomized prompt according to the rules in specified grammar file
        """
        rules = self.load_rules(grammar_file)
        artefact = self.apply_grammar("{}_{}".format(character_type, key), rules, True)
        return artefact


    def direct(self, grammar_file, key):
        rules = self.load_rules(grammar_file)
        artefact = self.apply_grammar(key, rules)
        return artefact
