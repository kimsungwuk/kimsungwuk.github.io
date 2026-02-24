import json
import os

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

money_tips_v2 = [
    {
        "title": "애드센스 첫 수익 정산을 위한 광고 배치 및 최적화 실전 전략",
        "date": "2026-02-24",
        "category": "수익화 팁",
        "summary": "승인 이후 실제 수익으로 연결되는 상단 광고, 자동 광고, 그리고 클릭률(CTR)을 높이는 전략적 위치 선정 방법을 알아봅니다.",
        "image_url": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&q=80&w=1000",
        "content": """애드센스 승인은 시작일 뿐입니다. 실제 수익을 내기 위해서는 전략적인 광고 배치가 필수적입니다.

첫째, 데스크톱과 모바일의 레이아웃 차이를 이해해야 합니다. 모바일 방문자가 많은 블로그라면 '페이지 상단 고정 광고'와 '본문 중간 삽입 광고'의 비중을 높이는 것이 클릭률 확보에 유리합니다.

둘째, 구글의 '자동 광고' 기능을 적극 활용하되 제어해야 합니다. 모든 곳에 광고가 뜨면 사용자 경험이 해쳐져 오히려 체류 시간이 줄어듭니다. 본문 상단과 하단 등 핵심 위치는 수동으로 배치하고, 나머지는 AI가 판단하게 두는 하이브리드 방식이 가장 효율적입니다.

셋째, 고단가 키워드 분석입니다. 금융, IT, 부동산 등 클릭당 단가(CPC)가 높은 주제의 글을 정기적으로 작성하여 전체적인 수익률을 끌어올려야 합니다."""
    },
    {
        "title": "구글 검색 결과 1페이지를 점령하는 검색 엔진 최적화(SEO) 체크리스트",
        "date": "2026-02-24",
        "category": "수익화 팁",
        "summary": "내 글이 검색 결과 상단에 노출되지 않는다면? 검색 로봇이 좋아하는 글쓰기 구조와 메타 태그 최적화 비법을 공개합니다.",
        "image_url": "https://images.unsplash.com/photo-1432888622747-4eb9a8f2c1d8?auto=format&fit=crop&q=80&w=1000",
        "content": """좋은 글을 써도 읽히지 않는다면 수익은 발생하지 않습니다. 검색 엔진의 선택을 받기 위한 3가지 체크리스트를 확인하세요.

1. 키워드 중심의 제목 설계: 사람들이 검색창에 칠 법한 핵심 키워드를 제목의 앞부분에 배치하세요. 예를 들어 '수익 내는 법'보다는 '구글 애드센스 수익 2배 높이는 배치 전략'이 훨씬 효과적입니다.

2. 이미지 Alt 태그와 용량 최적화: 검색 로봇은 이미지를 직접 보지 못합니다. 이미지에 설명을 달아주고(Alt text), 페이지 로딩 속도를 높이기 위해 이미지 용량을 압축하는 작업이 필요합니다.

3. 내부 및 외부 링크 활용: 내 블로그의 다른 글을 연결하거나 신뢰도 높은 외부 사이트를 링크하면, 검색 엔진은 이 글이 정보 가치가 높은 네트워크의 일부라고 판단합니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for tip in reversed(money_tips_v2):
    if not any(p['title'] == tip['title'] for p in posts_data):
        posts_data.insert(0, tip)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

print(f"Successfully added {len(money_tips_v2)} more money tips.")
