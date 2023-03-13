from arbiter.python import RunCheck

def test_python_success():
    run = RunCheck("examples/hello_world/hello_world.py")
    run.python()
    assert(run.success)
    assert(run.stdout == b"Hello World\n")



def test_python_fail():
    run = RunCheck("tests/resources/broken_hello_world.py")
    run.python()
    assert(not run.success)
