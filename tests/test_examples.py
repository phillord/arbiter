import arbiter
import os


exec(open("examples/hello_world/arb.py").read())


def test_direct_match():
    report = direct_match()
    assert(report.exercise.running_out_of==10)


exec(open("examples/panda/arb.py").read())

def test_blocking_script():
    blocking_script()
