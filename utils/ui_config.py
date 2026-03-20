import streamlit as st

def load_css():
    """앱 전반의 UI 스타일링(CSS)을 로드함"""
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* =========================
       [1] 기본 레이아웃
    ========================= */
    .stApp {
        background-color: #F8F9FA;
        font-family: 'Inter', sans-serif;
    }
    
    /* 메인 콘텐츠 영역 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* =========================
       [2] 사이드바 - Owlee 스타일 (화이트)
    ========================= */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #EAECF0 !important;
    }
    
    /* 사이드바 내 모든 텍스트 기본 컬러 */
    [data-testid="stSidebar"] * {
        color: #344054 !important;
    }
    
    /* 사이드바 제목만 더 굵게 */
    [data-testid="stSidebar"] h1 {
        color: #101828 !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }
    
    /* 사이드바 라벨 */
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stWidgetLabel p {
        color: #667085 !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
    }

    /* 사이드바 입력창 */
    [data-testid="stSidebar"] input, [data-testid="stSidebar"] textarea {
        color: #101828 !important;
        background-color: #F9FAFB !important;
        border: 1px solid #D0D5DD !important;
        border-radius: 8px !important;
    }
    
    /* =========================
       [3] 사이드바 Phase 버튼 - Owlee 스타일
    ========================= */
    [data-testid="stSidebar"] .stButton > button {
        width: 100% !important;
        background-color: transparent !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        margin-bottom: 2px !important;
        color: #344054 !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        text-align: left !important;
        transition: background-color 0.15s ease !important;
    }
    
    /* 버튼 내부 p 태그도 좌측 정렬 강제 */
    [data-testid="stSidebar"] .stButton > button p {
        text-align: left !important;
        margin: 0 !important;
        color: #344054 !important;
    }

    /* 호버 상태 */
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #F2F4F7 !important;
        color: #1D2939 !important;
    }

    /* 활성(Primary) 버튼 - 보라/파란색 강조 */
    [data-testid="stSidebar"] .stButton > button[kind="primary"],
    [data-testid*="stSidebar"] .stButton > button[type="primary"] {
        background-color: #edf2fb !important;
        color: #5465ff !important;
        font-weight: 700 !important;
        border-left: 5px solid #5465ff !important;
    }
    
    [data-testid="stSidebar"] .stButton > button[kind="primary"] p,
    [data-testid*="stSidebar"] .stButton > button[type="primary"] p {
        color: #5465ff !important;
    }
    
    /* 모델 로드 버튼 - 연한 회색 */
    [data-testid="stSidebar"] .stButton > button#btn_model_load,
    [data-testid="stSidebar"] button[aria-label="모델 로드"],
    [data-testid="stSidebar"] div[class*="stButton"] > button[kind="secondary"]:not([type="primary"]) {
        background-color: #E4E7EC !important;
        color: #344054 !important;
        border: 1px solid #D0D5DD !important;
        justify-content: center !important;
        font-weight: 500 !important;
    }

    /* =========================
       [5] 메인 화면 카드
    ========================= */
    div.stTextInput > div, div.stTextArea > div, div.stSelectbox > div {
        border-radius: 8px !important;
        border: 1px solid #D0D5DD !important;
    }
    
    /* 카드형 컨테이너 */
    div.stForm, [data-testid="stExpander"] {
        background: #FFFFFF !important;
        border-radius: 16px !important;
        border: 1px solid #EAECF0 !important;
        padding: 1.5rem !important;
        box-shadow: 0 1px 3px rgba(16, 24, 40, 0.1) !important;
    }
    
    /* =========================
       [6] 버튼 및 액션 요소 전역 스타일 (New Premium Blue Palette)
    ========================= */
    /* 모든 Primary 버튼 (메인 및 사이드바 공통) */
    button[kind="primary"], 
    button[data-testid*="primary"], 
    .stButton > button[kind="primary"],
    div[data-testid="stForm"] button[kind="primary"] {
        background-color: #5465ff !important;
        background: #5465ff !important;
        color: #FFFFFF !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }
    button[kind="primary"] p, button[data-testid*="primary"] p {
        color: #FFFFFF !important;
    }
    button[kind="primary"]:hover, button[data-testid*="primary"]:hover {
        background-color: #4a58e6 !important;
        box-shadow: 0 4px 12px rgba(84, 101, 255, 0.3) !important;
    }

    /* 멀티셀렉트 태그 강조 (텍스트 간섭 방지) */
    [data-baseweb="tag"], 
    .stMultiSelect [data-baseweb="tag"], 
    div[data-baseweb="select"] span[data-baseweb="tag"],
    [data-testid="stMultiSelect"] [data-baseweb="tag"] {
        background-color: #8da1ff !important;
        color: white !important;
    }
    
    /* 탭 활성화 상태 및 하단 라인 (전역) */
    button[data-baseweb="tab"]  {
        color: #667085 !important;
    }
    button[aria-selected="true"], 
    button[aria-selected="true"] p,
    button[data-testid="stMarkdownContainer"] p[style*="color"] {
        color: #5465ff !important;
    }
    
    /* 탭 강조선 고도화 */
    div[data-baseweb="tab-highlight"], 
    [data-testid="stHeader"] + div [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #5465ff !important;
    }
    
    /* 체크박스 및 라디오 버튼 등 기타 Primary 요소 */
    input[type="checkbox"]:checked + div {
        background-color: #5465ff !important;
    }
    
    /* =========================
       [8] 알림 메시지
    ========================= */
    .stAlert {
        border-radius: 10px !important;
    }
    
    /* =========================
       [9] 헤더
    ========================= */
    h1, h2, h3 {
        color: #101828 !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }

    /* =========================
       [10] 여백 조정 (사이드바)
    ========================= */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div {
        padding-top: 0.1rem !important;
        padding-bottom: 0.1rem !important;
    }
    [data-testid="stSidebar"] hr {
        margin: 0.3rem 0 !important;
    }
    [data-testid="stSidebar"] .stCaptionContainer {
        margin-top: -0.4rem !important;
        margin-bottom: -0.2rem !important;
    }
</style>
""", unsafe_allow_html=True)
