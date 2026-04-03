import json
import os
import subprocess

BASE_DIR = "/Users/kimsungwuk/.openclaw/workspace"
POSTS_DATA_PATH = os.path.join(BASE_DIR, "config/posts_data.json")
POSTS_DIR = os.path.join(BASE_DIR, "posts")

def cleanup():
    if not os.path.exists(POSTS_DATA_PATH):
        print("No posts_data.json found.")
        return

    with open(POSTS_DATA_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)

    original_count = len(posts)
    # Filter out posts without image_url or with invalid image_url
    # We also check if it's a string and starts with http
    valid_posts = []
    removed_titles = []

    for post in posts:
        img_url = post.get("image_url")
        if img_url and isinstance(img_url, str) and img_url.startswith("http"):
            valid_posts.append(post)
        else:
            removed_titles.append(post.get("title", "Unknown Title"))

    if len(valid_posts) == original_count:
        print("No posts found missing images.")
        return

    print(f"Removing {len(removed_titles)} posts missing images.")
    for title in removed_titles:
        print(f" - {title}")

    # Save updated posts_data.json
    with open(POSTS_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(valid_posts, f, indent=4, ensure_ascii=False)

    # Rebuild site
    print("Rebuilding site...")
    subprocess.run(["python3", os.path.join(BASE_DIR, "build_engine.py")], check=True)
    
    print("Cleanup complete.")

if __name__ == "__main__":
    cleanup()
