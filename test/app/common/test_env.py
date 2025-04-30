import unittest


class TestEnv(unittest.TestCase):
    """Envクラスのテストケース."""

    def test_config_path(self) -> None:
        """環境変数から値が取得できること."""
