from app.main import add, add_arrays, Location, add_lists
import numpy as np


class TestMain:
    def test_add(self):
        assert add(2, 2) == 4

    def test_add_np(self):
        x = np.array([1, 2])
        y = np.array([3, 4])
        result = add_arrays(x, y)
        assert result[0] == 4 and result[1] == 6

    def test_location(self):
        location1 = Location(0.1, 100)
        location2 = Location(0.1, 100)
        assert location1 == location2
        assert location1 is not location2

    def test_add_lists(self):
        x = [1, 2]
        y = [3, 4]
        assert add_lists(x, y) == [1, 2, 3, 4]
