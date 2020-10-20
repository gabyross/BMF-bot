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

    for i in lines(0,8):
        cocina[i] = lines
    del(cocina[0])

    for i in lines(10,17):
        especialidades[i] = lines
    del(especialidades[0])

    for i in lines(19,29):
        iconico[i] = lines
    del(iconico[0])

    for i in lines(31,43):
        frases[i] = lines
    del(frases[0])

    for i in lines(45,53):
        curiosidades[i] = lines
    del(curiosidades[0])

updater.start_polling()
updater.idle()
#------------MAIN PART ENDS HERE
"""def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
 
#------------CUTE RANDOM DOGS PART ENDS HERE"""