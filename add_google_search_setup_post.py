import json
import os
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

google_search_setup_post = [
    {
        "title": "구글 커스텀 검색 API 완벽 설정 가이드: 5분 만에 끝내는 API Key 발급과 비용 관리 비결",
        "date": "2026-02-25",
        "category": "수익화 팁",
        "summary": "구글 검색 데이터로 비즈니스 자동화를 시작하고 싶으신가요? 초보자도 바로 따라 할 수 있는 구글 커스텀 검색 API(Custom Search JSON API)의 단계별 설정법과 무료 할당량 활용법을 상세히 분석합니다.",
        "image_url": "https://images.unsplash.com/photo-1543286386-713bdd548da4?auto=format&fit=crop&q=80&w=1000",
        "content": """비즈니스 자동화나 데이터 스크래핑을 위해 구글의 방대한 검색 데이터를 활용하고 싶지만, 어디서부터 시작해야 할지 막막하신가요? 구글 커스텀 검색 API(Custom Search JSON API)는 개발자와 마케터들이 구글 검색 결과를 자신의 프로그램이나 서비스에 직접 연동할 수 있게 해주는 아주 강력한 도구입니다. 이번 포스팅에서는 최근 해외 마케팅 전문가들이 추천하는 설정 프로세스를 바탕으로, 5분 만에 API Key를 발급받고 비용을 효율적으로 관리하는 비법을 2배 더 풍성한 분량으로 상세히 파헤쳐 보겠습니다.

1. 구글 클라우드 콘솔에서의 첫 걸음: 프로젝트 생성
가장 먼저 방문해야 할 곳은 구글 클라우드 콘솔(console.cloud.google.com)입니다. 이곳은 구글의 수많은 API 서비스를 관리하는 중앙 통제실과 같습니다.
메인 화면 상단의 프로젝트 선택창에서 [새 프로젝트(New Project)]를 클릭하세요. 프로젝트 이름은 'Search-Automation'이나 'My-Citation-Scraper'와 같이 용도를 명확히 알 수 있는 이름으로 지어주는 것이 좋습니다. [만들기] 버튼을 누르면 구글 시스템 내부에서 여러분을 위한 독립된 작업 공간이 순식간에 구축됩니다. 프로젝트 생성은 모든 API 연동의 기초가 되는 아주 중요한 단계입니다.

2. Custom Search API 활성화 및 라이브러리 활용
프로젝트가 생성되었다면, 이제 우리가 사용할 구글의 '검색 능력'을 이 프로젝트에 부여해야 합니다.
왼쪽 메뉴에서 [API 및 서비스] > [라이브러리(Library)]로 이동하세요. 검색창에 'Custom Search API'를 입력하면 돋보기 아이콘과 함께 해당 API가 나타납니다. 이를 클릭한 뒤 파란색 [사용(Enable)] 버튼을 누르세요. 이 과정을 거치지 않으면 아무리 올바른 API 키를 사용하더라도 시스템에서 접근을 거부하게 됩니다. API를 활성화한다는 것은 구글에게 "내가 이 프로젝트에서 검색 기능을 사용하겠다"고 공식적으로 선언하는 것과 같습니다.

3. API Key 발급과 보안 관리 전략
API를 활성화하면 자동으로 관리 화면으로 이동하게 됩니다. 이제 실제로 우리의 손발이 되어줄 '열쇠'인 API Key를 만들어야 합니다.
화면 상단의 [사용자 인증 정보 만들기(Create Credentials)] 버튼을 누르고 첫 번째 항목인 [API 키(API Key)]를 선택하세요. 그러면 즉시 'AIza...'로 시작하는 긴 문자열의 키가 발급됩니다. 이 키는 절대 외부에 노출되어서는 안 되는 매우 민감한 정보입니다. 마케팅 자동화 툴이나 엑셀 시트에 이 키를 입력하면, 그때부터 여러분의 프로그램은 전 세계 구글 웹 데이터를 자유자재로 긁어올 수 있는 능력을 갖게 됩니다. 작업이 끝나면 반드시 '키 제한' 설정을 통해 특정 API(Custom Search API)만 호출할 수 있도록 보안을 강화하는 것이 필수입니다.

4. 비용 걱정 없는 무료 할당량 및 크레딧 활용법
많은 분들이 구글 API 사용 시 발생하는 비용을 걱정합니다. 하지만 구글은 신규 가입자에게 약 $300의 무료 크레딧을 제공하며, 매달 $200 상당의 할당량을 기본으로 지원합니다.
일반적인 마케팅 자동화나 소규모 데이터 수집 작업의 경우, 한 달 내내 툴을 돌려도 실제 청구되는 금액은 $2 내외이거나 무료 할당량 범위 내에서 해결되는 경우가 대다수입니다. "딸깍" 한 번으로 수천 개의 데이터를 정리해주는 생산성 향상 가치에 비하면 거의 무료에 가까운 수준입니다. 비용 관리가 걱정된다면 구글 클라우드 콘솔의 [결제] 메뉴에서 예산 알림을 설정해 두는 것을 추천합니다.

결론적으로, 구글 커스텀 검색 API는 디지털 노마드와 1인 기업가들에게 무한한 데이터의 바다를 열어주는 가장 쉽고 강력한 열쇠입니다. 지금 바로 이 가이드를 따라 API 세팅을 마치고, 여러분의 업무 프로세스를 10배 이상 자동화해 보세요. 정보의 가공이 곧 수익으로 직결되는 시대에, 이 강력한 도구는 여러분의 가장 든든한 무기가 될 것입니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for post in reversed(google_search_setup_post):
    if not any(p['title'] == post['title'] for p in posts_data):
        posts_data.insert(0, post)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

rebuild_all()
print(f"Successfully added Google Search API Setup post.")
