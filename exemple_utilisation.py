# Exemple d'utilisation des drivers 

from dynamixel_driver import *    # Importation des fonctions
import time

# Création du driver et initialisation
ax_12a_driver = Driver('/dev/ttyUSB0', 1000000)
ax_12a_driver.init()

# Création des deux servo
# Servo 4Angle min: 300, angle max: 850
servo4 = Servo("Servomoteur 4", 4, ax_12a_driver)
servo6 = Servo("Servomoteur 6", 6, ax_12a_driver)

# Ping une plage d'ID
for i in range(20):
    print("ID: %d, ping: %d" % (i, ax_12a_driver.ping(i)))

# Indique des informations sur le servo 4
print("Position du servo 4: %d" % servo4.lire_position())
print("Etat du couple du servo 4: %d" % servo4.lire_activation_couple())

# Lit la mémoire du servo 4
servo4.lire_memoire(0, 48)

ax_12a_driver.fermer_connection()