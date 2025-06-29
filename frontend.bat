@echo off
cd /d "%~dp0FrontEnd-PcCarton"

echo Instalando Ionic CLI...
call npm install -g @ionic/cli

echo Iniciando servidor...
call npx ionic serve

pause

