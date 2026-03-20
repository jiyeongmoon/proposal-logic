@echo off
setlocal
set "TARGET_DIR=%~dp0"

echo [1/3] 프로젝트 폴더로 이동 중...
cd /d "%TARGET_DIR%"

echo [2/3] 시스템 환경 최적화 중 (라이브러리 업데이트)...
if exist "requirements.txt" (
    pip install -r requirements.txt > nul
) else (
    pip install --upgrade typing_extensions pydantic google-generativeai streamlit pandas python-docx pdfplumber python-pptx Pillow requests > nul
)

echo [3/3] 제안서 자동화 시스템 구동 중...
echo.
streamlit run app.py

if %errorlevel% neq 0 (
    echo.
    echo [!] 오류가 발생했습니다. 창을 닫기 전 내용을 확인해 주세요.
    pause
)
