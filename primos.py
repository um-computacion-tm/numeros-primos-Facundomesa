def primos(value):
    if value <= 1:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    for i in range(3, int(value**0.5) + 1, 2):
        if value % i == 0:
            return False
    return True