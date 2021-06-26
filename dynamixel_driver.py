# FONCTIONS DE CONTROLE DES SERVO-MOTEURS DYNAMIXEL

import os

from dynamixel_sdk import *

PROTOCOL_VERSION = 1.0

class Servo:
    def __init__(self, name, id ):
        self.name = name     # Nom personnalisable du servo
        self.id = id         # ID Dynamixel du servo

        # ADDRESSES POUR LES AX-12A
        self.addr_activation_couple = 24
        self.addr_position_voulue   = 30
        self.addr_position_actuelle = 36

        # VALEURS PAR DEFAUT POUR LES AX-12A
        self.baudrate = 1000000
        pass
    def tourner(self):
        print("test")

class Driver:
    def __init__(self, port):
        self.port = port
        self.portHandler = PortHandler(port)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)
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