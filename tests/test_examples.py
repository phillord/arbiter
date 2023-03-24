import arbiter
import os


exec(open("examples/hello_world/arbiter.py").read())


def test_direct_match():
    direct_match()


exec(open("examples/panda/arbiter.py").read())

def test_blocking_script():
    blocking_script()
