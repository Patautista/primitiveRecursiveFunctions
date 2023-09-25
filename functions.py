import initials

# Função de adição (x + y)
def add(x, y):
    if y == 0:
        return x
    else:
        return add(initials.successor(x), absolute_difference(y, 1))

# Função de multiplicação (x * y)
def mult(x, y):
    if y == 0:
        return initials.zero(x)
    else:
        return x + mult(x, absolute_difference(y, 1))

# Função de fatorial (x!)
def factorial(x):
    if x == 0:
        return 1
    else:
        return mult(factorial(absolute_difference(x, 1)), x)

# Função de potenciação (x^y)
def power(x, y):
    if y == 0:
        return 1
    else:
        return mult(power(x, absolute_difference(y, 1)), x)

# |x - y|
def absolute_difference(x, y):
    if x >= y:
        return x - y
    else:
        return y - x
    
# Igualdade
def equals(x, y):
    if x != 0 and y != 0:
        return equals(absolute_difference(x, 1), absolute_difference(y, 1))
    elif x != 0:
        return 0
    elif y != 0:
        return 0
    else: 
        return 1