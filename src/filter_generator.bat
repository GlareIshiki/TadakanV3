@echo off
chcp 932 >nul
echo �t�B���^�[�o�b�`�����c�[��
echo.

set "user_home=%USERPROFILE%"
set "output_dir=%user_home%\Pictures\TadakanV3\FilterBats"

if not exist "%output_dir%" mkdir "%output_dir%"

echo �t�B���^�[��������͂��Ă�������:
echo ��: �H�t�����C�u �i�R���N�V����  (�X�y�[�X��؂��OR����)
echo ��: �H�t�����C�u AND �i�R���N�V����
echo ��: cd OR (����� AND �H�t�����C�u)
echo.
set /p condition=����: 

(
echo @echo off
echo chcp 932 ^>nul
echo cd /d "%%~dp0\..\tools"
echo python filter.py "%condition%"
echo pause
) > "%output_dir%\%condition%.bat"

echo %condition%.bat�𐶐����܂���
echo �ۑ��ꏊ: %output_dir%
pause