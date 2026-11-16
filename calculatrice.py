
def addition(a, b):
    return a + b


def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


# Fonction avec un bug volontaire
def soustraction(a, b):
    return a + b
