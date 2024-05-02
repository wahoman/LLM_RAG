import re
from konlpy.tag import Okt
from PyPDF2 import PdfReader
import jsonpickle

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    raw_text = ''
    for page in reader.pages:
        text = page.extract_text()
        if text:
            # 불필요한 문자 제거
            text = re.sub(r"\n", " ", text)  # 개행 문자를 공백으로 대체
            text = re.sub(r"(\w)([A-Z])", r"\1 \2", text)  # 대문자 앞에 공백 추가
            raw_text += text
    return raw_text

def tokenize_text(text):
    okt = Okt()
    tokens = okt.morphs(text)
    token_data = [{'token': token, 'lower_token': token.lower()} for token in tokens if len(token) > 1]  # 한 글자 토큰 제거
    return token_data

def save_tokens(tokens, file_path):
    with open(file_path, 'w') as file:
        serialized_data = jsonpickle.encode(tokens)
        file.write(serialized_data)

# 파일 경로 및 실행
pdf_path = "C:/Users/SSTLabs/Desktop/여형구/test.pdf"
tokens_file_path = "C:/Users/SSTLabs/Desktop/여형구/gptapi/test.json"
text = extract_text_from_pdf(pdf_path)
tokens = tokenize_text(text)
save_tokens(tokens, tokens_file_path)
