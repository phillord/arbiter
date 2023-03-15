from arbiter.util import FileMarker, match_to_string
import re

def test_test_file_exists():
    res_list = FileMarker("README.md").exists(2, 1, 0).results
    assert(len(res_list) == 1)
    res = res_list[0]
    assert(res.out_of == 2)
    assert(res.score == 1)
    assert(res.feedback == "The file \"README.md\" exists")

def test_file_does_not_exist():
    res_list = FileMarker("does_not_exist").exists(2, 1, 0).results
    assert(len(res_list) == 1)
    res = res_list[0]
    assert(res.out_of == 2)
    assert(res.score == 0)
    assert(res.feedback == "The file \"does_not_exist\" is not present")


def test_match_to_string():
    assert(match_to_string("hello world", "world"))

    assert(match_to_string("hello world", re.compile("world")))

    assert(match_to_string("hello world",
                           lambda s: s=="hello world"))
