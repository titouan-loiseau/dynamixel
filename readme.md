Dynamixel Repo
======

Repo pour les fichiers et les programmes des servo-moteurs. 

Servo-moteurs
------
Ref: AX-12A

Control Tables:

EEPROM AREA

| Addresse | Taille (octet) | Nom | Description | Accès | Valeur Initiale |
|---|---|---|---|---|---|
| 0 | 2 | Model Number | Numéro du modèle | R | 12 |
| 2 | 1 | Firmware Version | Verison du firmware | R | - |
| 3 | 1 | ID | ID Dynamixel | RW | 1 |
| 4 | 1 | Baud Rate | Vitesse de communication | RW | 1 |
| 5 | 1 | Return Delay Time | Délai de réponse | RW | 250 |
| 6 | 2 | CW Angle Limit | Numéro du modèle | R | 12 |
| 8 | 2 | CCW Angle Limit | Numéro du modèle | R | 12 |
| 11| 1 | Temperature Limit | Numéro du modèle | R | 12 |
| 12| 1 | Min Voltage Limit | Numéro du modèle | R | 12 |
| 13| 1 | Max Voltage Limit | Numéro du modèle | R | 12 |
| 14| 2 | Model Number | Numéro du modèle | R | 12 |
| 16| 1 | Model Number | Numéro du modèle | R | 12 |
| 17| 1 | Model Number | Numéro du modèle | R | 12 |
| 18| 1 | Model Number | Numéro du modèle | R | 12 |