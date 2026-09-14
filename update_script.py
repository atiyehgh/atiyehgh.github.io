import os
import re
import subprocess

DATA_JS_PATH = "data.js"

FOLDERS = {
    "gallery": "images/uploads/gallery",
    "evidence": "images/uploads/evidence",
    "stories": "images/uploads/stories"
}


def get_git_timestamp(file_path):
    """
    زمان آخرین commit مربوط به فایل را از Git می‌گیرد.
    """
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", file_path],
            capture_output=True,
            text=True,
            check=True
        )

        value = result.stdout.strip()

        if value:
            return int(value)

    except Exception:
        pass

    return 0


def get_images_from_folder(folder_path):
    if not os.path.exists(folder_path):
        return []

    valid_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".JPG",
        ".JPEG",
        ".PNG",
        ".WEBP"
    )

    files = [
        f for f in os.listdir(folder_path)
        if f.endswith(valid_extensions)
    ]

    # جدیدترین Commit اول
    files.sort(
        key=lambda f: get_git_timestamp(
            os.path.join(folder_path, f)
        ),
        reverse=True
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
                "    {\n"
                f'      src: "{path}",\n'
                f'      alt: "{alt_text}"\n'
                "    },\n"
            )

        pattern = rf"({section}\s*:\s*\[).*?(\],)"

        if re.search(pattern, content, re.DOTALL):

            replacement = (
                rf"\1\n"
                + new_entries.rstrip(",\n")
                + "\n  \\2"
            )

            content = re.sub(
                pattern,
                replacement,
                content,
                flags=re.DOTALL
            )

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("data.js با موفقیت به‌روزرسانی شد!")


if __name__ == "__main__":
    update_data_file()
