def direct_match():
    a = Aribter()

    ## Add a single exercise
    a.exercise(
        ## Check based on Running the code
        Run("hello_world.py")
        ## Run it
        .execute()
        ## Get the stdout
        .stdout(
            ## Check that we return hello
            Equals("Hello World", "You program outputs \"Hello World\" as required", 10, 0)
        )
    )

    a.complete()

def complex_match():
    a = Aribter()

    ## Add a single exercise
    a.exercise(
        ## Check based on Running the code
        Run("hello_world.py")
        ## Run it
        .execute()
        ## Get the stdout
        .stdout(
            Match(
                ["Hello World", "Your program outputs \"Hello World\" as required", 10]
                ["hello world", "Your program is nearly correct but does not use upper case", 8]
                [t, "Your program does not output correctly"]
            )
        )
    )

    a.complete()


def match_with_run_check():
    a = Aribter()

    ## Add a single exercise
    a.exercise(
        ## Check based on Running the code
        Run("hello_world.py")
        .exists("The file \"hello_world.py\" does not exist", 2, 0)
        ## Run it
        .execute()
        .success("The file \"hello_world.py\" runs correctly", 2,
                 "The file \"hello_world.py\" does not run correctly", 0)
        ## Get the stdout
        .stdout(
            Match(
                ["Hello World", "Your program outputs \"Hello World\" as required", 10]
                ["hello world", "Your program is nearly correct but does not use upper case", 8]
                [t, "Your program does not output correctly"]
            )
        )
    )

    a.complete()
