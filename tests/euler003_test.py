from euler.euler003 import Euler003

class TestEuler003:
    def test_easy_case(self):
        assert Euler003().call(10) == 5

    def test_harder_case(self):
        assert Euler003().call(13195) == 29
