import os
import json
import datetime
import subprocess
import requests
import sys

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"

def is_image_valid(url):
    if not url or not url.startswith('http'):
        return False
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400
    except Exception:
        try:
            response = requests.get(url, timeout=5, stream=True)
            return response.status_code < 400
        except Exception:
            return False

def create_posts(news_data_list):
    today = datetime.date.today().isoformat()
    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            posts_data = json.load(f)
    else:
        posts_data = []

    newly_added = 0
    for item in news_data_list:
        # Image validation
        if not is_image_valid(item.get("image_url")):
            print(f"⚠️ Skipping post: {item['title']} - Invalid image URL: {item.get('image_url')}")
            continue

        title = item["title"]
        keywords = item.get("keywords", ["AI 뉴스", "수익 자동화", "SearXNG"])
        
        # Remove existing if same title and date (update)
        posts_data = [p for p in posts_data if not (p['title'] == title and p['date'] == today)]
        
        posts_data.insert(0, {
            'title': title,
            'date': today,
            'category': item.get("category", "AI 최신뉴스"),
            'summary': item["summary"],
            'image_url': item["image_url"],
            'content': item["content"],
            'keywords': keywords
        })
        newly_added += 1
        
    if newly_added > 0:
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(posts_data, f, indent=4, ensure_ascii=False)
        
        # Build
        subprocess.run(["python3", os.path.join(BASE_DIR, "build_engine.py")], check=True)
        
        # Push
        try:
            subprocess.run(["git", "-C", BASE_DIR, "add", "."], check=True)
            subprocess.run(["git", "-C", BASE_DIR, "commit", "-m", f"Daily AI News Update {today}"], check=True)
            subprocess.run(["git", "-C", BASE_DIR, "push"], check=True)
            print(f"✅ Successfully deployed {newly_added} posts.")
        except Exception as e:
            print(f"❌ Git error: {e}")
        return True
    else:
        print("❌ No valid posts to add.")
    return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = json.load(f)
        create_posts(data)
    else:
        print("Usage: python3 daily_ai_news.py <json_data_file>")
        sys.exit(1)
