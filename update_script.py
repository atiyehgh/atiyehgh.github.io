import os
import re

DATA_JS_PATH = "data.js"
STORIES_ROOT = "images/uploads/stories"
GALLERY_PATH = "images/uploads/gallery"
EVIDENCE_PATH = "images/uploads/evidence"

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG", ".PNG", ".WEBP")

# 📌 لیست دقیق و قطعی پوشه‌ها به ترتیب دلخواه شما
# هر زمان پوشه جدیدی (مثلاً پوشه ۸) اضافه کردی، کافیست اسمش را به انتهای این لیست اضافه کنی.
CUSTOM_FOLDER_ORDER = [
    "paraffin-story",  # ۱. پارافین
    "kash_story",      # ۲. کاش
    "Hadieh_story",    # ۳. هدیه
    "Event_story",     # ۴. ایونت
    "Kederi_story",    # ۵. کدری
    "Tarak_story",     # ۶. ترک
    "Dama_story",      # ۷. دما
]

def get_files(folder):
    if not os.path.exists(folder):
        return []
    return sorted([f for f in os.listdir(folder) if f.endswith(VALID_EXTENSIONS)])

def update_data_file():
    if not os.path.exists(DATA_JS_PATH):
        print("فایل data.js پیدا نشد!")
        return

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # --- 1. بروزرسانی گالری ---
    gallery_files = get_files(GALLERY_PATH)
    if gallery_files:
        entries = [f'    {{\n      src: "{GALLERY_PATH}/{img}",\n      alt: "هویت بصری Alka"\n    }}' for img in gallery_files]
        new_gallery = "\n" + ",\n".join(entries) + "\n  "
        content = re.sub(r"(gallery\s*:\s*\[).*?(\])", rf"\1{new_gallery}\2", content, flags=re.DOTALL)

    # --- 2. بروزرسانی مدرک (Evidence) ---
    evidence_files = get_files(EVIDENCE_PATH)
    if evidence_files:
        entries = [f'    {{\n      src: "{EVIDENCE_PATH}/{img}",\n      alt: "نتیجه Alka"\n    }}' for img in evidence_files]
        new_evidence = "\n" + ",\n".join(entries) + "\n  "
        content = re.sub(r"(evidence\s*:\s*\[).*?(\])", rf"\1{new_evidence}\2", content, flags=re.DOTALL)

    # --- 3. خواندن خودکار title.txt و مرتب‌سازی قطعی ---
    if os.path.exists(STORIES_ROOT):
        # گرفتن همه پوشه‌های موجود در مسیر
        existing_folders = [d for d in os.listdir(STORIES_ROOT) if os.path.isdir(os.path.join(STORIES_ROOT, d))]
        
        # پیدا کردن پوشه‌هایی که در لیست تعریف شده‌اند به همان ترتیب دقیق لیست
        ordered_folders = []
        
        # ۱. اول پوشه‌هایی که توی لیست ثبت شده‌اند را دقیقاً به همان ترتیب می‌آوریم
        for folder_in_list in CUSTOM_FOLDER_ORDER:
            for actual_folder in existing_folders:
                if actual_folder.lower() == folder_in_list.lower():
                    ordered_folders.append(actual_folder)
                    break
        
        # ۲. اگر پوشه‌ای جدیدی بود که هنوز اسمش توی لیست وارد نشده، تهِ لیست اضافه می‌شود
        for actual_folder in existing_folders:
            if not any(actual_folder.lower() == f.lower() for f in CUSTOM_FOLDER_ORDER):
                ordered_folders.append(actual_folder)

        group_entries = []
        for group_index, folder_name in enumerate(ordered_folders, start=1):
            subfolder_path = os.path.join(STORIES_ROOT, folder_name)
            images = get_files(subfolder_path)
            
            if not images:
                continue

            # خواندن متن از فایل title.txt داخل پوشه
            title_file_path = os.path.join(subfolder_path, "title.txt")
            raw_title = ""
            if os.path.exists(title_file_path):
                try:
                    with open(title_file_path, "r", encoding="utf-8") as tf:
                        raw_title = tf.read().strip()
                except Exception as e:
                    print(f"خطا در خواندن فایل title.txt: {e}")
            
            if not raw_title:
                raw_title = folder_name.replace("-", " ").replace("_", " ")

            group_title = f"{group_index:02d}. " + raw_title

            item_entries = []
            for img_index, img in enumerate(images, start=1):
                path = f"{subfolder_path}/{img}".replace("\\", "/")
                item_entries.append(f'''        {{
          src: "{path}",
          alt: "استوری Alka",
          index: "{img_index:02d}"
        }}''')
            
            items_str = ",\n".join(item_entries)
            group_entries.append(f'''    {{
      groupTitle: "{group_title}",
      items: [
{items_str}
      ]
    }}''')

        if group_entries:
            groups_str = ",\n".join(group_entries)
            story_groups_block = f"storyGroups: [\n{groups_str}\n  ]"
            if "storyGroups:" in content:
                content = re.sub(r"storyGroups\s*:\s*\[.*?\](?=\s*,\s*(?:timeline|tools|instagramUrl|\}))", story_groups_block, content, flags=re.DOTALL)
            else:
                print("بخش storyGroups در فایل یافت نشد!")

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("فایل data.js با موفقیت و ۱۰۰٪ تضمینی به ترتیب درست آپدیت شد!")

if __name__ == "__main__":
    update_data_file()
