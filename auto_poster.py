import os
import datetime

def create_post(title, content):
    base_dir = "/Users/kimsungwuk/StudioProjects/chloe-blog"
    posts_dir = os.path.join(base_dir, "posts")
    
    # 1. 파일 이름 생성
    today = datetime.date.today().isoformat()
    filename = f"{today}-{title.replace(' ', '-').lower()}.html"
    filepath = os.path.join(posts_dir, filename)
    
    # 2. HTML 템플릿 작성 (특수문자/이모티콘 제외)
    html_template = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} - Chloe Dev Log</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.8; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f4f7f6; }}
        .content {{ background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        h1 {{ color: #1a237e; border-bottom: 2px solid #e8eaf6; padding-bottom: 10px; }}
        .date {{ color: #888; font-size: 0.9rem; }}
        .back-link {{ display: inline-block; margin-top: 30px; text-decoration: none; color: #3f51b5; font-weight: bold; }}
        .adsense-placeholder {{ background: #eee; border: 2px dashed #ccc; padding: 20px; text-align: center; color: #999; margin: 20px 0; border-radius: 10px; }}
    </style>
</head>
<body>
<div class="content">
    <h1>{title}</h1>
    <p class="date">작성일: {today}</p>
    <div class="adsense-placeholder">Google AdSense AD</div>
    <div class="post-body">
        {content.replace('\n', '<br>')}
    </div>
    <div class="adsense-placeholder">Google AdSense AD</div>
    <a href="../index.html" class="back-link">&larr; 목록으로 돌아가기</a>
</div>
</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"💰 [성공] 새 포스팅 생성 완료: {filename}")
    return filename

if __name__ == "__main__":
    # 나중에 내가 이 함수를 호출해서 글을 쓸 거야!
    pass
