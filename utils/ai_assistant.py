import os

def generate_proposal_draft(project_name, vision_keywords):
    """
    (Phase 3 Mock) 사용자가 입력한 비전 키워드를 바탕으로 제안서 초안 텍스트를 생성함.
    향후 실제 LLM API 연동 가능.
    """
    if not project_name:
        return "프로젝트명을 먼저 입력해 주세요."
    
    draft = f"""# {project_name} 제안서 초안

## 1. 사업의 비전 및 목표
- 본 사업은 '{vision_keywords}'을(를) 핵심 가치로 삼아 지속 가능한 도시 환경을 조성하는 데 목적이 있음.
- 주민 체감형 서비스 및 지역 특화 모델을 통해 시너지를 극대화함.

## 2. 핵심 전략 (Key Strategy)
- **전략 1**: 데이터 기반의 정밀 분석을 통한 맞춤형 재생 전략 수립
- **전략 2**: 민관 협력 거버넌스 구축 및 자생적 운영 조직 육성
- **전략 3**: ICT 기술을 결합한 스마트 도시 인프라 최적화

## 3. 기대 효과
- 지역 경제 활성화 및 신규 일자리 창출 보조
- 노후 주거지의 정주 여건 개선 및 공동체 회복
"""
    return draft

def get_suggested_content_list(job_type):
    """
    업무 유형별로 반드시 포함되어야 할 필수 항목 리스트 제공
    """
    guides = {
        "공공 제안서": ["사업 개요", "대상지 현황 분석", "추진 전략", "관리 운영 계획"],
        "사업 기획서": ["시장 분석", "사업 추진 로직", "수익 모델", "리스크 관리"],
        "기타 보고서": ["현황 종합", "문제점 도출", "개선 방안", "결론"]
    }
    return guides.get(job_type, ["기본 항목 1", "기본 항목 2"])

if __name__ == "__main__":
    # Test
    print(generate_proposal_draft("청주시 도시재생", "사람 중심, 스마트 재생"))
