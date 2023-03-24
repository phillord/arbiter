#!/usr/bin/env python


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
