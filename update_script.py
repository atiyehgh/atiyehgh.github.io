import os
import re

DATA_JS_PATH = "data.js"

FOLDERS = {
    "gallery": "images/uploads/gallery",
    "evidence": "images/uploads/evidence",
    "stories": "images/uploads/stories"
}

def update_data_file():
    if not os.path.exists(DATA_JS_PATH):
        print("فایل data.js پیدا نشد!")
        return

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    for section, folder in FOLDERS.items():
        if not os.path.exists(folder):
            continue

        # گرفتن تمام فایل‌های معتبر داخل پوشه
        valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.JPG', '.JPEG', '.PNG')
        all_files = [f for f in os.listdir(folder) if f.endswith(valid_extensions)]
        
        # مرتب‌سازی ساده بر اساس نام فایل برای ثبات
        all_files.sort()

        # استخراج عکس‌هایی که همین الان داخل data.js برای این بخش ثبت شده‌اند
        pattern = rf"({section}\s*:\s*\[)(.*?)(\],)"
        match = re.search(pattern, content, content.__class__ if hasattr(content, '__class__') else 0) # روش امن برای پیدا کردن بخش
        
        # پیدا کردن مسیرهای موجود در فایل
        existing_paths = re.findall(rf'"{folder}/([^"]+)"', content)

        # پیدا کردن فایل‌هایی که جدید هستند و هنوز در data.js نیستند
        new_files = [f for f in all_files if f not in existing_paths]
        
        # ترکیب: عکس‌های جدید اول قرار می‌گیرند، عکس‌های قبلی پشت سر آن‌ها حفظ می‌شوند
        combined_files = new_files + [f for f in all_files if f in existing_paths]
        # اگر هیچ‌کدام با الگوی قبلی تطابق نداشتند، همان لیست پوشه را بگذار
        if not combined_files:
            combined_files = all_files

        # ساختن متن جدید برای جایگذاری در آرایه
        new_entries = ""
        for img in combined_files:
            path = f"{folder}/{img}"
            alt_text = "هویت بصری Alka" if section == "gallery" else ("نتیجه Alka" if section == "evidence" else "استوری Alka")
            new_entries += f'    {{\n      src: "{path}",\n      alt: "{alt_text}"\n    }},\n'

        # جایگذاری در فایل data.js
        if re.search(pattern, content, re.DOTALL):
            replacement = rf"\1\n" + new_entries.rstrip(",\n") + f"\n  \\2"
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("فایل data.js با موفقیت و بدون جابجایی عکس‌های قبلی به‌روزرسانی شد!")

if __name__ == "__main__":
    update_data_file()
