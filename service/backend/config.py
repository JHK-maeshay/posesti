import os

class Config:
    # Flask 시크릿 키 (보안용, 필요시 변경)
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    # 이미지 업로드 제한, 용량(MB)*가로*세로
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024