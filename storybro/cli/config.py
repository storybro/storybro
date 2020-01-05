from storybro.models.manager import ModelManager
from storybro.models.registry import ModelRegistry
from storybro.stories.manager import StoryManager
from storybro.story.grammars import GrammarManager


class Config:
    models_path: str = None
    stories_path: str = None
    grammars_path: str = None

    model_registry: ModelRegistry = None
    model_manager: ModelManager = None
    story_manager: StoryManager = None
    grammar_manager: GrammarManager = None


