import streamlit as st

# 1. 웹페이지 기본 설정
st.set_page_config(
    page_title="청소년 디지털 건강 처방전",
    page_icon="🩺",
    layout="wide"
)

# 🎨 디자인 CSS
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
}

</style>
""", unsafe_allow_html=True)

# --- 🧠 현재 화면 상태 기억하기 ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 홈화면"

# 페이지 이동 함수
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

        elif 2.5 <= total_y < 5.0:
            st.warning("⚠️ [주의] 잘못된 디지털 기기 사용 습관이 감지되었습니다.")

        else:
            st.success("✅ [정상] 건강한 생활 습관을 유지하고 있습니다.")
