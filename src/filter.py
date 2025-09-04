import os
import sys
import shutil
import re

def parse_query(query):
    """検索クエリを解析してキーワードリストと演算子を返す"""
    query = query.strip()
    
    # AND/ORが明示的にある場合
    if " AND " in query or " OR " in query:
        return query  # そのまま返して後で評価
    else:
        # スペース区切りはOR条件として扱う
        keywords = query.split()
        return " OR ".join(f'"{keyword}"' for keyword in keywords)

def evaluate_condition(filename, condition):
    """ファイル名が条件に合致するかチェック"""
    # 簡単な実装：ANDとORを処理
    condition = condition.replace('"', '')  # クォートを削除
    
    # ORで分割
    or_parts = condition.split(' OR ')
    
    for or_part in or_parts:
        if ' AND ' in or_part:
            # AND条件をチェック
            and_parts = or_part.split(' AND ')
            if all(keyword.strip() in filename for keyword in and_parts):
                return True
        else:
            # 単一キーワード
            if or_part.strip() in filename:
                return True
    
    return False

def main():
    if len(sys.argv) < 2:
        print("エラー: 検索条件が指定されていません")
        return
    
    query = sys.argv[1]
    print(f"検索条件: {query}")
    
    # パスの設定
    user_home = os.path.expanduser("~")
    source_dir = os.path.join(user_home, "Pictures", "TadakanV3")
    view_dir = os.path.join(source_dir, "view")
    
    # viewフォルダをクリア・作成
    if os.path.exists(view_dir):
        shutil.rmtree(view_dir)
    os.makedirs(view_dir)
    
    print(f"検索対象: {source_dir}")
    print(f"結果表示: {view_dir}")
    
    # クエリを解析
    condition = parse_query(query)
    print(f"解析後の条件: {condition}")
    
    # ファイルを検索
    matched_files = []
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # ディレクトリやシステムフォルダはスキップ
        if os.path.isdir(file_path):
            continue
        if filename.startswith('.'):
            continue
            
        # 条件チェック
        if evaluate_condition(filename, condition):
            matched_files.append((filename, file_path))
    
    # 結果をviewフォルダにコピー
    print(f"\n見つかったファイル: {len(matched_files)}件")
    
    for i, (filename, source_path) in enumerate(matched_files, 1):
        dest_path = os.path.join(view_dir, filename)
        try:
            shutil.copy2(source_path, dest_path)
            print(f"[{i}] {filename}")
        except Exception as e:
            print(f"[{i}] エラー: {filename} - {e}")
    
    print(f"\nフィルター完了！")
    print(f"結果は {view_dir} で確認できます")

if __name__ == "__main__":
    main()