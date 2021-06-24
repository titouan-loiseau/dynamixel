Dynamixel Repo
======

Repo pour les fichiers et les programmes des servo-moteurs. 

Setup
------

1. Cloner ce repo dans un dossier 
`git clone https://github.com/titouan-loiseau/dynamixel.git .`
**Ne pas oublier le .**

2. Cloner les SDK Dynamixel
`git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git`

3. Ouvrir `DynamixelSDK/python` dans un terminal

4. Exécuter:
`python setup.py install`

5. Une fois la librairie installée, vous pouvez supprimer le fichier `DynamixelSDK` 

Servo-moteurs
------
Ref: AX-12A

Control Tables:

EEPROM AREA

| Addresse | Taille (octet) | Nom | Description | Accès | Valeur Initiale |
|----|---|---------------------|------------------------------|----|------|
| 0  | 2 | Model Number        | Numéro du modèle             | R  | 12   |
| 2  | 1 | Firmware Version    | Verison du firmware          | R  | -    |
| 3  | 1 | ID                  | ID Dynamixel                 | RW | 1    |
| 4  | 1 | Baud Rate           | Vitesse de communication     | RW | 1    |
| 5  | 1 | Return Delay Time   | Délai de réponse             | RW | 250  |
| 6  | 2 | CW Angle Limit      | Limite d'angle sens horaire  | RW | 0    |
| 8  | 2 | CCW Angle Limit     | Limite d'angle sens trigo    | RW | 1023 |
| 11 | 1 | Temperature Limit   | Température interne maximale | RW | 70   |
| 12 | 1 | Min Voltage Limit   | Tension d'entrée minimale    | RW | 60   |
| 13 | 1 | Max Voltage Limit   | Tension d'entrée maximale    | RW | 140  |
| 14 | 2 | Max Torque          | Couple maximal               | RW | 1023 |
| 16 | 1 | Status Return Level | ?                            | RW | 2    |
| 17 | 1 | Alarm LED           | LED d'alarme                 | RW | 36   |
| 18 | 1 | Shutdown            | Information d'erreur         | RW | 36   |

RAM

| Addresse | Taille (octet) | Nom | Description | Accès | Valeur Initiale |
|----|---|-----------------------|----------------------------------------|----|--------------------------|
| 24 | 1 | Torque Enable         | Couple moteur ON/OFF                   | RW | 0                        |
| 25 | 1 | LED                   | LED ON/OFF                             | RW | 0                        |
| 26 | 1 | CW Compliance Margin  | Marge de tolérence sens horaire        | RW | 1                        |
| 27 | 1 | CCW Compliance Margin | Marge de tolérence sens trigo          | RW | 1                        |
| 28 | 1 | CW Compliance Slope   | Pente de tolérence sens horaire        | RW | 32                       |
| 29 | 1 | CCW Compliance Slope  | Pente de tolérence sens trigo          | RW | 32                       |
| 30 | 2 | Goal Position         | Position voulue                        | RW | -                        |
| 32 | 2 | Moving Speed          | Vitesse de mouvement                   | RW | 70                       |
| 34 | 2 | Torque Limit          | Limite de couple                       | RW | Max Torque (addresse 14) |
| 36 | 2 | Present Position      | Position actuelle                      | R  | -                        |
| 38 | 2 | Present Speed         | Vitesse actuelle                       | R  | -                        |
| 40 | 2 | Present Load          | Charge actuelle (cf lien)              | R  | -                        |
| 42 | 1 | Present Voltage       | Tension actuelle                       | R  | -                        |
| 43 | 1 | Present Temperature   | Température actuelle                   | R  | -                        |
| 44 | 1 | Registered            | Si une instruction est inscrite        | R  | 0                        |
| 46 | 1 | Moving                | Inforation de mouvement                | R  | 0                        |
| 47 | 1 | Lock                  | Si la partie EEPROM peut être modifiée | RW | 0                        |
| 48 | 2 | Punch                 | Seuil d'intensité minimum              | RW | 32                       |

Lien pour plus d'infos: 
https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/