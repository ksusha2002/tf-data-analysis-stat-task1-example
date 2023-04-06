import pandas as pd
import numpy as np
from scipy.optimize import minimize


chat_id = 506081330 # Ваш chat ID, не меняйте название переменной

def solution(x: np.ndarray) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    def likelihood(params, x):
        a, s = params
        log_likelihood = -np.sum(np.log(s*x*np.sqrt(2*np.pi)) - ((np.log(x) - a)**2) / (2*s**2))
        return log_likelihood

    # Максимизация функции правдоподобия
    initial_guess = [0, 1]  # начальное приближение
    result = minimize(likelihood, initial_guess, args=(x,), method='Nelder-Mead')
    a_estimate = result.x[0]

    # Вывод результатов
    return a_estimate

   # return x.mean()  Ваш ответ
