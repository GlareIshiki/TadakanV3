@echo off
chcp 932 >nul
echo �L�[���[�h�̐�����͂��Ă�������:
set /p count=
echo.

set keywords=
set filename=
for /l %%i in (1,1,%count%) do (
    set /p word=�L�[���[�h%%i: 
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

echo %filename%.bat�𐶐����܂���
pause