import json
import os
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

openclaw_google_browser_posts = [
    {
        "title": "OpenClaw 필수 스킬 분석 8탄: 구글 워크스페이스 연동과 브라우저 직접 제어 기술 가이드",
        "date": "2026-02-24",
        "category": "OpenClaw",
        "summary": "OpenClaw와 구글 서비스(캘린더, 문서, 시트)를 연결하여 일정을 자동화하고, 크롬 브라우저를 직접 제어하는 혁신적인 업무 자동화 워크플로우를 소개합니다.",
        "image_url": "https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?auto=format&fit=crop&q=80&w=1000",
        "content": """단순한 대화를 넘어 실제 업무의 중심인 구글 생태계와 브라우저를 AI가 직접 제어할 수 있다면 업무의 생산성은 상상할 수 없을 정도로 높아집니다. 이번 포스팅에서는 OpenClaw를 구글 워크스페이스(Google Workspace)와 연동하여 캘린더, 문서, 시트를 자유자재로 다루고, 나아가 크롬 브라우저를 직접 제어하여 웹 상의 정보를 수집하는 고도화된 자동화 전략을 2배 더 풍성한 분량으로 상세히 파헤쳐 보겠습니다.

1. 구글 클라우드 콘솔 설정: 연동의 첫 단추
OpenClaw가 구글 서비스에 접근하기 위해서는 구글 클라우드(Google Cloud) 프로젝트 생성이 필수적입니다. 먼저 구글 클라우드 콘솔에 접속하여 새로운 프로젝트를 생성하고, 사용하고자 하는 API들을 활성화해야 합니다. 구글 캘린더 API, 구글 독스 API, 구글 시트 API, 그리고 구글 드라이브 API가 대표적입니다.
다음으로 중요한 단계는 OAuth 동의 구성입니다. OpenClaw는 외부에서 구글 데이터를 호출하는 방식이므로 '외부(External)' 유형으로 설정하고 필요한 권한(Scope)을 부여해야 합니다. 마지막으로 사용자 인증 정보에서 '데스크톱 앱' 유형의 클라이언트 ID를 생성하여 JSON 파일을 다운로드합니다. 이 파일을 'credentials.json'으로 이름을 변경하여 OpenClaw의 워크스페이스 경로에 업로드하면 기술적인 준비는 완료됩니다.

2. 구글 스킬 활용: 일상 업무의 완전 자동화
연동이 완료되면 OpenClaw에게 자연어로 명령을 내리는 것만으로 복잡한 구글 서비스 작업을 수행할 수 있습니다. 예를 들어 "내일 오후 2시에 유튜브 업로드 일정을 캘린더에 추가해줘"라고 말하면 즉시 반영됩니다.
단순 입력을 넘어선 복합적인 워크플로우도 가능합니다. "받은 이메일을 확인해서 회의 요청이 온 것이 있으면 내 캘린더의 빈 시간대에 맞춰 답장을 보내고 일정을 등록해줘"와 같은 명령은 AI가 이메일 내용 분석, 캘린더 조회, 답장 초안 작성, 일정 생성이라는 네 가지 단계를 스스로 수행하게 만듭니다. 또한 유튜브 업로드 계획을 위클리 단위로 세워 구글 시트에 정리하거나, 구글 독스로 콘텐츠 인트로 문장을 작성하여 공유하는 등 창의적인 업무 보조 역할까지 완벽하게 수행합니다.

3. 브라우저 직접 제어(Browser Relay): 웹 자동화의 정점
OpenClaw의 가장 강력한 기능 중 하나는 사용자의 브라우저를 직접 디버깅하고 제어하는 '브라우저 릴레이' 기술입니다. 이를 위해서는 전용 크롬 확장 프로그램(Extension)을 설치하고 개발자 모드에서 로드해야 합니다.
이 기능이 활성화되면 AI는 실제 사용자가 웹사이트를 서핑하는 것처럼 행동합니다. 네이버 지도에서 특정 위치 근처의 카페를 검색하여 리스트를 만들거나, 네이버 부동산에서 특정 아파트 단지의 상위 매물 10개의 정보를 긁어와 요약해주는 작업이 가능해집니다. 이는 별도의 복잡한 크롤링 코드를 짜지 않고도 AI에게 "저 사이트에 가서 정보 좀 찾아와"라고 시키는 것과 같아, 데이터 수집 생산성을 획기적으로 높여줍니다.

4. 컴패니언 앱과 맥OS 최적화
맥 사용자라면 OpenClaw 컴패니언 앱을 설치하여 더욱 편리하게 관리할 수 있습니다. 텔레그램 메신저를 거치지 않고 데스크톱 채팅 화면에서 즉각적으로 명령을 내리고 결과를 확인할 수 있어, 작업 흐름이 끊기지 않는 쾌적한 환경을 제공합니다.

결론적으로, 구글 워크스페이스와 브라우저 제어 기술의 결합은 OpenClaw를 단순한 인공지능을 넘어 '실제로 행동하는 가상 비서'로 완성시킵니다. 귀찮은 일정 관리와 반복적인 웹 데이터 수집은 이제 AI에게 맡기고, 여러분은 더 높은 가치를 창출하는 전략적인 고민에 집중하세요. 지금 바로 구글 연동을 시작하여 업무 자동화의 신세계를 경험해 보시기 바랍니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for post in reversed(openclaw_google_browser_posts):
    if not any(p['title'] == post['title'] for p in posts_data):
        posts_data.insert(0, post)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

rebuild_all()
print(f"Successfully added Google & Browser automation post.")
