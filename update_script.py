import os
import re
import subprocess

DATA_JS_PATH = "data.js"

FOLDERS = {
    "gallery": "images/uploads/gallery",
    "evidence": "images/uploads/evidence",
    "stories": "images/uploads/stories"
}

def get_git_time(file_path):
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return int(result.stdout.strip()) if result.stdout.strip() else 0
    except:
        return 0


def get_images_from_folder(folder_path):
    if not os.path.exists(folder_path):
        return []

    valid_extensions = (
        '.jpg', '.jpeg', '.png', '.webp',
        '.JPG', '.JPEG', '.PNG', '.WEBP'
    )

    files = [
        f for f in os.listdir(folder_path)
        if f.endswith(valid_extensions)
    ]

    # قدیمی‌ترین → جدیدترین
    # بنابراین عکس جدید همیشه به انتهای لیست اضافه می‌شود
    files.sort(
        key=lambda x: get_git_time(os.path.join(folder_path, x))
    )

    return files


def update_data_file():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    for section, folder in FOLDERS.items():
        images = get_images_from_folder(folder)

        if not images:
            continue

        new_entries = ""

        for img in images:
            path = f"{folder}/{img}"

            if section == "gallery":
                alt_text = "هویت بصری Alka"
            elif section == "evidence":
                alt_text = "نتیجه Alka"
            else:
                alt_text = "استوری Alka"

            new_entries += (
                f'    {{\n'
                f'      src: "{path}",\n'
                f'      alt: "{alt_text}"\n'
                f'    }},\n'
            )

        pattern = rf"({section}\s*:\s*\[).*?(\],)"

        if re.search(pattern, content, re.DOTALL):
            replacement = (
                rf"\1\n"
                + new_entries.rstrip(",\n")
                + f"\n  \\2"
            )

            content = re.sub(
                pattern,
                replacement,
                content,
                flags=re.DOTALL
            )

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("فایل data.js با موفقیت به‌روزرسانی شد!")


if __name__ == "__main__":
    update_data_file()
