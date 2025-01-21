# Python Study Project

このプロジェクトはPythonの学習を目的としたもので、基本的なアプリケーションの構造を示しています。

## プロジェクト構成

- `src/main.py`: アプリケーションのエントリーポイント。主要なロジックが含まれています。
- `src/utils/helper.py`: 補助的な関数やクラスを定義しています。`main.py` からインポートされて使用されます。
- `tests/test_main.py`: `main.py` のユニットテストを含んでいます。テストフレームワークを使用して機能を検証します。
- `requirements.txt`: プロジェクトに必要なPythonパッケージのリストを含んでいます。

## 使い方

1. リポジトリをクローンします。
2. 必要なパッケージをインストールします。
   ```
   pip install -r requirements.txt
   ```
3. アプリケーションを実行します。
   ```
   python src/main.py
   ```
4. テストを実行します。
   ```
   python -m unittest tests/test_main.py
   ```

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。