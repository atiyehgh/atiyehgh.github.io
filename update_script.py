import os
import json

DATA_JS_PATH = "data.js"

STORIES_ROOT = "images/uploads/stories"
GALLERY_PATH = "images/uploads/gallery"
EVIDENCE_PATH = "images/uploads/evidence"

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".JPG",
    ".JPEG",
    ".PNG",
    ".WEBP",
)

# ترتیب ثابت گروه‌های استوری
CUSTOM_FOLDER_ORDER = [
    "paraffin-story",
    "kash_story",
    "Hadieh_story",
    "Event_story",
    "Kederi_story",
    "Tarak_story",
    "Dama_story",
]


# =========================================================
# اطلاعات اصلی پورتفولیو
# =========================================================

BASE_PORTFOLIO = {
    "name": "عطیه قیومی‌پور",

    "title": "مدیر دیجیتال مارکتینگ برند Alka",

    "slogan": "از هویت بصری تا رشد واقعی.",

    "heroText": "طراحی کردم، محتوا ساختم و با ترکیب استراتژی و ابزارهای AI، حضور دیجیتال Alka را توسعه دادم؛ نتیجه، افزایش ۱۳ برابری تعامل پیج بود.",

    "profileImage": "/images/profile.jpg",

    "about": "وقتی همکاری با Alka را شروع کردم، پیج هویت بصری منسجمی نداشت. از بازطراحی لوگو، کاور هایلایت و پالت رنگ شروع کردم، سبک تصویری محصولات را شکل دادم و بعد سراغ استراتژی محتوا، رشته‌استوری‌های تعاملی، دایرکت مارکتینگ و تحلیل Insights رفتم. هدف فقط تولید محتوا نبود؛ ساختن یک سیستم منسجم برای دیده‌شدن، تعامل و فروش بود.",


    # =====================================================
    # خدمات
    # =====================================================

    "services": [
        {
            "title": "هویت بصری",
            "description": "بازطراحی هویت بصری پیج از لوگو و کاور هایلایت تا پالت رنگ و ایجاد یک زبان بصری یکپارچه و قابل تشخیص."
        },
        {
            "title": "استراتژی محتوا",
            "description": "ترکیب محتوای فروش، آموزشی، تعاملی و پشت‌صحنه برای اینکه پیج فقط تبلیغاتی نباشد و تعامل واقعی ایجاد کند."
        },
        {
            "title": "تولید محتوای بصری",
            "description": "طراحی پست، کاروسل و استوری و ساخت سبک تصویری محصولات؛ با استفاده هدفمند از AI در جاهایی که عکاسی حرفه‌ای محدود بود."
        },
        {
            "title": "مدیریت و رشد پیج",
            "description": "مدیریت روزانه محتوا، بررسی Insights و رفتار مخاطب و اصلاح زمان انتشار و فرمت محتوا بر اساس داده."
        }
    ],


    # =====================================================
    # Case Study
    # =====================================================

    "case": {
        "title": "یک پروژه، از بازطراحی هویت تا ساختن سیستم رشد",

        "lead": "سه ماه همکاری مستمر با Alka، از مدیریت روزانه پیج تا طراحی هویت بصری، استراتژی محتوا، سناریونویسی، دایرکت مارکتینگ و تحلیل داده."
    },


    # =====================================================
    # نتایج
    # =====================================================

    "stats": [
        {
            "value": "35,902 → 312,427",
            "label": "بازدید محتوا",
            "note": "حدود ۸.۷ برابر"
        },
        {
            "value": "2,191 → 29,365",
            "label": "تعامل",
            "note": "۱۳ برابر"
        },
        {
            "value": "+900",
            "label": "فالوور جدید",
            "note": "رشد خالص پروژه"
        },
        {
            "value": "3,636",
            "label": "ریپلای استوری",
            "note": "تعامل مستقیم مخاطب"
        }
    ],


    # =====================================================
    # فرآیند
    # =====================================================

    "process": [
        {
            "title": "۱. شروع با یکپارچه‌سازی برند",
            "text": "لوگو، کاور هایلایت‌ها، پالت رنگ و سبک تصویری از پایه بازطراحی شدند تا پیج قبل از هر چیز یک هویت مشخص داشته باشد."
        },
        {
            "title": "۲. ساختن سیستم محتوا",
            "text": "تقویم محتوا طوری چیده شد که معرفی محصول و آفر در کنار محتوای آموزشی، تعاملی و پشت‌صحنه قرار بگیرد."
        },
        {
            "title": "۳. طراحی تعامل، نه فقط انتشار",
            "text": "رشته‌استوری‌های چندقسمتی با CTA و سناریو طراحی شد تا مخاطب را به ادامه‌دادن، ریپلای و ورود به دایرکت تشویق کند."
        },
        {
            "title": "۴. تصمیم‌گیری با داده",
            "text": "Insights و رفتار مخاطب مرتب بررسی شد تا زمان انتشار، فرمت محتوا و نوع موضوعات بر اساس عملکرد واقعی اصلاح شوند."
        }
    ],


    # =====================================================
    # تایم‌لاین
    # =====================================================

    "timeline": [
        {
            "date": "مهر ۱۴۰۴",
            "title": "شروع همکاری",
            "text": "شروع مدیریت و بازطراحی حضور دیجیتال Alka."
        },
        {
            "date": "مهر تا آبان ۱۴۰۴",
            "title": "هویت بصری",
            "text": "بازطراحی لوگو، کاور هایلایت‌ها، پالت رنگ و سبک تصویری."
        },
        {
            "date": "آبان تا آذر ۱۴۰۴",
            "title": "سیستم محتوا",
            "text": "تولید محتوا، استوری، سناریو، CTA و دایرکت مارکتینگ."
        },
        {
            "date": "آذر تا دی ۱۴۰۴",
            "title": "تحلیل و بهینه‌سازی",
            "text": "بررسی Insights و اصلاح فرمت و زمان انتشار بر اساس داده."
        }
    ],


    # =====================================================
    # ابزارها
    # =====================================================

    "tools": [
        "Instagram",
        "Canva",
        "Adobe Photoshop",
        "Adobe Illustrator",
        "AI Tools",
        "Directam"
    ],


    # =====================================================
    # اینستاگرام
    # =====================================================

    "instagramUrl": "https://instagram.com/alka"
}


# =========================================================
# دریافت فایل‌های تصویری
# =========================================================

def get_files(folder):

    if not os.path.exists(folder):
        return []

    files = []

    for filename in os.listdir(folder):

        if filename.endswith(VALID_EXTENSIONS):
            files.append(filename)

    # ترتیب فایل‌ها بر اساس نام
    files.sort()

    return files


# =========================================================
# ساخت data.js
# =========================================================

def generate_data_file():

    # کپی مستقل از اطلاعات پایه
    portfolio = BASE_PORTFOLIO.copy()


    # =====================================================
    # 1. Gallery
    # =====================================================

    gallery_files = get_files(GALLERY_PATH)

    portfolio["gallery"] = []

    for img in gallery_files:

        portfolio["gallery"].append({
            "src": f"{GALLERY_PATH}/{img}".replace("\\", "/"),
            "alt": "هویت بصری Alka"
        })


    # =====================================================
    # 2. Evidence
    # =====================================================

    evidence_files = get_files(EVIDENCE_PATH)

    portfolio["evidence"] = []

    for img in evidence_files:

        portfolio["evidence"].append({
            "src": f"{EVIDENCE_PATH}/{img}".replace("\\", "/"),
            "alt": "نتیجه Alka"
        })


    # =====================================================
    # 3. Stories
    # =====================================================

    story_groups = []


    if os.path.exists(STORIES_ROOT):

        # گرفتن تمام پوشه‌های استوری
        existing_folders = [
            folder
            for folder in os.listdir(STORIES_ROOT)
            if os.path.isdir(
                os.path.join(STORIES_ROOT, folder)
            )
        ]


        # ساخت lookup برای جلوگیری از مشکل حروف بزرگ و کوچک
        folder_lookup = {
            folder.lower(): folder
            for folder in existing_folders
        }


        # =================================================
        # اعمال ترتیب دلخواه
        # =================================================

        ordered_folders = []


        for folder_in_list in CUSTOM_FOLDER_ORDER:

            key = folder_in_list.lower()

            if key in folder_lookup:

                real_folder_name = folder_lookup[key]

                ordered_folders.append(
                    real_folder_name
                )


        # اگر پوشه جدیدی بعداً اضافه شد
        # آن را هم در انتهای لیست قرار بده

        for folder in existing_folders:

            if folder not in ordered_folders:

                ordered_folders.append(folder)


        # =================================================
        # ساخت گروه‌ها
        # =================================================

        for group_index, folder_name in enumerate(
            ordered_folders,
            start=1
        ):

            subfolder_path = os.path.join(
                STORIES_ROOT,
                folder_name
            )


            # گرفتن تصاویر
            images = get_files(subfolder_path)


            # اگر پوشه خالی بود
            if not images:
                continue


            # =================================================
            # عنوان گروه
            # =================================================

            title_file_path = os.path.join(
                subfolder_path,
                "title.txt"
            )

            raw_title = ""


            if os.path.exists(title_file_path):

                try:

                    with open(
                        title_file_path,
                        "r",
                        encoding="utf-8"
                    ) as title_file:

                        raw_title = title_file.read().strip()

                except Exception as error:

                    print(
                        f"خطا در خواندن title.txt در {folder_name}: {error}"
                    )


            # اگر title.txt وجود نداشت
            if not raw_title:

                raw_title = (
                    folder_name
                    .replace("-", " ")
                    .replace("_", " ")
                )


            group_title = (
                f"{group_index:02d}. {raw_title}"
            )


            # =================================================
            # ساخت آیتم‌های استوری
            # =================================================

            items = []


            for img_index, img in enumerate(
                images,
                start=1
            ):

                path = os.path.join(
                    subfolder_path,
                    img
                ).replace("\\", "/")


                items.append({
                    "src": path,
                    "alt": "استوری Alka",
                    "index": f"{img_index:02d}"
                })


            # =================================================
            # اضافه کردن گروه
            # =================================================

            story_groups.append({

                "groupTitle": group_title,

                "items": items

            })


    # قرار دادن گروه‌های استوری در portfolio
    portfolio["storyGroups"] = story_groups


    # =====================================================
    # ساخت JavaScript
    # =====================================================

    json_data = json.dumps(
        portfolio,
        ensure_ascii=False,
        indent=2
    )


    js_content = (
        "var portfolio = "
        + json_data
        + ";\n"
    )


    # =====================================================
    # نوشتن data.js
    # =====================================================

    with open(
        DATA_JS_PATH,
        "w",
        encoding="utf-8"
    ) as data_file:

        data_file.write(js_content)


    # =====================================================
    # گزارش
    # =====================================================

    print("========================================")
    print("✅ data.js با موفقیت ساخته شد")
    print("========================================")

    print(
        f"📸 تعداد تصاویر Gallery: "
        f"{len(portfolio['gallery'])}"
    )

    print(
        f"📊 تعداد Evidence: "
        f"{len(portfolio['evidence'])}"
    )

    print(
        f"📱 تعداد گروه‌های Story: "
        f"{len(portfolio['storyGroups'])}"
    )

    for group in portfolio["storyGroups"]:

        print(
            f"   • {group['groupTitle']} "
            f"→ {len(group['items'])} تصویر"
        )

    print("========================================")


# =========================================================
# اجرای برنامه
# =========================================================

if __name__ == "__main__":

    generate_data_file()
