import pandas as pd
import numpy as np

chat_id = 474140315 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = x-139
    return  np.mean(np.exp(y))# Ваш ответ
