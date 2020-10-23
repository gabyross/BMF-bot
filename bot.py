import ast

'''# Método que imprimirá por pantalla la información que reciba
def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text

    print("ID: " + str(id) + " MENSAJE: " + mensaje)'''


#variables globales
list_cocina = []
list_frases = []
list_iconico = []
list_especialidades = []
list_curiosidades = []
songs

# Permite cargar un dictionario de un archivo que recibe como input
def cargar_dictionario(file_name):
    file_c = open(file_name, "r")
    contents = file_c.read()
    dictionary = ast.literal_eval(contents)
    file_c.close()
    return dictionary


#------------MAIN PART STARTS HERE
def main():
    file = open("data.in","r+") 
    lines = file.read().splitlines()

    #declaracion de las categorias
    global list_cocina
    global list_frases
    global list_iconico
    global list_especialidades
    global list_curiosidades
    global songs 

    #Cargo el diccionario de canciones
    songs = cargar_dictionario("diccionario_canciones.txt")
    

    flag = ""
    #vamos a usar un flag que nos indicara que hacer segun la seccion donde estemos
    for line in lines:
        ##seteamos el flag solo cuando empieza una categoria
        if line == "cocina":
            flag = "cocina"
            continue
        elif line == "especialidades":
            flag = "especialidades"
            continue
        elif line == "iconico":
            flag = "iconico"
            continue
        elif line == "frases":
            flag = "frases"
            continue
        elif line == "curiosidades":
            flag = "curiosidades"
            continue
        print(flag)
        ##ahora dependiendo del flag agregamos las lineas
        if flag == "cocina":
            list_cocina.append(line)
        elif flag == "especialidades":
            list_especialidades.append(line)
        elif flag == "iconico":
            list_iconico.append(line)
        elif flag == "frases":
            list_frases.append(line)
        elif flag == "curiosidades":
            list_curiosidades.append(line)
        #seguro hay formas mas lindas de hacerlo pero esta fue la primera que se me ocurrio
    
    #actualizar()
    #------------MAIN PART ENDS HERE

    #Esto es lo que ejecuta el main cuando uno hace python3 bot.py
if __name__ == '__main__':
    main()

##Primero se ejecuta el main, luego la parte del bot que hace polling, porque sino
##nunca se cargan las variables que quieres.

'''def actualizar():
    #creamos el Updater, objeto que se encargará de mandarnos las peticiones del bot
    updater = Updater('1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc')

    #registramos los comandos del bot y su funcionalidad
    dispatcher = updater.dispatcher

    #registramos el método que hemos definido antes como listener para que muestre la información de cada mensaje
    listener_handler = MessageHandler(Filters.text, listener)
    dispatcher.add_handler(listener_handler)

    
    ##Ahora registramos cada método a los comandos necesarios
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('cocina', cocina))

    #comenzamos la ejecucion del bot a las peticiones
    updater.start_polling()
    updater.idle()

if __name__ == '__actualizar__':
    main()'''