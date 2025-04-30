# pytools template

## 概要

- pythonでツールを作成する際のひな形
- 配布可能なexeに変換することも可能

## 準備

- 仮想環境を作成

```bash
python -m venv venv
```

- 仮想環境に入る

```bash
# windows
venv\Script\activate

# linux
source venv/bin/activate
```

- パッケージのインストール

```bash
make deps
```

## 開発

### Linter・Formatter

このアプリケーションではリンターとフォーマッターに`Ruff`を利用しています。
vscode利用している場合は[拡張機能](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)をインストールしてください。

- Linterのみ実行

```bash
make lint
```

- Formatterのみ実行

```bash
make fix
```

- LinterとFormatter実行

```bash
make lint-fix
```

### UnitTest

- テスト実行

```bash
make test
```

## 使い方

- バージョン確認

```bash
python -m main -v
# or
python -m main --version
```

- 実行

```bash
make run
```

- 配布可能なexe化

```bash
make build
```
