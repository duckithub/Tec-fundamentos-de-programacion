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
    
    # Si el retorno es 0, el host está activo
    if respuesta == 0:
        print(f"¡{host} está encendido y responde!")
    else:
        print(f"¡{host} no responde o está apagado!")

# Prueba la función
hacer_ping("https://smscompanyip.onrender.com")


