#Eric Daniel Carrilo Torres - 20/09/2026 - 7270381
#sms es la empresa que se me ocurrio, significa "Server Managment Services" (●'◡'●)

#========== Colores ==========
BLUE = "\033[94m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"
#=============================

#========== importaciones ==========
import requests
import time
import sys
import random
import os
import datetime 
#===================================

#======================= Pantalla de carga ====================================
def Pantalla_de_carga(max_duration=5, base_message="Cargando sistema"):

    duracion = random.uniform(1, max_duration)

    tiempo = time.time()
    tiempo_pasado = 0
    dots = 0

    while tiempo_pasado < duracion:

        mensaje_cargando = f"{base_message}{'.' * (dots % 4)}"

        progreso = (tiempo_pasado / duracion) * 100

        sys.stdout.write(f"\r{mensaje_cargando:<30} {progreso:.0f}%")
        sys.stdout.flush()

        time.sleep(0.2)
        tiempo_pasado = time.time() - tiempo
        dots += 1

    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()


# Esto es lo que hace que puedas invocar la pantalla de carga en cualquier punto del codigo ( •̀ ω •́ )✧
Pantalla_de_carga(max_duration=5)
#=============================

#==================================== Logo ===================================
print("  █████████  ██████   ██████  █████████     ███                      ")
print(" ███▒▒▒▒▒███▒▒██████ ██████  ███▒▒▒▒▒███    ▒▒▒                      ")
print("▒███    ▒▒▒  ▒███▒█████▒███ ▒███    ▒▒▒     ████  ████████    ██████ ")
print("▒▒█████████  ▒███▒▒███ ▒███ ▒▒█████████    ▒▒███ ▒▒███▒▒███  ███▒▒███")
print(" ▒▒▒▒▒▒▒▒███ ▒███ ▒▒▒  ▒███  ▒▒▒▒▒▒▒▒███    ▒███  ▒███ ▒███ ▒███ ▒▒▒ ")
print(" ███    ▒███ ▒███      ▒███  ███    ▒███    ▒███  ▒███ ▒███ ▒███  ███")
print("▒▒█████████  █████     █████▒▒█████████  ██ █████ ████ █████▒▒██████ ")
print(" ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒ ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒  ")
#===============================================================================

Pantalla_de_carga(max_duration=5)

#======================================= Login ============================================
print("----- Sistema de Login -----")

user = ""
while True:
    user = input("Ingresa tu nombre de usuario: ").strip()

    if not user:
        print("Error: El nombre de usuario no puede estar en blanco. Intenta de nuevo.")
    elif any(char.isdigit() for char in user):
        print("Error: El nombre de usuario no puede contener números. Intenta de nuevo.")
    elif not user.isalpha():
        print("Error: El nombre de usuario solo puede contener letras. Intenta de nuevo.")
    else:
        print(f"Nombre de usuario '{user}' aceptado.")
        break

contraseña_valida = "sms01"

login_code = ""
while True:
    login_code = input("Ingresa tu contraseña: ").strip()

    if not login_code:
        print("Error: La contraseña no puede estar en blanco. Intenta de nuevo.")
    elif login_code != contraseña_valida:
        print("Error: Contraseña incorrecta. Intenta de nuevo.")
    else:
        print("¡Inicio de sesión exitoso!")
        break

print(f"¡Bienvenido!, {user}")
#============================================================================================

Pantalla_de_carga(max_duration=5)

#========================= Menu =================

TIMEOUT = 600  # Para 10 minutos se usan 600 segundos.

def obtener_fecha_operacion():
    while True:
        fecha_str = input("Ingresa la fecha de operación (dd/mm/yyyy): ").strip()
        try:
            # Parsear la fecha para validarla
            fecha_dt = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            # Extraer día, mes, año y almacenar en tupla
            fecha_tuple = (fecha_dt.day, fecha_dt.month, fecha_dt.year)
            print(f"Fecha de operación establecida: {fecha_tuple[0]:02d}/{fecha_tuple[1]:02d}/{fecha_tuple[2]}")
            return fecha_tuple
        except ValueError:
            print("Error: Formato de fecha incorrecto o fecha inválida. Usa dd/mm/yyyy.")

def mostrar_menu():
    print(f"{BLUE}\n--- Menu de servicios ---{RESET}")
    print(f"{BLUE}1. Ping de servidores{RESET}")
    print(f"{BLUE}2. Gestión de Archivos{RESET}")
    print(f"{BLUE}3. Lector de textos (pendiente){RESET}")
    print(f"{BLUE}4. Salir del programa{RESET}")

def gestionar_archivos():
    while True:
        print(f"{YELLOW}\n--- Submenú: Gestión de Archivos ---{RESET}")
        print(f"{YELLOW}1. Listar archivos{RESET}")
        print(f"{YELLOW}2. Leer archivo{RESET}")
        print(f"{YELLOW}3. Escribir/Sobrescribir archivo{RESET}")
        print(f"{YELLOW}4. Añadir a archivo{RESET}")
        print(f"{YELLOW}5. Volver al menú principal{RESET}")

        opcion_archivo = input(f"{YELLOW}Selecciona una opción de gestión de archivos: {RESET}").strip()

        if opcion_archivo == '1':
            print("\n--- Archivos Disponibles en el directorio actual ---")
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            if files:
                for i, f in enumerate(files):
                    print(f"{i+1}. {f}")
            else:
                print("No hay archivos en el directorio actual.")

        elif opcion_archivo == '2':
            filename = input("Ingresa el nombre del archivo a leer: ").strip()
            try:
                with open(filename, 'r', encoding='utf-8') as f: # Añadi encoding para evitar errores
                    print("\n--- Opciones de lectura ---")
                    print("1. Leer todo (read())")
                    print("2. Leer línea por línea (readline()) - para archivos grandes")
                    print("3. Leer todas las líneas en una lista (readlines())")
                    read_option = input("Selecciona una opción de lectura: ").strip()

                    if read_option == '1':
                        content = f.read()
                        print(f"\n--- Contenido de '{filename}' (read()) ---")
                        print(content)
                    elif read_option == '2':
                        print(f"\n--- Contenido de '{filename}' (readline()) ---")
                        line_num = 1
                        while True:
                            line = f.readline()
                            if not line: # Si no hay más líneas, termina
                                break
                            print(f"Línea {line_num}: {line.strip()}")
                            line_num += 1
                    elif read_option == '3':
                        lines = f.readlines()
                        print(f"\n--- Contenido de '{filename}' (readlines()) ---")
                        for i, line in enumerate(lines):
                            print(f"Línea {i+1}: {line.strip()}")
                    else:
                        print("Opción de lectura no válida.")
            except FileNotFoundError:
                print(f"Error: El archivo '{filename}' no fue encontrado.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{filename}'.")
            except Exception as e:
                print(f"Ocurrió un error inesperado al leer el archivo: {e}")

        elif opcion_archivo == '3':
            fecha_operacion_tuple = obtener_fecha_operacion()
            fecha_formateada = f"[{fecha_operacion_tuple[0]:02d}/{fecha_operacion_tuple[1]:02d}/{fecha_operacion_tuple[2]}] "

            filename = input("Ingresa el nombre del archivo a escribir (se sobrescribirá si existe): ").strip()
            content = input("Ingresa el contenido a escribir: ")
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(fecha_formateada + content) # Prepend date
                print(f"Archivo '{filename}' escrito exitosamente con la fecha de operación.")
            except PermissionError:
                print(f"Error: No tienes permisos para escribir en el archivo '{filename}'.")
            except Exception as e:
                print(f"Ocurrió un error inesperado al escribir el archivo: {e}")

        elif opcion_archivo == '4':
            fecha_operacion_tuple = obtener_fecha_operacion()
            fecha_formateada = f"[{fecha_operacion_tuple[0]:02d}/{fecha_operacion_tuple[1]:02d}/{fecha_operacion_tuple[2]}] "

            filename = input("Ingresa el nombre del archivo al que añadir contenido: ").strip()
            content = input("Ingresa el contenido a añadir: ")
            try:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(f"\n{fecha_formateada}{content}") # Añadir nueva línea y fecha para el contenido
                print(f"Contenido añadido al archivo '{filename}' exitosamente con la fecha de operación.")
            except PermissionError:
                print(f"Error: No tienes permisos para añadir al archivo '{filename}'.")
            except Exception as e:
                print(f"Ocurrió un error inesperado al añadir al archivo: {e}")

        elif opcion_archivo == '5':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def loop_del_menu():
    ultima_interaccion = time.time() # revisa el inicio o ultima interaccion

    while True:
        tiempo_actual = time.time()

        # Comprueba el tiempo de inactividad
        if tiempo_actual - ultima_interaccion > TIMEOUT:
            print("\n--- Deteccion de Inactividad ---")
            print(f"Han pasado mas de {TIMEOUT} segundos sin interaccion.")

            # esta es la pausa para el usuario
            respuesta = input("¿Deseas continuar en el menu? (s/n): ").lower().strip()

            if respuesta == 's':
                print("Continuando el menu...")
                ultima_interaccion = time.time() # Reinicia el temporizador
            else:
                print("Saliendo del programa por inactividad.")
                break # Sale del bucle principal

        mostrar_menu()
        choice = input("Selecciona una opción: ").strip()

        if choice == '1':
            print("Has seleccionado la Opción 1. Ping de servidores.")
            ultima_interaccion = time.time() # esta parte hace que se reinicie la ultima interaccion asi evitando una pausa inesperada despues de estar "inactivo" 10 minutos (●ˇ∀ˇ●)
        #================================== Ping y heartbeat ==================================
            Pantalla_de_carga(max_duration=5)

            print("Ping de servidores seleccionado...")

            Pantalla_de_carga(max_duration=5)

            def heartbeat_url(url):
                try:
                    # Asegúrate de usar un esquema (http/https) para la URL PLZ (x_x)
                    full_url = url if url.startswith(('http://', 'https://')) else 'https://' + url
                    respuesta = requests.get(full_url, timeout=5) #esto puede aumentar el tiempo entre pings
                    if respuesta.status_code == 200:
                        print(f"{full_url} esta activo 💚 (Status: {respuesta.status_code})")
                        return True # Retorna True si está activo
                    else:
                        print(f"💔💥{full_url} no responde 💔 (Status: {respuesta.status_code}) / Iniciando diagnostico..")
                        return False # Retorna False si no responde 
                except requests.exceptions.RequestException as e:
                    print(f"❤️‍💥️{full_url} no responde 💔 / Iniciando diagnostico..")
                    return False # Retorna False si hay una excepción

            is_active = heartbeat_url("https://smscompanyip.onrender.com") # Ahora se manejará la adición de 'https://' internamente y se captura el estado

            #==================================== Ticket ====================================
            if not is_active: # Solo entra a diagnóstico si el servidor no está activo
                print("--------- Diagnostico ---------")
                print("aun tiene internet en su servidor?: si/no ")
                has_internet = input().lower().strip() # Captura la entrada y la convierte a minúsculas

                if has_internet == "si": # Comparar la variable capturada
                    print("Su problema es sobre switches\tporfavor dirigase a www.SMS.com")
                else:
                    print("Iniciando ticket...")

                print(f"\n========== TICKET ==========")
                # Añadi validación para asegurar que los inputs son numéricos cuando es necesario
                while True:
                    try:
                        num_tienda = float(input("Ingrese su numero de tienda: "))
                        break
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número para la tienda.")

                while True:
                    try:
                        num_server = float(input("Ingrese el numero del servidor caido: "))
                        break
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número para el servidor.")

                causa = input("Cual fue la causa del fallo del servidor?: ")
                ip_servidor = input("Ingrese la ip de su servidor: ")
                print(f"\n============================")

                print(f"\n{GREEN}========== RESUMEN =========={RESET}")
                print(f"{GREEN}Numero de tienda: {num_tienda}{RESET}")
                print(f"{GREEN}Numero de servidor: {num_server}{RESET}")
                print(f"{GREEN}IP del servidor : {ip_servidor}{RESET}")
                print(f"{GREEN}Causa de caida: {causa}{RESET}")



                print(f"{GREEN}=============================={RESET}")

                print("\nPara mas informacion y asistencia dirigase a www.SMS.com")
            #==================================================================================
            #===============================================================================
        elif choice == '2':
            print("Has seleccionado la Opción 2. Gestión de Archivos.")
            ultima_interaccion = time.time()
            gestionar_archivos()

        elif choice == '3':
            print("Has seleccionado la Opción 3. Lector de textos.")
            ultima_interaccion = time.time()
            Pantalla_de_carga(max_duration=5)
            print("Lector de textos activo. ")
            texto_a_leer = input("Ingresa el texto que quieres leer: ")
            print(f"El texto ingresado fue: {texto_a_leer}")
            with open("LSIDHCO.txt", mode="w") as a:
                texto_a_leer = a.read()
                print("contenido")

        #========================================================
        elif choice == '4': # Opción de salida re-numerada
            print("Saliendo del menú. ¡Hasta luego!")
            break # Sale del bucle principal
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            ultima_interaccion = time.time() # esto tambien reinicia el contador aunque hubiera estado mal el input


loop_del_menu()

#===============================================