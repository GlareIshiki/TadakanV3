@echo off
chcp 932 >nul
echo リネームバッチ生成ツール
echo.

set "user_home=%USERPROFILE%"
set "output_dir=%user_home%\Pictures\TadakanV3\RenameBats"

if not exist "%output_dir%" mkdir "%output_dir%"

echo キーワードの数を入力してください:
set /p count=
echo.

set keywords=
set filename=
for /l %%i in (1,1,%count%) do (
    set /p word=キーワード%%i: 
    call set keywords=%%keywords%% %%word%%
    if %%i==1 (
        call set filename=%%word%%
    ) else (
        call set filename=%%filename%%_%%word%%
    )
)

(
echo @echo off
echo chcp 932 ^>nul
echo cd /d "%%~dp0\..\tools"
echo python renumber.py %%* %keywords%
echo if errorlevel 1 pause
) > "%output_dir%\%filename%.bat"

echo %filename%.batを生成しました
echo 保存場所: %output_dir%
pause