import json
import os

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

money_tips = [
    {
        "title": "애드센스 승인 확률을 높이는 고퀄리티 포스팅의 3가지 핵심 요소",
        "date": "2026-02-24",
        "category": "수익화 팁",
        "summary": "구글 애드센스 승인을 한 번에 받기 위해 반드시 지켜야 할 전문성, 가독성, 그리고 고유 이미지 사용 전략을 공개합니다.",
        "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1000",
        "content": """블로그 수익화의 첫 번째 관문은 단연 애드센스 승인입니다. 많은 분들이 양질의 글을 쓰고도 승인 거절을 당하곤 하는데, 구글의 검토 기준을 명확히 이해하면 해결책이 보입니다.

첫째, 전문성(Authority)입니다. 단순히 뉴스를 전달하는 것이 아니라 해당 주제에 대한 본인의 분석이나 의견이 최소 30% 이상 포함되어야 합니다. '나만의 언어'로 재해석된 글은 구글 알고리즘이 가장 선호하는 형태입니다.

둘째, 가독성(Readability)입니다. 소제목을 활용하여 글의 구조를 나누고, 문장은 짧고 명확하게 유지해야 합니다. 방문자가 페이지에 머무는 시간(체류 시간)은 승인의 중요한 척도가 됩니다.

셋째, 고유한 시각 자료입니다. 저작권에 문제가 없는 고화질 이미지를 사용하되, 가능하다면 직접 캡처하거나 편집한 이미지를 활용하는 것이 좋습니다. 중복 이미지 사용은 콘텐츠의 가치를 떨어뜨리는 핵심 요인입니다."""
    },
    {
        "title": "AI 에이전트를 활용한 1인 블로그 자동화 수익 구조 설계법",
        "date": "2026-02-24",
        "category": "수익화 팁",
        "summary": "OpenClaw와 같은 AI 도구를 활용하여 콘텐츠 기획부터 배포까지 자동화함으로써 지속 가능한 수익을 창출하는 시스템 구축 가이드를 소개합니다.",
        "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=1000",
        "content": """1인 창업가에게 가장 소중한 자산은 시간입니다. AI 기술의 발전으로 이제는 콘텐츠 생성의 상당 부분을 자동화할 수 있게 되었습니다.

먼저, 데이터 수집의 자동화입니다. API를 활용해 매일 아침 특정 분야의 최신 소식을 수집하고 이를 분석하도록 AI를 설정할 수 있습니다. 이는 정보의 시의성을 확보하는 동시에 물리적 시간을 절약해 줍니다.

다음은 콘텐츠 최적화입니다. AI는 검색 엔진 최적화(SEO)에 유리한 키워드를 배치하고 메타 태그를 생성하는 데 탁월한 성능을 발휘합니다. 인간은 AI가 생성한 초안을 검토하고 전략적인 방향을 설정하는 '편집자'의 역할에 집중해야 합니다.

마지막으로 배포의 자동화입니다. 깃허브 액션(GitHub Actions)이나 크론(Cron) 작업을 통해 정해진 시간에 자동으로 포스팅이 업로드되도록 시스템을 구축하면, 잠자는 동안에도 수익이 발생하는 파이프라인이 완성됩니다."""
    },
    {
        "title": "디지털 노마드를 위한 앱 서비스 수익화 전략: 광고 vs 구독",
        "date": "2026-02-24",
        "category": "수익화 팁",
        "summary": "Block King과 같은 인디 앱 개발자가 선택할 수 있는 다양한 수익 모델의 장단점을 분석하고 최적의 조합을 제안합니다.",
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1000",
        "content": """앱을 만드는 것만큼 중요한 것이 어떻게 수익을 낼 것인가에 대한 고민입니다. 크게 광고 모델과 구독 모델로 나눌 수 있습니다.

광고 모델(AdMob 등)은 진입 장벽이 낮고 사용자에게 무료 경험을 제공할 수 있다는 장점이 있습니다. 캐주얼 게임이나 유틸리티 앱에 적합하며, 트래픽이 많을수록 수익이 극대화됩니다.

구독 모델(In-App Purchase)은 안정적이고 예측 가능한 수익을 제공합니다. 사용자가 지속적으로 가치를 느낄 수 있는 기능이 포함된 생산성 도구 등에 적합합니다.

가장 추천하는 방식은 하이브리드 전략입니다. 기본 기능은 광고와 함께 무료로 제공하고, 고급 기능이나 광고 제거 옵션을 유료 결제로 제공함으로써 사용자의 선택권을 넓히고 수익원을 다각화하는 것이 인디 개발자에게 가장 유리한 전략입니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

# 새로운 팁들을 맨 앞에 추가
for tip in reversed(money_tips):
    if not any(p['title'] == tip['title'] for p in posts_data):
        posts_data.insert(0, tip)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

print(f"Successfully added {len(money_tips)} money tips.")
