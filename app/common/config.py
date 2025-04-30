from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logging import Logger

    from app.common import Env

import yaml


class Config:
    """アプリケーションの設定.

    環境変数 > 設定ファイルの優先度で値を返す
    """

    FILE_PATH = "./app/config/config.yaml"
    VERSION = "0.0.1"

    def __init__(self, env: Env, logger: Logger) -> Config:
        """初期化."""
        if env.config_path is None:
            config_path = self.FILE_PATH
        with Path(config_path).open(encoding="utf-8") as f:
            config = yaml.safe_load(f)
        self.env = env
        self.config = config
        self.logger = logger

    def show_version(self) -> None:
        """バージョン情報を標準出力する."""
        print(f"Version : {self.VERSION}")  # noqa: T201
