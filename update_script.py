import os
import re

DATA_JS_PATH = "data.js"
STORIES_ROOT = "images/uploads/stories"
GALLERY_PATH = "images/uploads/gallery"
EVIDENCE_PATH = "images/uploads/evidence"

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG", ".PNG", ".WEBP")

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

    # --- 1. بروزرسانی بخش گالری ---
    gallery_files = get_files(GALLERY_PATH)
    if gallery_files:
        entries = [f'    {{\n      src: "{GALLERY_PATH}/{img}",\n      alt: "هویت بصری Alka"\n    }}' for img in gallery_files]
        new_gallery = "\n" + ",\n".join(entries) + "\n  "
        content = re.sub(r"(gallery\s*:\s*\[).*?(\])", rf"\1{new_gallery}\2", content, flags=re.DOTALL)

    # --- 2. بروزرسانی بخش Evidence (نتایج) ---
    evidence_files = get_files(EVIDENCE_PATH)
    if evidence_files:
        entries = [f'    {{\n      src: "{EVIDENCE_PATH}/{img}",\n      alt: "نتیجه Alka"\n    }}' for img in evidence_files]
        new_evidence = "\n" + ",\n".join(entries) + "\n  "
        content = re.sub(r"(evidence\s*:\s*\[).*?(\])", rf"\1{new_evidence}\2", content, flags=re.DOTALL)

    # --- 3. بروزرسانی هوشمند استوری‌ها بر اساس پوشه‌ها و فایل title.txt ---
    if os.path.exists(STORIES_ROOT):
        # پیدا کردن تمام زیرپوشه‌های داخل پوشه stories
        subfolders = sorted([d for d in os.listdir(STORIES_ROOT) if os.path.isdir(os.path.join(STORIES_ROOT, d))])
        
        group_entries = []
        for folder_name in subfolders:
            subfolder_path = os.path.join(STORIES_ROOT, folder_name)
            images = get_files(subfolder_path)
            
            if not images:
                continue

            # خواندن عنوان فارسی از فایل title.txt داخل پوشه (اگر نبود از اسم خود پوشه استفاده می‌کند)
            title_file_path = os.path.join(subfolder_path, "title.txt")
            if os.path.exists(title_file_path):
                with open(title_file_path, "r", encoding="utf-8") as tf:
                    group_title = tf.read().strip()
            else:
                group_title = folder_name.replace("-", " ").replace("_", " ")

            item_entries = []
            for img in images:
                path = f"{subfolder_path}/{img}".replace("\\", "/")
                item_entries.append(f'''        {{
          src: "{path}",
          alt: "استوری Alka"
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
            content = re.sub(r"storyGroups\s*:\s*\[.*?\]", story_groups_block, content, flags=re.DOTALL)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("فایل data.js با موفقیت بر اساس پوشه‌ها و عناوین فارسی به‌روزرسانی شد!")

if __name__ == "__main__":
    update_data_file()
