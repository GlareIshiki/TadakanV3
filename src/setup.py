import os
import shutil

def compare_version(ver1, ver2):
    """バージョン比較 (ver1 > ver2 なら True)"""
    # "ver3.01" -> "3.01" に変換
    v1 = ver1.replace("ver", "").replace("v", "")
    v2 = ver2.replace("ver", "").replace("v", "")
    
    # "3.01" -> [3, 1] に変換
    v1_parts = [int(x) for x in v1.split('.')]
    v2_parts = [int(x) for x in v2.split('.')]
    
    # 長さを合わせる
    while len(v1_parts) < len(v2_parts):
        v1_parts.append(0)
    while len(v2_parts) < len(v1_parts):
        v2_parts.append(0)
    
    return v1_parts > v2_parts

def main():
    print("TadakanV3 セットアップツール")
    print("=" * 30)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    user_home = os.path.expanduser("~")
    install_dir = os.path.join(user_home, "Pictures", "TadakanV3", "tools")
    
    version_file = os.path.join(current_dir, "version.txt")
    
    # バージョンファイルチェック
    if not os.path.exists(version_file):
        print("❌ エラー: version.txtが見つかりません")
        return
    
    # 新しいバージョンを読み込み
    try:
        with open(version_file, 'r', encoding='utf-8') as f:
            new_version = f.read().strip()
        print(f"📦 利用可能なバージョン: {new_version}")
    except Exception as e:
        print(f"❌ バージョンファイル読み込みエラー: {e}")
        return
    
    # 現在のバージョンチェック
    current_version_file = os.path.join(install_dir, "version.txt")
    current_version = None
    
    if os.path.exists(current_version_file):
        try:
            with open(current_version_file, 'r', encoding='utf-8') as f:
                current_version = f.read().strip()
            print(f"💾 現在のバージョン: {current_version}")
        except:
            print("⚠️ 現在のバージョン情報が読み込めませんでした")
    else:
        print("🆕 初回インストールです")
    
    # バージョン比較
    if current_version and not compare_version(new_version, current_version):
        if new_version == current_version:
            print("✅ 最新バージョンです。更新の必要はありません")
            return
        else:
            print("⚠️ 現在のバージョンの方が新しいようです")
            choice = input("それでもインストールしますか？ (y/N): ")
            if choice.lower() != 'y':
                print("インストールをキャンセルしました")
                return
    
    print(f"\n🚀 {new_version} をインストールします...")
    
    # インストールディレクトリ作成
    try:
        os.makedirs(install_dir, exist_ok=True)
        print(f"📁 インストール先: {install_dir}")
    except Exception as e:
        print(f"❌ ディレクトリ作成エラー: {e}")
        return
    
    # ファイルコピー
    files_to_copy = ["generator.bat", "renumber.py"]
    success_count = 0
    
    for filename in files_to_copy:
        source = os.path.join(current_dir, filename)
        dest = os.path.join(install_dir, filename)
        
        try:
            if os.path.exists(source):
                shutil.copy2(source, dest)
                print(f"✅ {filename} をコピーしました")
                success_count += 1
            else:
                print(f"⚠️ {filename} が見つかりません")
        except Exception as e:
            print(f"❌ {filename} のコピーに失敗: {e}")
    
    # バージョン情報を保存
    try:
        with open(current_version_file, 'w', encoding='utf-8') as f:
            f.write(new_version)
        print("✅ バージョン情報を保存しました")
    except Exception as e:
        print(f"❌ バージョン情報保存エラー: {e}")
    
    print(f"\n🎉 インストール完了！ ({success_count}/{len(files_to_copy)} ファイル)")
    print(f"📍 インストール場所: {install_dir}")
    print("💡 generator.bat を実行してバッチファイルを生成してください")

if __name__ == "__main__":
    main()