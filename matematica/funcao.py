# # adicionar neste programa
# # 1- a opção de o usuario digitar -AZ
# # 2- mostrar oque é uma função afim -AZ
# import numpy as np
# import matplotlib.pyplot as plt

# # Definindo as funções quadráticas
# n= int(input(""))
# def f(x):
#     return 2*x**2 - 3*x + 1

# def g(x):
#     return -x**2 + 2*x + 3

# # Gerando valores de x
# x_values = np.linspace(-2, 4, 400)

# # Calculando os valores correspondentes de y para cada função
# y_f = f(x_values)
# y_g = g(x_values)

# # Criando o gráfico
# plt.figure(figsize=(8, 6))
# plt.plot(x_values, y_f, label='f(x) = 2x^2 - 3x + 1', color='blue')
# plt.plot(x_values, y_g, label='g(x) = -x^2 + 2x + 3', color='red')

# # Adicionando rótulos e legendas
# plt.title('Gráfico de Duas Funções Quadráticas')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()

# # Exibindo o gráfico
# plt.grid(True)
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np


# def funcao_afim(x, a, b):
#     return a * x + b


# def plotar_grafico(a, b):
#     x = np.linspace(-10, 10, 100)
#     y = funcao_afim(x, a, b)

#     plt.plot(x, y, label=f"Função Afim: {a}x + {b}")
#     plt.axhline(0, color = 'black', linearwidth='0.5')
#     plt.xlabel("Eixo X")
    
#     plt.ylabel("Eixo Y")
    
#     plt.title("Gráfico de Função Afim")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#     # plt.legend(loc='lower left', ncol=80) 
    
# # Exemplo de uso
# a = float(input("Digite o coeficiente angular (a): "))
# b = float(input("Digite o coeficiente linear (b): "))

# plotar_grafico(a, b)
import numpy as np
import matplotlib.pyplot as plt

def calculadora_funcao_afim(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * x + b

    plt.plot(x, y, label=f'{a}x + {b}')
    plt.axhline(0, color='red',linewidth=1.0)
    plt.axvline(0, color='blue',linewidth=1.0)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Gráfico de uma Função Afim')
    plt.show()

# Exemplo de uso
a = float(input('Digite o coeficiente angular (a): '))
b = float(input('Digite o termo independente (b): '))

calculadora_funcao_afim(a, b)
