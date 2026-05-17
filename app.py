import streamlit as st

# 기본 설정
st.set_page_config(
    page_title="청소년 디지털 건강 처방전",
    page_icon="🩺",
    layout="wide"
)

# 🎨 디자인 추가
st.markdown("""
<style>

.stApp{
    background-color:#F5F9FF;
}

.main-title{
    text-align:center;
    color:#3A7BFF;
    font-size:48px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.stButton>button{
    background:linear-gradient(90deg,#6EA8FF,#3A7BFF);
    color:white;
    border:none;
    border-radius:12px;
    height:3em;
    font-weight:bold;
}

section[data-testid="stSidebar"]{
    background-color:#EAF2FF;
}

.score-box{
    background:#EEF4FF;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    color:#3A7BFF;
}

</style>
""", unsafe_allow_html=True)

# 상태 저장
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 홈화면"

def move_page(page_name):
    st.session_state.current_page = page_name

# 사이드바
with st.sidebar:
    st.header("📋 시스템 메뉴")

    st.button(
        "🏠 처음으로",
        use_container_width=True,
        key="sidebar_home",
        on_click=move_page,
        args=("🏠 홈화면",)
    )

    st.markdown("---")

    st.write("**💡 시스템 안내**")
    st.caption("AI 기반 청소년 디지털 건강 진단 서비스")
    st.caption("제작자: 백신고 1학년 10반 이소은")

# 홈화면
if st.session_state.current_page == "🏠 홈화면":

    st.markdown("""
    <div class='main-title'>
    🩺 Teen Digital Health Care
    </div>

    <div class='sub-title'>
    AI 기반 청소년 건강 분석 및 디지털 처방 시스템
    </div>
    """, unsafe_allow_html=True)

    st.info("💡 원하는 카테고리의 진단 시작 버튼을 눌러주세요!")

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
        <p><b>성적 압박 · 번아웃</b></p>
        <p>청소년 심리 스트레스 상태를 분석합니다.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "👉 심리 진단 시작",
            key="btn_stress",
            use_container_width=True,
            on_click=move_page,
            args=("🧠 스트레스 및 가면 우울",)
        )

# 💻 VDT 화면
elif st.session_state.current_page == "💻 VDT 증후군":

    st.title("💻 거북목 및 VDT 증후군 AI 예측 모델")

    q1_ans = st.radio(
        "질문 1. 하루 평균 스마트폰/PC 사용 시간은?",
        ["3시간 미만", "3~6시간", "6시간 이상"]
    )

    q2_ans = st.radio(
        "질문 2. 현재 목이나 어깨에 통증이 있나요?",
        ["통증 없음", "뻐근함", "심한 통증"]
    )

    x1 = ["3시간 미만", "3~6시간", "6시간 이상"].index(q1_ans)
    x2 = ["통증 없음", "뻐근함", "심한 통증"].index(q2_ans)

    if st.button("VDT 증후군 AI 정밀 진단", use_container_width=True):

        total_y = (1.2 * x1) + (2.0 * x2)

        st.markdown(f"""
        <div class='score-box'>
        📊 종합 위험도 지수<br>
        {total_y:.2f} / 6.40
        </div>
        """, unsafe_allow_html=True)

        if total_y >= 4:
            st.error("🚨 VDT 증후군 고위험군 단계입니다.")
            st.markdown("""
            ### 🩺 디지털 처방전
            * 💻 화면 높이기
            * 📱 스마트폰 눈높이 유지
            * ⏰ 50분 공부 후 10분 휴식
            """)

        elif total_y >= 2:
            st.warning("⚠️ 자세 교정이 필요합니다.")

        else:
            st.success("✅ 건강한 생활 습관을 유지하고 있습니다.")

        st.markdown("---")

        st.button(
            "🏠 홈 화면으로 돌아가기",
            use_container_width=True,
            key="go_home",
            on_click=move_page,
            args=("🏠 홈화면",)
        )
