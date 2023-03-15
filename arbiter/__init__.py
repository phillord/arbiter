from dataclasses import dataclass

## Result of an individual check
@dataclass
class Result:
    out_of: int
    score: int
    feedback: str


## Class for handling Section
## Use builder pattern, so everything returns Section object
@dataclass
class Exercise():
    out_of:int
    title:str
    results:list[Result, "Exercise"]

    def __init__(self, title, out_of):
        self.title = title
        self.out_of = out_of
        self.results = []

    ## Use a check to record a mark
    def mark(self, marker):
        self.results.extend(marker.results)
        return self

    ## Add a sub exercise
    def sub(self, exercise):
        self.results.append(exercise)
        return self

    ## Check that everything adds up
    def check(self):
        print(self)
        if not self.will_check():
            raise Exception(f"Check fails: Max score is {self.running_out_of}, expected {self.out_of}")
        return self

    def will_check(self):
        return self.running_out_of == self.out_of

    @property
    def running_out_of(self):
        scores = [
            (x.out_of if isinstance(x, Result) else x.running_out_of)
            for x in self.results
        ]
        return sum(scores)


    def report(self):
        return Report(self)

## Base class for Markers. Builder interface but with an "results"
## method which returns a list of results
class Marker():
    def __init__(self):
        ## Should we continue or as a result so far meant we need to stop
        self.cont = True
        self.results = []

    def log(self, message):
        print(message)

    def result(self,result):
        self.log(result.feedback)
        self.results.append(result)
        return result

    def ask_for_score(self, question, out_of):
        print(f"{question}: {out_of}")
        print("\tPlease Enter Score")
        score = input()
        print("\tPlease Enter feedback")
        feedback = input()
        self.result(
            Result(out_of=out_of, score=score, feedback=feedback)
        )

        return self


## Class that turns exercise into some consumable format (nicely printed, JSON, what ever)
class Report:
    def __init__(self,exercise):
        self.exercise = exercise
