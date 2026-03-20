import os

# Base Path Configuration
# 드롭박스 동기화 폴더 내 프로젝트 위치 설정 (환경 변수가 있으면 우선 사용, 없으면 로컬 기본값 사용)
DEFAULT_LOCAL_ROOT = r"c:\Users\user\공간환경계획연구실 Dropbox\04_Knowledge_Base\00_Obsidian\moon"
PROJECT_ROOT = os.getenv("PROJECT_ROOT", DEFAULT_LOCAL_ROOT) if os.path.exists(DEFAULT_LOCAL_ROOT) else os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PROPOSAL_BASE_DIR = os.path.join(PROJECT_ROOT, "01_프로젝트_실무_산출물")

# Folder Structure Configuration
# 나래공간 8대 표준 하위 폴더 체계
NARE_STANDARD_FOLDERS = [
    "00_행정 및 착수",
    "01_기초조사 및 현황분석",
    "02_기본구상 및 전략",
    "03_계획수립 및 설계",
    "04_협의 및 심의",
    "05_최종성과물",
    "06_회의록 및 보고",
    "07_참고 및 기초자료"
]

# 업무 유형별 코드 및 상세 명칭 (나래공간 표준)
BIZ_CODE_DISPLAY = {
    "UR": "UR (도시재생 전략·활성화계획 (본사업, 공모))",
    "CS": "CS (변경용역, 모니터링, 추진실적보고, 성과평가)",
    "PS": "PS (용역 제안서 작성, 가격입찰, 설계 공모)"
}

FOLDER_STRUCTURES = {code: NARE_STANDARD_FOLDERS for code in BIZ_CODE_DISPLAY.keys()}

# UI Configuration
APP_TITLE = "사업 분석 및 전략 도출시스템"
APP_SUBTITLE = "공간환경계획연구실(Moon) 업무자동화 프로젝트"

# Data Path Configuration
# 내부 스크립트 기반 상대 경로 우선 탐색
INTERNAL_APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(INTERNAL_APP_DIR, "data", "master_db.xlsx")
TEMPLATE_DIR = os.path.join(INTERNAL_APP_DIR, "templates")

# 프로젝트 내 절대 경로가 필요한 경우 폴백
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(PROJECT_ROOT, "02_데이터_및_스크립트", "02_자동화_스크립트", "proposal_system", "data", "master_db.xlsx")
if not os.path.exists(TEMPLATE_DIR):
    TEMPLATE_DIR = os.path.join(PROJECT_ROOT, "02_데이터_및_스크립트", "02_자동화_스크립트", "proposal_system", "templates")
