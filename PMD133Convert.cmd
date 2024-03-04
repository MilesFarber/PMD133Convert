@echo off
winget install Python.Python.3.11 -h -e -s winget
python -m pip install --upgrade pip
python -m pip install --upgrade Pillow
python PMD133Convert.py
pause