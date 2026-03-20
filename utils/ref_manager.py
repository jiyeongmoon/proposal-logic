import os
import glob

def get_reference_library_path(base_dir):
    """
    Reference Library 폴더 경로를 반환함.
    """
    path = os.path.join(base_dir, "00_가이드_및_매뉴얼", "Reference_Library")
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    return path

def list_best_practices(project_base_dir):
    """
    프로젝트 폴더들 내에서 [BEST_PRACTICE] 태그가 포함된 파일을 탐색함.
    """
    best_practices = []
    # 01_프로젝트_실무_산출물 폴더 내 모든 프로젝트 스캔
    project_root = os.path.join(project_base_dir, "01_프로젝트_실무_산출물")
    if not os.path.exists(project_root):
        return []
        
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file.endswith(".md"):
                fpath = os.path.join(root, file)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        content = f.read(500) # 상단 태그만 확인
                        if "[BEST_PRACTICE]" in content or "#BEST_PRACTICE" in content:
                            best_practices.append({
                                "name": file,
                                "path": fpath,
                                "project": os.path.basename(root)
                            })
                except:
                    continue
    return best_practices
