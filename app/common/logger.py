import logging
from logging import DEBUG, INFO, basicConfig, getLogger


class Logger:
    """ロガークラス."""

    FILE_NAME: str = "./log/app.log"

    @classmethod
    def setup_logger(cls, debug: bool) -> logging.Logger:  # noqa: FBT001
        """初期化."""
        basicConfig()
        logger: logging.Logger = getLogger(__name__)

        if debug:
            logger.setLevel(DEBUG)
        else:
            logger.setLevel(INFO)

        ## ログをファイル出力したい場合はコメントアウトを外す

        # Path(cls.FILE_NAME).parent.mkdir(parents=True, exist_ok=True)
        # rotating_handler = handlers.RotatingFileHandler(
        #     cls.FILE_NAME,
        #     mode="a",
        #     maxBytes=100 * 1024,
        #     backupCount=3,
        #     encoding = "utf-8"
        # )
        # format = Formatter('%(asctime)s : %(levelname)s : %(messages)s')
        # rotating_handler.setFormatter(format)
        # logger.addHandler(rotating_handler)

        return logger
