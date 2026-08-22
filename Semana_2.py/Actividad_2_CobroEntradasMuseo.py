#Eric Daniel Carrillo Torres / 7270381 / 21/08/2026

bebe = 0
menor = 30
adulto = 45

descuento_mayor = 0.12
descuento_profesor = 0.10
descuento_estudiante = 0.10



while True:
        cantidad = int(input("Bienvenido al museo, nuestros tickets son: \n(1) Niños (menores a 3), \n(2) Menores de edad(3 a 17), \n(3) Mayor de edad, \ntambien tenemos descuentos especiales para: \n(4) Adultos mayores, \n(5) Profesores y \n(6) Estudiantes. \nPor favor ingrese la cantidad de entradas que desea comprar: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            continue
        break

total_general = 0
visitantes_procesados = 0

for visitante in range(1, cantidad + 1):

    print(f"Visitante {visitante}")

    while True:
            edad = int(input("Ingresa la edad: "))

            break
    if edad < 3:
        precio_base = bebe
        categoria = "Niño menor de 3 años"

    elif edad <= 17:
        precio_base = menor
        categoria = "Menor de edad"

    else:
        precio_base = adulto
        categoria = "Mayor de 18 años"

    descuento = 0
    tipo_descuento = "Sin descuento"

    if edad >= 60:
        descuento = descuento_mayor
        tipo_descuento = "Adulto mayor (12%)"

    elif edad >= 18:
        descuento = descuento_profesor
        tipo_descuento = "Profesor (10%)"

    elif edad >= 3: 
        descuento = descuento_estudiante
        tipo_descuento = "Estudiante (10%)"

    monto_descuento = precio_base * descuento
    total_pagar = precio_base - monto_descuento

    total_general += total_pagar
    visitantes_procesados += 1


print("RESUMEN DE LA COMPRA")

print(f"Total a pagar: {total_general}") 