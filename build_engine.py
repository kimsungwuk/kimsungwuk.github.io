import os
import json
import datetime
import re

# 설정 로드
BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
with open(os.path.join(BASE_DIR, "config/settings.json"), "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

def build_post(title, content, category="AI를 활용한 개발정보", summary="", image_url=""):
    today = datetime.date.today().isoformat()
    safe_title = re.sub(r'[^\w\s-]', '', title.replace('/', '-')).strip()
    post_id = safe_title.replace(' ', '-').lower()
    filename = f"{today}-{post_id}.html"
    
    # 이미지 태그
    image_tag = f'<img src="{image_url}" alt="{title}" style="width:100%; border-radius:18px; margin-bottom:40px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">' if image_url else ""
    
    # 템플릿 로드
    with open(os.path.join(BASE_DIR, "templates/post_layout.html"), "r", encoding="utf-8") as f:
        template = f.read()
    
    # 변수 치환 (엔진 핵심 로직)
    rendered = template.replace("{{title}}", title)\
                       .replace("{{blog_title}}", CONFIG["blog_title"])\
                       .replace("{{category}}", category)\
                       .replace("{{date}}", today)\
                       .replace("{{content}}", content.replace('\n', '<br>'))\
                       .replace("{{image_tag}}", image_tag)\
                       .replace("{{github_repo}}", CONFIG["github_repo"])\
                       .replace("{{post_id}}", post_id)\
                       .replace("{{v_style}}", CONFIG["visitor_counter"]["style"])\
                       .replace("{{v_color}}", CONFIG["visitor_counter"]["color"])\
                       .replace("{{g_repo}}", CONFIG["giscus"]["repo"])\
                       .replace("{{g_repo_id}}", CONFIG["giscus"]["repo_id"])\
                       .replace("{{g_category}}", CONFIG["giscus"]["category"])\
                       .replace("{{g_category_id}}", CONFIG["giscus"]["category_id"])\
                       .replace("{{g_mapping}}", CONFIG["giscus"]["mapping"])\
                       .replace("{{g_reactions}}", CONFIG["giscus"]["reactions_enabled"])\
                       .replace("{{g_theme}}", CONFIG["giscus"]["theme"])\
                       .replace("{{g_lang}}", CONFIG["giscus"]["lang"])

    # 파일 저장
    output_path = os.path.join(BASE_DIR, f"posts/{filename}")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)
    
    # index.html 데이터 업데이트 (이 로직은 추후 index 전용 템플릿 도입 시 개선 가능)
    update_index_json(title, today, category, summary or (content[:100] + "..."), filename, image_url)
    
    print(f"✅ [Engine] Post built successfully: {filename}")
    return filename

def update_index_json(title, date, category, summary, filename, image):
    index_path = os.path.join(BASE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    new_entry = f"""{{
            title: "{title}",
            date: "{date}",
            category: "{category}",
            summary: "{summary}",
            image: "{image}",
            url: "posts/{filename}"
        }},"""
    
    if new_entry not in html:
        updated_html = html.replace("const posts = [", f"const posts = [\n        {new_entry}")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(updated_html)

if __name__ == "__main__":
    # Test Build
    build_post(
        "아키텍처 개편 및 자동화 엔진 도입 보고",
        "블로그의 유지보수성을 높이기 위해 템플릿 기반의 정적 엔진을 도입했습니다. 이제 모든 설정은 단 한 곳에서 관리됩니다.",
        "AI를 활용한 개발정보"
    )
