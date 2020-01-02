@ECHO OFF
TITLE Storybro: A community driven fork of AIDungeon 2

ECHO This is installing chocolatey
ECHO ==========================================================

powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"

ECHO Done!

PAUSE