# Pythonのインストール

Pythonのインストールに関する備忘録

## 概要

- Python実行時のTkinterのエラーの解消
- Pythonインストール時のlzmaに関する警告の解消

## 発生環境

- Mac mini M2
- Homebrew
- pyenv

## 結論

Pythonをインストールする前にtcl-tkとxzをインストールする。

## 解消手順

### pyenvのPythonをアンインストールする。

Pythonのインストール状況を確認する。

```
% pyenv versions
  system
* 3.12.6 (set by /Users/username/.pyenv/version)
```

systemが選択されていない場合には、systemに変更する。

```
% pyenv global system
* system (set by /Users/username/.pyenv/version)
  3.12.6
```

system以外のPythonをアンインストールする。

```
% pyenv uninstall 3.12.6
```

### tcl-tkをインストールする。

Python実行時のTkinterのエラーの解消

```
% brew install tcl-tk
```

### xzをインストールする。

Pythonインストール時のlzmaに関する警告の解消

```
% brew install xz
```

### Pythonをインストールする。

```
% pyenv install 3.12.6
```
