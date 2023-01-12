from dataclasses import dataclass


## Class for handling exercises
## Use builder pattern, so everything returns Exercise object

class Exercise():
    def __init__(self):
        pass

    ## Specifies the expected mark
    ## Complain if we don't get that
    def expected_total(i):
        pass

    ## Does something with a checker
    def mark(checker):
        pass

    ## Adds a title to the results
    def heading(title):
        pass

## Base class for checkers. Builder interface but with an "results"
## method which returns a list of results
class Check():
    def __init__(self):
        ## Should we continue or as a result so far meant we need to stop
        self.cont = True
        self.results = []

    def result(self,result):
        self.results.append(result)
        return result

## Result of an individual check
@dataclass
class Result:
    out_of: int
    score: int
    feedback: str

## Class that turns exercise into some consumable format (nicely printed, JSON, what ever)
class Report:
    def __init__(self,exercise):
        pass
