import json
import os
from build_engine import rebuild_all

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"
data_path = os.path.join(BASE_DIR, "config/posts_data.json")

openclaw_skill_posts_v3 = [
    {
        "title": "OpenClaw 필수 스킬 분석 3탄: 내 시스템을 철벽 방어하는 보안 보안관 Healthcheck 가이드",
        "date": "2026-02-24",
        "category": "OpenClaw",
        "summary": "AI 에이전트 운영의 핵심은 보안입니다. 시스템의 취약점을 점검하고 안전하게 보호하는 OpenClaw의 Healthcheck 스킬 활용법을 완벽 정리합니다.",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000",
        "content": """강력한 인공지능 에이전트를 내 컴퓨터에서 실행한다는 것은 편리함을 주지만, 동시에 보안에 대한 책임도 뒤따릅니다. 내 시스템의 문이 열려있지는 않은지, 중요한 데이터가 외부에 노출될 위험은 없는지 늘 점검해야 합니다. OpenClaw의 Healthcheck 스킬은 단순한 진단을 넘어 내 시스템의 보안 상태를 강화(Hardening)하고 최적의 위험 허용 범위를 설정해주는 든든한 보안 파트너입니다.

왜 Healthcheck 스킬이 필수적인가
개인용 컴퓨터나 서버에 OpenClaw를 설치하면 에이전트는 파일 시스템, 네트워크, 다양한 API에 접근하게 됩니다. 이때 보안 설정이 허술하면 외부 공격의 타겟이 될 수 있습니다. Healthcheck를 사용해야 하는 이유는 명확합니다. 첫째, 자동화된 보안 감사(Audit)입니다. 시스템의 열려있는 포트, 방화벽 상태, OpenClaw 자체의 권한 설정 등을 정밀하게 분석하여 보고해줍니다. 둘째, 맞춤형 보안 프로필 설정입니다. 사용자의 환경에 따라 '균형 잡힌 워크스테이션' 모드나 '강력하게 보호된 서버' 모드 등 상황에 맞는 보안 수준을 제안하고 적용할 수 있습니다. 셋째, 정기적인 상태 점검입니다. 크론(Cron) 기능을 활용해 매일 또는 매주 자동으로 시스템 건강 상태를 체크하고 업데이트가 필요한지 알려주어 늘 최신 보안 상태를 유지하게 돕습니다.

보안 점검을 위한 기본 워크플로우
Healthcheck 스킬은 매우 신중하게 작동하도록 설계되었습니다. 먼저 시스템의 운영체제(OS)와 현재 접속 방식(로컬 또는 SSH)을 파악한 뒤, 사용자에게 '읽기 전용' 점검 권한을 요청합니다. 권한이 부여되면 다음과 같은 핵심 명령어들을 통해 진단을 시작합니다.
시스템 전체 보안 감사: openclaw security audit --deep
이 명령은 OpenClaw 설정 파일의 권한이 너무 느슨하지 않은지, 외부에서 접근 가능한 위험한 설정은 없는지 깊숙이 파고들어 확인합니다.
OpenClaw 업데이트 상태 확인: openclaw update status
최신 버전의 보안 패치가 적용되어 있는지 확인하는 것은 보안의 기본입니다.

실전 보안 강화 및 정기 예약 방법
진단 결과 취약점이 발견되었다면, Healthcheck는 구체적인 해결 방안을 제시합니다.
명령어 예시: openclaw security audit --fix
이 명령은 안전한 범위 내에서 OpenClaw의 기본 보안 설정을 자동으로 조여줍니다. 다만, 시스템의 방화벽이나 SSH 설정 같은 중요한 변경은 반드시 사용자의 명시적인 승인 하에 단계별로 진행됩니다.
또한, 바쁜 일상 속에서도 보안을 놓치지 않으려면 정기 검사를 예약하는 것이 좋습니다.
명령어 예시: openclaw cron add --name healthcheck:security-audit --schedule "0 0 * * *"
이렇게 설정하면 매일 자정에 시스템 보안 점검이 자동으로 수행됩니다.

내 시스템을 가장 잘 아는 AI 에이전트와 함께 안전한 작업 환경을 구축하는 것은 지속 가능한 수익 자동화의 밑바탕입니다. 지금 바로 Healthcheck 스킬을 실행하여 여러분의 디지털 자산을 안전하게 보호하시기 바랍니다."""
    }
]

with open(data_path, "r", encoding="utf-8") as f:
    posts_data = json.load(f)

for post in reversed(openclaw_skill_posts_v3):
    if not any(p['title'] == post['title'] for p in posts_data):
        posts_data.insert(0, post)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(posts_data, f, indent=4, ensure_ascii=False)

rebuild_all()
print(f"Successfully added 3rd OpenClaw skill post and rebuilt blog.")
