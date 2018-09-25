from euler.euler001 import Euler001

class TestEuler001:
    def test_easy_case(self):
        assert Euler001().call(10) == 23

    def test_harder_case(self):
        assert Euler001().call(13) == 45
