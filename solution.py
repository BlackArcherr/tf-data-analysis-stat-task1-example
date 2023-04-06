import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 474140315 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = x - 139
    log_x = np.log(x)
    mu = np.mean(log_x)
    return mu
