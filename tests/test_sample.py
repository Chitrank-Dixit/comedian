class TestCase(object):
    def test_1(self):
        assert 1 == 1

    def test_some_data(self, some_data):
        assert some_data == 42
