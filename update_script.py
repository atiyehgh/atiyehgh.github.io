import os
import re

DATA_JS_PATH = "data.js"

# پوشه‌های مربوط به هر بخش
FOLDERS = {
    "gallery": "images/uploads/gallery",
    "evidence": "images/uploads/evidence",
    "stories": "images/uploads/stories"
}

def get_images_from_folder(folder_path):
    if not os.path.exists(folder_path):
        return []
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.JPG', '.JPEG', '.PNG')
    files = [f for f in os.listdir(folder_path) if f.endswith(valid_extensions)]
    files.sort(reverse=True) # جدیدترین عکس‌ها بالا باشند
    return files

def update_data_file():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # برای هر بخش، عکس‌های داخل پوشه‌اش را می‌خوانیم و جایگزین می‌کنیم
    for section, folder in FOLDERS.items():
        images = get_images_from_folder(folder)
        if not images:
            continue  # اگر پوشه‌ای خالی بود کاری به آن نداریم

        new_entries = ""
        for img in images:
            path = f"{folder}/{img}"
            # متن alt را بر اساس نام بخش تنظیم می‌کنیم
            alt_text = "هویت بصری Alka" if section == "gallery" else ("نتیجه Alka" if section == "evidence" else "استوری Alka")
            new_entries += f'    {{\n      src: "{path}",\n      alt: "{alt_text}"\n    }},\n'

        # الگوی پیدا کردن بخش مورد نظر در فایل data.js (مثلا gallery یا evidence یا stories)
        pattern = rf"({section}\s*:\s*\[).*?(\],)"
        
        if re.search(pattern, content, re.DOTALL):
            replacement = rf"\1\n" + new_entries.rstrip(",\n") + f"\n  \\2"
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # ذخیره کردن فایل نهایی
    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("فایل data.js با موفقیت برای تمام بخش‌ها به‌روزرسانی شد!")

if __name__ == "__main__":
    update_data_file()
