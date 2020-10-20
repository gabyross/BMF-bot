from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import random

"""
 random.choice(r)
'chao'
 random.choice(r)
'hola' """

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


#------------MAIN PART STARTS HERE
def main():
    file = open("data.in","r+") 
    lines = file.readlines()

    #declaracion de las categorias
    cocina = []
    frases = []
    iconico = []
    especialidades = []
    curiosidades = []

    for i in lines:
        if lines[i] == "cocina":
            while lines[i] != "especialidades":
                cocina.append(lines[i])

        if lines[i] == "especialidades":
            while lines[i] != "iconico":
                especialidades.append(lines[i])

        if lines[i] == "iconico":
            while lines[i] != "frases":
                iconico.append(lines[i])

        if lines[i] == "frases":
            while lines[i] != "curiosidades":
                frases.append(lines[i])

        if lines[i] == "curiosidades":
            while lines[i] != lines[-1]:
                curiosidades.append(lines[i])
        
        print(lines)

    del(cocina[0])
    del(especialidades[0])
    del(iconico[0])
    del(frases[0])
    del(curiosidades[0])

    """canciones={}
    file_canciones = open("diccionario_canciones.txt", "r")
    canciones={}


updater.start_polling()
updater.idle()"""
#------------MAIN PART ENDS HERE
"""def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
 
#------------CUTE RANDOM DOGS PART ENDS HERE"""