# Simple Python

A simple python skeleton to setup testing and create a python wheel

## Pre-Requisites

Using pyenv and poetry to manage the venv and package management. 

```shell
$ pyenv install 3.8.13
$ pyenv global 3.8.13
$ poetry install 
$ poetry shell
```
> **Note:** May need a python hook in your `.*rc` or `.*profile` inject `eval "$(pyenv init --path)"`

## Running 

Running the application
```shell
$ python3 simplepython/main.py
```

Generating a wheel 
```shell
$ python3 setup.py bdist_wheel
```
Running the tests
```shell
$ pytest test/
```
