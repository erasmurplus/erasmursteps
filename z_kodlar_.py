import os

# Ana dizin (şu anki çalışma dizini içinde erasmurnext klasörü açar)
BASE_DIR = os.path.join(os.getcwd(), "erasmurnext")

# Alt klasörler ve dosyalar
folders = {
    "controllers": ["__init__.py", "controller.py"],
    "models": ["__init__.py", "model.py"],
    "views": ["__init__.py", "view.py"]
}

# Ana uygulama dosyası
main_app_file = os.path.join(BASE_DIR, "app.py")

# Dizin ve dosya oluşturma işlemi
def create_mvc_structure():
    print(f"📁 Ana dizin: {BASE_DIR}")
    os.makedirs(BASE_DIR, exist_ok=True)

    for folder, files in folders.items():
        folder_path = os.path.join(BASE_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"📂 Oluşturuluyor: {folder_path}")
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                pass  # Dosyayı boş oluştur
            print(f"  └─ 📄 Dosya oluşturuldu: {file_path}")

    # app.py dosyası oluştur
    with open(main_app_file, "w", encoding="utf-8") as f:
        pass
    print(f"📄 Ana dosya oluşturuldu: {main_app_file}")

if __name__ == "__main__":
    create_mvc_structure()
