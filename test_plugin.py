import pytest


def test_div():
    1/0

def test_pytest_assume():
    # assert 1 == 1
    # assert 1 == 2
    # assert 2 == 2
    pytest.assume(1 == 1)
    pytest.assume(1 == 2)
    pytest.assume(2 == 2)
    print("执行完成")

@pytest.mark.run(order=3)
def test_ordering1():
    print("ordering1")

@pytest.mark.run(order=1)
def test_ordering2():
    print("ordering2")

@pytest.mark.run(order=2)
def test_ordering3():
    print("ordering3")

@pytest.mark.dependency()
def test_caseA():
    print("test_caseA")
    raise Exception


@pytest.mark.dependency(depends=['test_caseA'])
def test_caseB():
    print("test_caseB")

@pytest.mark.dependency(name='caseA')
def test_caseA():
    print("test_caseA")
    raise Exception


@pytest.mark.dependency(depends=['caseA'])
def test_caseB():
    print("test_caseB")