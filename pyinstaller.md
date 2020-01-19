# Python製スタンドアロンアプリのデプロイ手順（PyInstaller）

- PyInstallerをインストール

    ```
    pip install pyinstaller
    ```

- `app.py(例)`をスタンドアロンアプリ化

  - 基本形

    ```
    pyinstaller app.py
    ```

  - オプションで、`--noconsole`（コンソール非表示）、`--onefile`（１ファイルにバンドル）設定可能。

    ※ただし`onefile`は、観測の範囲では不具合を起こす可能性が高まることが多く、できれば不使用がのぞましい。

    ```
    pyinstaller app.py --noconsole --onefile
    ```

  - 軽量化の為、使用しないライブラリ等を含めない方法

    ```
    pyinstaller app.py --exclude-module=PyQt5 --exclude splite
    ```

## 生成アプリ実行方法

- app.py同階層に生成されたディレクトリ`dict` > ディクショナリ > `app.exe` から実行可能。
- 初回のみ自動ビルドが走るため、実行まで時間がかかる（数十秒～数分以内。アプリ規模による）
