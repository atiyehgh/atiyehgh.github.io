import os
import re

UPLOAD_DIR = "images/uploads"
DATA_JS_PATH = "data.js"

def get_uploaded_images():
    if not os.path.exists(UPLOAD_DIR):
        return []
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.JPG', '.JPEG', '.PNG', '.JPG')
    files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(valid_extensions)]
    files.sort(reverse=True) # جدیدترین عکس‌ها بالاتر قرار بگیرند
    return files

def update_data_file():
    images = get_uploaded_images()
    if not images:
        print("هیچ عکسی پیدا نشد!")
        return

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # ساختن ساختار جدید برای گالری
    new_gallery_entries = ""
    for img in images:
        path = f"images/uploads/{img}"
        new_gallery_entries += f'    {{\n      src: "{path}",\n      alt: "هویت بصری Alka"\n    }},\n'

    # جایگزین کردن بخش gallery در فایل data.js
    pattern = r"(gallery\s*:\s*\[).*?(\],)"
    
    if re.search(pattern, content, re.DOTALL):
        replacement = r"\1\n" + new_gallery_entries.rstrip(",\n") + r"\n  \2"
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("فایل data.js با موفقیت به‌روزرسانی شد!")
    else:
        print("خطا: بخش gallery پیدا نشد.")

if __name__ == "__main__":
    update_data_file()
