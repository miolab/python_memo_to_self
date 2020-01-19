# python_memo_to_self

自分用いろいろメモ。

- 順次、整理＆追記。
- GitHub<br>
  https://github.com/miolab/python_memo_to_self.git


## __Index__

#### README.md

- いろいろメモ書き。
- 長くなったトピックは、別途ファイルに移していく。

#### aws_pipenv.md

- AWSのEC2でのpipenvとPython3系の環境構築手順


# Python開発でよく使うシリーズ

## pipenv

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


## poetry

- _
    ```
    ```

---

## pytest

`pip install pytest`

```
import pytest


# Decorator: Skip
@pytest.mark.skip(reason = "Sentence_why_skip")

```

## pytest-watch

`pip install pytest-watch`

`ptw`

---

## os
## sys
## re
## time

## shutil
```
import shutil

# copy
shutil.copy("path_file_name", "path_directory_name/")

# move
shutil.copy("path_file_name", "path_directory_name/")
```

## pathlib
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
## pprint

## date
## datetime

## flask
## django
## requests

## selenium
## bs4

## jupyterlab

## numpy
## pandas
## mecab
## opencv-python
## pymovie
## PyInstaller

## openxl
## xlwings

## concurrent.futures
## sqlalchemy

## 
## 
## 