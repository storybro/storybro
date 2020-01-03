@ECHO OFF

TITLE Storybro: A community driven fork of AIDungeon 2

ECHO This installs all the proper tools to get the game running
ECHO ==========================================================

choco install python3 --version=3.6.8

pip install poetry

choco install aria2

powershell -Command "cd %~dp0; poetry install; poetry run pip install tensorflow==1.15; ECHO Done!;poetry shell;"

PAUSE
