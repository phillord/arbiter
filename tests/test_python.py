from arbiter.python import RunMarker

def test_python_success():
    run = RunMarker("examples/hello_world/hello_world.py")
    run.python()
    assert(run.completed_process.returncode == 0)
    assert(run.completed_process.stdout == b"Hello World\n")



def test_python_fail():
    run = RunMarker("tests/resources/broken_hello_world.py")
    run.python()
    assert(run.completed_process.returncode != 0)
