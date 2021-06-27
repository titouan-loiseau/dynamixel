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
        self.seuil_rotation = 10
        pass

    # Fait tourner le moteur à l'angle donné
    def tourner(self, angle):
        if self.driver.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
        else:
            dxl_comm_result, dxl_error = self.driver.packetHandler.write2ByteTxRx(self.driver.portHandler, self.id, self.addr_position_voulue, angle)
            if dxl_comm_result != COMM_SUCCESS:
                print("ERREUR DANS L'ECRITURE DE L'ANGLE VOULU : %s" % self.driver.packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("ERREUR LORS DE LA LECTURE DU PAQUET : %s" % self.driver.packetHandler.getRxPacketError(dxl_error))

    # Permet d'activer ou non le bloquage de la rotation
    def bloquer_rotation(self, valeur):
        if self.driver.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
        else:
            if not (valeur == 0 or valeur == 1):
                print("ERREUR: La valeur de l'activation ne peut être que 0 ou 1.")
            else:
                dxl_comm_result, dxl_error = self.driver.packetHandler.write1ByteTxRx(self.driver.portHandler, self.id, self.addr_activation_couple, valeur)
                if dxl_comm_result != COMM_SUCCESS:
                    print("ERREUR DANS L'ECRITURE DE LA VALEUR D'ACTIVATION DU COUPLE : %s" % self.driver.packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("ERREUR LORS DE LA LECTURE DU PAQUET : %s" % self.driver.packetHandler.getRxPacketError(dxl_error))

    # Lire la position actuelle stockée dans la RAM et renvoie: -1 (erreur de driver ou de lecture), position (position dans la RAM)
    def lire_position(self):
        if self.driver.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
            return -1
        else:
            dxl_present_position, dxl_comm_result, dxl_error = self.driver.packetHandler.read2ByteTxRx(self.driver.portHandler, self.id, self.addr_position_actuelle)
            if dxl_comm_result != COMM_SUCCESS:
                print("ERREUR DANS LA LECTURE DE LA POSITION : %s" % self.driver.packetHandler.getTxRxResult(dxl_comm_result))
                return -1
            elif dxl_error != 0:
                print("ERREUR LORS DE LA LECTURE DU PAQUET : %s" % self.driver.packetHandler.getRxPacketError(dxl_error))
                return -1
            else:
                return dxl_present_position

    # Lire la valeur du bloquage de rotation et renvoie: -1 (erreur de driver ou de lecture), valeur (valeur du bloquage)
    def lire_activation_couple(self):
        if self.driver.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
            return -1
        else:
            dxl_torque_status, dxl_comm_result, dxl_error = self.driver.packetHandler.read2ByteTxRx(self.driver.portHandler, self.id, self.addr_activation_couple)
            if dxl_comm_result != COMM_SUCCESS:
                print("ERREUR DANS LA LECTURE DE L'ETAT D'ACTIVATION DU COUPLE : %s" % self.driver.packetHandler.getTxRxResult(dxl_comm_result))
                return -1
            elif dxl_error != 0:
                print("ERREUR LORS DE LA LECTURE DU PAQUET : %s" % self.driver.packetHandler.getRxPacketError(dxl_error))
                return -1
            else:
                return dxl_torque_status

    # Print la mémoire du servo et renvoie: -1 (erreur du driver ou de lecture), array[] (tableau des valeurs de la mémoire)
    def lire_memoire(self, début, fin):
        if self.driver.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
            return -1
        else:
            i = début
            tableauMem = []
            while i <= fin :
                j = 0
                mem_str = ("MEM [0x%04X]: " % i)
                while j < 8:
                    dxl_memory_read, dxl_comm_result, dxl_error = self.driver.packetHandler.read1ByteTxRx(self.driver.portHandler, self.id, i+j)
                    if dxl_comm_result != COMM_SUCCESS:
                        print("ERREUR DANS LA LECTURE DE LA MEMOIRE A L'ADDRESSE %d" % i)
                        return -1
                    elif dxl_error != 0:
                        print("ERREUR LORS DE LA LECTURE DU PAQUET A L'ADRESSE %d: %s" % (i, self.driver.packetHandler.getRxPacketError(dxl_error)))
                        return -1
                    else: 
                        mem_str += ("%02X " % dxl_memory_read)
                        tableauMem.append(dxl_memory_read)
                    if i+j <= fin:
                        j += 1
                    else:
                        j = 10
                print(mem_str)
                i+=8
            return tableauMem




class Driver:
    def __init__(self, port, baudrate):
        self.port = port
        self.portHandler = PortHandler(port)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)
        self.initiated = 0
        self.baudrate = baudrate
        pass

    # Lit le caractère dans la console
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

    # Initialise les ports USB 
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

    # Ping l'ID passé en argument et renvoie: -1 (erreur d'initialisation du driver ou de lecture), 0: ID non présent, 1: ID présent
    def ping(self, id):
        if self.initiated == 0:
            print("Le driver n'a pas encore été initialisé. Veuillez appeler driver.init()")
            return -1
        else:
            # Le ping lit la valeur dans l'addresse 0 (numéro de modèle) et regarde si sa valeur est non nulle, auquel cas le servo existe
            dxl_model_number, dxl_comm_result, dxl_error = self.packetHandler.read2ByteTxRx(self.portHandler, id, 0)
            if dxl_comm_result != COMM_SUCCESS or dxl_model_number == 0:
                return 0
            elif dxl_error != 0:
                print("ERREUR LORS DE LA LECTURE DU PAQUET : %s" % self.packetHandler.getRxPacketError(dxl_error))
                return -1
            else: 
                return 1
    
    # Ferme la connexion du driver
    def fermer_connection(self):
        self.initiated = 0
        self.portHandler.closePort()