import math
import numpy as np
import matplotlib.pyplot as plt

def ler_numero(nome):
    while True:
        entrada = input(f{nome}:)
        if entrada.strip() == "":
                print("erro, digite numero")
                continue
        try:
            valor = float(input(f"{nome}:"))
            return valor
        except ValueError:
            print("erro,valor invalido")


def calcular_delta ():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    delta = (b**2-4*a*c)
    print(f"Delta: {delta}")
    
    if delta < 0:
        print("Não existem")
    elif delta == 0:
        x = -b / (2*a)
        print(f"raiz {x}")
        
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"raizes {x1} e {x2}")
        
    X = np.linspace(-10, 10, 400)
    y = a*X**2 + b*X + c
    
    plt.plot(X, y, label="função")
    plt.axhline(0, color="black" )
    plt.axvline(0, color="black")
    plt.legend()
    plt.title("Grafico da função")
    plt.show()
 
    

        
calcular_delta()