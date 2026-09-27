import os
import json

DATA_JS_PATH = "data.js"
STORIES_ROOT = "images/uploads/stories"
GALLERY_PATH = "images/uploads/gallery"
EVIDENCE_PATH = "images/uploads/evidence"

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG", ".PNG", ".WEBP")

CUSTOM_FOLDER_ORDER = [
    "paraffin-story",  # ۱. پارافین
    "kash_story",      # ۲. کاش
    "Hadieh_story",    # ۳. هدیه
    "Event_story",     # ۴. ایونت
    "Kederi_story",    # ۵. کدری
    "Tarak_story",     # ۶. ترک
    "Dama_story",      # ۷. دما
]

# اطلاعات ثابت پورتفولیو
BASE_PORTFOLIO = {
    "name": "عطیه قیومی‌پور",
    "title": "مدیر دیجیتال مارکتینگ برند Alka",
    "slogan": "از هویت بصری تا رشد واقعی.",
    "heroText": "طراحی کردم، محتوا ساختم و با ترکیب استراتژی و ابزارهای AI، حضور دیجیتال Alka را توسعه دادم؛ نتیجه، افزایش ۱۳ برابری تعامل پیج بود.",
    "profileImage": "/images/profile.jpg",
    "about": "وقتی همکاری با Alka را شروع کردم، پیج هویت بصری منسجمی نداشت. از بازطراحی لوگو، کاور هایلایت و پالت رنگ شروع کردم، سبک تصویری محصولات را شکل دادم و بعد سراغ استراتژی محتوا، رشته‌استوری‌های تعاملی، دایرکت مارکتینگ و تحلیل Insights رفتم. هدف فقط تولید محتوا نبود؛ ساختن یک سیستم منسجم برای دیده‌شدن، تعامل و فروش بود.",
    "services": [
        {"title": "هویت بصری", "description": "بازطراحی هویت بصری پیج از لوگو و کاور هایلایت تا پالت رنگ و ایجاد یک زبان بصری یکپارچه و قابل تشخیص."},
        {"title": "استراتژی محتوا", "description": "ترکیب محتوای فروش، آموزشی، تعاملی و پشت‌صحنه برای اینکه پیج فقط تبلیغاتی نباشد و تعامل واقعی ایجاد کند."},
        {"title": "تولید محتوای بصری", "description": "طراحی پست، کاروسل و استوری و ساخت سبک تصویری محصولات؛ با استفاده هدفمند از AI در جاهایی که عکاسی حرفه‌ای محدود بود."},
        {"title": "مدیریت و رشد پیج", "description": "مدیریت روزانه محتوا، بررسی Insights و رفتار مخاطب و اصلاح زمان انتشار و فرمت محتوا بر اساس داده."}
    ],
    "case": {
        "title": "یک پروژه، از بازطراحی هویت تا ساختن سیستم رشد",
        "lead": "سه ماه همکاری مستمر با Alka، از مدیریت روزانه پیج تا طراحی هویت بصری، استراتژی محتوا، سناریونویسی، دایرکت مارکتینگ و تحلیل داده."
    },
    "stats": [
        {"value": "35,902 → 312,427", "label": "بازدید محتوا", "note": "حدود ۸.۷ برابر"},
        {"value": "2,191 → 29,365", "label": "تعامل", "note": "۱۳ برابر"},
        {"value": "+900", "label": "فالوور جدید", "note": "رشد خالص پروژه"},
        {"value": "3,636", "label": "ریپلای استوری", "note": "تعامل مستقیم مخاطب"}
    ],
    "process": [
        {"title": "۱. شروع با یکپارچه‌سازی برند", "text": "لوگو، کاور هایلایت‌ها، پالت رنگ و سبک تصویری از پایه بازطراحی شدند تا پیج قبل از هر چیز یک هویت مشخص داشته باشد."},
        {"title": "۲. ساختن سیستم محتوا", "text": "تقویم محتوا طوری چیده شد که معرفی محصول و آفر در کنار محتوای آموزشی، تعاملی و پشت‌صحنه قرار بگیرد."},
        {"title": "۳. طراحی تعامل، نه فقط انتشار", "text": "رشته‌استوری‌های چندقسمتی با CTA و سناریو طراحی شد تا مخاطب را به ادامه‌دادن، ریپلای و ورود به دایرکت تشویق کند."},
        {"title": "۴. تصمیم‌گیری با داده", "text": "Insights و رفتار مخاطب مرتب بررسی شد تا زمان انتشار، فرمت محتوا و نوع موضوعات بر اساس عملکرد واقعی اصلاح شوند."}
    ]
}

def get_files(folder):
    if not os.path.exists(folder):
        return []
    return sorted([f for f in os.listdir(folder) if f.endswith(VALID_EXTENSIONS)])

def generate_data_file():
    portfolio = BASE_PORTFOLIO.copy()

    # ۱. اسکن گالری
    gallery_files = get_files(GALLERY_PATH)
    portfolio["gallery"] = [
        {"src": f"{GALLERY_PATH}/{img}".replace("\\", "/"), "alt": "هویت بصری Alka"}
        for img in gallery_files
    ]

    # ۲. اسکن مدارک (Evidence)
    evidence_files = get_files(EVIDENCE_PATH)
    portfolio["evidence"] = [
        {"src": f"{EVIDENCE_PATH}/{img}".replace("\\", "/"), "alt": "نتیجه Alka"}
        for img in evidence_files
    ]

    # ۳. اسکن استوری‌ها
    story_groups = []
    if os.path.exists(STORIES_ROOT):
        existing_folders = [d for d in os.listdir(STORIES_ROOT) if os.path.isdir(os.path.join(STORIES_ROOT, d))]
        folder_lookup = {f.lower(): f for f in existing_folders}
        
        ordered_folders = []
        for folder_in_list in CUSTOM_FOLDER_ORDER:
            key = folder_in_list.lower()
            if key in folder_lookup:
                ordered_folders.append(folder_lookup[key])
        
        for f in existing_folders:
            if f not in ordered_folders:
                ordered_folders.append(f)

        for group_index, folder_name in enumerate(ordered_folders, start=1):
            subfolder_path = os.path.join(STORIES_ROOT, folder_name)
            images = get_files(subfolder_path)
            
            if not images:
                continue

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

            group_title = f"{group_index:02d}. {raw_title}"

            items = []
            for img_index, img in enumerate(images, start=1):
                path = os.path.join(subfolder_path, img).replace("\\", "/")
                items.append({
                    "src": path,
                    "alt": "استوری Alka",
                    "index": f"{img_index:02d}"
                })

            story_groups.append({
                "groupTitle": group_title,
                "items": items
            })

    portfolio["storyGroups"] = story_groups

    # ۴. خروجی اسکریپت سراسری (بدون export) برای تطابق با <script src="data.js"></script>
    js_content = f"var portfolio = {json.dumps(portfolio, ensure_ascii=False, indent=2)};\n"

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)

    print("✅ فایل data.js با موفقیت ساخته شد و با فراخوانی عادی HTML سازگار است!")

if __name__ == "__main__":
    generate_data_file()
