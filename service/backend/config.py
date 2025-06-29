import os

class Config:
    # Flask 시크릿 키 (보안용, 필요시 변경)
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')