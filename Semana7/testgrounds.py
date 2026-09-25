#========== importaciones ==========
import os                           
import platform
import time
#===================================

#========== Colores ==========
GREEN = "\033[32m"
RESET = "\033[0m"
#=============================

#========== Heartbeat ==========

#===============================

def hacer_ping(host):
    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    
    comando = f"ping {parametro} 1 {host}"
    respuesta = os.system(comando)
    
    if respuesta == 0:
        print(f"{host} esta activo 💚")
    else:
        print(f"¡{host} no responde 💔! / Iniciando diagnostico..")

# Prueba la función
hacer_ping("https://smscompanyip.onrender.com")


