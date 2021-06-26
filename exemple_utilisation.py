# Exemple d'utilisation des drivers 

from dynamixel_driver import *    # Importation des fonctions

ax_12a_driver = Driver('/dev/ttyUSB0', 1000000)
ax_12a_driver.init()

servo4 = Servo("Servomoteur 4", 4, ax_12a_driver)

ax_12a_driver.ping(4)