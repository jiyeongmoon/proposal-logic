import google.generativeai as genai
import json

def validate_logic_block(api_key, logic_block_json, model_name='gemini-1.5-flash'):
    """
    Gemini를 사용하여 논리 블록의 인과관계 및 정합성을 검증함.
    """
    if not api_key:
        return None, "API 키가 설정되지 않았습니다."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        
        prompt = f"""
너는 대한민국 최고의 제안서 전략 기획자이자 논리 검증 전문가야.
입력된 '논리 블록(Logic Block)'의 인과관계, 타당성, 그리고 제안 논리로서의 완성도를 검증해줘.

[검증 대상 논리 블록]
{json.dumps(logic_block_json, indent=2, ensure_ascii=False)}

[검증 기준]
1. **Fact Relevance**: 제시된 Evidence(근거)가 Pain Point(문제점)와 직접적인 상관관계가 있는가?
2. **Logical Flow**: Pain Point를 해결하기 위한 Solution(전략)이 논리적으로 타당한가?
3. **Selling Point**: 제안사만의 차별화된 강점이 전략에 명확히 녹아 있는가?
4. **Narrative Integrity**: HWP 구술형 문장이 전문적인 개조식이며 구조적으로 완벽한가?

[출력 형식]
반드시 아래 JSON 형식으로만 답변할 것:
{{
  "score": 1~10 (정합성 점수),
  "status": "PASS" | "WARNING" | "FAIL",
  "critique": "논리적 약점 및 개선 방향에 대한 전문적인 코멘트",
  "suggestions": ["구체적인 보완 내용 1", "구체적인 보완 내용 2"]
}}
"""
        response = model.generate_content(prompt)
        
        if response and response.text:
            cleaned_text = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(cleaned_text), "검증 완료"
        else:
            return None, "AI 응답 생성 실패"
            
    except Exception as e:
        return None, f"검증 중 오류 발생: {str(e)}"
