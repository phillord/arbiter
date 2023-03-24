#!/usr/bin/env python

from arbiter import Exercise
from arbiter.python import RunMarker

def blocking_script():
    e = Exercise("Simple Exercise", 10)

    r = (
        RunMarker("panda.py").python()
        .match_stdout(
            b"panda", 10, 10, 0
        )
    )

    e.mark(r).check()

    return e.report()


if __name__ == "__main__":
    print(blocking_script())
