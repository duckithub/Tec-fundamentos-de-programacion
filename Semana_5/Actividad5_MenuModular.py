def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Tuplas")
    print("2. Diccionarios")
    print("3. Excepciones")
    print("4. Strings")
    print("5. Finalizar")
    print("\n======================")


def sumar_tupla(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


def manejar_tuplas():
    numeros = (10, 20, 30, 40, 50)
    print("\nTupla inicial:", numeros)
    print("Tercer elemento de la tupla:", numeros[2])

    try:
        num1 = int(input("Ingresa un número adicional para agregar a la tupla: "))
        num2 = int(input("Ingresa otro número adicional para agregar a la tupla: "))
    except ValueError:
        print("Error: Debes ingresar solo números enteros.")
        return

    nueva_tupla = numeros + (num1, num2)
    print("Nueva tupla creada:", nueva_tupla)

    lista_numeros = list(nueva_tupla)
    lista_numeros.sort()
    print("Lista ordenada:", lista_numeros)

    print("Suma de todos los elementos de la tupla:", sumar_tupla(nueva_tupla))


def manejar_diccionarios():
    contactos = {
        "Ana": "555-1001",
        "Luis": "555-1002",
        "Sofía": "555-1003"
    }

    print("\nContactos actuales:", contactos)

    try:
        nombre_nuevo = input("Ingresa el nombre del nuevo contacto: ").strip()
        telefono_nuevo = input("Ingresa el número de teléfono del nuevo contacto: ").strip()

        if nombre_nuevo == "" or telefono_nuevo == "":
            raise ValueError("Los campos no pueden estar vacíos.")

        contactos[nombre_nuevo] = telefono_nuevo
        print("Contacto agregado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")

    print("\nNombres de contactos registrados:")
    for nombre in contactos:
        print("-", nombre)

    nombre_busqueda = input("\nIngresa el nombre del contacto que deseas buscar: ").strip()
    telefono = buscar_contacto(contactos, nombre_busqueda)

    if telefono is None:
        print(f"No se encontró el contacto '{nombre_busqueda}'.")
    else:
        print(f"El teléfono de {nombre_busqueda} es: {telefono}")


def buscar_contacto(contactos, nombre):
    return contactos.get(nombre)


def manejar_excepciones():
    print("\nEjemplo de manejo de excepciones")

    try:
        num1 = input("Ingresa el primer número entero: ").strip()
        num2 = input("Ingresa el segundo número entero: ").strip()

        if num1 == "" or num2 == "":
            raise ValueError("No puedes dejar campos vacíos.")

        num1 = int(num1)
        num2 = int(num2)

        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero. El segundo número no puede ser 0.")

        print("Suma de los dos números:", num1 + num2)
        print("División de los dos números:", num1 / num2)

    except ValueError:
        print("Error controlado: Debes ingresar números enteros válidos y no dejar espacios vacíos.")
    except ZeroDivisionError as error:
        print(f"Error controlado: {error}")
    except Exception as error:
        print(f"Se produjo un error inesperado: {error}")


def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)


def manejar_strings():
    mensaje = "Python es una herramienta poderosa para aprender programación"

    print("\nMensaje original:", mensaje)
    print("Longitud del mensaje:", len(mensaje))
    print("Mensaje en mayúsculas:", mensaje.upper())

    mensaje_reemplazado = mensaje.replace("poderosa", "increíble")
    print("Mensaje con reemplazo:", mensaje_reemplazado)

    print("Cantidad de palabras en el mensaje:", contar_palabras(mensaje))



def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            manejar_tuplas()
        elif opcion == "2":
            manejar_diccionarios()
        elif opcion == "3":
            manejar_excepciones()
        elif opcion == "4":
            manejar_strings()
        elif opcion == "5":
            print("\nGracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

        input("\nPresiona Enter para regresar al menú...")


if __name__ == "__main__":
    main()
