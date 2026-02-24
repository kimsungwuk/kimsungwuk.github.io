import json
import os
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

openclaw_dashboard_posts = [
    {
        "title": "OpenClaw 필수 스킬 분석 6탄: 나만의 AI 비서 '자비스'를 시각화하는 대시보드 구축 전략",
        "date": "2026-02-24",
        "category": "OpenClaw",
        "summary": "텔레그램을 넘어 웹 대시보드와 음성 인터페이스로 OpenClaw를 제어하고, 비트코인 투자까지 자동화하는 '배달의 민족 김문장'님의 실전 활용 사례를 분석합니다.",
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1000",
        "content": """단순히 텍스트로 대화하는 인공지능을 넘어, 내 비즈니스와 일상을 한눈에 파악할 수 있는 '중앙 통제실'을 가질 수 있다면 어떨까요? 최근 '배움의 달인 김문장'님이 공개한 OpenClaw 활용법은 인공지능 에이전트가 어떻게 실질적인 개인 자산 관리와 업무 자동화의 핵심이 될 수 있는지 보여주는 완벽한 교과서입니다. 이번 포스팅에서는 텔레그램의 한계를 넘어 웹 대시보드와 음성 시스템을 결합한 OpenClaw의 진화된 활용 전략을 2배 더 풍성한 분량으로 상세히 파헤쳐 보겠습니다.

1. 시각화의 정점: Tailscale을 활용한 외부 접속형 대시보드
대부분의 사용자가 OpenClaw를 텔레그램 봇으로만 사용하지만, 김문장님은 자신만의 웹 대시보드를 구축하여 모든 대화 데이터와 지표를 시각화했습니다.
핵심 기술은 테일스케일(Tailscale)입니다. 이를 통해 집에 있는 서버(맥미니 등)에 설치된 OpenClaw를 외부 어디서든 보안 걱정 없이 전용 웹사이트처럼 접속할 수 있게 만듭니다. 대시보드에는 비트코인 실시간 시세, RSI 지표, AI 핫 이슈 리스트, 리마인더 일정 등이 배치되어 있어, 에이전트가 수행한 모든 작업 결과를 한눈에 모니터링할 수 있습니다. 이는 에이전트가 '보이지 않는 곳에서 일하는 존재'에서 '실시간으로 소통하는 파트너'로 격상되는 중요한 지점입니다.

2. 실전 경제적 이득: 비트코인 투자 자동화와 자가 학습
AI를 업무에만 쓰는 것이 아니라 실질적인 경제적 이익을 창출하는 '머니 머신'으로 만드는 전략입니다. 김문장님은 업비트(Upbit) API를 OpenClaw와 연결하여 비트코인 자동 매매 시스템을 구축했습니다.
여기서 주목할 점은 '철저한 교육 과정'입니다. 약 2~3주간 에이전트에게 차트 데이터 분석법과 경제 지표 해석법을 집중적으로 학습시켰으며, 실제 투입 전 페이퍼 트레이닝(모의 투자)을 통해 예측 정확도를 검증했습니다. 또한 리스크 관리를 위해 '출금 기능 제외', '손절(Sell-stop) 금지', '저가 매수 중심'이라는 명확한 가이드라인을 설정했습니다. 인공지능이 스스로 시장 데이터를 학습하고 최적의 매수 타이밍을 제안하는 자가 학습(Self-learning) 구조는 수익 자동화의 미래를 보여줍니다.

3. 사용자 경험의 혁신: 내 목소리를 닮은 음성 인터페이스
운전 중이나 이동 중에도 에이전트와 소통하기 위해 김문장님은 음성 대화 시스템을 통합했습니다. 단순히 음성을 텍스트로 바꾸는 수준이 아니라, 자신의 목소리를 학습시킨 클론 보이스를 사용하여 마치 진짜 비서와 대화하는 듯한 친밀감을 구현했습니다.
"오늘 경제 브리핑 해줘", "적절한 저가 매수 구간이 언제야?"라는 질문에 에이전트가 실시간 시장 상황을 분석하여 내 목소리로 답변해주는 시스템은 사용자 경험을 극적으로 끌어올립니다. 이는 OpenClaw가 단순한 소프트웨어를 넘어 사용자의 개성과 니즈가 반영된 '진정한 페르소나'로 진화하고 있음을 증명합니다.

4. 데이터 레이크(Data Lake) 구축: 옵시디언과의 연동
모든 대화 내역과 분석 결과는 휘발되지 않고 옵시디언(Obsidian)과 같은 지식 관리 도구에 누적됩니다. 7일간의 작업 기록, 크론(Cron) 스케줄 완료 현황 등이 데이터베이스화되어 쌓이면서, 시간이 흐를수록 나만의 비즈니스 지식 베이스가 더욱 견고해집니다.

결론적으로, 김문장님의 사례는 OpenClaw를 어떻게 개인의 강력한 비즈니스 대시보드이자 투자 파트너로 성장시킬 수 있는지 그 가능성을 명확히 보여줍니다. 텔레그램을 넘어 시각화와 음성, 그리고 실제 수익화 시스템을 구축해 보세요. 여러분의 OpenClaw는 이제 단순한 도구가 아닌, 대체 불가능한 비즈니스 자산이 될 것입니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for post in reversed(openclaw_dashboard_posts):
    if not any(p['title'] == post['title'] for p in posts_data):
        posts_data.insert(0, post)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

rebuild_all()
print(f"Successfully added OpenClaw Dashboard & Investment post.")
