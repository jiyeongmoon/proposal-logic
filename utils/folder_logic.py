import os
from datetime import datetime
try:
    from config import PROPOSAL_BASE_DIR, FOLDER_STRUCTURES
except ImportError:
    # For standalone testing
    PROPOSAL_BASE_DIR = r"c:\Users\user\공간환경계획연구실 Dropbox\04_Knowledge_Base\00_Obsidian\moon\01_프로젝트_실무_산출물"
    FOLDER_STRUCTURES = {}

def create_project_folders(project_id, project_name, project_type, base_dir=PROPOSAL_BASE_DIR):
    """
    나래공간 표준에 따라 [ID]_[프로젝트명] 형식의 폴더를 생성하고 8대 하위 폴더를 구축함.
    예: 25-UR01_청주성안동
    """
    folder_name = f"{project_id}_{project_name}"
    project_path = os.path.join(base_dir, folder_name)
    
    if os.path.exists(project_path):
        return False, f"이미 존재하는 프로젝트 폴더입니다: {folder_name}"
    
    try:
        # 메인 프로젝트 폴더 생성
        os.makedirs(project_path)
        
        # 하위 표준 폴더 구조 생성 (8대 표준)
        sub_folders = FOLDER_STRUCTURES.get(project_type, [])
        for sub in sub_folders:
            os.makedirs(os.path.join(project_path, sub))
            
        return True, project_path
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    # Test script
    success, msg = create_project_folders("공공 제안서", "테스트_자동생성_프로젝트")
    print(f"Success: {success}, Message: {msg}")
