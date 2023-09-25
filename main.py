import initials

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
print(initials.u(4,3)(4,6,3,12))

#f() = g1(1,5,3) * g2(1,5,3)    
