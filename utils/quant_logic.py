import pandas as pd
import os
try:
    from config import DB_PATH
except ImportError:
    # Standalone fallback
    DB_PATH = r"c:\Users\user\공간환경계획연구실 Dropbox\04_Knowledge_Base\00_Obsidian\moon\02_데이터_및_스크립트\02_자동화_스크립트\proposal_system\data\master_db.xlsx"

def load_master_db():
    """마스터 엑셀 DB를 로드함"""
    if not os.path.exists(DB_PATH):
        return None, None
    
    try:
        personnel_df = pd.read_excel(DB_PATH, sheet_name="인력DB")
        project_df = pd.read_excel(DB_PATH, sheet_name="실적DB")
        return personnel_df, project_df
    except Exception as e:
        print(f"Error loading DB: {e}")
        return None, None

def match_personnel(req_field, min_months):
    """
    RFP 요구사항에 맞는 인력을 매칭하고 Gap Analysis를 수행함
    """
    p_df, _ = load_master_db()
    if p_df is None:
        return None, "DB를 찾을 수 없습니다."
    
    # 1차 필터링 (분야 일치)
    matched = p_df[p_df["분야"] == req_field].copy()
    
    if matched.empty:
        return None, f"'{req_field}' 분야의 인력이 DB에 없습니다."
    
    # 경력 검증
    matched["경력부족분"] = min_months - matched["경력개월수"]
    matched["상태"] = matched["경력부족분"].apply(lambda x: "✅ 충족" if x <= 0 else f"⚠️ 부족 ({x}개월)")
    
    return matched, "매칭 성공"

if __name__ == "__main__":
    # Test
    res, msg = match_personnel("도시계획", 100)
    if res is not None:
        print(res[["성명", "경력개월수", "상태"]])
