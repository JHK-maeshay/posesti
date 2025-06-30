from flask import Blueprint, jsonify, request
import os

# API 그룹을 정의 (이름: api)
bp = Blueprint('api', __name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 핑 테스트
@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'success'})

# 모델로 이미지 전송, 분류결과 반환
@bp.route('/predict', methods=['POST'])
def predict():
    # 이미지인지 확인
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 이미지 캐시 삭제
    for f in os.listdir(UPLOAD_FOLDER):
        if f.lower().endswith(('.png')):
            try:
                os.remove(os.path.join(UPLOAD_FOLDER, f))
            except Exception as e:
                print(f'파일 삭제 실패: {f}, {e}')

    # 이미지 저장
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # 모델 부분

    label = '개발중입니다'  # 임시로 반환

    return jsonify({'result': label})