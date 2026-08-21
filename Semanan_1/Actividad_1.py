
GREEN = "\033[32m"
RESET = "\033[0m"

print(" ✿ ★<CALCULADORA DE TIEMPO DIGITAL>★ ✿")

nombre = input("Ingresa tu nombre: ")

redes = float(input("Horas en redes sociales: "))
mensajeria = float(input("Horas en mensajería: "))
streaming = float(input("Horas en servicios de streaming: "))
videojuegos = float(input("Horas en videojuegos: "))
estudio = float(input("Horas en estudio en línea: "))

tiempo_total = (
    redes
    + mensajeria
    + streaming
    + videojuegos
    + estudio
)

porcentaje = (tiempo_total / 24) * 100

print(f"\n{GREEN}========== RESUMEN =========={RESET}")
print(f"{GREEN}Usuario: {nombre}{RESET}")
print(f"{GREEN}Tiempo total diario: {tiempo_total}horas{RESET}")
print(f"{GREEN}Porcentaje del día: {porcentaje}%{RESET}")
print(f"{GREEN}=============================={RESET}")