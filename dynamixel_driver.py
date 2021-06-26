# FONCTIONS DE CONTROLE DES SERVO-MOTEURS DYNAMIXEL

import os

from dynamixel_sdk import *

PROTOCOL_VERSION = 1.0

class Servo:
    def __init__(self, name, id, driver):
        self.name = name     # Nom personnalisable du servo
        self.id = id         # ID Dynamixel du servo
        self.driver = driver # driver qui prendra en charge les communications USB

        # ADDRESSES POUR LES AX-12A
        self.addr_activation_couple = 24
        self.addr_position_voulue   = 30
        self.addr_position_actuelle = 36
        pass
    def tourner(self):
        print("test")

class Driver:
    def __init__(self, port, baudrate):
        self.port = port
        self.portHandler = PortHandler(port)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)
        self.initiated = 0
        self.baudrate = baudrate
        pass

    def getch():
        if os.name == 'nt':
            import msvcrt
            return msvcrt.getch().decode()
        else:
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    def init(self):
        if self.portHandler.openPort():
            print("Port ouvert avec succès")
        else:
            print("Erreur lors de l'ouverture du port")
            print("Appuyez sur n'importe quelle touche pour quitter...")
            self.getch()
            quit()
        
        if self.portHandler.setBaudRate(self.baudrate):
            print("Baudrate changé avec succès")
        else:
            print("Erreur lors du changement du baudrate")
            print("Appuyez sur n'importe quelle touche pour quitter...")
            self.getch()
            quit()
        self.initiated = 1
    
    def exemple(self):
        if self.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
        else:
            print("test")

    def ping(self, id):
        if self.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
        else:
            # Le ping lit la valeur dans l'addresse 0 (numéro de modèle) et regarde si sa valeur est non nulle, auquel cas le servo existe
            dxl_model_number, dxl_comm_result, dxl_error = self.packetHandler.read2ByteTxRx(self.portHandler, id, 0)
            if dxl_comm_result != COMM_SUCCESS or dxl_model_number == 0:
                print("PING: L'ID %d n'existe pas" % id)
            elif dxl_error != 0:
                print("ERREUR LORS DE LA LECTURE DU PAQUET : %s" % self.packetHandler.getRxPacketError(dxl_error))
            else: 
                print("PING: L'ID %d est présent sur le bus" % id)
    
    def lire_memoire(self, id, taille):
        if self.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
        else:
            i = 0
            while i <= taille :
                j = 0
                mem_str = ("MEM [0x%04X]: " % i)
                while j < 8:
                    dxl_memory_read, dxl_comm_result, dxl_error = self.packetHandler.read1ByteTxRx(self.portHandler, id, i+j)
                    if dxl_comm_result != COMM_SUCCESS:
                        print("ERREUR DANS LA LECTURE DE LA MEMOIRE A L'ADDRESSE %d" % i)
                        return
                    elif dxl_error != 0:
                        print("ERREUR LORS DE LA LECTURE DU PAQUET A L'ADRESSE %d: %s" % (i, self.packetHandler.getRxPacketError(dxl_error)))
                        return
                    else: 
                        mem_str += ("%02X " % dxl_memory_read)
                    if i+j <= taille:
                        j += 1
                    else:
                        j = 10
                print(mem_str)
                i+=8 