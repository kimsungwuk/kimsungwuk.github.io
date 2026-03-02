import os
import json
import datetime
import subprocess

BASE_DIR = "/Users/kimsungwuk/StudioProjects/chloe-blog"

def get_journalistic_news():
    """
    실시간 검색 결과를 바탕으로 2026년 3월 3일 기준 최신 AI 뉴스를 제공합니다.
    최고의 저널리스트 모드로 상세 분석을 포함하며, 이모티콘 및 특수문자(**)를 사용하지 않습니다.
    """
    news_data = [
        {
            "title": "화웨이 MWC 2026에서 에이전틱 인터넷 시대 선언",
            "category": "AI 산업",
            "summary": "화웨이가 바르셀로나에서 열린 MWC 2026에서 5G-A 기술과 AI의 결합을 통해 에이전틱 인터넷 시대로의 전환을 가속화하겠다고 발표했습니다.",
            "content": "화웨이의 리 펭 수석 부사장은 MWC 2026 기조연설을 통해 통신 인프라가 단순한 데이터 전송을 넘어 자율적인 AI 에이전트들의 활동을 지원하는 에이전틱 인터넷으로 진화해야 함을 강조했습니다. 5G-Advanced 네트워크는 초저지연과 고대역폭을 제공하여 AI 에이전트가 실시간으로 복잡한 의사결정을 내릴 수 있는 기반이 됩니다. 이는 산업 자동화와 스마트 시티 구현에 있어 핵심적인 역할을 할 것으로 보이며 화웨이는 관련 기술 표준화를 주도하겠다는 의지를 분명히 했습니다. 특히 네트워크 자체가 지능을 갖추는 AI-native 인프라 구축이 향후 10년의 핵심 경쟁력이 될 것이라는 분석입니다.",
            "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475",
            "keywords": ["화웨이", "MWC 2026", "에이전틱 인터넷", "5G-A", "AI 인프라"]
        },
        {
            "title": "레노버 MWC 2026에서 차세대 AI PC 및 혁신 컨셉 공개",
            "category": "AI 디바이스",
            "summary": "레노버가 요가 및 아이디어패드 AI 노트북 시리즈와 함께 3D 및 폴더블 컨셉 기기를 선보이며 소비자 AI 시장 공략을 강화합니다.",
            "content": "레노버는 MWC 2026에서 온디바이스 AI 성능을 극대화한 요가 북 프로 3D 컨셉과 리전 고 폴드 컨셉을 공개하며 하드웨어 혁신을 주도하고 있습니다. 이번에 발표된 신제품들은 사용자의 작업 습관을 학습하여 최적의 성능을 배분하는 지능형 소프트웨어를 탑재했습니다. 특히 안경 없이도 입체 영상을 구현하는 3D 디스플레이 기술과 AI의 결합은 창작자들에게 새로운 작업 환경을 제공할 것으로 기대됩니다. 레노버는 하드웨어 제조사를 넘어 AI 솔루션 제공 기업으로 거듭나겠다는 전략 하에 생태계 확장에 박차를 가하고 있으며 이는 글로벌 PC 시장의 판도 변화를 예고하고 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8",
            "keywords": ["레노버", "AI 노트북", "MWC 2026", "요가 북 프로", "온디바이스 AI"]
        },
        {
            "title": "오픈AI 미 국방부와 협력하여 전략적 AI 배치 원칙 발표",
            "category": "AI 정책",
            "summary": "오픈AI가 미 국방부와 고도화된 AI 시스템 배치를 위한 협약을 체결하고 안전성과 윤리를 보장하기 위한 3대 핵심 원칙을 제시했습니다.",
            "content": "오픈AI는 국가 안보 분야에서 AI의 역할이 커짐에 따라 국방부와 긴밀히 협력하기로 했습니다. 이번 협약의 핵심은 인간의 통제권 유지, 투명한 의사결정 프로세스 구축, 그리고 기술의 오용 방지라는 3대 원칙에 기반합니다. 이는 AI 기술이 군사적 목적으로 활용될 때 발생할 수 있는 윤리적 우려를 불식시키기 위한 선제적 조치로 풀이됩니다. 오픈AI는 기술적 우위를 바탕으로 국가적 안전을 도모하는 동시에 책임 있는 AI 개발이라는 기업 철학을 유지하겠다는 입장입니다. 전문가들은 이번 협력이 민간 AI 기술의 공공 및 국방 분야 도입을 가속화하는 이정표가 될 것으로 보고 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
            "keywords": ["오픈AI", "국방부 협력", "AI 윤리", "국가 안보", "AI 배치 원칙"]
        },
        {
            "title": "노키아 글로벌 통신사들과 AI 기술 협력 대폭 확대",
            "category": "AI 통신",
            "summary": "노키아가 TIM 브라질 및 도이치텔레콤과 파트너십을 확장하며 지능형 네트워크 운영을 위한 AI 기술 도입에 속도를 내고 있습니다.",
            "content": "노키아는 통신망 운영의 효율성을 높이기 위해 AI 기반의 자동화 솔루션을 글로벌 시장에 적극 보급하고 있습니다. 이번 파트너십 확대를 통해 브라질과 유럽 시장에서 AI-RAN 기술의 상용화를 앞당길 계획입니다. AI-RAN은 기지국 인프라에 인공지능 연산 능력을 결합하여 트래픽을 지능적으로 분산하고 에너지 소비를 최적화하는 기술입니다. 노키아는 이를 통해 통신사들의 운영 비용을 절감하는 동시에 6G 시대를 대비한 기반 기술을 확보한다는 전략입니다. 통신과 AI의 결합은 단순한 기술 트렌드를 넘어 산업 인프라의 근본적인 변혁을 의미하며 노키아가 그 중심에 서 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1516110833967-0b5716ca1387",
            "keywords": ["노키아", "AI-RAN", "도이치텔레콤", "TIM 브라질", "네트워크 자동화"]
        },
        {
            "title": "팔란티어 국방 분야 AI 수요 급증으로 강력한 성장세 확인",
            "category": "AI 경제",
            "summary": "팔란티어 테크놀로지스가 정부 및 국방 분야의 AI 수요 증가에 힘입어 4분기 실적 호조와 함께 향후 시장 전망을 낙관했습니다.",
            "content": "팔란티어는 최근 미 국토안보부와의 대규모 계약 체결과 국방용 AI 플랫폼인 AIP의 가파른 도입 확산을 통해 기업 가치를 증명하고 있습니다. 특히 복잡한 데이터를 분석하여 전술적 의사결정을 돕는 에이전틱 기능을 강화하며 시장의 독보적인 위치를 굳히고 있습니다. 실적 발표 이후 팔란티어의 주가는 AI 방산 수요에 대한 기대감을 반영하며 급등세를 보였습니다. 팔란티어 경영진은 인공지능이 실제 전장과 정부 행정 업무의 효율성을 어떻게 바꾸고 있는지 구체적인 사례를 제시하며 향후 수년간 지속적인 성장이 가능할 것이라고 자신감을 내비쳤습니다. 이는 AI 기술의 실질적 수익화 모델을 보여주는 대표적인 사례입니다.",
            "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa",
            "keywords": ["팔란티어", "AIP", "국방 AI", "데이터 분석", "AI 수익화"]
        },
        {
            "title": "카고원 물류 산업 최초의 AI 네이티브 운영 체제 출시",
            "category": "AI 물류",
            "summary": "항공 화물 예약 플랫폼 카고원이 AI를 기반으로 설계된 차세대 운영 체제를 출시하며 물류 디지털 전환의 새로운 기준을 제시했습니다.",
            "content": "카고원이 발표한 AI 네이티브 운영 체제는 예약부터 경로 최적화, 가격 산정까지 전 과정을 인공지능이 자율적으로 처리하거나 보조하는 기능을 갖추고 있습니다. 기존의 수동적인 시스템에서 벗어나 데이터 흐름을 실시간으로 파악하고 예측하여 물류 효율성을 극대화합니다. 이는 공급망의 불확실성을 최소화하고 비용을 절감하려는 항공 화물 업계의 요구를 반영한 결과입니다. 카고원은 AI 기술이 물류 산업의 복잡한 문제를 해결하는 핵심 열쇠가 될 것이라고 강조하며 향후 다양한 운송 수단으로 서비스 범위를 확대할 계획입니다. 물류 분야의 AI 도입은 글로벌 공급망의 안정성을 높이는 데 크게 기여할 전망입니다.",
            "image_url": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d",
            "keywords": ["카고원", "AI 물류", "항공 화물", "운영 체제", "디지털 전환"]
        },
        {
            "title": "의료 AI 분야 혁신 출산 예정일 예측 기술 FDA 승인",
            "category": "AI 의료",
            "summary": "울트라사운드 AI의 클라우드 기반 출산 예정일 예측 기술이 FDA로부터 드 노보 승인을 획득하며 정밀 의료 시대의 개막을 알렸습니다.",
            "content": "초음파 영상과 AI 알고리즘을 결합하여 출산 예정일을 정밀하게 예측하는 기술이 미국 FDA의 엄격한 심사를 통과했습니다. 이 기술은 기존의 단순 측정 방식보다 높은 정확도를 제공하여 임산부와 의료진이 보다 체계적인 출산 계획을 세울 수 있도록 돕습니다. 클라우드 기반 소프트웨어로서의 강점을 활용해 전 세계 어디서든 표준화된 진단 결과를 얻을 수 있다는 점이 특징입니다. 이번 FDA 승인은 의료 현장에서 AI의 신뢰성을 입증한 중요한 사례이며 향후 다양한 산부인과 질환 진단 및 관리 분야로 AI 적용이 확대되는 계기가 될 것입니다. 의료와 기술의 결합이 인류의 건강권을 증진하는 실질적인 결과물로 나타나고 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528",
            "keywords": ["의료 AI", "FDA 승인", "출산 예측", "울트라사운드 AI", "정밀 의료"]
        }
    ]
    return news_data

def create_daily_news_posts():
    today = datetime.date.today().isoformat()
    category = "AI 최신뉴스"
    
    news_data_list = get_journalistic_news()
    
    if not news_data_list:
        print("⚠️ 업데이트할 새로운 뉴스 데이터가 없습니다. 실시간 검색을 먼저 수행하세요.")
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
        
        print(f"💰 [성공] 총 {newly_added}개의 개별 뉴스 포스팅이 완료되었습니다.")
        return True
    
    return False

if __name__ == "__main__":
    create_daily_news_posts()
