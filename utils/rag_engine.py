import os
import re

def retrieve_similar_references(base_path, query, top_k=3):
    """
    로컬 드롭박스 폴더에서 과거 우수 사례(MD 파일)를 검색하여 관련 논리 블록을 추출함.
    base_path: '01_프로젝트_실무_산출물' 절대 경로
    query: 검색 키워드 문자열 또는 리스트
    top_k: 최대 결과 수
    """
    references = []
    
    if not os.path.exists(base_path):
        return []

    # 쿼리가 문자열인 경우 키워드 리스트로 분리
    if isinstance(query, str):
        keywords = [k for k in query.split() if len(k) > 1] # 1글자 키워드 제외
    else:
        keywords = query

    if not keywords:
        return []

    # 프로젝트 폴더 순회
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md') and any(k in file for k in keywords):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # 특정 섹션(전략, 추진계획 등) 추출 시도
                        for keyword in keywords:
                            # 헤더(#)를 포함한 섹션 추출
                            match = re.search(f"(#+.*{keyword}.*?\n)([\s\S]*?)(?=#+|$)", content)
                            if match:
                                # app.py에서 "\n".join()으로 사용하므로 문자열로 포맷팅하여 저장
                                source_info = f"[{file}] {match.group(1).strip()}"
                                snippet = match.group(2).strip()[:500]
                                references.append(f"{source_info}\n{snippet}...")
                                
                                if len(references) >= top_k:
                                    return references
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    
    return references
