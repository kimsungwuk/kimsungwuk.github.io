import os
import json
import datetime
import subprocess

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"

def add_post():
    today = datetime.date.today().isoformat()
    title = "AI 기반 캐릭터 이미지의 픽셀 아트 변환 및 게임 애니메이션 활용 전략"
    category = "AI를 활용한 개발정보"
    summary = "고퀄리티 원화 이미지를 단 16초 만에 게임용 픽셀 캐릭터로 변환하고 보행 및 주행 애니메이션까지 생성하는 인공지능 워크플로우를 분석합니다."
    content = """인공지능 기술의 발전은 게임 개발의 에셋 제작 공정을 획기적으로 단축시키고 있습니다. 최근 주목받는 워크플로우 중 하나는 주술회전의 고조 사토르와 같은 고해상도 전신 캐릭터 이미지를 입력받아 게임에서 즉시 활용 가능한 픽셀 아트 캐릭터로 변환하는 기술입니다. 이 과정은 단순히 해상도를 낮추는 것을 넘어 캐릭터의 특징을 유지하면서 픽셀 아트 특유의 감성을 구현하는 고도의 이미지 프로세싱을 포함합니다.

인공지능 모델에 전신 이미지를 입력하고 실행하면 평균적으로 약 16초 내외의 짧은 시간 안에 정교한 픽셀 캐릭터가 생성됩니다. 이는 과거 전문 디자이너가 수작업으로 수 시간 이상 작업해야 했던 분량을 단 몇 초 만에 완성하는 놀라운 효율성을 보여줍니다. 특히 현대 모바일 게임의 트렌드인 픽셀 기반 인게임 화면과 고퀄리티 원화 기반의 캐릭터 상세 보기 화면을 유기적으로 연결하는 시스템을 구축하는 데 있어 이 인공지능 워크플로우는 핵심적인 역할을 수행할 수 있습니다.

단순한 이미지 변환을 넘어 실제 게임 제작에 있어 가장 중요한 요소는 캐릭터의 움직임입니다. 생성된 픽셀 캐릭터는 인공지능 기반의 애니메이션 생성 도구와 결합하여 걷기, 뛰기, 공격 등 게임 내 필수 동작들을 포함한 스프라이트 시트로 즉시 확장될 수 있습니다. 인공지능은 캐릭터의 골격 구조를 이해하고 각 관절의 움직임을 픽셀 단위로 예측하여 자연스러운 프레임 간 전환을 만들어냅니다.

이러한 기술의 민주화는 소규모 인디 게임 개발팀이나 개인 개발자들에게 대형 게임사 수준의 에셋 퀄리티와 제작 속도를 제공합니다. 캐릭터 디자인에 투입되던 리소스를 게임의 기획이나 밸런싱 등 핵심 재미 요소에 더 집중할 수 있게 함으로써 전체적인 게임 산업의 생산성 향상을 이끌어낼 것으로 기대됩니다. 다만 생성된 캐릭터의 저작권 문제와 독창성 확보는 향후 기술 활용에 있어 반드시 고려되어야 할 윤리적 과제입니다. 결론적으로 인공지능을 활용한 픽셀 아트 변환 기술은 게임 개발의 장벽을 낮추고 창의적인 아이디어를 빠르게 실체화하는 강력한 도구로 자리 잡을 것입니다."""

    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        posts_data = json.load(f)

    # Check for duplicates
    if any(p['title'] == title for p in posts_data):
        print("이미 포스팅된 내용입니다.")
        return

    posts_data.insert(0, {
        'title': title,
        'date': today,
        'category': category,
        'summary': summary,
        'image_url': "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&q=80&w=1000",
        'content': content
    })

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(posts_data, f, indent=4, ensure_ascii=False)

    # Build blog
    build_script = os.path.join(BASE_DIR, "build_engine.py")
    subprocess.run(["python3", build_script], check=True)
    print("성공적으로 포스팅되었습니다.")

if __name__ == "__main__":
    add_post()
