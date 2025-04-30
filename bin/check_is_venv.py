import sys

def is_venv() -> bool:
    """venv, virtualenvその他環境で動作しているか判定する"""

    # base_prefixはインストール元のpython, prefixは仮想環境のpythonを指すパス
    #  - https://docs.python.org/ja/3/library/sys.html#sys.base_prefix
    #  - https://docs.python.org/ja/3/library/sys.html#sys.prefix
    # これらの値が同一でなければ、仮想環境での実行と判断する
    return sys.base_prefix != sys.prefix

result = is_venv()

if result:
    sys.exit(0)
else:
    sys.exit(1)