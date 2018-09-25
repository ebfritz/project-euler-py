from euler.euler002 import Euler002

class TestEuler002:
    def test_easy_case(self):
        assert Euler002().call(10) == 10

    def test_harder_case(self):
        assert Euler002().call(100) == 44
