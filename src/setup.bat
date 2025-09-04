@echo off
chcp 932 >nul
cd /d "%~dp0"
python setup.py
pause