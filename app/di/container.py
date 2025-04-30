from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logging import Logger

    from app.common import Config


class Container:
    """DIコンテナ."""

    def __init__(self, config: Config, logger: Logger) -> Container:
        """初期化処理."""
        self.logger = logger
        self.config = config
