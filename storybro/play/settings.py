
class PlayerSettings:
    def __init__(self,
                 memory: int = None,
                 max_repeats: int = None,
                 icon_for_input: str = None,
                 icon_for_output: str = None,
                 icon_for_pins: str = None,
                 icon_for_delete: str = None,
                 top_separator: str = None,
                 bottom_separator: str = None,
                 fill_width: int = None
                 ):
        self.memory: int = memory or 20
        self.max_repeats: int = max_repeats or 5
        self.icon_for_input: str = icon_for_input or "📖"
        self.icon_for_output: str = icon_for_input or "💻"
        self.icon_for_pins: str = icon_for_pins or "📌"
        self.icon_for_delete: str = icon_for_delete or "❌"
        self.top_separator: str = ""
        self.bottom_separator: str = ""
        self.fill_width: int = fill_width or 80

    def settable(self):
        return {
            'debug': 'whether to print debug messages',
            'max_repeats': 'how many times the ai will attempt to regenerate',
            'icon_for_input': 'icon denoting user input blocks',
            'icon_for_output': 'icon denoting ai output blocks',
            'icon_for_pins': 'icon denoting pinned story blocks',
            'icon_for_delete': 'icon denoting story blocks to delete',
            'top_separator': 'string to use at the top of ai responses',
            'bottom_separator': 'string to use at the bottom of ai responses',
            'fill_width': 'number of characters to wrap ai responses. None to disable',
            'memory': 'how many blocks the ai will remember',
        }
