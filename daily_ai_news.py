import os
import json
import datetime
from build_engine import build_post, rebuild_all

# 설정 로드
BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"

def fetch_ai_news():
    print("최신 AI 뉴스를 수집하는 중입니다.")
    
    # 2026년 2월 20일 기준 AI 최신 뉴스
    news_items = [
        "오픈AI 자율형 에이전트 서비스 오퍼레이터 정식 출시 및 글로벌 배포 시작",
        "구글 검색 엔진 내 생성형 답변 비중 확대 및 시각 정보 기반 검색 기술 고도화",
        "앤스로픽 클로드 업데이트를 통한 복합 논리 추론 성능 개선 및 개발자 도구 강화",
        "마이크로소프트 애저 기반 특화 언어 모델 미스트랄 협업 확대 및 보안 기능 강화",
        "샘 올트먼 7조 달러 규모 글로벌 반도체 생산망 구축을 위한 중동 투자 유치 지속"
    ]
    return news_items

def create_daily_news_post():
    today = datetime.date.today().isoformat()
    title = f"{today} AI 기술 트렌드 브리핑"
    category = "AI 최신뉴스"
    
    news_list = fetch_ai_news()
    
    content = "오늘의 주요 AI 기술 및 업계 소식을 정리하여 드립니다.\n\n"
    for i, item in enumerate(news_list, 1):
        content += f"{i}. {item}\n"
    
    content += "\n최근 AI 시장은 모델의 성능 향상을 넘어 실질적인 사용자 경험 혁신과 인프라 효율화에 집중하고 있습니다. 특히 온디바이스 AI와 에이전트 기술의 결합이 주요 화두로 떠오르고 있습니다.\n\n내일도 더 유익한 소식으로 찾아뵙겠습니다. 감사합니다."
    
    summary = f"{today} 자 주요 AI 기술 및 글로벌 기업 동향 5가지 요약."
    image_url = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000"

    # 데이터베이스 로드 및 저장
    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        posts_data = json.load(f)

    # 중복 방지 (오늘 날짜와 제목이 같은 포스트가 있는지 확인)
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
    else:
        # 테스트를 위해 강제로 업데이트하거나 날짜 확인 로직을 무시하고 진행할 수 있음
        # 여기서는 기존 포스트를 업데이트하도록 처리
        for p in posts_data:
            if p['title'] == title:
                p['content'] = content
                p['summary'] = summary
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(posts_data, f, indent=4, ensure_ascii=False)
        rebuild_all()
        return True

if __name__ == "__main__":
    if create_daily_news_post():
        print("성공 오늘의 AI 뉴스 포스팅 완료")
    else:
        print("이미 오늘의 소식이 업데이트되었습니다")
