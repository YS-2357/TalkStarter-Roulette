import streamlit as st
import random
import time

# 주제 정의
categories = ["여행", "요리", "취미", "혈액형", "MBTI", "영화/드라마", "반려동물", "음악", "패션", "기술/IT"]
subtopics = {
    "여행": [
        "일본 vs 한국", "국내 여행 vs 해외 여행", "혼자 여행 vs 단체 여행", "계획 여행 vs 즉흥 여행",
        "도시 여행 vs 자연 여행", "비행기 vs 기차", "패키지 vs 자유 여행",
        "호텔 vs 에어비앤비", "여름 휴가 vs 겨울 휴가", "유럽 vs 미주", "동남아 vs 일본"
    ],
    "요리": [
        "한식 vs 양식", "요리 vs 배달", "집밥 vs 외식", "맵게 vs 안 맵게", "설거지 vs 요리하기",
        "라면 끓이기 vs 비빔면 만들기",
        "고기 vs 해산물", "달콤한 맛 vs 짭짤한 맛", "아침 식사 vs 저녁 식사", "간편식 vs 정성 요리"
    ],
    "취미": [
        "혼자 하는 취미 vs 같이 하는 취미", "야외 활동 vs 실내 활동", "독서 vs 영화 감상", "운동 vs 음악 감상",
        "손으로 만드는 것 vs 머리로 하는 것", "실용적 취미 vs 재미 중심 취미",
        "게임 vs 스포츠", "사진 찍기 vs 그림 그리기", "배우는 취미 vs 즐기는 취미", "아침형 인간 취미 vs 저녁형 인간 취미"
    ],
    "혈액형": [
        "A형 vs B형 vs O형 vs AB형", "혈액형 믿는다 vs 안 믿는다", "혈액형별 성격 신뢰함? vs 안 함?",
        "혈액형 vs MBTI",
        "내 혈액형 vs 상대방 혈액형", "혈액형 궁합 믿는다 vs 안 믿는다"
    ],
    "MBTI": [
        "E vs I", "N vs S", "T vs F", "J vs P", "MBTI 믿는다 vs 안 믿는다", "MBTI 소개팅 참고한다 vs 안 한다",
        "내 MBTI vs 네 MBTI",
        "MBTI 과몰입 vs MBTI 불신", "MBTI 맹신 vs 재미로 본다", "MBTI 바꾸고 싶다 vs 아니다"
    ],
    "영화/드라마": [
        "영화 vs 드라마", "한국영화 vs 외국영화", "로맨스 vs 스릴러", "넷플릭스 vs 극장", "배우 중심 vs 감독 중심",
        "자막 vs 더빙",
        "코미디 vs 다큐멘터리", "개봉날 보기 vs 나중에 보기", "결말 미리 알기 vs 모른 채 보기", "시즌 몰아보기 vs 매주 보기"
    ],
    "반려동물": [
        "강아지 vs 고양이", "키워봤다 vs 안 키워봤다", "펫카페 좋다 vs 불편하다", "작은 동물 vs 큰 동물",
        "유기동물 입양한다 vs 고민된다",
        "산책 vs 집콕", "사료 vs 수제간식", "털 빠짐 감수 vs 깔끔한 환경", "고양이 집사 vs 강아지 집사"
    ],
    "음악": [
        "아이돌 음악 vs 인디 음악", "발라드 vs 댄스", "힙합 vs 락", "국내 가수 vs 해외 가수",
        "음악 감상 vs 라이브 공연", "멜론 vs 스포티파이", "노래방 vs 코인 노래방", "음악 추천 받기 vs 직접 찾기"
    ],
    "패션": [
        "편한 옷 vs 예쁜 옷", "유행 따르기 vs 개성 중시", "온라인 쇼핑 vs 오프라인 쇼핑", "명품 vs 보세",
        "밝은 색 옷 vs 어두운 색 옷", "운동화 vs 구두", "모자 vs 안경", "새 옷 vs 빈티지 옷"
    ],
    "기술/IT": [
        "아이폰 vs 갤럭시", "PC vs 노트북", "인공지능 vs 인간 지능", "데이터 절약 vs 무제한 요금제",
        "새로운 기술 습득 vs 익숙한 것 사용", "게임 콘솔 vs PC 게임", "스마트 워치 vs 일반 시계", "웹툰 vs 웹소설"
    ]
}


tmi = {
    "여행": "✈️ 제작자는 일본, 태국, 미국, 홍콩 등지를 여행했다.",
    "요리": "🍳 제작자는 설거지보다 요리를 더 잘한다.",
    "취미": "🎮 제작자는 매일 웹소설을 읽는다.",
    "혈액형": "🧬 제작자는 O형이다. 다들 잘 어울린다고 한다.",
    "MBTI": "🧠 제작자는 ESFP이며 사람 만나는 걸 겁내지 않는다.",
    "영화/드라마": "🎬 제작자는 '도깨비'를 5번 봤다.",
    "반려동물": "🐾 제작자는 강아지 두 마리를 키웠다.",
    "음악": "🎶 제작자는 장범준 음악을 좋아한다.",
    "패션": "👕 제작자는 편안한 복장을 선호한다.",
    "기술/IT": "💻 제작자는 갤럭시 유저이다."
}

# 세션 초기화
if 'main_topic' not in st.session_state:
    st.session_state.main_topic = None
if 'final_subtopic' not in st.session_state:
    st.session_state.final_subtopic = None
if 'visited_main' not in st.session_state:
    st.session_state.visited_main = []
if 'visited_sub' not in st.session_state:
    st.session_state.visited_sub = []

st.title("🎯 대화 주제 룰렛 | TalkStarter Roulette")

# 대주제 룰렛
main_placeholder = st.empty()
if st.session_state.main_topic is None:
    if st.button("👉 대주제 룰렛 돌리기"):
        # 방문하지 않은 대주제 목록
        available_main = [cat for cat in categories if cat not in st.session_state.visited_main]

        # 모두 방문했으면 초기화
        if not available_main:
            st.session_state.visited_main = []
            available_main = categories

        # 룰렛 애니메이션
        for _ in range(15):
            topic = random.choice(available_main)
            main_placeholder.markdown(f"### 🎡 {topic}")
            time.sleep(0.08)

        st.session_state.main_topic = topic
        st.session_state.visited_main.append(topic)
        st.session_state.visited_sub = []  # 소주제도 리셋
        main_placeholder.markdown(f"## 🎯 최종 대주제: **{topic}**")
else:
    main_placeholder.markdown(f"## 🎯 대주제: **{st.session_state.main_topic}**")
    if st.button("🔄 대주제 다시 고르기"):
        st.session_state.main_topic = None
        st.session_state.final_subtopic = None
        st.session_state.visited_sub = []

# 소주제 룰렛
if st.session_state.main_topic:
    sub_placeholder = st.empty()
    current_subtopics = subtopics[st.session_state.main_topic]
    available_sub = [s for s in current_subtopics if s not in st.session_state.visited_sub]

    if st.button("🎲 소주제 룰렛 돌리기"):
        # 모두 방문했으면 초기화
        if not available_sub:
            st.session_state.visited_sub = []
            available_sub = current_subtopics

        for _ in range(15):
            sub = random.choice(available_sub)
            sub_placeholder.markdown(f"#### 🌀 {sub}")
            time.sleep(0.05)

        st.session_state.final_subtopic = sub
        st.session_state.visited_sub.append(sub)
        sub_placeholder.markdown(f"### ✅ 최종 소주제: **{sub}**")

# TMI 출력
if st.session_state.main_topic:
    st.markdown("---")
    st.caption(tmi.get(st.session_state.main_topic, "제작자의 TMI 정보가 없습니다."))