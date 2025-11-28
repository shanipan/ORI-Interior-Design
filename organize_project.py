import os
import shutil

# 設定專案主資料夾
FOLDER_NAME = "ORI_Website"

# 設定檔案結構：{ "目標子資料夾": [檔案清單] }
STRUCTURE = {
    "": ["index.html"], 
    
    "images/common": ["LOGO黑-01.JPG"],
    
    # 新增團隊資料夾
    "images/team": ["Joshua.avif"],
    
    "images/beitou": [
        "34B.jpg", "34.jpg", "34A.jpg", "34C.jpg", "34D.jpg", "34E.jpg", "34F.jpg"
    ],
    
    "images/zhang": [
        "36.jpg", "36A.jpg", "36B.jpg", "36C.jpg", "36D.jpg", "36E.jpg"
    ],
    
    "images/xinzhuang": [
        "IMG_6265.jpg", "IMG_6272.jpg", "IMG_6273.jpg", "IMG_6266.jpg", 
        "IMG_6267.jpg", "IMG_6269.jpg", "IMG_6278.jpg"
    ],
    
    "images/pet": [
        "興希望寵物沙龍001-黃.jpg", "興希望寵物沙龍002.JPG", "興希望寵物沙龍006.JPG",
        "興希望寵物沙龍008.JPG", "興希望寵物沙龍007.JPG"
    ]
}

def organize_files():
    current_dir = os.getcwd()
    project_root = os.path.join(current_dir, FOLDER_NAME)

    print(f"🔨 正在更新網站專案結構: {FOLDER_NAME} ...")

    moved_count = 0
    missing_files = []

    # 遍歷設定好的結構
    for subfolder, files in STRUCTURE.items():
        # 建立目標路徑
        target_dir = os.path.join(project_root, subfolder)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"📂 建立資料夾: {target_dir}")

        # 搬移檔案
        for filename in files:
            source_path = os.path.join(current_dir, filename)
            destination_path = os.path.join(target_dir, filename)

            # 檢查檔案是否存在 (先在當前目錄找)
            if os.path.exists(source_path):
                try:
                    shutil.move(source_path, destination_path)
                    print(f"➡️  搬移: {filename} -> {subfolder}")
                    moved_count += 1
                except Exception as e:
                    print(f"❌ 搬移失敗 {filename}: {e}")
            
            # 如果檔案已經在目標位置了
            elif os.path.exists(destination_path):
                 print(f"👌 已就位: {filename}")
            
            else:
                missing_files.append(filename)

    # 總結
    print("\n" + "="*30)
    print(f"🎉 整理完成！")
    
    if missing_files:
        print("\n⚠️  以下檔案找不到 (請確認您是否已下載到與本程式同一目錄)：")
        for f in missing_files:
            print(f" - {f}")
    
    input("\n按任意鍵結束程式...")

if __name__ == "__main__":
    organize_files()