#Eric Daniel Carrillo Torres / 2720381 / 04-09-2026

tabla = []

for renglon in range(1, 11):
    fila = []
    for columna in range(1, 11):
        fila.append(renglon * columna)
    tabla.append(fila)

def imprimir_tabla(matriz):
    print("------------------")
    print("TABLA DE PITÁGORAS")
    print("------------------")

    for fila in matriz:
        for numero in fila:
            print(f"{numero:4}", end="")
        print()

def mult(matriz, renglon, columna):
    resultado = matriz[renglon - 1][columna - 1]
    return resultado

imprimir_tabla(tabla)

print("\nConsulta de multiplicación")
renglon = int(input("Ingresa el primer numero (1-10): "))
columna = int(input("Ingresa el segundo numero (1-10): "))

producto = mult(tabla, renglon, columna)

print(f"\nResultado: {renglon} x {columna} = {producto}")