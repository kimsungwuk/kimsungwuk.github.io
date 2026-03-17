import json
import os
import datetime
import sys
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

def add_post(title, content, category, summary, image_url, date=None):
    if not os.path.exists(data_path):
        posts_data = []
    else:
        with open(data_path, "r", encoding="utf-8") as f:
            posts_data = json.load(f)

    new_post = {
        "title": title,
        "date": date or datetime.date.today().isoformat(),
        "category": category,
        "summary": summary,
        "image_url": image_url,
        "content": content
    }

    # 중복 체크
    if any(p['title'] == title for p in posts_data):
        print(f"Post with title '{title}' already exists.")
        return

    posts_data.insert(0, new_post)

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(posts_data, f, indent=4, ensure_ascii=False)

    rebuild_all()
    print(f"Successfully added post: {title}")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python add_post.py <title> <content> <category> <summary> <image_url> [date]")
    else:
        title = sys.argv[1]
        content = sys.argv[2]
        category = sys.argv[3]
        summary = sys.argv[4]
        image_url = sys.argv[5]
        date = sys.argv[6] if len(sys.argv) > 6 else None
        add_post(title, content, category, summary, image_url, date)
