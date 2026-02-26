import os
import json
import sys
import datetime
import subprocess

# Simple script to integrate a new post into the chloe-blog system
BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
DATA_PATH = os.path.join(BASE_DIR, "config/posts_data.json")

def add_post(title, content, category, summary, image_url):
    if not os.path.exists(DATA_PATH):
        print(f"Error: {DATA_PATH} not found.")
        return False

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        posts_data = json.load(f)

    # 중복 체크: 제목이 이미 존재하면 추가하지 않음
    if any(p['title'] == title for p in posts_data):
        print(f"Skip: '{title}' is already posted.")
        return False

    new_post = {
        "title": title,
        "date": datetime.date.today().isoformat(),
        "category": category,
        "summary": summary,
        "image_url": image_url,
        "content": content
    }

    # Add to the beginning
    posts_data.insert(0, new_post)

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(posts_data, f, indent=4, ensure_ascii=False)
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 add_youtube_post.py <title> <category> <summary> <image_url> <content_file>")
        sys.exit(1)
    
    title = sys.argv[1]
    category = sys.argv[2]
    summary = sys.argv[3]
    image_url = sys.argv[4]
    content_file = sys.argv[5]

    with open(content_file, "r", encoding="utf-8") as f:
        content = f.read()

    if add_post(title, content, category, summary, image_url):
        print(f"Post '{title}' added successfully.")
    else:
        print("Failed to add post.")
