from flask import Blueprint, jsonify, request

# API 그룹을 정의 (이름: api)
bp = Blueprint('api', __name__)

# 핑 테스트
@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'success'})