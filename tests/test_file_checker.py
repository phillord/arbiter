from arbiter.util import FileCheck

def test_file_exists():
    res_list = FileCheck("README.md").exists(2, 1, 0).results
    assert(len(res_list) == 1)
    res = res_list[0]
    print(res)
    assert(res.out_of == 2)
    assert(res.score == 1)
    assert(res.feedback == "The file \"README.md\" exists")

def test_file_does_not_exist():
    res_list = FileCheck("does_not_exist").exists(2, 1, 0).results
    assert(len(res_list) == 1)
    res = res_list[0]
    print(res)
    assert(res.out_of == 2)
    assert(res.score == 0)
    assert(res.feedback == "The file \"does_not_exist\" is not present")
