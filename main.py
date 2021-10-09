import numpy as np

X,Y = [],[]
proximos_dias = []


with open("x.txt") as file:
    for line in file:
        X = [int(i) for i in line.split()]

with open("y.txt") as file:
    for line in file:
        Y = [int(i) for i in line.split()]

with open("proximos_dias.txt") as file:
    for line in file:
        proximos_dias.append([int(i) for i in line.split()])

X = np.array(X)
Y = np.array(Y)

V = np.array([X**1,X**0]).transpose()
a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(Y)

V2 = np.array([X**2,X**1,X**0]).transpose()
b = ((np.linalg.inv((V2.transpose()).dot(V2))).dot(V2.transpose())).dot(Y)

for i in range(len(proximos_dias)):
    dia = proximos_dias[i][0]
    valor_esperado = proximos_dias[i][1]
    
    linear = a[0] * dia + a[1]
    quadratico = b[0] * dia * dia + b[1] * dia + b[2]
    
    #erros absolutos
    erro_linear = abs(linear - valor_esperado) / abs(linear) * 100
    erro_quadratico = abs(quadratico - valor_esperado) / abs(quadratico) * 100
    

    print(("Dia {}, valor esperado {}, linear {:.0f}, quadratico {:.0f}").format(dia,valor_esperado,linear,quadratico))
    print(("erro linear: {:.2f}%, erro quadratico {:.2f}%").format(erro_linear,erro_quadratico))
    print()