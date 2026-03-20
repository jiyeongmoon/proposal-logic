from docx import Document
import os

def parse_docx_to_markdown(file_path):
    """
    DOCX 파일의 텍스트와 표를 마크다운 형식으로 변환함.
    """
    if not os.path.exists(file_path):
        return None, "파일을 찾을 수 없습니다."

    try:
        doc = Document(file_path)
        md_content = []

        # 문서를 순회하며 텍스트 및 표 추출
        for element in doc.element.body:
            # Paragraph 추출
            if element.tag.endswith('p'):
                from docx.text.paragraph import Paragraph
                p = Paragraph(element, doc)
                if p.text.strip():
                    md_content.append(p.text)
            
            # Table 추출
            elif element.tag.endswith('tbl'):
                from docx.table import Table
                t = Table(element, doc)
                md_content.append("\n" + _parse_table_to_markdown(t) + "\n")

        return "\n\n".join(md_content), "추출 성공"
    except Exception as e:
        return None, f"문서 읽기 중 오류 발생: {str(e)}"

def _parse_table_to_markdown(table):
    """
    docx.table 객체를 마크다운 표 형식으로 변환함.
    """
    rows = []
    for row in table.rows:
        rows.append([cell.text.replace("\n", " ").strip() for cell in row.cells])
    
    if not rows:
        return ""
    
    md_table = []
    # 헤더 생성
    header = "| " + " | ".join(rows[0]) + " |"
    separator = "| " + " | ".join(["---"] * len(rows[0])) + " |"
    md_table.append(header)
    md_table.append(separator)
    
    # 데이터 행 생성 (중복 셀 방지 로직 포함)
    for row in rows[1:]:
        md_table.append("| " + " | ".join(row) + " |")
        
    return "\n".join(md_table)
