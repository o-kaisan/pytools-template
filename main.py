from typing import TYPE_CHECKING

from app.common import CommandArgs, Config, Env
from app.common import Logger as AppLogger
from app.di import Container
from app.interfaces import Cli

if TYPE_CHECKING:
    from logging import Logger


def main() -> None:
    """メイン処理."""
    try:
        # コマンドライン引数を取得
        args = CommandArgs()

        # 環境変数から設定を取得
        env = Env()

        # ロガーの設定
        logger: Logger = AppLogger.setup_logger(args.debug)

        # 設定ファイルを取得
        conf = Config(env, logger)

        # DIコンテナ
        container = Container(conf, logger)

        # ハンドラー
        cli = Cli(container, args)
        cli.handler()

    except Exception:
        logger.exception("An unexpected error occurred")


if __name__ == "__main__":
    main()
