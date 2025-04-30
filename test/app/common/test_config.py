import unittest


class TestConfig(unittest.TestCase):
    """Configクラスのテストケース."""

    def test_show_version(self) -> None:
        """バージョンが標準出力できること."""
