import os
import json
import datetime
import re
import hashlib
import requests
from bs4 import BeautifulSoup

# 설정 로드
BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
with open(os.path.join(BASE_DIR, "config/settings.json"), "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

def get_link_metadata(url):
    try:
        print(f"🔍 링크 데이터 수집 중: {url}")
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title_meta = soup.find("meta", property="og:title")
        image_meta = soup.find("meta", property="og:image")
        
        title = title_meta["content"] if title_meta else "Google Play Store"
        image = image_meta["content"] if image_meta else ""
        
        if len(title) > 50:
            title = title[:47] + "..."
            
        return {"title": title, "image": image}
    except Exception as e:
        print(f"⚠️ 메타데이터 수집 실패: {e}")
        return {"title": "Google Play Store", "image": ""}

def format_content(text):
    # 0. Handle literal \n if they exist (common when injecting JSON)
    text = text.replace('\\n', '\n')

    # 1. Headers (###, ##, #) - ensure they don't capture across lines
    text = re.sub(r'^### (.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # 2. Bold (**text**) - non-greedy
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # 3. Lists (- item)
    text = re.sub(r'^- (.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    # Wrap adjacent <li> tags in <ul>
    text = re.sub(r'((?:<li>.*?</li>\n?)+)', r'<ul>\1</ul>', text, flags=re.DOTALL)

    # 4. URLs to clickable links (excluding images or existing tags)
    url_pattern = r'(?<!href=")(?<!src=")(https?://[^\s\n<]+)'
    text = re.sub(url_pattern, r'<a href="\1" target="_blank">\1</a>', text)

    # 5. 명령어 박스 변환 (Existing logic)
    cmd_pattern = r'(?:명령어|명령어 예시|상태 확인 명령어):\s*(.+)'
    def replace_with_code_box(match):
        code = match.group(1).strip().replace('\"', '')
        block_id = f"code-{hashlib.md5(code.encode()).hexdigest()[:6]}"
        return f"""
        <div class="code-container">
            <span class="code-text" id="{block_id}">{code}</span>
            <button class="copy-btn" onclick="copyToClipboard('{block_id}')" title="복사하기">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            </button>
        </div>
        """
    text = re.sub(cmd_pattern, replace_with_code_box, text)

    # 6. Newlines to <br> for non-HTML blocks
    lines = text.split('\n')
    formatted_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            formatted_lines.append('<br>')
        elif not re.match(r'<(h[1-3]|ul|li|div|p|a)', stripped):
            formatted_lines.append(line + '<br>')
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def build_post(title, content, category, summary, image_url, date=None, keywords=None):
    if not date:
        date = datetime.date.today().isoformat()
    
    post_hash = hashlib.md5(title.encode()).hexdigest()[:8]
    filename = f"post-{date}-{post_hash}.html"
    
    # [FIX] 엔진 레벨에서 이미지 누락 방지 및 기본 이미지 설정
    if not image_url:
        image_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1000"
        
    image_tag = f'<img src="{image_url}" alt="{title}" style="width:100%; border-radius:18px; margin-bottom:40px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">'
    
    visitor_badge = f'<img src="https://hits.dwyl.com/kimsungwuk/chloekim/{post_hash}.svg?style=flat-square&color=0066cc" style="margin-bottom:20px;">'

    # SEO Keywords 처리
    if not keywords:
        keywords = [category, "AI 뉴스", "수익 자동화", "kimsungwuk"]
    keywords_str = ", ".join(keywords)

    with open(os.path.join(BASE_DIR, "templates/post_layout.html"), "r", encoding="utf-8") as f:
        template = f.read()
    
    rendered = template.replace("{{title}}", title)\
                       .replace("{{blog_title}}", CONFIG["blog_title"])\
                       .replace("{{author}}", CONFIG["author"])\
                       .replace("{{base_url}}", CONFIG["base_url"])\
                       .replace("{{filename}}", filename)\
                       .replace("{{summary}}", summary or (content[:150] + "..."))\
                       .replace("{{og_image}}", image_url)\
                       .replace("{{category}}", category)\
                       .replace("{{date}}", date)\
                       .replace("{{content}}", format_content(content))\
                       .replace("{{image_tag}}", image_tag)\
                       .replace("{{visitor_badge}}", visitor_badge)\
                       .replace("{{github_repo}}", CONFIG["github_repo"])\
                       .replace("{{keywords}}", keywords_str)

    output_path = os.path.join(BASE_DIR, f"posts/{filename}")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)
    
    return {
        "title": title, "date": date, "category": category,
        "summary": summary or (content[:100] + "..."),
        "image": image_url, "url": f"posts/{filename}"
    }

def rebuild_all():
    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        posts_data = json.load(f)
    
    posts_dir = os.path.join(BASE_DIR, "posts")
    if os.path.exists(posts_dir):
        for f_name in os.listdir(posts_dir):
            if f_name.endswith(".html"):
                os.remove(os.path.join(posts_dir, f_name))
    else:
        os.makedirs(posts_dir)

    processed_posts = []
    for post in posts_data:
        p_info = build_post(
            post["title"], 
            post["content"], 
            post["category"], 
            post["summary"], 
            post.get("image_url", ""), 
            post.get("date"),
            post.get("keywords")
        )
        processed_posts.append(p_info)
    
    index_path = os.path.join(BASE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    start_marker = "const posts = ["
    end_marker = "];"
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker, start_idx)
    
    if start_idx != -1 and end_idx != -1:
        posts_js = "const posts = " + json.dumps(processed_posts, indent=8, ensure_ascii=False)
        new_html = html[:start_idx] + posts_js + html[end_idx + 1:]
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_html)

    # Generate SEO files
    generate_robots_txt()
    generate_sitemap(processed_posts)

    print("🚀 [Engine] QA Fix Build complete.")

def generate_robots_txt():
    content = f"User-agent: *\nAllow: /\nSitemap: {CONFIG['base_url']}/sitemap.xml\n"
    with open(os.path.join(BASE_DIR, "robots.txt"), "w") as f:
        f.write(content)

def generate_sitemap(posts):
    base_url = CONFIG['base_url']
    today = datetime.date.today().isoformat()
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{base_url}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>"""
    for post in posts:
        xml += f"\n  <url><loc>{base_url}/{post['url']}</loc><lastmod>{post['date']}</lastmod><priority>0.8</priority></url>"
    xml += "\n</urlset>"
    with open(os.path.join(BASE_DIR, "sitemap.xml"), "w") as f:
        f.write(xml)

if __name__ == "__main__":
    rebuild_all()
