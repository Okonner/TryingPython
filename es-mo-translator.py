#Translator Spanish-Morse
alfabeto=[
('a','.-')
,('b','-...')
,('c','-.-.')
,('ch','----')
,('d','-..')
,('e','.')
,('f','..-.')
,('g','--.')
,('h','....')
,('y','..')
,('j','--')
,('k','-.-')
,('m','.-..')
,('n','--')
,('l','-.')
,('ñ','--.--')
,('o','---')
,('p','.--.')
,('q','--.-')
,('r','.-.')
,('s','...')
,('t','-')
,('u','..-')
,('v','...-')
,('w','.--')
,('x','-..-')
,('y','-.--')
,('z','--..')]

modos = [('t', 'Español-Morse'),('m', 'Archivos')]

class record():
    users = []
    def __init__(self, user, texto1, texto2):
        record.users.append(self)
        self.usuario = user
        self.mitexto = texto1
        self.restexto = texto2

    # esto es para configurar la salida
    def __str__(self):
        return "Usuario: {}, Texto:{}, Traducción:{}".format(self.usuario, self.mitexto, self.restexto)

def mostrar():
	print([str(record) for record in record.users])

def traducir(modo, texto):
	res=""
	for i in texto:
		if i!=" ":
			for j in alfabeto:
				if i==j[0]:
					res += j[1]
		else:
			res += "  "
	return res

def menu():
	modo = input("MENU\nPara traducir "
			+ modos[0][1] + ": " + modos[0][0]
			+"\nPara ver " + modos[1][1] + ": " + modos[1][0]
			+"\nPara salir: e"
			+"\n")
	while modo!=modos[0][0] and modo!=modos[1][0] and modo!="e":
		modo = input("Para traducir" + modos[0][1] + ": " + modos[0][0]
			+"\nPara " + modos[1][1] + ": " + modos[1][0]
			+"\n")
	if modo==modos[0][0]:
		text = input("Escribe el texto a traducir\n")
		traducido = traducir(modo, text)
		print("Tu texto:\n"
		+ text
		+ "\nTraducción:\n"
		+ traducido)
		if input("¿Quieres guardar esta traducción? s/n\n")=="s":
			record(input("Escribe tu nombre"), text, traducido)
			print("Archivo guardado!\n")
			menu()
		else:
			menu()
	elif modo==modos[1][0]:
		mostrar()
		menu()
	elif modo=="e":
		print("Bye Bye!")

# inicializacion del programa
menu()