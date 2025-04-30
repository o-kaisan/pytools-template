#!/bin/bash

# Pythonでvenv判定（仮想環境なら"1"、そうでなければ"0"を返す）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python "$SCRIPT_DIR/check_is_venv.py"
IS_VENV=$?

if [ "$IS_VENV" -eq "0" ]; then
    echo "python -m pip install -r requirements.txt"
    python -m pip install -r requirements.txt
else
    echo "仮想環境ではありません..."
    echo "仮想環境に入ってから再度実行してください"
fi