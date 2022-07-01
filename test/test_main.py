import pytest
import runpy
import pathlib
from simplepython import main



def test_init(capsys):
    scripts = pathlib.Path('../simplepython/main.py').resolve()
    runpy.run_path(scripts, run_name='__main__')
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"

def test_main():
    assert main.main() == "Hello World!"
