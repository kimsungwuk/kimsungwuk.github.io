import json
import os
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

openclaw_skill_posts = [
    {
        "title": "OpenClaw 필수 스킬 분석 1탄: 정보 홍수 속의 구원자 Summarize 스킬 활용 가이드",
        "date": "2026-02-24",
        "category": "OpenClaw",
        "summary": "방대한 웹 문서부터 긴 유튜브 영상까지 단 몇 초 만에 핵심을 꿰뚫는 OpenClaw의 Summarize 스킬 설치 및 실전 사용법을 심층 분석합니다.",
        "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&q=80&w=1000",
        "content": """인공지능 에이전트 OpenClaw를 사용하면서 가장 먼저 마주하게 되는 강력한 도구 중 하나는 바로 Summarize 스킬입니다. 현대 사회는 정보의 양이 너무 많아 모든 내용을 직접 읽고 판단하기에는 시간이 턱없이 부족합니다. 이때 Summarize 스킬은 수천 단어의 기사나 수십 분 분량의 유튜브 영상을 단 몇 문장으로 압축하여 핵심 인사이트를 제공하는 혁신적인 역할을 수행합니다.

왜 Summarize 스킬을 사용해야 하는가
우리가 웹 서핑을 하거나 업무를 처리할 때 마주하는 긴 보고서, 뉴스 기사, 그리고 학습을 위해 시청하는 유튜브 영상들은 그 가치가 높지만 끝까지 읽거나 시청하는 데 많은 에너지가 소모됩니다. Summarize 스킬을 사용하면 다음과 같은 이점을 얻을 수 있습니다. 첫째, 정보 습득 시간의 획기적인 단축입니다. 인공지능이 맥락을 파악하여 불필요한 서술은 걷어내고 핵심 논점만을 남깁니다. 둘째, 언어 장벽의 해소입니다. 외국어로 된 방대한 문서나 영상도 한국어로 즉시 요약하여 이해의 폭을 넓혀줍니다. 셋째, 업무 효율성의 극대화입니다. 자료 조사 단계에서 수많은 링크를 일일이 확인할 필요 없이 요약본을 먼저 훑어보고 심층 분석이 필요한 자료만 선별할 수 있습니다.

Summarize 스킬 설치 및 환경 설정 방법
OpenClaw 환경에서 Summarize 스킬을 사용하기 위해서는 먼저 시스템에 해당 바이너리를 설치해야 합니다. 맥OS 사용자라면 홈브루(Homebrew)를 통해 간단히 설치할 수 있습니다. 터미널을 열고 다음 명령어를 입력하세요.
명령어: brew tap steipete/tap/summarize && brew install summarize
설치가 완료되었다면 인공지능 모델이 작동할 수 있도록 API 키를 설정해야 합니다. 구글의 제미나이(Gemini)나 오픈AI의 GPT 모델 등을 지원하며, 가장 권장되는 모델은 구글의 제미나이 1.5 플래시입니다. 터미널 환경 변수에 본인의 API 키를 등록하면 준비는 끝납니다.

실전 사용 방법과 활용 팁
설치가 끝났다면 이제 OpenClaw에게 링크나 파일을 던져주기만 하면 됩니다. 사용 방법은 매우 직관적입니다.
명령어 예시: summarize "https://example.com/long-article" --length medium
유튜브 영상의 경우 자막 정보를 기반으로 텍스트를 추출하여 요약해 줍니다. 특히 긴 영상에서 특정 정보를 찾고 싶을 때 매우 유용합니다.
명령어 예시: summarize "https://youtu.be/video-id" --youtube auto --extract-only
더 정교한 요약을 원한다면 --length 플래시를 사용하여 요약본의 길이를 조절하거나, --json 옵션을 통해 다른 프로그램에서 데이터를 활용할 수 있도록 출력 형식을 지정할 수도 있습니다.

장문의 콘텐츠를 빠르게 소화하고 나만의 지식 자산으로 만들고 싶은 분들에게 OpenClaw의 Summarize 스킬은 선택이 아닌 필수입니다. 지금 바로 설치하여 인공지능 파트너와 함께 정보의 바다를 효율적으로 항해해 보시기 바랍니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for post in reversed(openclaw_skill_posts):
    if not any(p['title'] == post['title'] for p in posts_data):
        posts_data.insert(0, post)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

rebuild_all()
print(f"Successfully added OpenClaw skill post and rebuilt blog.")
