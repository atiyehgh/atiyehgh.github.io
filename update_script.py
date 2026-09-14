import os
import re

DATA_JS_PATH = "data.js"

FOLDERS = {
    "gallery": "images/uploads/gallery",
    "evidence": "images/uploads/evidence",
    "stories": "images/uploads/stories"
}

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".JPG",
    ".JPEG",
    ".PNG",
    ".WEBP"
)


def get_files(folder):
    if not os.path.exists(folder):
        return []

    return [
        f for f in os.listdir(folder)
        if f.endswith(VALID_EXTENSIONS)
    ]


def update_section(content, section, folder):

    all_files = get_files(folder)

    if not all_files:
        return content

    # پیدا کردن بخش مربوط به gallery / evidence / stories
    section_pattern = rf"({section}\s*:\s*\[)(.*?)(\n\s*\])"

    match = re.search(section_pattern, content, re.DOTALL)

    if not match:
        print(f"بخش {section} در data.js پیدا نشد.")
        return content

    section_content = match.group(2)

    # عکس‌هایی که همین الان داخل data.js هستند
    existing_paths = re.findall(
        rf'src\s*:\s*"{re.escape(folder)}/([^"]+)"',
        section_content
    )

    # فقط عکس‌هایی که هنوز در data.js نیستند
    new_files = [
        f for f in all_files
        if f not in existing_paths
    ]

    # اگر عکس جدیدی وجود ندارد، هیچ چیزی را جابه‌جا نکن
    if not new_files:
        print(f"{section}: عکس جدیدی پیدا نشد.")
        return content

    print(f"{section}: {len(new_files)} عکس جدید پیدا شد.")

    # عکس‌های جدید باید اول لیست باشند
    combined_files = new_files + existing_paths

    # حذف موارد تکراری، بدون تغییر ترتیب
    seen = set()
    final_files = []

    for file_name in combined_files:
        if file_name not in seen:
            seen.add(file_name)
            final_files.append(file_name)

    # ساختن آبجکت‌های جدید
    entries = []

    for img in final_files:

        path = f"{folder}/{img}"

        if section == "gallery":
            alt_text = "هویت بصری Alka"

        elif section == "evidence":
            alt_text = "نتیجه Alka"

        else:
            alt_text = "استوری Alka"

        entries.append(
            f'''    {{
      src: "{path}",
      alt: "{alt_text}"
    }}'''
        )

    new_section_content = "\n" + ",\n".join(entries) + "\n  "

    # فقط محتوای همان آرایه را جایگزین می‌کنیم
    content = (
        content[:match.start(2)]
        + new_section_content
        + content[match.end(2):]
    )

    return content


def update_data_file():

    if not os.path.exists(DATA_JS_PATH):
        print("فایل data.js پیدا نشد!")
        return

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # هر سه بخش را بررسی کن
    for section, folder in FOLDERS.items():
        content = update_section(
            content,
            section,
            folder
        )

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("data.js با موفقیت به‌روزرسانی شد!")


if __name__ == "__main__":
    update_data_file()
