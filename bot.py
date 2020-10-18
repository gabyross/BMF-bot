#IMPORT LIBRARYIES
from telegram.ext import Updater, CommandHandler
import requests
import re

#CUTE RANDOM DOGS PART STARTS HERE------------

#function to get the URL.
def get_url():
    #using the requests library, we can acces the API and get json data
    contents = requests.get('https://random.dog/woof.json').json()
    #get the image url since we need that parameter to be able to send the image
    url = contents['url']
    return url

def perritos(bot, update):
    #get the url image
    url = get_url()
    #get recipient's ID
    chat_id = update.message.chat_id
    #send message (image)
    bot.send_photo(chat_id = chat_id, photo = url)

def dogs_main():
    updater = Updater('1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('perritos', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__dogs_main__':
    dogs_main()
#------------CUTE RANDOM DOGS PART ENDS HERE