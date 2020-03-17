from app.main import add


class TestMain:
    def test_add(self):
        assert add(2, 2) == 4
