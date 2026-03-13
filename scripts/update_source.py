import json
import os

path = "/Users/kimsungwuk/StudioProjects/chloe-blog/config/posts_data.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

target_title = "개인 AI 에이전트의 보안 요새 구축 전략: 오픈클로(OpenClaw) Fortress Build 아키텍처 완벽 가이드"
source_url = "https://youtu.be/Euf_x66_ON4?si=APgqo5a09mRLScGn"

for post in data:
    if post['title'] == target_title:
        if "출처:" not in post['content']:
            post['content'] += f"\n\n출처: {source_url}"
            print(f"Updated post: {target_title}")
        else:
            print("Already updated.")
        break

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
