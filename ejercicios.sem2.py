import numpy as np

print("\nEJERCICIO N° 1\n")
arreglo1 = np.random.randint(0, 100, (3, 3))
arreglo2 = np.random.randint(0, 100, (3, 3))

print(arreglo1, "Matriz 1")
print("-"*30)
print(arreglo2, "Matriz 2")
print("-"*30)

mult = arreglo1 * arreglo2
print(mult, "Multiplicación de matrices")
print("-"*30)

print("\nEJERCICIO N° 2\n")
arreglo3 = np.arange(1, 41)
print(arreglo3.reshape(10, 4))
print("-"*30)