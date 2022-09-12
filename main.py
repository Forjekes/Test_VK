# This is a test exercise for VK EDU

import pytest


class Tests:

    def test_float_one(self):  # is number more than 3.2
        x = 3.33
        assert x > 3.2

    def test_float_two(self):  # is remainder exist
        x = 4.00
        assert x % 1 == 0

    def test_str_one(self):  # is "in" in "In in n is inn!" :)
        n = "In in n is inn!"
        assert "in" in n

    def test_dict_one(self):  # is dict works correctly
        d = {i: i**i for i in range(5)}
        assert d.get(3) == 3*3*3

    def test_dict_two(self):  # are inappropriate values in dict | NameError – key "objects"
        d = {"food": ["apple", "fish", "burger", "fly agaric"], "objects": ["table", "tv", "weather"]}
        try:
            assert not("fly agaric" in d.get("food")) or not("weather" in d.get(objects))
        except NameError:
            pass


@pytest.mark.parametrize("before,after", [("Snoop", "Snoop Dog"), ("Hot ", "Hot  Dog"), (" HipHop", " HipHop Dog")])
def test_str_two(before, after):  # is space works correctly
    assert before + " Dog" == after
