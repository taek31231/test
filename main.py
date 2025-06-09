import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": {
        "jobs": ["데이터 과학자", "정책 분석가", "전략 컨설턴트"],
        "reason": "INTJ는 전략적 사고와 분석적 사고에 뛰어난 능력을 가지고 있어 복잡한 문제 해결과 미래 예측에 능합니다.",
        "skills": ["문제 해결 능력", "분석적 사고", "창의적 아이디어"],
        "activities": ["과학적 연구", "문제 해결 게임", "시뮬레이션"]
    },
    "INTP": {
        "jobs": ["연구원", "프로그래머", "이론물리학자"],
        "reason": "INTP는 논리적이고 분석적인 사고가 뛰어나 새로운 이론을 개발하거나 시스템을 설계하는 데 강점을 보입니다.",
        "skills": ["논리적 사고", "창의성", "추상적 사고"],
        "activities": ["코딩", "토론", "수학 문제 풀기"]
    },
    "ENTJ": {
        "jobs": ["경영 컨설턴트", "CEO", "프로젝트 매니저"],
        "reason": "ENTJ는 리더십과 조직 관리 능력이 뛰어나며, 큰 그림을 보는 능력과 팀을 이끄는 능력이 우수합니다.",
        "skills": ["리더십", "전략적 사고", "의사소통 능력"],
        "activities": ["팀 리더 역할", "경영 관련 책 읽기", "기획 및 실행"]
    },
    "ENTP": {
        "jobs": ["벤처 창업가", "기획자", "마케팅 디렉터"],
        "reason": "ENTP는 창의적이고 혁신적인 아이디어를 떠올리는 데 능숙하며, 새로운 기회를 창출하는 데 탁월한 능력을 발휘합니다.",
        "skills": ["창의력", "적응력", "문제 해결 능력"],
        "activities": ["스타트업 관련 책 읽기", "문제 해결 게임", "아이디어 브레인스토밍"]
    },
    "INFJ": {
        "jobs": ["상담가", "작가", "심리학자"],
        "reason": "INFJ는 타인의 감정을 잘 이해하고, 깊은 공감 능력을 바탕으로 사람들에게 도움을 주고 싶은 성향을 가지고 있습니다.",
        "skills": ["공감 능력", "문제 해결 능력", "인간 심리 이해"],
        "activities": ["심리학 관련 공부", "창의적 글쓰기", "명상"]
    },
    "INFP": {
        "jobs": ["작가", "교사", "디자이너"],
        "reason": "INFP는 이상주의적이고 창의적인 성향을 가지고 있으며, 세상을 더 나은 방향으로 변화시키는 데 큰 가치를 둡니다.",
        "skills": ["창의성", "상상력", "공감 능력"],
        "activities": ["문학 창작", "자원봉사", "자기 표현 활동"]
    },
    "ENFJ": {
        "jobs": ["교육 컨설턴트", "리더십 코치", "홍보 담당자"],
        "reason": "ENFJ는 사람들과의 관계에서 큰 만족을 얻으며, 타인을 격려하고 이끄는 능력이 뛰어납니다.",
        "skills": ["리더십", "공감 능력", "의사소통 능력"],
        "activities": ["리더십 훈련", "공공연한 발표", "사회적 프로젝트 참여"]
    },
    "ENFP": {
        "jobs": ["광고 기획자", "방송 작가", "공연 예술가"],
        "reason": "ENFP는 창의력과 열정으로 가득 차 있으며, 다양한 분야에서 새로운 아이디어를 제시하고 사람들에게 영감을 주는 것을 즐깁니다.",
        "skills": ["창의력", "열정", "상상력"],
        "activities": ["공연 기획", "디자인 작업", "글쓰기"]
    },
    # 나머지 MBTI 유형에 대해서도 같은 형식으로 추가합니다.
}

# Streamlit 앱 시작
st.set_page_config(page_title="MBTI 직업 추천기", layout="centered")
st.title("🧭 MBTI 직업 추천기")

st.write("당신의 MBTI 유형을 선택하면, 그에 맞는 직업과 추천 이유를 알려드릴게요!")

# 사용자 입력 받기
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 유형에게 추천하는 직업:")
    
    # 추천 직업 목록
    for job in mbti_jobs[selected_mbti]["jobs"]:
        st.markdown(f"- {job}")
    
    # 추천 이유
    st.subheader("📌 추천 이유")
    st.write(mbti_jobs[selected_mbti]["reason"])

    # 추천하는 스킬
    st.subheader("🔧 관련 스킬")
    for skill in mbti_jobs[selected_mbti]["skills"]:
        st.markdown(f"- {skill}")

    # 추천 활동
    st.subheader("🎯 추천 활동")
    for activity in mbti_jobs[selected_mbti]["activities"]:
        st.markdown(f"- {activity}")

st.markdown("---")
st.caption("© 2025 중고생 진로 탐색 도우미")
