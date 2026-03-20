import pandas as pd
import os

# Define file path
db_path = r"c:\Users\user\공간환경계획연구실 Dropbox\04_Knowledge_Base\00_Obsidian\moon\02_데이터_및_스크립트\02_자동화_스크립트\proposal_system\data\master_db.xlsx"

# Ensure directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# 1. 인력 DB (Personnel)
personnel_data = {
    "성명": ["홍길동", "김철수", "이영희", "박민수", "최지우"],
    "부서": ["도시설계팀", "지역계획팀", "단지개발팀", "도시설계팀", "환경계획팀"],
    "직급": ["이사", "팀장", "차장", "차장", "주임"],
    "분야": ["도시계획", "도시계획", "건축", "도시계획", "조경"],
    "경력개월수": [180, 120, 96, 72, 24],
    "자격증": ["도시계획기술사", "도시계획기사", "건축사", "도시계획기사", "조경기사"],
    "주요실적": ["청주시 활성화계획", "진천군 전략계획", "서울시 지구단위계획", "세종시 마스터플랜", "전주시 공원계획"]
}

# 2. 유사용역 실적 DB (Projects)
project_data = {
    "용역명": ["2024 진천군 쇠퇴진단 분석", "2023 청주시 성안동 활성화", "2023 민관상생 투자사업", "2022 세종시 스마트시티", "2021 전북 국가산단"],
    "발주처": ["진천군", "청주시", "국토교통부", "세종특별자치시", "LH"],
    "금액(백만원)": [150, 450, 800, 1200, 600],
    "시작일": ["2024-01-01", "2023-05-01", "2023-03-01", "2022-06-01", "2021-02-01"],
    "종료일": ["2024-12-31", "2024-04-30", "2023-12-31", "2023-05-31", "2022-08-31"],
    "분류": ["도시재생", "도시재생", "투자사업", "스마트시티", "산업단지"]
}

# Save to Excel with multiple sheets
with pd.ExcelWriter(db_path) as writer:
    pd.DataFrame(personnel_data).to_excel(writer, sheet_name="인력DB", index=False)
    pd.DataFrame(project_data).to_excel(writer, sheet_name="실적DB", index=False)

print(f"Sample Master DB created at: {db_path}")
