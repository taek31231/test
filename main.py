import streamlit as st

# MBTI별 추천 직업 데이터 (16개 MBTI 포함)
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
    "ISTJ": {
        "jobs": ["회계사", "공무원", "법률 보조원"],
        "reason": "ISTJ는 세부사항을 정확히 다루고, 실용적인 문제 해결에 능합니다. 체계적이고 안정적인 환경을 선호합니다.",
        "skills": ["조직 능력", "책임감", "세심한 주의"],
        "activities": ["계획적인 업무 관리", "규칙적인 일정 관리", "서류 작성"]
    },
    "ISFJ": {
        "jobs": ["간호사", "사회복지사", "사서"],
        "reason": "ISFJ는 타인을 돕는 것에 큰 가치를 두고, 실용적이고 신뢰할 수 있는 성향을 가집니다.",
        "skills": ["세심함", "봉사정신", "협동심"],
        "activities": ["봉사 활동", "어르신 돌봄", "일상적인 관리"]
    },
    "ESTJ": {
        "jobs": ["군인", "현장 관리자", "행정 담당자"],
        "reason": "ESTJ는 효율적이고 체계적인 작업 방식을 선호하며, 강한 리더십과 실행 능력을 가지고 있습니다.",
        "skills": ["리더십", "실행력", "체계적인 관리"],
        "activities": ["팀 리딩", "업무 프로세스 최적화", "행정 관리"]
    },
    "ESFJ": {
        "jobs": ["교사", "의료 서비스 직원", "이벤트 플래너"],
        "reason": "ESFJ는 사람들과의 관계에서 중요한 만족을 느끼며, 세심하고 친절한 성향으로 다른 사람들을 돕고자 합니다.",
        "skills": ["사교성", "협력", "조직력"],
        "activities": ["친구 모임 주선", "이벤트 기획", "교실 관리"]
    },
    "ISTP": {
        "jobs": ["기계공", "파일럿", "컴퓨터 기술자"],
        "reason": "ISTP는 실제적인 문제 해결에 강점을 가지고 있으며, 손기술과 현실적인 사고 방식을 선호합니다.",
        "skills": ["기술적 능력", "문제 해결", "분석적 사고"],
        "activities": ["기계 작업", "스포츠", "모험적인 활동"]
    },
    "ISFP": {
        "jobs": ["사진작가", "조각가", "물리치료사"],
        "reason": "ISFP는 예술적이고 창의적인 성향을 가지고 있으며, 감각적이고 직관적인 작업에서 큰 만족을 얻습니다.",
        "skills": ["창의성", "감각적인 경험", "감정 표현"],
        "activities": ["예술 창작", "자연과의 교감", "감각적 체험"]
    },
    "ESTP": {
        "jobs": ["영업사원", "소방관", "스포츠 트레이너"],
        "reason": "ESTP는 빠르게 상황을 파악하고, 즉각적인 문제 해결에 능숙한 활동적인 성격을 가지고 있습니다.",
        "skills": ["적응력", "즉흥적인 사고", "행동력"],
        "activities": ["운동", "모험적인 활동", "영업 현장"]
    },
    "ESFP": {
        "jobs": ["배우", "패션 스타일리스트", "여행 가이드"],
        "reason": "ESFP는 사람들과의 상호작용에서 큰 만족을 느끼며, 창의적이고 감각적인 활동을 좋아합니다.",
        "skills": ["사교성", "창의력", "상상력"],
        "activities": ["연기", "패션 디자인", "여행과 탐험"]
    }
}

# MBTI별 추천 직업 데이터 (16개 MBTI 포함)
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
    # (다른 MBTI 유형도 동일하게 작성)
}

# 퀴즈 질문
questions = [
    ("사람들과 함께 있는 것이 편한가요?", ["매우 그렇다", "그렇다", "그렇지 않다", "전혀 그렇지 않다"]),  # E/I
    ("새로운 아이디어를 제시하는 것을 좋아하나요?", ["매우 그렇다", "그렇다", "그렇지 않다", "전혀 그렇지 않다"]),  # S/N
    ("일을 계획하고 실행하는 것이 중요한가요?", ["매우 그렇다", "그렇다", "그렇지 않다", "전혀 그렇지 않다"]),  # J/P
    ("기획보다는 즉흥적으로 해결하는 것이 더 편한가요?", ["매우 그렇다", "그렇다", "그렇지 않다", "전혀 그렇지 않다"]),  # P/J
    ("구체적이고 세부적인 일을 하는 것을 좋아하나요?", ["매우 그렇다", "그렇다", "그렇지 않다", "전혀 그렇지 않다"])  # S/N
]

# 점수 계산
mbti_scores = {
    "E": 0, "I": 0,
    "S": 0, "N": 0,
    "T": 0, "F": 0,
    "J": 0, "P": 0
}

# 퀴즈 시작
st.set_page_config(page_title="MBTI 직업 추천기", layout="centered")
st.title("🧭 MBTI 성향 퀴즈")
st.write("아래 5개의 질문에 답해보세요! 각 답변을 바탕으로 당신의 MBTI 유형을 알아볼 수 있습니다.")

# 퀴즈 진행
for i, (question, options) in enumerate(questions):
    st.subheader(f"{i + 1}. {question}")
    answer = st.radio("선택하세요:", options, key=f"q{i}")
    
    # 첫 번째 질문 - E/I 성향
    if i == 0:
        if answer == "매우 그렇다":
            mbti_scores["E"] += 2
        elif answer == "그렇다":
            mbti_scores["E"] += 1
        elif answer == "그렇지 않다":
            mbti_scores["I"] += 1
        elif answer == "전혀 그렇지 않다":
            mbti_scores["I"] += 2
    # 두 번째 질문 - S/N 성향
    elif i == 1:
        if answer == "매우 그렇다":
            mbti_scores["N"] += 2
        elif answer == "그렇다":
            mbti_scores["N"] += 1
        elif answer == "그렇지 않다":
            mbti_scores["S"] += 1
        elif answer == "전혀 그렇지 않다":
            mbti_scores["S"] += 2
    # 세 번째 질문 - J/P 성향
    elif i == 2:
        if answer == "매우 그렇다":
            mbti_scores["J"] += 2
        elif answer == "그렇다":
            mbti_scores["J"] += 1
        elif answer == "그렇지 않다":
            mbti_scores["P"] += 1
        elif answer == "전혀 그렇지 않다":
            mbti_scores["P"] += 2
    # 네 번째 질문 - P/J 성향
    elif i == 3:
        if answer == "매우 그렇다":
            mbti_scores["P"] += 2
        elif answer == "그렇다":
            mbti_scores["P"] += 1
        elif answer == "그렇지 않다":
            mbti_scores["J"] += 1
        elif answer == "전혀 그렇지 않다":
            mbti_scores["J"] += 2
    # 다섯 번째 질문 - S/N 성향
    elif i == 4:
        if answer == "매우 그렇다":
            mbti_scores["S"] += 2
        elif answer == "그렇다":
            mbti_scores["S"] += 1
        elif answer == "그렇지 않다":
            mbti_scores["N"] += 1
        elif answer == "전혀 그렇지 않다":
            mbti_scores["N"] += 2

# 결과 출력
if sum(mbti_scores.values()) > 0:
    # 각 성향에 맞는 MBTI 유형 계산
    personality = ""
    
    # E/I
    if mbti_scores["E"] > mbti_scores["I"]:
        personality += "E"
    else:
        personality += "I"
    
    # S/N
    if mbti_scores["S"] > mbti_scores["N"]:
        personality += "S"
    else:
        personality += "N"
    
    # T/F
    if mbti_scores["T"] > mbti_scores["F"]:
        personality += "T"
    else:
        personality += "F"
    
    # J/P
    if mbti_scores["J"] > mbti_scores["P"]:
        personality += "J"
    else:
        personality += "P"
    
    # MBTI 유형 결과
    st.write(f"**당신의 MBTI 성향은**: {personality}")
    
    selected_mbti = personality
    st.subheader(f"{selected_mbti} 유형에게 추천하는 직업:")
    
    # 직업 추천
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
