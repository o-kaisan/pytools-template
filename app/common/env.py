from __future__ import annotations

import os

from dotenv import load_dotenv


class Env:
    """環境変数."""

    ENV_PATH = ".env"

    def __init__(self, env_path: str | None = None) -> Env:
        """初期化."""
        if env_path is None:
            env_path = self.ENV_PATH

        # .envから設定を読み込む
        load_dotenv(env_path)

    @property
    def config_path(self) -> str:
        """設定ファイルのパスを返す.

        設定されていない場合はNoneを返す.
        """
        config_path: str = os.environ.get("CONFIG_PATH")
        return config_path
