from . import Check, Result
import os
import platform
import subprocess
import sys

## Checker that looks for the existance of files
class FileCheck(Check):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename


    def exists(self, score_out_of, score_exists, score_missing):
        if not self.cont:
            return self

        ## if the file exists
        if os.path.isfile(self.filename):
            self.result(
                Result(
                    out_of=score_out_of, score=score_exists,
                    feedback=f"The file \"{self.filename}\" exists"
                )
            )
        else:
            self.result(
                Result(
                    out_of=score_out_of, score=score_missing,
                    feedback=f"The file \"{self.filename}\" is not present"
                    )
            )

        return self


    def open_file(self):
        system_open(self.filename)

        return self


def system_open(filename):
    ## Do something non interactive in test mode!
    if "pytest" in sys.modules:
        return

    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filename))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filename)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filename))
