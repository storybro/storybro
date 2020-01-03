import textwrap

from storybro.play.settings import PlayerSettings
from storybro.stories.block import Block
from storybro.stories.story import Story
from storybro.story.utils import cut_trailing_sentence


class BlockFormatter:
    def __init__(self, settings: PlayerSettings):
        self.settings: PlayerSettings = settings

    # before saving to disk

    def filter_block(self, block: Block) -> Block:
        if block.attrs.get('type') == 'input':
            return self.filter_input(block)
        else:
            return self.filter_output(block)

    def filter_input(self, block: Block) -> Block:
        return Block(block.text.strip(' \t\n\r'), attrs=block.attrs.copy())

    def filter_output(self, block: Block) -> Block:
        text = cut_trailing_sentence(block.text)

        if len(text) == 0:
            text = ""
        else:
            text = text.replace('."', '".')
            text = text.replace("#", "")
            text = text.replace("*", "")
            text = text.replace("\n\n", "\n")

            text = text.strip(' \t\n\r')

            if not text.endswith("."):
                text = text + "."

        return Block(text, attrs=block.attrs.copy())

    # before sending to generator

    def process_block(self, block: Block) -> Block:
        if block.attrs.get('type') == 'input':
            return self.process_input(block)
        else:
            return self.process_output(block)

    def process_input(self, block: Block) -> Block:
        return Block("\n> " + block.text + "\n", block.attrs.copy())

    def process_output(self, block: Block) -> Block:
        return Block(block.text, block.attrs.copy())

    def process_story(self, story: Story) -> str:
        return "".join([self.process_block(b).text for b in story.blocks])

    # before sending to user

    def render_block(self, block: Block) -> Block:
        if block.attrs.get('type') == 'input':
            return self.render_input(block)
        else:
            return self.render_output(block)

    def fill_text(self, text, is_input, is_pinned):
        input_icon = self.settings.icon_for_input if is_input else self.settings.icon_for_output
        pin_icon = self.settings.icon_for_pins if is_pinned else "  "
        initial_indent = input_icon + pin_icon + " "
        return textwrap.fill(
            text,
            width=self.settings.fill_width,
            replace_whitespace=True,
            drop_whitespace=True,
            initial_indent=initial_indent,
            subsequent_indent="     ",
            fix_sentence_endings=True)

    def render_input(self, block: Block) -> Block:
        rendered_input = block.text
        is_input = block.attrs.get('type') == 'input'
        is_pinned = block.attrs.get('pinned')

        if self.settings.fill_width:
            rendered_input = "\n".join([self.fill_text(l, is_input, is_pinned) for l in rendered_input.splitlines()])

        return Block(rendered_input, block.attrs.copy())

    def render_output(self, block: Block) -> Block:
        rendered_output = block.text
        is_input = block.attrs.get('type') == 'input'
        is_pinned = block.attrs.get('pinned')

        if self.settings.fill_width:
            rendered_output = "\n".join([self.fill_text(l, is_input, is_pinned) for l in rendered_output.splitlines()])

        rendered_output = f"{self.settings.top_separator}\n{rendered_output}\n{self.settings.bottom_separator}"
        return Block(rendered_output, block.attrs.copy())

    def render_story(self, story: Story, last_n: int = 0) -> str:
        blocks = story.blocks
        if last_n:
            blocks = blocks[-last_n:]
        return "\n".join([self.render_block(b).text for b in blocks])
