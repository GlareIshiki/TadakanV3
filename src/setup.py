import os
import shutil

def compare_version(ver1, ver2):
    """バージョン比較 (ver1 > ver2 なら True)"""
    v1 = ver1.replace("ver", "").replace("v", "")
    v2 = ver2.replace("ver", "").replace("v", "")
    
    v1_parts = [int(x) for x in v1.split('.')]
    v2_parts = [int(x) for x in v2.split('.')]
    
    while len(v1_parts) < len(v2_parts):
        v1_parts.append(0)
    while len(v2_parts) < len(v1_parts):
        v2_parts.append(0)
    
    return v1_parts > v2_parts

def clean_install(install_dir):
    """toolsディレクトリを完全にクリア"""
    if os.path.exists(install_dir):
        print(f"🧹 既存ファイルをクリア中: {install_dir}")
        try:
            shutil.rmtree(install_dir)
            print("✅ クリア完了")
        except Exception as e:
            print(f"❌ クリアエラー: {e}")
            return False
    return True

def main():
    print("TadakanV3 セットアップツール (Version 3.02)")
    print("=" * 40)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    user_home = os.path.expanduser("~")
    base_dir = os.path.join(user_home, "Pictures", "TadakanV3")
    install_dir = os.path.join(base_dir, "tools")
    
    version_file = os.path.join(current_dir, "version.txt")
    
    # バージョンチェック
    if not os.path.exists(version_file):
        print("❌ エラー: version.txtが見つかりません")
        return
    
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
    is_update = False
    
    if os.path.exists(current_version_file):
        try:
            with open(current_version_file, 'r', encoding='utf-8') as f:
                current_version = f.read().strip()
            print(f"💾 現在のバージョン: {current_version}")
            is_update = True
        except:
            print("⚠️ 現在のバージョン情報が読み込めませんでした")
    else:
        print("🆕 初回インストールです")
    
    # バージョン比較
    if current_version and not compare_version(new_version, current_version):
        if new_version == current_version:
            print("✅ 最新バージョンです")
            choice = input("再インストールしますか？ (y/N): ")
            if choice.lower() != 'y':
                print("インストールをキャンセルしました")
                return
        else:
            print("⚠️ 現在のバージョンの方が新しいようです")
            choice = input("それでもインストールしますか？ (y/N): ")
            if choice.lower() != 'y':
                print("インストールをキャンセルしました")
                return
    
    print(f"\n🚀 {new_version} をインストールします...")
    
    # クリーンインストール実行
    if is_update:
        print("\n📋 アップデート方式:")
        print("  既存のtoolsフォルダを完全にクリアして新規インストールします")
        print("  ※ RenameBats, FilterBats, viewフォルダは保持されます")
        
        choice = input("\nクリーンインストールを実行しますか？ (Y/n): ")
        if choice.lower() == 'n':
            print("インストールをキャンセルしました")
            return
        
        if not clean_install(install_dir):
            print("❌ クリーンインストールに失敗しました")
            return
    
    # 必要なディレクトリを作成
    dirs_to_create = [
        install_dir,
        os.path.join(base_dir, "RenameBats"),
        os.path.join(base_dir, "FilterBats"),
        os.path.join(base_dir, "view")
    ]
    
    for dir_path in dirs_to_create:
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"📁 ディレクトリ確認: {os.path.basename(dir_path)}")
        except Exception as e:
            print(f"❌ ディレクトリ作成エラー: {dir_path} - {e}")
    
    # ファイルコピーリスト
    files_to_copy = [
        "rename_generator.bat",  # generator.bat から変更
        "renumber.py",
        "filter_generator.bat",
        "filter.py"
    ]
    success_count = 0
    
    print(f"\n📦 ファイルをインストール中...")
    for filename in files_to_copy:
        source = os.path.join(current_dir, filename)
        dest = os.path.join(install_dir, filename)
        
        try:
            if os.path.exists(source):
                shutil.copy2(source, dest)
                print(f"✅ {filename}")
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
    # 使用方法の表示も修正
    print("\n💡 使用方法:")
    print("  • リネームバッチ生成: rename_generator.bat を実行")  # 変更
    print("  • フィルターバッチ生成: filter_generator.bat を実行")
        
    if is_update:
        print(f"\n📋 アップデート完了:")
        print(f"  {current_version} → {new_version}")

if __name__ == "__main__":
    main()