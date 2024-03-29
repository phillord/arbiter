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


def test_checker_simple():
    e = Exercise("Simple", 10)

    assert(e.running_out_of == 0)

    e.mark(
        NullMarker().
        null_mark(2, 0).
        null_mark(2, 0)
    )

    assert(e.running_out_of == 4)

    assert(not e.will_check())

    e.mark(
        NullMarker().
        null_mark(6, 0)
    )

    assert(e.will_check())


def test_arbiter_section():
    e = Exercise("Top Exercise", 4)

    e.mark(
        NullMarker().null_mark(2, 2)
    ).sub(
        Exercise("SubExercise", 2).
        mark(NullMarker().null_mark(2, 2))
    )

    assert(e.running_out_of == 4)
