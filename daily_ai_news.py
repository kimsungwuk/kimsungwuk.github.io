import os
import json
import datetime
import subprocess

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"

def get_journalistic_news():
    """
    실시간 검색 결과를 바탕으로 2026년 3월 4일 기준 최신 AI 뉴스를 제공합니다.
    최고의 저널리스트 모드로 상세 분석을 포함하며, 이모티콘 및 특수문자(**)를 사용하지 않습니다.
    """
    news_data = [
        {
            "title": "오픈아이 마이크로소프트 깃허브에 도전하는 새로운 코드 저장소 개발",
            "category": "AI 산업",
            "summary": "오픈아이가 마이크로소프트의 깃허브와 경쟁할 새로운 코드 저장소 프로젝트를 추진 중이라는 소식이 전해졌습니다.",
            "content": "외신 보도에 따르면 오픈아이는 깃허브를 대체하거나 경쟁할 수 있는 독자적인 코드 리포지토리 시스템을 개발하고 있습니다. 이는 오픈아이가 마이크로소프트에 대한 기술적 의존도를 낮추고 AI 모델 개발부터 코드 관리까지 이어지는 수직 계열화를 완성하려는 전략으로 풀이됩니다. 특히 AI 에이전트가 코드를 직접 작성하고 관리하는 시대에 최적화된 새로운 형태의 협업 플랫폼이 될 가능성이 큽니다. 이러한 움직임은 양사의 파트너십에 미묘한 변화를 불러올 수 있으며 전 세계 개발자 생태계에 큰 파장을 일으킬 것으로 전망됩니다.",
            "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c",
            "keywords": ["오픈아이", "깃허브", "코드저장소", "마이크로소프트", "AI개발환경"]
        },
        {
            "title": "미국 정부 앤스로픽 AI 도구 사용 중단 지침 하달",
            "category": "AI 정책",
            "summary": "트럼프 행정부가 보안 우려를 이유로 연방 기관들에 앤스로픽 AI 제품 사용을 중단하고 오픈아이와 구글 등으로 전환할 것을 명령했습니다.",
            "content": "미국 행정부는 앤스로픽의 AI 모델이 공급망 보안 리스크를 초래할 수 있다는 판단 하에 모든 연방 기관의 사용을 중단시켰습니다. 이에 따라 재무부와 국무부 등 주요 부처들은 기존 앤스로픽 기반 시스템을 오픈아이나 구글의 모델로 긴급 교체하기 시작했습니다. 이번 조치는 국가 안보와 직결된 AI 기술에 대한 정부의 통제권 강화를 의미하며 특정 기업의 기술적 중립성보다는 국가적 신뢰성을 우선시하겠다는 강력한 신호로 해석됩니다. 앤스로픽은 이에 대해 즉각적인 논평을 피하고 있으나 실리콘밸리 AI 기업들 사이에서는 규제 리스크에 대한 긴장감이 고조되고 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
            "keywords": ["앤스로픽", "미국정부", "AI보안", "오픈아이", "행정명령"]
        },
        {
            "title": "엔비디아 GTC 2026에서 차세대 AI 시대 비전 선포 예정",
            "category": "AI 하드웨어",
            "summary": "젠슨 황 CEO가 GTC 2026을 통해 인류의 삶을 근본적으로 바꿀 AI 시대의 새로운 하드웨어와 소프트웨어 혁신을 공개합니다.",
            "content": "엔비디아는 세계 최대 AI 컨퍼런스인 GTC 2026의 개최를 앞두고 젠슨 황 CEO의 기조연설을 통해 새로운 산업 혁명을 예고했습니다. 이번 행사에서는 성능이 대폭 향상된 차세대 GPU 아키텍처와 함께 물리 기반 AI 및 로보틱스 분야의 비약적인 발전이 소개될 예정입니다. 엔비디아는 단순한 칩 제조사를 넘어 전 세계 AI 연산 인프라의 표준을 정립하고 있으며 이번 발표는 에이전틱 AI가 일상에 깊숙이 침투하는 전환점이 될 것입니다. 시장 전문가들은 엔비디아가 제시할 새로운 기술 로드맵이 향후 5년의 테크 산업 지형도를 결정지을 것으로 보고 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475",
            "keywords": ["엔비디아", "GTC 2026", "젠슨황", "AI인프라", "차세대GPU"]
        },
        {
            "title": "미국 연방준비제도 AI가 고용과 물가에 미치는 영향 집중 분석",
            "category": "AI 경제",
            "summary": "미 연준 인사들이 AI 기술 도입이 경제 전반에 가져올 생산성 향상과 인플레이션 변화 가능성에 대해 심도 있는 논의를 시작했습니다.",
            "content": "연방준비제도(Fed) 관계자들은 인공지능이 노동 시장의 구조를 바꾸고 물가 흐름에 미치는 영향을 파악하기 위해 다각도의 분석을 진행하고 있습니다. AI로 인한 급격한 생산성 증가는 잠재 성장률을 높이는 긍정적 효과가 있으나 단기적인 고용 불안과 소득 불균형을 초래할 수 있다는 우려도 제기됩니다. 연준은 통화 정책 수립에 있어 AI라는 변수를 어떻게 반영할지 고심 중이며 이는 향후 금리 결정 경로에도 중요한 영향을 미칠 전망입니다. 기술 혁신이 거시 경제 지표에 투영되는 속도가 빨라짐에 따라 중앙은행의 정책 대응 속도 역시 시험대에 올랐습니다.",
            "image_url": "https://images.unsplash.com/photo-1611974714658-058e11ee906e",
            "keywords": ["연준", "AI경제", "생산성", "노동시장", "통화정책"]
        },
        {
            "title": "아마존 스페인 AI 데이터 센터에 210억 달러 추가 투자",
            "category": "AI 인프라",
            "summary": "아마존이 유럽 내 AI 경쟁력 강화를 위해 스페인에 대규모 데이터 센터 확충 및 기술 혁신을 위한 추가 투자를 단행합니다.",
            "content": "아마존은 스페인 지역의 디지털 인프라와 AI 생태계를 지원하기 위해 180억 유로에 달하는 대규모 투자 계획을 발표했습니다. 이번 투자는 클라우드 서비스인 AWS의 역량을 확장하고 유럽 기업들이 최신 AI 모델을 원활하게 활용할 수 있는 기반을 마련하는 데 집중됩니다. 유럽 내 데이터 주권 문제와 효율적인 AI 운영을 동시에 해결하려는 전략적 포석으로 보입니다. 스페인 정부는 아마존의 이번 결정을 환영하며 이를 통해 자국 내 기술 일자리 창출과 디지털 전환이 가속화될 것으로 기대하고 있습니다. 빅테크 기업들의 유럽 내 인프라 선점 경쟁은 더욱 치열해지는 양상입니다.",
            "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51",
            "keywords": ["아마존", "스페인", "데이터센터", "AI투자", "클라우드"]
        },
        {
            "title": "미 대법원 AI 생성 저작물에 대한 저작권 인정 분쟁 기각",
            "category": "AI 법률",
            "summary": "미국 연방법원이 AI가 단독으로 만든 예술 작품에 대해 저작권을 부여할 수 없다는 기존 판결을 유지하며 관련 상고를 기각했습니다.",
            "content": "미국 대법원은 인간의 창의적 개입 없이 인공지능 시스템이 생성한 이미지에 대해 저작권을 인정해달라는 과학자의 요청을 받아들이지 않았습니다. 이는 저작권법의 보호 대상이 인간 작가에 한정된다는 원칙을 재확인한 것으로 AI 창작물의 법적 지위에 대한 중요한 선례가 될 것입니다. 다만 인간과 AI가 협업하여 만든 작품의 경우 어느 정도의 기여도가 있어야 저작권을 인정받을 수 있는지에 대한 논의는 여전히 과제로 남아 있습니다. 이번 결정으로 생성형 AI를 활용하는 콘텐츠 제작자들 사이에서는 법적 권리를 확보하기 위한 인간의 주도적 역할이 더욱 강조될 것으로 보입니다.",
            "image_url": "https://images.unsplash.com/photo-1589254065675-d0581d4d0d9f",
            "keywords": ["대법원", "AI저작권", "창작물", "지식재산권", "판례"]
        }
    ]
    return news_data

def create_daily_news_posts():
    today = datetime.date.today().isoformat()
    category = "AI 최신뉴스"
    
    news_data_list = get_journalistic_news()
    
    if not news_data_list:
        print("업데이트할 새로운 뉴스 데이터가 없습니다. 실시간 검색을 먼저 수행하세요.")
        return False
    
    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        posts_data = json.load(f)

    newly_added = 0
    for item in news_data_list:
        title = item["title"]
        keywords = item.get("keywords", [item["category"], "AI 뉴스", "수익 자동화"])
        
        posts_data = [p for p in posts_data if not (p['title'] == title and p['date'] == today)]
        
        posts_data.insert(0, {
            'title': title,
            'date': today,
            'category': category,
            'summary': item["summary"],
            'image_url': item["image_url"],
            'content': item["content"],
            'keywords': keywords
        })
        newly_added += 1
        
    if newly_added > 0:
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(posts_data, f, indent=4, ensure_ascii=False)
        
        build_script = os.path.join(BASE_DIR, "build_engine.py")
        subprocess.run(["python3", build_script], check=True)
        
        print(f"총 {newly_added}개의 개별 뉴스 포스팅이 완료되었습니다.")
        return True
    
    return False

if __name__ == "__main__":
    create_daily_news_posts()
