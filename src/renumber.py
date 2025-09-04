import os
import sys
import re
import shutil

# 引数を取得
args = sys.argv[1:]
file_or_folder_path = args[0]
keywords = args[1:]

print(f"処理対象: {file_or_folder_path}")
print(f"キーワード: {keywords}")

# 移動先ディレクトリを設定
user_home = os.path.expanduser("~")
target_dir = os.path.join(user_home, "Pictures", "TadakanV3")

# TadakanV3フォルダがなければ作成
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"フォルダを作成しました: {target_dir}")

print(f"移動先: {target_dir}")

# キーワードを_でつなげてベース名を作成
base_name = "_".join(keywords)
print(f"ベース名: {base_name}")

# 処理するファイルリストを作成
files_to_process = []

# 複数ファイルが渡された場合（バッチファイルで%*を使用）
if len(args) > len(keywords) + 1:
    # 最初の引数以降で、キーワードでないものはファイルパス
    for i in range(1, len(args) - len(keywords)):
        path = args[i]
        if os.path.isfile(path):
            files_to_process.append(path)

# 単一のパスが渡された場合
else:
    if os.path.isfile(file_or_folder_path):
        # ファイルの場合
        files_to_process.append(file_or_folder_path)
    elif os.path.isdir(file_or_folder_path):
        # フォルダの場合、中のファイルを全て取得
        print(f"フォルダを処理中: {file_or_folder_path}")
        for file in os.listdir(file_or_folder_path):
            file_path = os.path.join(file_or_folder_path, file)
            if os.path.isfile(file_path):
                files_to_process.append(file_path)

print(f"処理するファイル数: {len(files_to_process)}")

# 移動先ディレクトリで同じベース名の既存ファイルの最大番号を探す
max_num = 0
for file in os.listdir(target_dir):
    if file.startswith(base_name):
        numbers = re.findall(r'_(\d+)\.\w+$', file)
        if numbers:
            max_num = max(max_num, int(numbers[0]))

print(f"最大番号: {max_num}")

# 各ファイルを処理
for i, file_path in enumerate(files_to_process):
    new_num = max_num + i + 1
    ext = os.path.splitext(os.path.basename(file_path))[1]
    new_name = f"{base_name}_{new_num:05d}{ext}"
    new_path = os.path.join(target_dir, new_name)
    
    print(f"処理中 ({i+1}/{len(files_to_process)}): {os.path.basename(file_path)} -> {new_name}")
    shutil.move(file_path, new_path)

print(f"すべて完了しました！")