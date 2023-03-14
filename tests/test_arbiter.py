from arbiter import Exercise, Marker, Result

class NullMarker(Marker):

    def null_mark(self, score_out_of, score):
        self.result(
            Result(out_of=score_out_of,score=score,
                   feedback="Null Check Passed")
            )
        return self

def test_null_marker():
    null = NullMarker()
    null.null_mark(2, 2)
    assert(null.results[0].out_of == 2)
    assert(null.results[0].score == 2)


# def test_arbiter_section():
#     section = Section(
#         "Simple Exercise", 10
#     ).mark(NullMarker().null_marker(2, 2))

#     print(section)

#     assert(False)
