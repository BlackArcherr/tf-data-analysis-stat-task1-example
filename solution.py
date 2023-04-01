import pandas as pd
import numpy as np
from scipy.stats import lognorm

chat_id = 474140315 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu, sigma = lognorm.fit(x-139, floc=0)
    return mu # Ваш ответ
