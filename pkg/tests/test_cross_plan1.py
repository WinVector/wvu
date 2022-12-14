import wvu.util


def test_cross_plan1():
    n = 10
    k = 3
    plan = wvu.util.mk_cross_plan(n, k)

    assert len(plan) == k
    universe = set(range(n))
    saw = set()
    for split in plan:
        train = split["train"]
        test = split["test"]
        assert len(train) > 0
        assert len(test) > 0
        assert len(set(train) - universe) == 0
        assert len(set(test) - universe) == 0
        assert len(set(train).intersection(test)) == 0
        assert len(saw.intersection(test)) == 0
        saw.update(test)

    assert universe == saw
