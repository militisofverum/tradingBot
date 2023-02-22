def toBalance(str):
    number = float(str) - 0.01
    return round(number, 2)

def toBalanceStable(str):
    number = float(str) - 0.1
    return round(number, 1)

def toPrice(str):
    number = float(str) - 0.1
    return round(number, 1)