@echo off
chcp 932 >nul
echo ���l�[���o�b�`�����c�[��
echo.

set "user_home=%USERPROFILE%"
set "output_dir=%user_home%\Pictures\TadakanV3\RenameBats"

if not exist "%output_dir%" mkdir "%output_dir%"

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
echo cd /d "%%~dp0\..\tools"
echo python renumber.py %%* %keywords%
echo if errorlevel 1 pause
) > "%output_dir%\%filename%.bat"

echo %filename%.bat�𐶐����܂���
echo �ۑ��ꏊ: %output_dir%
pause