file_texto = open("data.in","r+") 
lines = file_texto.readlines()
file_texto.close()
print(lines)


# Se te ocurre como separar la lista lines en toras lsitas mas chiquitas? por categoria 

cocina = []
frases = []
iconico = []
especialidades = []
curiosidades = []


#Aparte hay qeu leer un dictionario de canciones con links 
canciones={}

file_canciones = open("diccionario_canciones.txt", "r")

##googlea como hacerlo 