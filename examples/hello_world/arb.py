#!/usr/bin/env python3
from arbiter import Exercise
from arbiter.python import RunMarker

def direct_match():
    e = Exercise("Simple Exercise", 10)

    r =  (
        ## Check based on Running the code
        RunMarker("hello_world.py")
        ## Run it
        .python()
        ## Get the stdout
        .match_stdout(
            ## Check that we return hello
            b"Hello World\n", 10, 10, 0
        )
    )

    ## Add a single marker
    e.mark(
        r
    ).check()

    return e.report()


def complex_match():
    e = Exercise()

    ## Add a single exercise
    e.mark(
        ## Check based on Running the code
        RunMarker("hello_world.py")
        ## Run it
        .python()
        ## Get the stdout
        .match_stdout(
            Match(
                ["Hello World", "Your program outputs \"Hello World\" as required", 10],
                ["hello world", "Your program is nearly correct but does not use upper case", 8],
                [t, "Your program does not output correctly"]
            )
        )
    ).check()

    return e.report()


def match_with_run_check():
    e = Exercise()

    ## Add a single exercise
    e.mark(
        ## Check based on Running the code
        RunMarker("hello_world.py")
        .exists("The file \"hello_world.py\" does not exist", 2, 0)
        ## Run it
        .python()
        .success("The file \"hello_world.py\" runs correctly", 2,
                 "The file \"hello_world.py\" does not run correctly", 0)
        ## Get the stdout
        .stdout(
            Match(
                ["Hello World", "Your program outputs \"Hello World\" as required", 10],
                ["hello world", "Your program is nearly correct but does not use upper case", 8],
                [t, "Your program does not output correctly"]
            )
        )
    ).check()

    return e.report()


if __name__ == "__main__":
    print(direct_match())
