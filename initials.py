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