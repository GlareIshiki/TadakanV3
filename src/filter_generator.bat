@echo off
chcp 932 >nul
echo フィルターバッチ生成ツール
echo.

set "user_home=%USERPROFILE%"
set "output_dir=%user_home%\Pictures\TadakanV3\FilterBats"

if not exist "%output_dir%" mkdir "%output_dir%"

echo フィルター条件を入力してください:
echo 例: 秋葉原ライブ ナコレクション  (スペース区切りはOR条件)
echo 例: 秋葉原ライブ AND ナコレクション
echo 例: cd OR (限定版 AND 秋葉原ライブ)
echo.
set /p condition=条件: 

(
echo @echo off
echo chcp 932 ^>nul
echo cd /d "%%~dp0\..\tools"
echo python filter.py "%condition%"
echo pause
) > "%output_dir%\%condition%.bat"

echo %condition%.batを生成しました
echo 保存場所: %output_dir%
pause