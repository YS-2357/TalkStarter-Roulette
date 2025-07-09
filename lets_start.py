import streamlit as st
import random
import time

st.title("🎯 대화 주제 룰렛 | TalkStarter Roulette")

categories = ["여행", "음식", "취미", "혈액형", "MBTI"]
selected_main = st.button("돌려서 주제 선택하기!")

if selected_main:
    with st.spinner("주제 고르는 중..."):
        time.sleep(3)
    main_topic = random.choice(categories)
    st.success(f"🎉 선택된 주제: {main_topic}")

subtopics = {
    "여행": ["일본", "태국", "유럽", "국내 기차 여행", "혼자 여행 vs 단체 여행"],
    "요리": ["한식", "양식", "도시락 싸기", "편의점 레시피"],
    "취미": ["게임", "독서", "등산", "보드게임", "프라모델"],
    "혈액형": ["A형", "B형", "O형", "AB형"],
    "MBTI": ["INTJ", "INFP", "ENFP", "ESTJ", "ISFJ", "ENTP", "ISTP", "ESFJ", "ISTJ", "ENTJ", "ENFJ", "ISFP", "ESFP", "INFJ", "ESTP", "INTP"]
}

if 'main_topic' in locals():
    chosen_sub = random.choice(subtopics[main_topic])
    st.info(f"🧩 세부 주제: {chosen_sub}")


tmi = {
    "여행": "✈️ 제작자는 일본, 태국, 중국, 미국, 홍콩 등을 여행했다.",
    "요리": "🍜 제작자는 라면을 순정으로 조리하는 걸 좋아한다.",
    "취미": "🎮 제작자는 하루에 한 번씩 웹소설을 읽는다.",
    "혈액형": "🧬 제작자는 O형이다. 남들이 잘 맞는다고 한다.",
    "MBTI": "🧠 제작자는 ESFP이며, 다른 사람과 대화하는 걸 겁내지않는다."
}

if 'main_topic' in locals():
    st.markdown("---")
    st.caption(tmi[main_topic])
