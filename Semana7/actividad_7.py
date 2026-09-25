#Eric Daniel Carrillo Torres/ 27-08-2026 / 2720381

#hacer un codigo que te muestre el estado de un servidor y que con "time" te haga un ping cada 4-5~ min y si  el servidor no hace ping hacer un input para hacer un ticket y hacer una seccion para poner informacion y de la tienda y la causa  y dar un overall del ticket pero si hay internet en los servidore spero no r3sponden es una situacion de switches y hacer un elif sobre que el problema es de switches y enviar un correo (de forma estilizada)

## TODAS LAS VARIABLES SON PROVISIONALES Y UNA IDEA DE COMO PODRIA ESTAR ESTRUCTURADO EL CODIGO FINAl o(≧口≦)o y posiblemente no compile asi como esta 

GREEN = "\033[32m"
RESET = "\033[0m"

import time

#aqui va el codigo necesario para hacer el login del servidor y para que pueda empezar el "heartbeat" osea el ping constante.. sigo trabajando en como poner un servidor （；´д｀）ゞ

time.sleep(500)

if servidor {ip_server} == 1:
  print(f"Servidor {ip_server} SERVIDOR ACTIVO 💚")
else:
  print(f"Servidor {ip_server} SERVIDOR CAIDO 💔 / Iniciando diagnostico..") 

print("aun tiene internet en su servidor?: si/no ")
int(input())

if input == si:
  print("Su problema es sobre switches\tporfavor dirigase a www.SMS.com")
  break

else:
  print("Iniciando ticket...")

print(f"\n========== TICKET ==========")
num_tienda = float(input("Ingrese su numero de tienda: "))
num_server = float(input("Ingrese el numero del servidor caido: "))
causa = float(input("Cual fue la causa del fallo del servidor?: "))
ip_servidor = float(input("Ingrese la ip de su servidor: "))
print(f"\n============================")

#en teoria tendria que despues de esto ^ deberia ir a esto v <( - > - )>

print(f"\n{GREEN}========== RESUMEN =========={RESET}")
print(f"{GREEN}Numero de tienda: {num_tienda}{RESET}")
print(f"{GREEN}Numero de servidor: {num_server}{RESET}")
print(f"{GREEN}IP del servidor : {ip_servidor}{RESET}")
print(f"{GREEN}Causa de caida: {causa}{RESET}")

print("\tPara mas informacion y asistencia dirigase a www.SMS.com")

print(f"{GREEN}=============================={RESET}")

#Creo que asi deberia estar bien buscare como poder hostear un servidor en otro dispositivo y conectrlo a vscode aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 
