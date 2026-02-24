import json
import os
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

openclaw_skill_posts_v5 = [
    {
        "title": "OpenClaw 필수 스킬 분석 5탄: 잠자는 동안에도 수익을 내는 AI 투자 어시스턴트 구축 가이드",
        "date": "2026-02-24",
        "category": "OpenClaw",
        "summary": "구형 노트북과 OpenClaw를 결합하여 24시간 주식 시장을 감시하고 자동 매매까지 수행하는 AI 투자 시스템 구축법을 상세히 알아봅니다.",
        "image_url": "https://images.unsplash.com/photo-1611974714014-48f0796a558e?auto=format&fit=crop&q=80&w=1000",
        "content": """집에서 놀고 있는 구형 노트북이나 데스크톱 PC가 있다면, 이제는 그 고철덩어리를 24시간 쉬지 않고 일하는 나만의 'AI 투자 어시스턴트'로 재탄생시킬 시간입니다. OpenClaw의 강력한 자율 작동 메커니즘인 크론(Cron), 하트비트(Heartbeat), 그리고 스킬(Skill) 시스템을 결합하면, 우리가 잠든 사이에도 주식 시장을 분석하고 전략을 수립하여 실제 매매까지 수행하는 지능형 시스템을 구축할 수 있습니다. 이번 가이드에서는 단태랩스(Dante Labs)의 실전 사례를 바탕으로 AI 투자 에이전트를 만드는 전 과정을 2배 더 풍성한 분량으로 상세히 파헤쳐 보겠습니다.

AI 투자 시스템의 4계층 아키텍처 이해하기
성공적인 자동 매매 시스템을 구축하기 위해서는 체계적인 구조 설계가 필수적입니다.
첫째, 데이터 수집 레이어입니다. 키움증권 REST API나 오픈다트(OpenDart) 공시 정보 등을 통해 종목별 실적과 차트 데이터를 실시간으로 수집합니다.
둘째, 투자 전략 레이어입니다. 단순히 감으로 투자하는 것이 아니라, 라이너(Liner)와 같은 AI 딥 리서치 도구를 활용해 퀀트 논문과 전문가들의 전략을 분석하고 이를 AI 에이전트가 이해할 수 있는 수학적 모델로 변환합니다.
셋째, 분석 및 스코어링 레이어입니다. 수집된 로우 데이터를 바탕으로 AI가 각 종목의 투자 가치를 점수화(Scoring)합니다. 70점 이상일 때만 매수 진입을 하는 등 명확한 임계점을 설정하여 감정 섞이지 않은 이성적인 판단을 내리게 합니다.
넷째, 실행 레이어입니다. 크론(Cron) 스케줄러를 통해 장 초반인 9시 30분에 데이터를 분석해 매수를 진행하고, 장 마감 전인 3시에 일괄 청산하는 등의 매매 로직을 자동으로 실행합니다.

OpenClaw의 자율 작동 메커니즘 활용법
OpenClaw가 일반적인 챗봇과 다른 점은 사용자의 개입 없이도 스스로 판단하고 움직인다는 것입니다.
1. 크론(Cron): 특정 시간(예: 장 시작 9시)에 맞춰 정해진 작업을 수행하게 만듭니다. 데이터 수집 파이프라인과 매매 로직 실행의 핵심 엔진입니다.
2. 하트비트(Heartbeat): 일정한 간격으로 시스템의 상태를 확인합니다. API 연결이 끊기지는 않았는지, 예상치 못한 오류가 발생하지 않았는지 감시하고 문제가 생기면 즉시 텔레그램으로 보고합니다.
3. 스킬(Skill): 복잡한 API 호출이나 데이터 처리 로직을 '스킬'로 등록해두면, 에이전트가 필요할 때마다 해당 기능을 꺼내어 사용합니다. 단태랩스에서 제공하는 전용 트레이딩 툴스(Trading Tools)를 설치하면 키움증권 연동이 훨씬 쉬워집니다.

성공적인 투자를 위한 실전 구축 프로세스
먼저, 환경 변수 설정을 통해 보안을 강화해야 합니다. 수파베이스(Supabase)와 같은 클라우드 데이터베이스를 연결하여 분석 데이터를 안전하게 저장하고, 증권사 API 키들을 OpenClaw의 인버런먼트(Environment) 설정에 등록합니다.
다음으로, AI 딥 리서치를 통해 나만의 투자 전략 보고서를 작성합니다. 영상에서는 '당일 양봉 마감 예측 기반 데이트레이딩' 전략을 예로 들었는데, 이 보고서를 PDF로 OpenClaw에게 전달하면 에이전트가 이를 분석해 직접 파이썬 분석 모듈을 코딩해냅니다.
마지막으로 반드시 모의 투자 계좌를 통해 백테스팅(Backtesting)을 거쳐야 합니다. 과거 데이터를 바탕으로 승률과 수익률을 검증하고, AI와의 대화를 통해 전략의 허점을 보완하는 피드백 루프를 반복하면서 시스템을 고도화해 나갑니다.

결론적으로, OpenClaw 기반의 AI 투자 에이전트는 단순히 자동 매매 봇을 넘어, 나와 함께 성장하는 투자 파트너입니다. 데이터적 근거 없이 편향된 사고로 투자하는 위험을 줄이고, 24시간 시장을 감시하는 AI의 힘을 빌려보세요. 지금 바로 구형 노트북을 깨워 여러분만의 수익 파이프라인을 구축해 보시기 바랍니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for post in reversed(openclaw_skill_posts_v5):
    if not any(p['title'] == post['title'] for p in posts_data):
        posts_data.insert(0, post)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

rebuild_all()
print(f"Successfully added AI Trading Assistant skill post.")
