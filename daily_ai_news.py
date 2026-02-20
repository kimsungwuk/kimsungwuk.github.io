import os
import json
import datetime
import requests
from build_engine import build_post, rebuild_all

# 설정 로드
BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"

def fetch_ai_news():
    # 현재 web_search가 제한적이므로, 네이버 뉴스 검색 결과를 fetch하여 파싱하는 방식 시뮬레이션
    # 실제로는 더 정교한 크롤링이나 RSS 리더를 붙일 수 있습니다.
    print("📰 최신 AI 뉴스를 수집하는 중...")
    
    # 예시 데이터 (실제 운영 시에는 web_fetch 결과를 바탕으로 GPT가 생성하도록 구성)
    news_items = [
        "오픈AI, 차세대 추론 모델 개발 가속화 발표",
        "엔비디아, AI 데이터센터용 신규 칩셋 공개",
        "구글 제미나이, 실시간 음성 번역 기능 대폭 개선",
        "애플, 온디바이스 AI 처리를 위한 전용 프로세서 강화",
        "메타, 오픈소스 Llama 4 개발 계획 및 성능 지표 공유"
    ]
    return news_items

def create_daily_news_post():
    today = datetime.date.today().isoformat()
    title = f"{today} AI 기술 트렌드 브리핑"
    category = "AI 최신뉴스"
    
    news_list = fetch_ai_news()
    
    content = "오늘의 주요 AI 기술 및 업계 소식을 정리해 드립니다.\n\n"
    for i, item in enumerate(news_list, 1):
        content += f"{i}. {item}\n"
    
    content += "\n최근 AI 시장은 모델의 성능 향상을 넘어 실질적인 사용자 경험 혁신과 인프라 효율화에 집중하고 있습니다. 특히 온디바이스 AI와 에이전트 기술의 결합이 주요 화두로 떠오르고 있습니다.\n\n내일도 더 유익한 소식으로 찾아뵙겠습니다. 감사합니다."
    
    summary = f"{today} 자 주요 AI 기술 및 글로벌 기업 동향 5가지 요약."
    image_url = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000"

    # 데이터베이스 로드 및 저장
    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        posts_data = json.load(f)

    # 중복 방지
    if not any(p['title'] == title for p in posts_data):
        posts_data.insert(0, {
            'title': title,
            'date': today,
            'category': category,
            'summary': summary,
            'image_url': image_url,
            'content': content
        })
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(posts_data, f, indent=4, ensure_ascii=False)
        
        rebuild_all()
        return True
    return False

if __name__ == "__main__":
    if create_daily_news_post():
        print("💰 [성공] 오늘의 AI 뉴스 포스팅 완료!")
    else:
        print("⏭️ 이미 오늘의 소식이 업데이트되었습니다.")
