import pytest

class TestClass:
    def test_bidon1(self):
        x = "this"
        assert "h" in x

    def test_bidon2(self):
        x = "bidon"
        assert hasattr(x, "check")