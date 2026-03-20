import os
import json
import google.generativeai as genai

def get_available_models(api_key):
    """
    사용 가능한 Gemini 모델 목록을 가져옴 (generateContent 지원 모델만 필터링)
    """
    if not api_key:
        return []
    try:
        genai.configure(api_key=api_key)
        models = [m.name.replace('models/', '') for m in genai.list_models() 
                  if 'generateContent' in m.supported_generation_methods]
        # 최신 모델이 상단으로 오도록 정렬 (Flash 모델 우선 등)
        models.sort(key=lambda x: ('flash' in x.lower(), 'pro' in x.lower()), reverse=True)
        return models
    except Exception as e:
        print(f"Error fetching models: {e}")
        return ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"] # 폴백

def analyze_rfp_with_gemini(api_key, prompt, model_name='gemini-1.5-flash'):
    """
    선택된 Gemini 모델을 사용하여 전달받은 프롬프트를 실행함.
    """
    if not api_key:
        return None, "API 키가 설정되지 않았습니다."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text, "분석 완료"
        else:
            return None, "AI 응답 생성 실패"
            
    except Exception as e:
        return None, f"Gemini API 호출 중 오류 발생: {str(e)}"

def refine_logic_with_feedback(api_key, original_logic, feedback, model_name='gemini-1.5-flash'):
    """
    검증 피드백을 바탕으로 논리 블록을 자가 교정(Self-Refine)함.
    """
    if not api_key:
        return None, "API 키가 설정되지 않았습니다."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        
        prompt = f"""
너는 제안서의 논리적 완결성을 책임지는 최고 기획 파트너야.
아래의 [1차 생성 논리]와 [전문가 검증 피드백]을 바탕으로, 논리의 빈틈을 메우고 인과관계를 강화한 **[최종 교정 논리]**를 작성해줘.

[1차 생성 논리]
{json.dumps(original_logic, indent=2, ensure_ascii=False)}

[전문가 검증 피드백]
{feedback}

[교정 지침]
1. 피드백에서 지적된 논리적 약점을 반드시 보완할 것.
2. 근거 데이터(Evidence)와 전략(Solution) 간의 연결고리를 더 구체적인 수치나 사례로 강화할 것.
3. 실현 가능한 수준의 구체적인 액션 플랜을 제시할 것.

[출력 형식]
기존 논리 블록의 JSON 구조를 유지하며, 내용만 업그레이드하여 답변할 것.
"""
        response = model.generate_content(prompt)
        
        if response and response.text:
            cleaned_text = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(cleaned_text), "교정 완료"
        else:
            return None, "AI 응답 생성 실패"
            
    except Exception as e:
        return None, f"교정 중 오류 발생: {str(e)}"
