from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.common import CommandArgs
    from app.di import Container


class Cli:
    """コマンド制御クラス."""

    def __init__(self, container: Container, args: CommandArgs) -> Cli:
        """初期化."""
        self.c = container
        self.args = args
        self.logger = container.logger

    def handler(self) -> None:
        """アプリケーションの制御."""
        # バージョン表示
        if self.args.version:
            self.c.config.show_version()
