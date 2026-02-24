import json
import os
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

openclaw_skill_posts_v4 = [
    {
        "title": "OpenClaw 필수 스킬 분석 4탄: 클로드를 200% 활용하는 3종 세트와 MCP 커넥터 완벽 해부",
        "date": "2026-02-24",
        "category": "OpenClaw",
        "summary": "최신 클로드(Claude) 업데이트를 OpenClaw와 연결하여 업무 효율을 극대화하는 법을 알아봅니다. 프로젝트, 코워크, 그리고 코드 에이전트의 유기적 결합 전략을 소개합니다.",
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1000",
        "content": """인공지능 에이전트의 세계에서 가장 뜨거운 화두 중 하나는 바로 앤스로픽(Anthropic)의 클로드(Claude)입니다. 특히 최근 소네 4.6 업데이트와 함께 등장한 '클로드 코드(Claude Code)'와 '코워크(Co-work)' 시스템은 단순히 묻고 답하는 채팅을 넘어, 인공지능이 실제 업무를 수행하는 '실행 주체'로 거듭났음을 보여줍니다. OpenClaw는 이러한 클로드의 강력한 기능을 MCP(Model Context Protocol) 커넥터를 통해 우리 시스템으로 가져와 업무 자동화의 정점을 찍을 수 있게 도와줍니다. 이번 가이드에서는 클로드의 3종 세트를 OpenClaw와 연결하여 업무 효율을 수십 배 높이는 전략을 2배 더 풍성한 분량으로 파헤쳐 보겠습니다.

클로드 업무 효율화의 3종 세트 이해하기
클로드를 제대로 활용하려면 채팅(Chat), 코워크(Co-work), 그리고 코드(Code)라는 세 가지 축을 유기적으로 연결해야 합니다.
첫째, 채팅 기반의 프로젝트(Projects)입니다. 여기서는 나만의 지침(Instructions)과 지식(Knowledge) 베이스를 구축하여 AI에게 특정 역할을 부여합니다. 예를 들어 '유튜브 마케팅 팀'이라는 프로젝트를 만들고 채널의 정체성과 가이드라인을 학습시키는 단계입니다.
둘째, 로컬 환경과 연결되는 코워크(Co-work)입니다. 코워크는 내 컴퓨터의 실제 폴더와 파일을 읽고 쓸 수 있는 권한을 가집니다. 프로젝트에서 정의한 전략을 바탕으로 내 폴더에 있는 원고를 분석하고 결과물을 생성하는 실질적인 작업이 여기서 일어납니다.
셋째, 에이전트 기반의 클로드 코드(Claude Code)입니다. 터미널 환경이나 에이전트 모드에서 작동하며, 복잡한 소프트웨어 개발이나 여러 단계를 거치는 자동화 워크플로우를 명령 한 줄로 처리할 수 있게 해줍니다.

OpenClaw와 MCP 커넥터의 강력한 시너지
OpenClaw를 사용하는 가장 큰 이유 중 하나는 바로 MCP(Model Context Protocol) 커넥터입니다. 영상에서 소개된 '나노바나(Nano Banana)'와 같은 외부 도구들을 클로드와 직접 연결할 수 있습니다.
예를 들어, OpenClaw를 통해 클로드 코드를 실행하면서 나노바나 MCP를 소환하면, 클로드가 분석한 원고 내용을 바탕으로 즉석에서 카드 뉴스 이미지를 생성하고 이를 내 컴퓨터의 특정 폴더에 저장하는 전 과정을 완전 자동화할 수 있습니다. 이는 단순히 AI가 글만 써주는 것을 넘어, 이미지 생성, 파일 관리, 배포까지 이어지는 '엔드 투 엔드(End-to-End)' 자동화 파이프라인이 완성됨을 의미합니다.

실전 활용: 스킬(Skill)과 플러그인(Plugin)으로 만드는 나만의 비서
우리가 주목해야 할 기능은 반복되는 복잡한 작업을 '스킬'로 만드는 것입니다. 클로드에게 "이 업무 과정을 카드뉴스 메이커라는 스킬로 만들어줘"라고 명령하면, AI는 해당 업무의 레시피(지침)를 MD 파일이나 JSON 형태로 생성합니다.
이렇게 만들어진 스킬을 OpenClaw의 스킬 디렉토리에 등록하면, 다음부터는 긴 설명 필요 없이 "카드뉴스 메이커 실행해줘"라는 짧은 명령만으로 복잡한 작업을 즉시 시작할 수 있습니다. 더 나아가 이를 '플러그인' 형태로 패키징하면 팀원들과 공유하거나 다른 프로젝트에도 쉽게 이식할 수 있어 기업용 자동화 솔루션으로의 확장성도 매우 뛰어납니다.

결론적으로, OpenClaw와 클로드의 결합은 1인 기업가나 개발자에게 수십 명의 직원을 둔 팀과 같은 파워를 제공합니다. 채팅으로 전략을 짜고, 코워크로 파일을 주무르며, 코드로 시스템을 자동화하는 이 놀라운 여정을 지금 바로 시작해 보세요. 정보의 바다를 항해하는 가장 강력한 함선을 손에 넣게 될 것입니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for post in reversed(openclaw_skill_posts_v4):
    if not any(p['title'] == post['title'] for p in posts_data):
        posts_data.insert(0, post)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

rebuild_all()
print(f"Successfully added Claude 3-set & MCP skill post.")
