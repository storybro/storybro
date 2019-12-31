import os

from storybro.transcripts.transcript import Transcript
from storybro.utils import find_files


class DuplicateTranscriptError(Exception):
    def __init__(self, transcript_name):
        self.transcript_name = transcript_name


class TranscriptManager:
    def __init__(self, root_path):
        self.root_path = root_path

    @property
    def transcripts(self):
        scripts = dict()

        for script_file in find_files(self.root_path):
            script_path = os.path.join(self.root_path, script_file)
            scripts[script_file] = Transcript.fromJSON(script_path)

        return scripts

    def new_transcript(self, name):
        script = self.transcripts.get(name)

        if script:
            raise DuplicateTranscriptError(name)

        script_path = os.path.join(self.root_path, name)

        return Transcript(script_path)
