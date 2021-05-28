import obd

def tour_min():
	connection = obd.OBD() #connexion automatique
	tr_min = connection.query(command.obd.RPM) #envoi la donnée tour/min et retourne la réponse
	print("tour/min = %d"% tr_min)

def vitesse():
	connection = obd.OBD() #connexion automatique
	vitess = connection.query(command.obd.SPEED) #envoi la donnée vitesse et retourne la réponse
	print("vitesse = %d"% vitess)

def temp_liquide_refroid():
	connection = obd.OBD() #connexion automatique
	temp = connection.query(command.obd.COOLANT_TEMP) #envoi la donnée de la température du liquide et retourne la réponse
	print("temperature liquide de refroidissement = %d"% temp)

def temp_huile_mot():
	connection = obd.OBD() #connexion automatique
	temp = connection.query(command.obd.OIL_TEMP) #envoi la donnée température de l'huile et retourne la réponse
	print("temperature de l'huile moteur = %d"% temp)

def niveau_carburant():
	connection = obd.OBD() #connexion automatique
	niv = connection.query(command.obd.FUEL_LEVEL) #envoi la donnée du niveau de carburant et retourne la réponse
	print("Niveau de carburant = %d"% niv)

def conso_carburant():
	connection = obd.OBD() #connexion automatique
	conso = connection.query(command.obd.FUEL_RATE) #envoi la donnée tour/min et retourne la réponse
	print("consommation de carburant = %d"% conso)
