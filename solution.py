import pandas as pd
import numpy as np


chat_id = 345280072 # Ваш chat ID, не меняйте название переменной
def solution(x: np.array, y: np.array) -> bool:
# Применим тест Манна-Уитни для проверки гипотезы
    stat, p_value = mannwhitneyu(x, y, alternative='two-sided')
    
    # Уровень значимости
    alpha = 0.06
    
    # Если p-значение меньше уровня значимости, отвергаем нулевую гипотезу
    return p_value < alpha
