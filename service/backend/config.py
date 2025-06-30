import os

class Config:
    # Flask 시크릿 키 (보안용, 필요시 변경)
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    # 이미지 업로드 제한, 용량(MB)*가로*세로
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    # 입력값 주소
    INPUT_CSV_PATH = 'static/uploads/test.csv'
    # 추정 모델 주소(무브넷)
    MOVENET_MODEL_PATH = 'posetifinalcode\movenet_thunder.tflite'
    # 분류 모델 주소
    TRAINED_MODEL_PATH = 'posetifinalcode\pose_classifier.tflite'