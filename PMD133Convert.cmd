@echo off
winget install Python.Python.3.11 -h -e -s winget
py -m pip install --upgrade pip
py -m pip install --upgrade Pillow
py PMD133Convert.py
pause