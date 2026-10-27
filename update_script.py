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

    "about": "وقتی همکاری با آلکا را شروع کردم، پیج هویت بصری منسجمی نداشت در همکاری با آلکا، تمرکز من فقط بر تولید محتوا نبود؛سبک تصویری محصولات را شکل دادم و هدفم ایجاد یک مسیر منسجم میان هویت بصری برند، استراتژی محتوا، تعامل با مخاطب از طریق استوری و دایرکت مارکتینگ و تحلیل عملکرد و فروش بود.",


    # =====================================================
    # خدمات
    # =====================================================

    "services": [
        {
            "title": "استراتژی و برنامه ریزی محتوا",
            "description": "تدوین مسیر محتوایی، تقویم انتشار و ایده پردازی متناسب با هدف برند و شناخت مخاطب."
        },
        {
            "title": "مهندسی پرامپت و طراحی خلاقانه راهکارهای مبتنی بر هوش مصنوعی",
            "description": "ترکیب تفکر ساختاری، خلاقیت، شناخت مخاطب و هدف‌گذاری برای طراحی پرامپت‌های دقیق و هدفمند؛ به‌کارگیری این مهارت در ایده‌پردازی، سناریونویسی،کپی رایتینگ و تولید محتوای متنی و بصری و حل مسائل محتوایی، با هدف دستیابی به خروجی‌های مرتبط‌تر، باکیفیت‌تر و کارآمدتر."
        },
        {
            "title": "طراحی هویت بصری و محتوای برند",
            "description": "طراحی عناصر بصری هماهنگ با شخصیت برند برای ایجاد حضوری منسجم و حرفه ای در شبکه های اجتماعی."
        },
        {
            "title": "مدیریت و بهینه سازی شبکه های اجتماعی",
            "description": "مدیریت انتشار محتوا، تحلیل عملکرد، بهینه سازی تعامل و کمک به رشد هدفمند صفحه."
        }
        ,{
            "title": "هوشمندسازی تعامل با مخاطب",
            "description": "طراحی سناریوهای تعاملی و پیاده سازی راهکارهای اتوماسیون دایرکت و پاسخ گویی با ابزارهای مرتبط."
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
            "value": "35,902 ← 312,427",
            "label": "بازدید محتوا",
            "note": "حدود ۸.۷ برابر"
        },
        {
            "value": "2,191 ← 29,365",
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
            "title": "1. شکل‌دهی به هویت یکپارچه‌ی برند",
            "text": "بازطراحی هویت بصری با تمرکز بر لوگو، پالت رنگی، کاورها و سبک تصاویر محصولات، برای ایجاد ظاهری هماهنگ و قابل‌شناسایی در صفحه."
        },
        {
            "title": "2. طراحی مسیر محتوایی هدفمند",
            "text": "تدوین ایده‌ها و سناریوهای محتوا با توجه به ماهیت محصولات و اهداف صفحه؛ تقویم محتوایی طوری نوشته شد که  تصاویر معرفی محصول تولید شده با هوش مصنوعی و محتوای فروش تا روایت‌های تعاملی و پشت صحنه در کنار هم قرار بگیرند "
        },
        {
            "title": "3. تبدیل محتوا به فرصتی برای تعامل",
            "text": "طراحی رشته‌های استوری، پرسش‌ها و دعوت به اقدام (CTA) با هدف تقویت مشارکت مخاطبان؛ در کنار استفاده از اتوماسیون دایرکت برای پاسخ‌گویی هدفمندتر."
        },
        {
            "title": "4. تحلیل عملکرد و بهینه‌سازی",
            "text": "بررسی داده‌های Insights و واکنش مخاطبان برای ارزیابی عملکرد محتوا و اصلاح زمان انتشار، قالب‌ها و موضوعات بر اساس نتایج به‌دست‌آمده."
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

    gallery_groups = []

    if os.path.exists(GALLERY_PATH):

        gallery_folders = [
            folder
            for folder in os.listdir(GALLERY_PATH)
            if os.path.isdir(
                os.path.join(GALLERY_PATH, folder)
            )
        ]
        gallery_folders.sort()

        for folder_name in gallery_folders:

            folder_path = os.path.join(
                GALLERY_PATH,
                folder_name
            )
            images = get_files(folder_path)

            if not images:
                continue

            items = []

            for img in images:
                path = os.path.join(
                    folder_path,
                    img
                ).replace("\\", "/")

                items.append({
                    "src": path,
                    "alt": "هویت بصری Alka"
                })

            gallery_groups.append({
                "items": items
            })

    portfolio["gallery"] = gallery_groups

    # =====================================================
    # 2. Evidence
    # =====================================================

    evidence_groups = []

    if os.path.exists(EVIDENCE_PATH):

        # گرفتن تمام پوشه‌های Evidence
        existing_folders = [
            folder
            for folder in os.listdir(EVIDENCE_PATH)
            if os.path.isdir(
                os.path.join(EVIDENCE_PATH, folder)
            )
        ]

        # ترتیب پوشه‌ها بر اساس نام
        existing_folders.sort()

        for folder_name in existing_folders:

            folder_path = os.path.join(
                EVIDENCE_PATH,
                folder_name
            )

            # گرفتن تصاویر داخل این گروه
            images = get_files(folder_path)

            if not images:
                continue
            # =================================================
            # خواندن title.txt
            # =================================================

            title_file_path = os.path.join(
                folder_path,
                "title.txt"
            )

            titles = []

            if os.path.exists(title_file_path):

                try:

                    with open(
                        title_file_path,
                        "r",
                        encoding="utf-8"
                    ) as title_file:

                        content = title_file.read().strip()

                        titles = [
                            title.strip()
                            for title in content.split("\n---\n")
                            if title.strip()
                        ]

                except Exception as error:

                    print(
                        f"خطا در خواندن title.txt در {folder_name}: {error}"
                    )

            # =================================================
            # ساخت آیتم‌های Evidence
            # =================================================
            items = []

            for img_index, img in enumerate(images):

                path = os.path.join(
                    folder_path,
                    img
                ).replace("\\", "/")

                title = ""

                if img_index < len(titles):
                    title = titles[img_index]

                items.append({
                    "src": path,
                    "alt": "نتیجه Alka",
                    "title": title
                })

            # =================================================
            # اضافه کردن گروه
            # =================================================

            evidence_groups.append({
                "items": items
            })

    portfolio["evidence"] = evidence_groups


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
