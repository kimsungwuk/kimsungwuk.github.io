import os
import json
import datetime
import subprocess

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"

def get_journalistic_news():
    """
    [중요] 데이터 하드코딩 금지
    실시간 검색을 통해 최신 AI 뉴스를 가져오는 로직으로 전환합니다.
    자동화 에이전트는 이 함수를 직접 수정하거나 최신 정보를 주입해야 합니다.
    """
    # 에이전트 가이드: 
    # 1. web_search를 통해 오늘의 최신 AI 뉴스 5~7개를 수집하세요.
    # 2. 수집된 내용을 바탕으로 news_data 리스트를 실시간으로 업데이트하세요.
    # 3. [초정밀 SEO 모드]: 각 뉴스마다 'keywords' 리스트를 생성하여 주입하세요.
    #    예: "keywords": ["갤럭시 S26", "에이전틱 AI", "삼성 언팩"]
    news_data = []
    return news_data

def create_daily_news_posts():
    today = datetime.date.today().isoformat()
    category = "AI 최신뉴스"
    
    news_data_list = get_journalistic_news()
    
    if not news_data_list:
        print("⚠️ 업데이트할 새로운 뉴스 데이터가 없습니다. 실시간 검색을 먼저 수행하세요.")
        return False
    
    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        posts_data = json.load(f)

    newly_added = 0
    for item in news_data_list:
        title = item["title"]
        # SEO 키워드 추출 (데이터에 없을 경우 기본값 사용)
        keywords = item.get("keywords", [item["category"], "AI 뉴스", "수익 자동화"])
        
        # 중복 체크: 이미 존재하는 타이틀이면 삭제 후 다시 추가하여 내용 업데이트
        posts_data = [p for p in posts_data if not (p['title'] == title and p['date'] == today)]
        
        posts_data.insert(0, {
            'title': title,
            'date': today,
            'category': category,
            'summary': item["summary"],
            'image_url': item["image_url"],
            'content': item["content"],
            'keywords': keywords # SEO 키워드 저장
        })
        newly_added += 1
        
    if newly_added > 0:
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(posts_data, f, indent=4, ensure_ascii=False)
        
        # 블로그 빌드 (build_engine.py 실행)
        build_script = os.path.join(BASE_DIR, "build_engine.py")
        subprocess.run(["python3", build_script], check=True)
        
        print(f"💰 [성공] 총 {newly_added}개의 개별 뉴스 포스팅이 완료되었습니다.")
        return True
    
    return False

if __name__ == "__main__":
    create_daily_news_posts()
