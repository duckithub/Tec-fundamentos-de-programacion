#Eric Daniel Carrillo Torres / 7270381 / 21/08/2026

print("Bienvenido al museo, nuestros tickets son: \n(1) Niños (menores a 3), \n(2) Menores de edad(3 a 17), \n(3) Mayor de edad, \ntambien tenemos descuentos especiales para: \n(4) Adultos mayores, \n(5) Profesores y \n(6) Estudiantes. \nPor favor ingrese la cantidad de entradas que desea comprar: ")
visitante = input()

while int(visitante) >= 0:
    print("Que tipo de entrada desea comprar:") 
    visitante = str(input())
    if visitante.lower() == "no":
        break
    else:
        print("la entrada")
        visitante = input()
        
1 == "bebe"
2 == "menor"
3 == "mayor"
4 == "adulto"
5 == "profesor"
6 == "estudiante"

if visitante == "1":
    print("El precio de la entrada para niños menores a 3 años es de $0.00")
elif visitante == "2":
    print("El precio de la entrada para menores de edad es de $30.00")
elif visitante == "3":
    print("El precio de la entrada para mayores de edad es de $45.00")
elif visitante == "4":
    print("El descuento de la entrada para adultos mayores es de 12% y el precio final es de $39.60")
elif visitante == "5":
    print("El descuento de la entrada para profesores es de 10% y el precio final es de $40.50")
elif visitante == "6":
    print("El descuento de la entrada para estudiantes es de 10% y el precio final es de $40.50")
else:
    print("Opción inválida. Por favor ingrese un número del 1 al 6.")

