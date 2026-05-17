import streamlit as st

# 1. 웹페이지 기본 설정
st.set_page_config(
    page_title="청소년 디지털 건강 처방전",
    page_icon="🩺",
    layout="wide"
)

# 🎨 디자인 CSS (서은님이 만든 예쁜 디자인 유지)
st.markdown("""
<style>
/* 전체 배경 */
.stApp{
    background-color:#F5F9FF;
}

/* 카드 디자인 */
.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:15px;
}

/* 버튼 디자인 */
.stButton > button{
    background:linear-gradient(90deg,#6EA8FF,#3A7BFF);
    color:white;
    border:none;
    border-radius:12px;
    height:3em;
    font-weight:bold;
}

/* 결과 점수 박스 */
.score-box{
    background:#EEF4FF;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    color:#3A7BFF;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# --- 🧠 현재 화면 상태 기억하기 ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 홈화면"

# 페이지 이동 함수 (안전한 on_click 방식)
def move_page(page_name):
    st.session_state.current_page = page_name

# --- 📋 왼쪽 사이드바 ---
with st.sidebar:
    st.header("📋 시스템 메뉴")

    st.button(
        "🏠 처음으로 (홈화면 이동)",
        use_container_width=True,
        key="sidebar_home",
        on_click=move_page,
        args=("🏠 홈화면",)
    )

    st.markdown("---")

    st.write("**💡 시스템 안내**")
    st.caption("본 프로그램은 가중치 인공신경망 원리를 활용한 청소년 디지털 건강 진단 서비스입니다.")
    st.caption("제작자: 백신고 1학년 10반 이소은")

# --- 🏠 홈화면 ---
if st.session_state.current_page == "🏠 홈화면":

    st.title("🩺 청소년 디지털 건강 처방전")
    st.write("학업 스트레스와 전자기기 사용으로 지친 나의 건강 상태를 체크하고 맞춤형 디지털 처방전을 받아보세요!")
    st.info("💡 아래에서 원하는 진단의 버튼을 눌러주세요!")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card'>
        <h3>💻 VDT 증후군</h3>
        <p><b>거북목 · 일자목 · 손목 통증</b></p>
        <p>스마트폰과 PC 사용 습관으로 인한 자세 위험도를 분석합니다.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "👉 VDT 진단 시작",
            key="btn_vdt",
            use_container_width=True,
            on_click=move_page,
            args=("💻 VDT 증후군",)
        )

    with col2:
        st.markdown("""
        <div class='card'>
        <h3>😴 수면위상지연</h3>
        <p><b>만성 피로 · 블루라이트 장애</b></p>
        <p>청소년 수면 패턴과 피로도를 분석합니다.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "👉 수면 진단 시작",
            key="btn_sleep",
            use_container_width=True,
            on_click=move_page,
            args=("😴 수면위상지연 증후군",)
        )

    with col3:
        st.markdown("""
        <div class='card'>
        <h3>🧠 학업 스트레스</h3>
        <p><b>성적 압박 · 가면 우울증</b></p>
        <p>학업과 대인관계 스트레스를 AI가 분석합니다.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "👉 심리 진단 시작",
            key="btn_stress",
            use_container_width=True,
            on_click=move_page,
            args=("🧠 스트레스 및 가면 우울",)
        )

    st.markdown("---")

# --- 💻 VDT 증후군 ---
elif st.session_state.current_page == "💻 VDT 증후군":

    st.title("💻 거북목 및 VDT 증후군 AI 예측 모델")
    st.write("각 증상별 의학적 가중치(Weight)를 반영하여 위험도를 정밀 분석합니다.")
    st.markdown("---")

    q1_ans = st.radio(
        "질문 1. 하루 평균 스마트폰/PC 사용 시간은?",
        ["3시간 미만", "3~6시간", "6시간 이상"],
        key="vdt1"
    )

    q2_ans = st.radio(
        "질문 2. 스마트폰을 볼 때 고개를 심하게 숙이는 편인가요?",
        ["안 그런다", "가끔 그렇다", "자주 그렇다"],
        key="vdt2"
    )

    q3_ans = st.radio(
        "질문 3. 현재 목이나 어깨에 통증이 있나요?",
        ["통증 없음", "뻐근함", "심한 통증"],
        key="vdt3"
    )

    x1 = ["3시간 미만", "3~6시간", "6시간 이상"].index(q1_ans)
    x2 = ["안 그런다", "가끔 그렇다", "자주 그렇다"].index(q2_ans)
    x3 = ["통증 없음", "뻐근함", "심한 통증"].index(q3_ans)

    if st.button("VDT 증후군 AI 정밀 진단", use_container_width=True):

        w1, w2, w3 = 0.8, 1.5, 2.0
        total_y = (w1 * x1) + (w2 * x2) + (w3 * x3)

        st.markdown("---")
        st.write("## 📊 AI 정밀 분석 및 디지털 처방전")

        st.markdown(f"""
        <div class='score-box'>
        📊 종합 위험도 지수<br>
        {total_y:.2f} / 8.60
        </div>
        """, unsafe_allow_html=True)

        if total_y >= 5.0:
            st.error("🚨 [위험] VDT 증후군 및 거북목 고위험군 단계입니다.")
            st.markdown("""
            ### 🩺 의학 행동 처방전
            * **💻 화면 높이기:** 모니터 화면을 눈높이에 맞추세요.
            * **⏰ 5010 법칙:** 50분 공부 후 10분 휴식하세요.
            * **🧘 맥켄지 운동:** 고개를 뒤로 젖히는 스트레칭을 해주세요.
            """)
        elif 2.5 <= total_y < 5.0:
            st.warning("⚠️ [주의] 잘못된 디지털 기기 사용 습관이 감지되었습니다.")
            st.markdown("""
            ### 🩺 의학 행동 처방전
            * **📱 스마트폰 올리기:** 고개를 숙이지 말고 눈앞으로 들어 올리세요.
            * **📖 독서대 필수:** 인강이나 책을 볼 때는 반드시 독서대를 쓰세요.
            """)
        else:
            st.success("✅ [정상] 건강한 생활 습관을 유지하고 있습니다.")
            st.markdown("""
            ### 🩺 의학 관리 처방전
            * **🛏️ 경추 베개 사용:** 자는 동안 목 곡선이 유지되는 적절한 높이의 베개를 쓰세요.
            * **🏃 꾸준한 스트레칭:** 척추 주변 근육 강화를 위해 주 2회 스트레칭을 하세요.
            """)

        # 진단 버튼 클릭 시에만 처방전 하단에 내비게이션 버튼 표시
        st.markdown("---")
        st.write("### 🧭 다음 단계 선택")
        next_col1, next_col2, next_col3 = st.columns(3)
        with next_col1:
            st.button("😴 수면 장애 검사해보기", use_container_width=True, key="go_sleep_from_vdt", on_click=move_page, args=("😴 수면위상지연 증후군",))
        with next_col2:
            st.button("🧠 스트레스 검사해보기", use_container_width=True, key="go_stress_from_vdt", on_click=move_page, args=("🧠 스트레스 및 가면 우울",))
        with next_col3:
            st.button("🏠 홈 화면으로 돌아가기", use_container_width=True, key="go_home_from_vdt", on_click=move_page, args=("🏠 홈화면",))

# --- 😴 수면위상지연 증후군 ---
elif st.session_state.current_page == "😴 수면위상지연 증후군":

    st.title("😴 청소년 수면 장애 및 만성피로 AI 예측 모델")
    st.write("청소년기 불규칙한 블루라이트 노출과 호르몬 변화를 고려하여 수면 건강을 분석합니다.")
    st.markdown("---")

    q4_ans = st.radio("질문 1. 평소 밤 11시 이후에도 스마트폰/태블릿을 보나요?", ["거의 안 본다", "주 2~3회 본다", "매일 본다"], key="sleep1")
    q5_ans = st.radio("질문 2. 주말에 평일보다 2시간 이상 몰아서 잠을 자나요?", ["안 그런다", "가끔 그렇다", "항상 그렇다"], key="sleep2")
    q6_ans = st.radio("질문 3. 아침에 기상할 때 두통이나 극심한 피로감을 느끼나요?", ["전혀 없다", "가끔 느낀다", "매일 느낀다"], key="sleep3")

    x4 = ["거의 안 본다", "주 2~3회 본다", "매일 본다"].index(q4_ans)
    x5 = ["안 그런다", "가끔 그렇다", "항상 그렇다"].index(q5_ans)
    x6 = ["전혀 없다", "가끔 느낀다", "매일 느낀다"].index(q6_ans)

    if st.button("수면 상태 AI 정밀 진단", use_container_width=True):

        w4, w5, w6 = 1.8, 1.0, 1.5
        total_y = (w4 * x4) + (w5 * x5) + (w6 * x6)

        st.markdown("---")
        st.write("## 📊 AI 정밀 분석 및 디지털 처방전")

        st.markdown(f"""
        <div class='score-box'>
        📊 종합 위험도 지수<br>
        {total_y:.2f} / 8.60
        </div>
        """, unsafe_allow_html=True)

        if total_y >= 5.0:
            st.error("🚨 [위험] 수면위상지연 증후군 및 수면 장애 고위험군 단계입니다.")
            st.markdown("""
            ### 🩺 의학 행동 처방전
            * **🚫 취침 전 오프:** 취침 1시간 전 스마트폰을 완전히 차단하세요.
            * **☀️ 햇빛 샤워:** 기상 후 5분간 햇빛을 쬐어 수면 주기를 맞추세요.
            """)
        elif 2.5 <= total_y < 5.0:
            st.warning("⚠️ [주의] 수면 패턴의 불균형으로 인해 만성 피로가 유발되고 있습니다.")
            st.markdown("""
            ### 🩺 의학 행동 처방전
            * **🛀 온수 샤워:** 취침 1~2시간 전 따뜻한 물로 샤워하세요.
            * **☕ 카페인 금지:** 오후 2시 이후 고카페인 음료를 금지하세요.
            """)
        else:
            st.success("✅ [정상] 생체 리듬이 안정적이며 매우 건강한 수면 패턴을 유지하고 있습니다.")
            st.markdown("""
            ### 🩺 의학 관리 처방전
            * **🛏️ 쾌적한 환경:** 침실 온도를 서늘하게 유지하고 빛을 완전히 차단하세요.
            * **🏃 낮 시간 활동:** 낮 동안 30분씩 가벼운 운동을 하면 숙면에 도움이 됩니다.
            """)

        st.markdown("---")
        st.write("### 🧭 다음 단계 선택")
        next_col1, next_col2, next_col3 = st.columns(3)
        with next_col1:
            st.button("💻 VDT 증후군 검사해보기", use_container_width=True, key="go_vdt_from_sleep", on_click=move_page, args=("💻 VDT 증후군",))
        with next_col2:
            st.button("🧠 스트레스 검사해보기", use_container_width=True, key="go_stress_from_sleep", on_click=move_page, args=("🧠 스트레스 및 가면 우울",))
        with next_col3:
            st.button("🏠 홈 화면으로 돌아가기", use_container_width=True, key="go_home_from_sleep", on_click=move_page, args=("🏠 홈화면",))

# --- 🧠 스트레스 및 가면 우울 ---
elif st.session_state.current_page == "🧠 스트레스 및 가면 우울":

    st.title("🧠 학업 스트레스 및 가면 우울증 AI 예측 모델")
    st.write("청소년기 대인관계 및 성적 압박으로 인한 스트레스 수치를 정밀 진단합니다.")
    st.markdown("---")

    q7_ans = st.radio("질문 1. 최근 학업이나 시험 성적으로 인해 심한 불안감이나 압박감을 느끼나요?", ["전혀 없다", "보통이다", "매우 심하다"], key="stress1")
    q8_ans = st.radio("질문 2. 이유 없이 갑자기 짜증이 나거나 감정 조절이 어렵다고 느낀 적이 있나요?", ["전혀 없다", "가끔 그렇다", "자주 그렇다"], key="stress2")
    q9_ans = st.radio("질문 3. 스트레스로 인해 최근 두통, 소화불량 등 신체적 증상이 나타나나요?", ["전혀 없다", "가끔 그렇다", "자주 그렇다"], key="stress3")

    x7 = ["전혀 없다", "보통이다", "매우 심하다"].index(q7_ans)
    x8 = ["전혀 없다", "가끔 그렇다", "자주 그렇다"].index(q8_ans)
    x9 = ["전혀 없다", "가끔 그렇다", "자주 그렇다"].index(q9_ans)

    if st.button("정신 건강 AI 정밀 진단", use_container_width=True):

        w7, w8, w9 = 1.2, 1.3, 1.8
        total_y = (w7 * x7) + (w8 * x8) + (w9 * x9)

        st.markdown("---")
        st.write("## 📊 AI 정밀 분석 및 디지털 처방전")

        st.markdown(f"""
        <div class='score-box'>
        📊 종합 위험도 지수<br>
        {total_y:.2f} / 8.60
        </div>
        """, unsafe_allow_html=True)

        if total_y >= 5.0:
            st.error("🚨 [위험] 심리적 스트레스 과부하 및 가면 우울증 고위험군 단계입니다.")
            st.markdown("""
            ### 🩺 심리 행동 처방전
            * **🏫 위클래스 방문:** 학교 상담실을 찾아 마음을 편하게 털어놓으세요.
            * **🌬️ 4-7-8 호흡법:** 불안할 때 4초 흡입, 7초 멈춤, 8초 내쉬는 호흡을 하세요.
            """)
        elif 2.5 <= total_y < 5.0:
            st.warning("⚠️ [주의] 지속적인 압박감으로 인해 가벼운 무기력증이나 번아웃 징후가 보입니다.")
            st.markdown("""
            ### 🩺 심리 행동 처방전
            * **🎨 감정 일기 쓰기:** 답답했던 감정을 마음껏 공책에 적어 털어내 보세요.
            * **🧍 나만의 루틴:** 일주일에 한 번은 내가 좋아하는 취미에 몰두하는 시간을 가지세요.
            """)
        else:
            st.success("✅ [정상] 심리적 회복탄력성이 높으며 아주 건강한 정신 건강 상태를 유지하고 있습니다.")
            st.markdown("""
            ### 🩺 심리 관리 처방전
            * **🙏 감사 명상:** 긍정적인 생각 회로 유지를 위해 매일 밤 가벼운 명상을 하세요.
            * **🤝 원활한 소통:** 친구나 가족들과 깊은 이야기를 나누며 끈끈한 유대를 유지하세요.
            """)

        st.markdown("---")
        st.write("### 🧭 다음 단계 선택")
        next_col1, next_col2, next_col3 = st.columns(3)
        with next_col1:
            st.button("💻 VDT 증후군 검사해보기", use_container_width=True, key="go_vdt_from_stress", on_click=move_page, args=("💻 VDT 증후군",))
        with next_col2:
            st.button("😴 수면 장애 검사해보기", use_container_width=True, key="go_sleep_from_stress", on_click=move_page, args=("😴 수면위상지연 증후군",))
        with next_col3:
            st.button("🏠 홈 화면으로 돌아가기", use_container_width=True, key="go_home_from_stress", on_click=move_page, args=("🏠 홈화면",))
