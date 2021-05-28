#création d'un objet pour pouvoir lire et envoyer des données en série
ser = serial.Serial(
	port = '/dev/ttyUSB0', #port connecté à la rasp
	baudrate = 38400,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

def tour_min():
	ser.write(str.encode('01 0C\r\n')) #envoi de la donnée que l'on souhaite récupérer
	x = ser.readline() #récupération des données souhaitées
	val = str(x) #passage des données en chaine de caractère
	valeur = val[15:18] #récupération des caractères de la valeur A
	A = int(valeur, 16) #transformation de A en entier
	vale = val [18:21] #récupération des caractères de la valeur B
	B = int(vale,16) #transformation de B en entier
	tr_min = ((256*A)+B)/4 #interprétation des trames
	print("tour/min = %d"% tr_min)

def vitesse():
	ser.write(str.encode('01 0D\r\n')) #envoi de la donnée que l'on souhaite récupérer
	x = ser.readline() #récupération des données souhaitées
	val = str(x) #passage des données en chaine de caractère
	valeur = val[15:18] #récupération des caractères de la valeur A
	A = int(valeur, 16) #transformation de A en entier
	vale = val [18:21] #récupération des caractères de la valeur B
	B = int(vale,16) #transformation de B en entier
	vitess = A+B #interprétation des trames
	print("vitesse = %d"% vitess)
	
def niveau_essence():
	ser.write(str.encode('01 2F\r\n')) #envoi de la donnée que l'on souhaite récupérer
	x = ser.readline() #récupération des données souhaitées
	val = str(x) #passage des données en chaine de caractère
	valeur = val[15:18] #récupération des caractères de la valeur A
	A = int(valeur, 16) #transformation de A en entier
	vale = val [18:21] #récupération des caractères de la valeur B
	B = int(vale,16) #transformation de B en entier
	niveau = #interprétation des trames
	print("niveau d'essence = %d"% niveau)
