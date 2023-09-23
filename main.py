# Função Zero
def zero(x):
    return 0

# Função Sucessor
def successor(x):
    return x + 1

# Função de Projeção
def u(x, y):
    def projection(*args):
        if len(args) != x:
            raise ValueError(f"A função u({x},{y}) espera {x} argumentos, mas {len(args)} foram fornecidos.")
        if y < 1 or y > x:
            raise ValueError(f"O argumento y deve estar entre 1 e {x}.")

        return args[y - 1]

    return projection

# Composição
def comp(f, *args):
    def composition(*h_args):
        for g in args:
            if len(h_args) != g.__code__.co_argcount:
                raise ValueError(f"A função {g.__name__} deve ter a mesma assinatura que h.")

        results_g = [g(*h_args) for g in args]

        return f(*results_g)

    return composition

# Recursão
def rec(f, g):
    def h(x1, x2):
        def recursive(t):
            if t == 0:
                return x1
            else:
                return f(t, recursive(t - 1), g(t, recursive(t - 1)))

        return recursive(x2)

    return h

# Exemplo de uso
def f(a,b):
    return a * b
def g1(a,b,c):
    return a + b + c + 10
def g2(a,b,c):
    return a * b + c
print(comp(f , g1 , g2 )(1,5,3))

#f() = g1(1,5,3) * g2(1,5,3)    
