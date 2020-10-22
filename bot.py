from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import random, ast

"""
 random.choice(r)
'chao'
 random.choice(r)
'hola' """

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
    cocina = []
    frases = []
    iconico = []
    especialidades = []
    curiosidades = []
    canciones = {}

    #Cargo el diccionario de canciones
    canciones = cargar_dictionario("diccionario_canciones.txt")
    
    """
    Te dejo esto para que veas mejor el cambio
    for i in lines:
        if lines[i] == "cocina":
            while lines[i] != "especialidades":
                cocina.append(lines[i])

    """
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
            cocina.append(line)
        elif flag == "especialidades":
            especialidades.append(line)
        elif flag == "iconico":
            iconico.append(line)
        elif flag == "frases":
            frases.append(line)
        elif flag == "curiosidades":
            curiosidades.append(line)
        #seguro hay formas mas lindas de hacerlo pero esta fue la primera que se me ocurrio
    
    print(lines[0:5])
    print(cocina)


    

    #canciones={}
    #file_canciones = open("diccionario_canciones.txt", "r")
    #canciones={}


    #updater.start_polling()
    #updater.idle()
    #------------MAIN PART ENDS HERE

#def get_url():
#    contents = requests.get('https://random.dog/woof.json').json()    
 
##------------CUTE RANDOM DOGS PART ENDS HERE

#Esto es lo que ejecuta el main cuando uno hace python3 bot.py
if __name__ == '__main__':
    main()

##Primero se ejecuta el main, luego la parte del bot que hace polling, porque sino
##nunca se cargan las variables que quieres.


#------------START PART STARTS HERE
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hola {update.effective_user.first_name}, escribe "/" para ver los comandos disponibles')


updater = Updater('1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
#------------START PART ENDS HERE


#------------COCINA PART STARTS HERE
def cocina(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{random.choice([cocina])}')


updater = Updater('1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc')

updater.dispatcher.add_handler(CommandHandler('cocina', cocina))

updater.start_polling()
updater.idle()
#------------COCINA PART ENDS HERE