import os
import re
import json
import google.generativeai as genai

def extract_standardized_reference(api_key, raw_text, metadata, model_name='gemini-1.5-flash'):
    """
    과거 프로젝트 텍스트에서 RAG 최적화된 논리 블록을 추출하여 정규화함.
    """
    if not api_key:
        return None, "API 키가 설정되지 않았습니다."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        
        prompt = f"""
너는 최고의 데이터 엔지니어이자 제안서 전략 전문가야.
공공사업 제안서의 원문 텍스트에서 향후 RAG(검색 증강 생성)에 활용할 수 있도록 **[핵심 논리 데이터 블록]**을 추출하여 정규화해줘.

[입력 데이터 메타정보]
{json.dumps(metadata, indent=2, ensure_ascii=False)}

[원문 텍스트]
{raw_text[:5000]}

[추출 및 정규화 규칙]
1. **의미 단위 추출**: 단순 요약이 아니라, '어떤 문제(Context)를 어떤 논리(Strategy)로 해결했는지'가 드러나도록 추출할 것.
2. **수식어 제거**: "~를 위한", "~하고자 하는" 등의 수동적/감성적 표현을 제거하고 팩트와 논리 구조만 남길 것.
3. **태깅**: 주제별 카테고리와 핵심 키워드 5개 내외를 선정.

[출력 형식]
반드시 아래 마크다운(YAML 헤더 포함) 형식으로만 답변할 것:
---
category: "사업분야"
project_name: "프로젝트명"
keywords: ["키워드1", "키워드2", ...]
logic_type: "Strategy | Implementation | Governance"
---
# [핵심 논리 블록 제목]
- **Context**: 당시 지역의 핵심 문제 상황 (수치 포함)
- **Winning Logic**: 이를 해결하기 위해 적용한 결정적 논리 및 차별화 포인트
- **Key Action**: 구체적인 실행 방안
- **Expected Effect**: 생성된 기대 효과 (수치 중심)
"""
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text, "추출 완료"
        else:
            return None, "AI 응답 생성 실패"
            
    except Exception as e:
        return None, f"추출 중 오류 발생: {str(e)}"

def save_to_reference_library(library_path, normalized_content, filename):
    """
    정규화된 내용을 Reference_Library 폴더에 저장함.
    """
    try:
        if not os.path.exists(library_path):
            os.makedirs(library_path)
        
        target_path = os.path.join(library_path, filename)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(normalized_content)
        return True, f"저장 완료: {target_path}"
    except Exception as e:
        return False, f"저장 중 오류 발생: {str(e)}"
