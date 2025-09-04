@echo off
chcp 932 >nul
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
echo cd /d "%%~dp0"
echo python renumber.py %%* %keywords%
echo pause
) > "%filename%.bat"

echo %filename%.batを生成しました
pause