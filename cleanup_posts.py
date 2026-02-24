import json
import os

path = '/Users/kimsungwuk/StudioProjects/chloe-blog/config/posts_data.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

old_titles = [
    "구글 제미나이 3.1 프로 출시와 핵심 추론 능력의 진보",
    "앤스로픽 클로드 소넷 4.6 업데이트와 자율적 컴퓨터 조작 기술",
    "넷플릭스와 바이트댄스의 저작권 분쟁과 생성형 인공지능의 법적 과제",
    "메타의 정치적 영향력 확대와 인공지능 입법 대응 전략",
    "오픈AI 챗봇 광고 도입과 수익 모델의 다변화 시도"
]

# 2026-02-25 날짜이면서 위 제목들에 해당하는 포스트만 제거
new_data = [p for p in data if not (p['date'] == '2026-02-25' and p['title'] in old_titles)]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=4, ensure_ascii=False)

print(f"Cleaned up {len(data) - len(new_data)} duplicate/stale posts.")
