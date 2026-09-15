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


def find_section(content, section):
    """
    پیدا کردن محدوده آرایه gallery / evidence / stories
    """

    pattern = rf"{section}\s*:\s*\["

    match = re.search(pattern, content)

    if not match:
        return None

    start = match.end()

    bracket_count = 1
    i = start

    while i < len(content):

        if content[i] == "[":
            bracket_count += 1

        elif content[i] == "]":
            bracket_count -= 1

            if bracket_count == 0:
                return match.start(), start, i

        i += 1

    return None


def update_section(content, section, folder):

    section_info = find_section(content, section)

    if not section_info:
        print(f"بخش {section} پیدا نشد.")
        return content

    section_start, content_start, content_end = section_info

    section_content = content[content_start:content_end]

    all_files = get_files(folder)

    if not all_files:
        print(f"{section}: عکسی در پوشه پیدا نشد.")
        return content

    # پیدا کردن فایل‌هایی که همین الان در data.js هستند
    existing_paths = re.findall(
        rf'src\s*:\s*"?/?{re.escape(folder)}/([^"]+)"?',
        section_content
    )

    # فایل‌هایی که در پوشه هستند ولی هنوز در data.js نیستند
    new_files = [
        f for f in all_files
        if f not in existing_paths
    ]

    if not new_files:
        print(f"{section}: عکس جدیدی پیدا نشد.")
        return content

    print(f"{section}: {len(new_files)} عکس جدید پیدا شد.")

    # ---------------------------------------
    # ترتیب مهم:
    #
    # عکس‌های قبلی همان جای خود می‌مانند
    # عکس‌های جدید به انتهای لیست اضافه می‌شوند
    # ---------------------------------------

    combined_files = existing_paths + new_files

    # حذف تکراری‌ها بدون تغییر ترتیب
    final_files = []
    seen = set()

    for file_name in combined_files:

        if file_name not in seen:
            seen.add(file_name)
            final_files.append(file_name)

    # ساخت آبجکت‌های data.js
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

    # جایگزینی فقط محتوای همان آرایه
    content = (
        content[:content_start]
        + new_section_content
        + content[content_end:]
    )

    return content


def update_data_file():

    if not os.path.exists(DATA_JS_PATH):
        print("فایل data.js پیدا نشد!")
        return

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # بررسی هر سه بخش
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
