# python_memo_to_self

- 自分用いろいろメモ。
- 順次整理。

---

## 💻 __Index__

- README.md

  - いろいろメモ書き。
  - 長くなったトピックは、別途ファイルに移していく。

- aws_pipenv.md

  - AWSのEC2でのpipenvとPython3系の環境構築手順

- pyinstaller.md

  - Python製スタンドアロンアプリのデプロイ手順（PyInstaller）

- python_zundoko.py

  - ズンドコキヨシのPython実装。


---

## 💻 Python開発でよく使うシリーズ

### pipenv

- Init pipenv
    ```
    pip install pipenv
    ```

- Check pipenv version
    ```
    pipenv --version
    ```

- __Prepare Env__
    ```
    mkdir dir_project
    cd dir_project
    pipenv install
    pipenv --python 3.8
    ```

- Checking PEP 508 requirements
    ```
    pipenv check
    ```

- Check pipenv version
    ```
    python --version
    ```

- Into env & Exit
    ```
    pipenv shell

    exit
    ```

- Execute

    e.g.
    ```
    pipenv run python hoge.py

    pipenv run ptw
    ```

- Other Commands
    ```
    pip search package_hoge

    pipenv install package_hoge
    pipenv install package_hoge --dev

    pipenv update

    pipenv uninstall package_hoge
    ```


### poetry

- _
    ```
    ```

---

### pytest

`pip install pytest`

```
import pytest


# Decorator: Skip
@pytest.mark.skip(reason = "Sentence_why_skip")
```

### pytest-watch

`pip install pytest-watch`

`ptw`

---

### os
### sys
### re

### time
```
time.sleep(1)
time.sleep(10)
time.sleep(60)
```

### threading
`from threading import Timer`
```
Timer(sec, function)
```

### shutil
```
import shutil

# copy
shutil.copy("path_file_name", "path_directory_name/")

# move
shutil.copy("path_file_name", "path_directory_name/")
```


### pathlib
```
from pathlib import Path

# get Absolute path of File
path = Path("path_dir_name/*.path_file_name")

with path.open() as f:
    # Operation
    # e.g.
    # f.readline()
    # f.write()
```

### pprint

### date

### datetime

### gunicorn

### flask

- バージョン確認
    ```
    python
    .
    .
    .
    >>> import flask
    >>> flask.__version__
    '1.1.1'
    ```
    `$ python` で入って、`flask.__version__`で確認.


### django

### requests
- `pip install requests`
```
import requests
```


### json
import json

### selenium

### bs4
`pip install bs4`
```
from bs4 import BeautifulSoup as bs
```

### jupyterlab
`pip install jupyterlab`

### numpy
### pandas
### mecab

### opencv-python
```
pip install opencv-python

import cv2
```

### pymovie

### PyInstaller
`pip install pyinstaller`

### openxl
### xlwings

### concurrent.futures

- pip install は不要（標準パッケージ）

```
from concurrent.futures
import os

max_cores = os.cpu_count()
executor = concurrent.futures.ThreadPoolExecutor(max_workers=pc_cores)


def function_1():
    for _ in range(1000):
        example_method.execute_something_do(*example_arg)

def function_2():
    for _ in range(1000):
        example_method.execute_something_do(*example_arg)

def function_3():
    for _ in range(1000):
        example_method.execute_something_do(*example_arg)

def function_4():
    for _ in range(1000):
        example_method.execute_something_do(*example_arg)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=max_cores) as executor:
        executor.submit(function_1)
        executor.submit(function_2)
        executor.submit(function_3)
        executor.submit(function_4)
```

### FastAPI

### sqlalchemy

### 
### 
### 