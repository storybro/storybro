import json
import os

from importlib_resources import read_text, path

import tracery
from tracery.modifiers import base_english


def apply_grammar(key, rules):
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#{}#".format(key))


def load_rules(grammar_file):
    with path('storybro.data.grammars', f"{grammar_file}.json") as grammar_path:
        with open(grammar_path, 'r') as fobj:
            return json.load(fobj)


def generate(grammar_file, character_type, key):
    """
    Provides a randomized prompt according to the rules in specified grammar file
    """
    rules = load_rules(grammar_file)
    artefact = apply_grammar("{}_{}".format(character_type, key), rules)
    return artefact


def direct(grammar_file, key):
    rules = load_rules(grammar_file)
    artefact = apply_grammar(key, rules)
    return artefact
