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
    update.message.reply_text(f'{random.choice([])}')


updater = Updater('1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc')

updater.dispatcher.add_handler(CommandHandler('cocina', cocina))

updater.start_polling()
updater.idle()
#------------COCINA PART ENDS HERE




"""def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
 
#------------CUTE RANDOM DOGS PART ENDS HERE"""