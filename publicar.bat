@echo off
chcp 65001 > nul
echo ============================================================
echo   ACSOFT STUDIOS - DEPLOY AUTOMATICO PARA O SITE ONLINE
echo ============================================================
echo.
echo [1/3] Preparando arquivos modificados...
"C:\Program Files\Git\cmd\git.exe" add .
echo.
set /p msg="[2/3] Descreva o que mudou (ou aperte Enter para padrao): "
if "%msg%"=="" set msg="Atualizacao no site ACsoft"
"C:\Program Files\Git\cmd\git.exe" commit -m "%msg%"
echo.
echo [3/3] Enviando para o GitHub e disparando deploy automatico...
"C:\Program Files\Git\cmd\git.exe" push
echo.
echo ============================================================
echo   ✓ SUCESSO! O site estara atualizado no ar em ~15 segundos!
echo ============================================================
pause
