import math


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
    y = a*x**2 + b*x + c
    
 
    

        
calcular_delta()