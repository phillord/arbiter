from .util import FileMarker

import subprocess

## Class that runs a python file


class RunMarker(FileMarker):
    def __init__(self, filename):
        super().__init__(filename)

    def subprocess(self, args=[]):
        return self._subprocess(False, args)

    def _subprocess(self, is_python, args=[]):
        _args = [self.filename]

        if is_python:
            new_args = ["python3"]
            new_args.extend(_args)
            _args=new_args

        if isinstance(args, list):
            _args.extend(args)

        self._completed_process = subprocess.run(
            _args, capture_output=True
        )

        return self

    def python(self, args=[]):
        self._subprocess(True, args)
        return self

    @property
    def success(self):
        return self._completed_process.returncode == 0

    @property
    def returncode(self):
        return self._completed_process.returncode
