import numpy as np 
#enunciado
#crea una matriz de 3 filas y 3 columnas llena de unos y:
#cambia todos los valores a 5.
#calcula el valor maximo de la matriz
#calcula la suma total de los elemetos

matriz = np.ones((3,3))
print("Matriz original:")
print(matriz)
#cambiar valores a 5
matriz[:] = 5
print("Matriz modificada:")
print(matriz)
#calcular valor maximo
maximo = np.max(matriz)
print(f"Valor maximo de la matriz: {maximo}")
#calcular suma total
suma_total = np.sum(matriz)
print(f"Suma total de los elementos: {suma_total}")
