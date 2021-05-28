# Project_embedded_linux
# -----------------------
# Récupération des trames de la voiture
  # L’acquisition des informations
    Le boitier ELM327

    L’ELM327 est un outil de diagnostic sous la forme d’un petit boitier, il permet de lire et analyser les  données  extraitesde l’OBD2. Couplé  avec  un  ordinateur  et  un programme  (que  nous avons tenté de réaliser), l’ELM327 permet denumériser clairement les codes du moteur, de voir et d’enregistrer les données. Mais il est également possible de voir les performances et les données en temps réel. Ce type d’outil fonctionne avec tous les véhicules qui ont été produit après l’instauration de la norme OBD2 et avec ceux qui suivent la réglementation EOBD, plus tardive. L’ELM327 est l’interface la plus standard. C’est celle qui lit le plus de données, mais c’est aussi celle qui est compatible avec tous les protocoles OBD: KWP, CAN, VPN, PWM, etc. Ce protocole diffère sur chaque voiture. La communication avec cette interface se fait selon une logique maitre-esclave, où l'on envoi une donnée «question» puis on attend la donnée «réponse» qui contient l’information que l’on a demandée et qui provient du calculateur moteur. 

On a ensuite autorisé la communication via USB pour notre raspberry avec la commande "rasp-config"

# Récupération des trames

    Après  avoir établit  la liaisonavec  l’ELM327,  nous  devons  récupérer  et  interpréter  les informations de la voiture. Celles-ci sont transmises via des chaînes de caractères que l’on appelle des trames. Pour récupérer les informations, on va dans un premier temps envoyer une trame maîtressequi va poser une question, soit demander l’information souhaitée,et on recevra ensuite une trame esclave qui nous donnera les informations demandée
    
    Trame maitresse:
    Sur la trame maitresse, seul les 4 bits de poids fort nous intéresse. Les deux premiers correspondent au protocole que l'on choisit (dans notre cas : 01) et les 2 suivants correspondent à l'information que l'on souhaite récupérer (par exemple la vitesse de la voiture)
    
    Trame esclave:
    Sur la trame maitresse, les 8 premiers bits de poids forts nous intéresse. Les deux premiers sont en fonction du protocole que l'on choisit (dans notre cas 41), les 2 suivants sont l'information que l'on récupère. Les 4 suivants correspondent à la valeur de l'information. Les deux premiers sont A et les deux suivantes sont B. Les valeurs A et B nous permettront de mettre en forme les valeurs que l'on récupère.

# les différentes trames maîtres que l'on va envoyer
    tout les bits après les 4 premiers vaudront 0
    
    Tour/minute : 01 0C
    Vitesse : 01 0D
    Niveau d'essence %: 01 2F
    Température liquide refroidissement : 01 05
    Température huile moteur : 01 5C
    Consommation carburant (l/h) : 01 5E
    
    Toutes ces caractéristiques sont disponibles sur https://www.elm327.fr/norme-obd/modes-obd/ et bien d'autres encore
    
# Les résultats

    Les informations que nous allons récupérer sont ensuite à mettre en forme. Il faut faire des calculs afin d'avoir les bonnes informations.
    
    Tour/min : [(256*A)+B]/4
    Vitesse : A+B
    Niveau d'essence % : Pas de 
