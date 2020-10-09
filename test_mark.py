import pytest
import yaml


# @pytest.mark.parametrize("a", [1, 2, 3])
# @pytest.mark.parametrize("b", ["a", "b", "c"])
# def test_func(a, b):
#     print(a, "-", b)
#
#
# @pytest.mark.parametrize("a,b", yaml.safe_load(open("data.yaml")))
# def test_func2(a, b):
#     print(a, "+", b, "=", a + b)
#
#
# @pytest.mark.skip
# def test_skip():
#     print("skip")
#
#
# @pytest.mark.xfail
# def test_xfail():
#     assert 1 == 0
#     print("xfail")


class TestClass:
    @pytest.mark.parametrize('a,b,result',
                             [
                                 (1, 2, 3),
                                 (4, 5, 9)
                             ],
                             ids=["case1", "case2"])
    def test_func(self, a, b, result):
        print(f"{result}={a} + {b}")

    # def test_func2(self, a, b, result):
    #     print('test_func2')
