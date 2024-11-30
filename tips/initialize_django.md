# Djangoの環境構築

https://reservoir.design/django-tutorial/

## 作業ディレクトリの作成

### ディレクトリの作成

```
% mkdir {プロジェクト名}
```

### ディレクトリの移動

```
% cd {プロジェクト名}
```

## Pythonの設定

### バージョンの確認

```
% pyenv versions
```

### バージョンの変更

```
% pyenv global {バージョン名}
```

### 仮想環境の作成

```
% python -m venv .venv
```

### 仮想環境の有効化

```
% source .venv/bin/activate
```

## Djangoの設定

### インストール

```
% pip install django
```

### プロジェクトの作成

- configの部分には、任意のディレクトリ名を設定
- 末尾の.（ドット）を外すと1階層深いディレクトリで初期化

```
% django-admin startproject config .
```

### アプリケーションの作成

```
% python manage.py startapp {アプリケーション名}
```

### settings.pyの設定

プロジェクトの作成でconfigを指定した場合、config/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{アプリケーション名}.apps.{アプリケーション名/apps.pyのクラス名}',
]

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
```
