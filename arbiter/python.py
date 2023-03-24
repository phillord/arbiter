from . import Result
from .util import FileMarker, match_to_string

import subprocess

## Class that runs a python file


class RunMarker(FileMarker):
    def __init__(self, filename):
        super().__init__(filename)

    def subprocess(self, *args, **kargs):
        return self._subprocess(False, *args, **kargs)

    def _subprocess(self, is_python, *args, **kargs):
        _args = [self.filename]

        if is_python:
            new_args = ["python3"]
            new_args.extend(_args)
            _args=new_args

        if isinstance(args, list):
            _args.extend(args)

        self.completed_process = subprocess.run(
            _args, capture_output=True, **kargs
        )

        return self

    def python(self, *args, **kargs):
        self._subprocess(True, *args, **kargs)
        return self

    def success(self, score_out_of, score_success, score_failure):
        if self.completed_process.returncode == 0:
            self.result(
                Result(
                    out_of=score_out_of,score=score_success,
                    feedback=f"The file \"{self.filename}\" executed"
                )
            )
        else:
            self.result(
                Result(
                    out_of=score_out_of,score=score_failure,
                    feedback=f"The file \"{self.filename}\" failed to execute"
                )
            )

        return self

    def match_stdout(self, match, score_out_of, score_matches, score_does_not_match):
        if match_to_string(self.completed_process.stdout, match):
            self.result(
                Result(
                    out_of=score_out_of, score=score_matches,
                    feedback=f"The standard output matches {match}"
                )
            )
        else:
            self.result(
                Result(
                    out_of=score_out_of, score=score_does_not_match,
                    feedback=f"The standard output does not match {match}"
                )
            )

        return self
