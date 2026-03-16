import os
import json
import datetime
import subprocess
import requests
import sys

BASE_DIR = os.getcwd()

def is_image_valid(url):
    if not url or not url.startswith('http'):
        return False
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400
    except Exception:
        try:
            response = requests.get(url, timeout=5, stream=True)
            return response.status_code < 400
        except Exception:
            return False

def generate_news_data():
    news_data = [
        {
            "title": "엔비디아 GTC 2026 젠슨 황의 1조 달러 AI 로드맵과 삼성 SK 하이닉스의 동맹 강화",
            "category": "AI 하드웨어",
            "summary": "젠슨 황 엔비디아 CEO가 GTC 2026에서 2027년까지 1조 달러 규모의 AI 인프라 투자를 예고하며 삼성전자와 SK하이닉스와의 협력을 공고히 했습니다.",
            "content": """반가워 친구들 클로이야. 오늘은 전 세계 테크 산업의 눈과 귀가 쏠린 미국에서 날아온 가장 뜨거운 소식을 가져왔어. 바로 2026년 3월 17일 현재 진행 중인 엔비디아 GTC 2026 행사와 젠슨 황 CEO의 파격적인 발표 내용이야. 젠슨 황은 이번 기조연설에서 AI 인프라 시장이 2027년까지 1조 달러 규모로 성장할 것이라고 자신하며 그 중심에 엔비디아의 차세대 기술과 한국 반도체 기업들의 강력한 파트너십이 있음을 선언했어. 클로이가 이 발표가 왜 우리 경제와 기술 미래에 결정적인지 아주 날카롭게 분석해줄게.

먼저 비즈니스 시사점부터 파헤쳐보자. 젠슨 황의 1조 달러 발언은 단순한 수치가 아니라 AI가 모든 산업의 근간이 되는 '소프트웨어 르네상스'가 시작됐음을 의미해. 비즈니스 리더들은 여기서 인프라 주도권의 중요성을 읽어야 해. 엔비디아는 이번에 차세대 HBM4E 메모리를 탑재한 새로운 가속기 라인업을 공개했는데 이는 데이터 처리 속도를 혁신적으로 끌어올려 기업들의 운영 비용을 획기적으로 낮출 거야. 삼성전자가 이번 GTC에서 HBM4E 실물을 최초 공개하며 엔비디아와의 동맹을 고도화한 점은 한국 반도체 산업에 엄청난 기회지. 이제 기업들은 성능 경쟁을 넘어 얼마나 효율적으로 AI 공장을 구축하느냐가 생존의 열쇠가 될 거야.

기술적인 세부 분석으로 들어가볼까. 이번 GTC 2026의 핵심 하이워드는 'HBM4E'와 '추론 전용 칩'이야. 기술적으로는 기존 블랙웰 아키텍처를 넘어선 차세대 루빈 플랫폼의 세부 사양이 일부 공개됐어. 삼성전자는 엔비디아의 차세대 추론용 AI 칩 생산을 맡게 되면서 파운드리 분야에서도 큰 도약을 이뤄냈지. 또한 SK하이닉스는 최태원 회장이 직접 나서 젠슨 황과 AI 메모리 협력을 논의하며 메모리 반도체의 초격차를 다시 한번 확인시켜줬어. 기술적으로 보면 이제 AI는 학습의 시대를 지나 실전 배치와 추론의 시대로 완전히 진입했음을 알 수 있어.

향후 전망은 'AI 팩토리'의 보편화와 에이전틱 AI의 확산으로 요약돼. 젠슨 황은 올라프 로봇을 선보이며 피지컬 AI 시대가 본격적으로 열렸음을 시각적으로 증명했어. 2026년 하반기면 우리는 공장과 물류센터뿐만 아니라 일상의 모든 영역에서 엔비디아의 지능을 탑재한 자율 로봇들을 보게 될 거야. 클로이가 보기에 이는 AI가 디지털 공간을 넘어 물리적 공간까지 지배하기 시작하는 거대한 전환점이야.

(심층 분석 계속)
글로벌 금융 시장은 엔비디아의 이번 발표를 AI 버블 논란을 잠재울 강력한 실체로 평가하고 있어. 삼성전자와 SK하이닉스 주가가 긍정적으로 반응하는 것 역시 이 거대한 인프라 사이클에 대한 기대감 때문이지. 비즈니스 리더들은 이제 자사의 데이터 전략이 엔비디아와 한국 반도체 연합이 만드는 초고속 연산 환경과 어떻게 결합될지 진지하게 고민해봐야 해.

또한 이번 행사에서는 기업용 AI 에이전트 플랫폼인 '네모클로'도 공개됐어. 클로이는 여러분이 이 거대한 기술의 파도를 보며 우리 비즈니스가 10배 더 빠르고 지능적인 환경에서 어떤 혁신을 만들어낼지 상상력을 발휘해보길 바랄게. 인프라의 승자가 곧 미래 시장의 승자니까. 오늘의 AI 리포트는 여기까지야.""" ,
            "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
            "keywords": ["엔비디아", "GTC2026", "젠슨황", "삼성전자", "SK하이닉스", "HBM4E"]
        },
        {
            "title": "에이전틱 AI 시대의 개막 엔비디아 네모클로와 자율 업무 시스템의 진화",
            "category": "소프트웨어 AI",
            "summary": "엔비디아가 기조연설에서 AI 에이전트 플랫폼 '네모클로(NemoClaw)'를 공개하며 업무 전반을 자율적으로 수행하는 에이전틱 AI 시대를 선언했습니다.",
            "content": """반가워 친구들 클로이야. 오늘은 우리가 일하는 방식을 근본적으로 바꿀 혁신적인 소프트웨어 기술 소식을 가져왔어. 바로 2026년 3월 17일 GTC 2026에서 공개된 엔비디아의 AI 에이전트 플랫폼 '네모클로(NemoClaw)' 소식이야. 이제 AI는 우리가 시키는 말에 답하는 수준을 넘어 스스로 목표를 이해하고 복잡한 업무를 계획하며 실행까지 완수하는 '에이전틱 AI'로 진화했어. 클로이가 이 변화가 왜 기업의 생산성 지형도를 통째로 바꾸게 될지 아주 깊이 있게 분석해줄게.

비즈니스 시사점부터 파헤쳐보자. 네모클로의 등장은 기업 내 모든 워크플로우에 지능형 에이전트를 배치할 수 있는 표준 도구가 생겼음을 의미해. 비즈니스 리더들은 여기서 '업무의 자율화'를 읽어야 해. 그동안 인간이 개입해야 했던 승인 프로세스 데이터 분석 보고서 작성 등의 반복 업무를 이제는 여러 대의 AI 에이전트가 협업하여 처리하게 될 거야. 엔비디아는 IBM 및 블랙스톤과 손잡고 이 에이전트들을 실제 기업 환경에 도입하는 컨설팅 사업까지 확장했지. 이건 인적 자원의 효율성을 극대화하는 동시에 의사결정 속도를 빛의 속도로 빠르게 만들 거야. 이제 경영진은 실무를 관리하는 게 아니라 AI 에이전트들의 목표와 윤리를 설계하는 설계자가 되어야 해.

기술적인 세부 분석으로 들어가볼까. 네모클로 플랫폼의 핵심은 '도구 활용 능력'과 '장기 기억'의 결합이야. 기술적으로는 LLM이 단순한 텍스트 생성을 넘어 외부 API와 소프트웨어를 자유자재로 다루며 다단계 작업을 수행하는 능력이 비약적으로 발전했어. 특히 이번에 주목받는 기술은 '멀티 에이전트 오케스트레이션'이야. 서로 다른 역할을 가진 AI 에이전트들이 통신 규약을 통해 정보를 주고받으며 최적의 해법을 찾아가는 구조지. 또한 보안과 신뢰를 보장하기 위해 기업 내부 데이터가 외부로 유출되지 않도록 하는 '프라이버시 레이어'가 강력하게 적용되어 있어 기업용 솔루션으로서의 완성도를 높였어.

향후 전망은 전문직 업무의 자동화와 개인별 AI 비서 시대의 완성으로 요약돼. 2026년 하반기면 우리는 재무 분석 법률 검토 코딩 업무까지 자율적으로 수행하는 AI 에이전트를 직장 동료로 맞이하게 될 거야. 클로이가 보기에 이는 일자리의 상실이 아니라 직무의 고도화야. 인간은 AI가 처리한 결과물을 최종 승인하고 더 창의적이고 전략적인 의사결정에만 집중하게 되겠지.

(심층 분석 계속)
앤트로픽과 오픈AI 역시 이 에이전틱 AI 시장을 선점하기 위해 대규모 합작사 설립과 사모펀드 투자를 이어가고 있어. 기술 거인들이 모두 에이전트 기술에 사활을 거는 이유는 이것이 AI의 최종적인 수익 모델이기 때문이야. 비즈니스 리더들은 이제 자사 비즈니스 프로세스 중 어떤 부분을 에이전트화할 수 있을지 진지하게 고민해봐야 해.

또한 에이전틱 AI의 확산은 '책임 있는 AI'에 대한 새로운 논의를 불러일으키고 있어. 클로이는 여러분이 이 자율형 AI의 물결을 보며 우리 조직이 얼마나 유연하게 이 기술을 받아들이고 통제할 준비가 되어 있는지 냉정하게 점검해보길 바랄게. 똑똑한 에이전트를 잘 다루는 사람이 미래의 핵심 인재가 될 거야. 오늘의 소프트웨어 리포트는 여기까지야.""" ,
            "image_url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e",
            "keywords": ["에이전틱AI", "네모클로", "NemoClaw", "엔비디아", "자율업무", "AI에이전트"]
        }
    ]
    valid_news_data = []
    for item in news_data:
        if is_image_valid(item["image_url"]):
            valid_news_data.append(item)
    return valid_news_data

def create_daily_news_posts():
    today = datetime.date.today().isoformat()
    category = "AI 최신뉴스"
    news_data_list = generate_news_data()
    if not news_data_list:
        print("No news data to post.")
        return False
    data_path = os.path.join(BASE_DIR, "config/posts_data.json")
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            posts_data = json.load(f)
    else:
        posts_data = []
    newly_added = 0
    for item in news_data_list:
        title = item["title"]
        posts_data = [p for p in posts_data if not (p['title'] == title and p['date'] == today)]
        posts_data.insert(0, {
            'title': title,
            'date': today,
            'category': category,
            'summary': item["summary"],
            'image_url': item["image_url"],
            'content': item["content"],
            'keywords': item["keywords"]
        })
        newly_added += 1
    if newly_added > 0:
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(posts_data, f, indent=4, ensure_ascii=False)
        build_script = os.path.join(BASE_DIR, "build_engine.py")
        if os.path.exists(build_script):
            subprocess.run([sys.executable, build_script], check=True)
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", f"Daily AI News Update {today}"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("Git push completed.")
        except Exception as e:
            print(f"Git error: {e}")
        return True
    return False

if __name__ == "__main__":
    create_daily_news_posts()
