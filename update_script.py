return

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # ---------------------------------------
    # بررسی هر سه بخش
    # ---------------------------------------

    for section, folder in FOLDERS.items():

        content = update_section(
            content,
            section,
            folder
        )

    # ---------------------------------------
    # ذخیره data.js
    # ---------------------------------------

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("data.js با موفقیت به‌روزرسانی شد!")


if __name__ == "__main__":
    update_data_file()
