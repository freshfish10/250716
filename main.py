import streamlit as st

# -----------------------
# 데이터 정의
# -----------------------
mbti_entrepreneurs = {
    "INTJ": ["일론 머스크 (Tesla)", "리드 헤이스팅스 (Netflix)", "제프 베조스 (Amazon)"],
    "INTP": ["래리 페이지 (Google)", "마크 저커버그 (Facebook)", "브라이언 체스키 (Airbnb)"],
    "ENTJ": ["스티브 잡스 (Apple)", "샤릴 샌드버그 (Meta)", "잭 웰치 (GE)"],
    "ENTP": ["리처드 브랜슨 (Virgin)", "토니 셰이 (Zappos)", "벤 호로위츠 (Andreessen Horowitz)"],
    "INFJ": ["요나스 사크 (백신 개발자)", "피에르 오미디야르 (eBay)", "오프라 윈프리 (OWN Network)"],
    "INFP": ["J.K. 롤링 (해리포터 작가)", "찰스 슐츠 (스누피 창작자)", "비욘세 (아티스트 & 사업가)"],
    "ENFJ": ["버락 오바마 (전 미국 대통령)", "벤자민 프랭클린 (발명가)", "데이비드 켈리 (IDEO 창립자)"],
    "ENFP": ["월트 디즈니 (Disney)", "사라 블레이크리 (Spanx)", "로빈 윌리엄스 (배우 & 크리에이터)"],
    "ISTJ": ["워렌 버핏 (Berkshire Hathaway)", "잉그바르 캄프라드 (IKEA)", "조지 워싱턴 (초대 대통령)"],
    "ISFJ": ["샘 월튼 (Walmart)", "아그네스 곤자 (마더 테레사)", "로사 파크스 (시민운동가)"],
    "ESTJ": ["마사 스튜어트 (Martha Stewart)", "존 록펠러 (Standard Oil)", "프랭크 시나트라 (가수 & 사업가)"],
    "ESFJ": ["테일러 스위프트 (가수 & 사업가)", "제니퍼 로페즈 (JLo)", "휴 잭맨 (배우 & 기획자)"],
    "ISTP": ["스티브 워즈니악 (Apple)", "엘론 머스크 (Tesla)", "해리 후디니 (마술사 & 사업가)"],
    "ISFP": ["밥 딜런 (가수)", "마이클 잭슨 (아티스트)", "브루스 리 (무술가 & 배우)"],
    "ESTP": ["도널드 트럼프 (사업가)", "어니스트 헤밍웨이 (작가)", "마돈나 (가수 & 사업가)"],
    "ESFP": ["제이미 올리버 (셰프)", "리처드 시몬스 (피트니스 강사)", "밀리 바비 브라운 (배우 & 창업가)"]
}

# -----------------------
# UI 구성
# -----------------------
st.set_page_config(page_title="MBTI 기업가 추천기", page_icon="💡")
st.title("💡 MBTI 기반 기업가 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 유명 기업가 3인을 추천해드려요!")

mbti_list = list(mbti_entrepreneurs.keys())
selected_mbti = st.selectbox("당신의 MBTI는?", sorted(mbti_list))

# -----------------------
# 결과 출력
# -----------------------
if selected_mbti:
    st.markdown("---")
    st.subheader(f"🧠 {selected_mbti} 유형에게 어울리는 기업가")
    for idx, name in enumerate(mbti_entrepreneurs[selected_mbti], start=1):
        st.markdown(f"**{idx}.** {name}")
    st.markdown("---")
    st.caption("🔎 단순 추천이므로 재미로 활용해 주세요 :)")
