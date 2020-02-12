# Python製スタンドアロンアプリのデプロイ手順（PyInstaller）

以下手順により、Pythonが入っていない環境やPCでもPythonプログラムが実行できるよう、スタンドアロンアプリ化することが可能となります。

具体的にはexe実行ファイルをふくむツールディレクトリを生成し、配布等も行うことができます。

## 方法

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

  - 軽量化の為に不要ライブラリ等を抜いておく方法

    ```
    pyinstaller app.py --exclude-module=PyQt5 --exclude splite
    ```

### アプリ実行方法

- app.py同階層に生成されたディレクトリ`dist` > ディクショナリ > `app.exe` から実行可能。
- 初回のみ自動ビルドが走るため、実行まで時間がかかる（数十秒～数分以内。アプリ規模による）
