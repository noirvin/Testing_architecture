
ADJ_FACTOR = 0.7
def get_adjusted_capital(capital, rate, duration, income):
    result = 0
    if (capital > 0 and rate > 0 and duration > 0):
      return income / duration * ADJ_FACTOR
    return result

adjusted_capital = get_adjusted_capital(50000, 4,10, 10000)
print(adjusted_capital)
