# Importamos las librerías necesarias
from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, CommandHandler, InlineQueryHandler, Filters
import random, ast

import bot.py

# Establecemos el token
updater = Updater('1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc')

## Inicio del establecimiento de las funciones de los comandos
#------------START PART STARTS HERE
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hola {update.effective_user.first_name}, escribe "/" para ver los comandos disponibles')
updater.dispatcher.add_handler(CommandHandler('start', start))
#------------START PART ENDS HERE


#------------COCINA PART STARTS HERE
def cocina(update: Update, context: CallbackContext) -> None:
    global list_cocina
    update.message.reply_text(random.choice(list_cocina))
updater.dispatcher.add_handler(CommandHandler('cocina', cocina))
#------------COCINA PART ENDS HERE


#------------ESPECIALIDADES PART STARTS HERE
def especialidades(update: Update, context: CallbackContext) -> None:
    global list_especialidades
    update.message.reply_text(random.choice(list_especialidades))
updater.dispatcher.add_handler(CommandHandler('especialidades', especialidades))
#------------ESPECIALIDADES PART ENDS HERE


#------------ICONICO PART STARTS HERE
def iconico(update: Update, context: CallbackContext) -> None:
    global list_iconico
    update.message.reply_text(random.choice(list_iconico))
updater.dispatcher.add_handler(CommandHandler('iconico', iconico))
#------------ICONICO PART ENDS HERE


#------------FRASES PART STARTS HERE
def frases(update: Update, context: CallbackContext) -> None:
    global list_frases
    update.message.reply_text(random.choice(list_frases))
updater.dispatcher.add_handler(CommandHandler('frases', frases))
#------------FRASES PART ENDS HERE


#------------CURIOSIDADES PART STARTS HERE
def curiosidades(update: Update, context: CallbackContext) -> None:
    global list_curiosidades
    update.message.reply_text(random.choice(list_curiosidades))
updater.dispatcher.add_handler(CommandHandler('curiosidades', curiosidades))
#------------CURIOSIDADES PART ENDS HERE


'''def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()  

def get_url_cat():
    contents = requests.get('').json()

#------------CANCIONES PART STARTS HERE
def canciones(update: Update, context: CallbackContext) -> None:
    global songs
    update.message.reply_text(random.choice(songs))
updater.dispatcher.add_handler(CommandHandler('canciones', canciones))
#------------CANCIONES PART ENDS HERE'''
## Fin del establecimiento de las funciones de los comandos

updater.start_polling()
updater.idle()