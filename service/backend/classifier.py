import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import itertools

from .config import Config

# 텐서플로우 인터프리터 로드
interpreter = tf.lite.Interpreter(model_path=Config.TRAINED_MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 예측
def predict_pose(X_input):
    interpreter.set_tensor(input_details[0]['index'], X_input)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    class_idx = np.argmax(output_data, axis=1)[0]
    return class_idx, output_data[0]

# CSV import
df = pd.read_csv(Config.INPUT_CSV_PATH)
vector = df.values[0, :51].astype(np.float32)
X_input = np.expand_dims(vector, axis=0)

# 예측 실행
pred_class_idx, y_pred = predict_pose(X_input)

# 클래스 이름
class_names = ['pushup', 'situp', 'jumpingjacks', 'squat', 'pullup']