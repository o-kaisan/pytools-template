from __future__ import annotations

import argparse


class CommandArgs:
    """コマンドライン引数."""

    def __init__(self) -> CommandArgs:
        """初期化."""
        parser = argparse.ArgumentParser()
        parser.add_argument("-v", "--version", help="show app version", action="store_true")
        parser.add_argument("--debug", help="debug mode", action="store_true")
        args = parser.parse_args()

        # デバッグモード
        self.debug = args.debug

        # バージョン表示
        self.version = args.version
