# AWSのEC2でのpipenvとPython3系の環境構築手順

- EC2インスタンス起動
- ssh接続

が済んでいるところから、以下スタート。

---

- yumをアップデート（事前準備）

    ```
    yum version

    sudo  yum update
    ```

- Python3.6とpipenvをインストール

    ```
    yum list | grep python

    sudo yum install -y python36

    vi .bash_profile

    alias python=python3

    source .bash_profile

    python --version
    // Python 3.6.8

    sudo pip install pipenv
    ```

- プロジェクト用ディレクトリを用意し、pipenvで仮想環境構築

    ```
    mkdir dir_project

    cd dir_project

    pipenv install

    pipenv --python 3.6

    pipenv check
    ```

- いちおう容量もつど確認

    ```
    df
    ```
