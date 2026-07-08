@echo off
REM Double-cliquez ce fichier pour lancer la galerie des ecrans Smuppy.
cd /d "%~dp0"
set PORT=8799
echo Demarrage du serveur local sur http://127.0.0.1:%PORT% ...
start "" "http://127.0.0.1:%PORT%/index.html"
where python >nul 2>nul
if %ERRORLEVEL%==0 (
  python -m http.server %PORT% --bind 127.0.0.1
) else (
  where npx >nul 2>nul
  if %ERRORLEVEL%==0 (
    npx --yes serve -l %PORT% .
  ) else (
    echo Ni python ni npx trouves. Installez Python 3 : https://www.python.org/downloads/
    pause
  )
)
