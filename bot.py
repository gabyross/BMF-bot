# Importamos las librerías necesarias
from telegram import Update, InputMediaPhoto
from telegram.ext import CallbackContext, Updater, MessageHandler, CommandHandler, InlineQueryHandler, Filters
import random, ast, json, requests, re


# Establecemos el token
updater = Updater('tuToken')

#variables globales
list_cocina = []
list_frases = []
list_iconico = []
list_especialidades = []
list_curiosidades = []

# Permite cargar un dictionario de un archivo que recibe como input
def cargar_dictionario(file_name):
    file_c = open(file_name, "r")
    contents = file_c.read()
    dictionary = ast.literal_eval(contents)
    file_c.close()
    return dictionary


#------------LISTAS PART STARTS HERE
file = open("data.in","r+") 
lines = file.read().splitlines()

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

    ##ahora dependiendo del flag agregamos las lineas
    if flag == "cocina":
        list_cocina.append(line.encode('utf-8').decode())
    elif flag == "especialidades":
        list_especialidades.append(line.encode('utf-8').decode())
    elif flag == "iconico":
        list_iconico.append(line.encode('utf-8').decode())
    elif flag == "frases":
        list_frases.append(line.encode('utf-8').decode())
    elif flag == "curiosidades":
        list_curiosidades.append(line.encode('utf-8').decode())
#------------LISTAS PART ENDS HERE


## Inicio del establecimiento de las funciones de los comandos
#------------START PART STARTS HERE
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hola {update.effective_user.first_name}, escribe "/" para ver los comandos disponibles')
updater.dispatcher.add_handler(CommandHandler('start', start))
#------------START PART ENDS HERE


#------------COCINA PART STARTS HERE
def cocina(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(list_cocina))
updater.dispatcher.add_handler(CommandHandler('cocina', cocina))
#------------COCINA PART ENDS HERE


#------------ESPECIALIDADES PART STARTS HERE
def especialidades(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(list_especialidades))
updater.dispatcher.add_handler(CommandHandler('especialidades', especialidades))
#------------ESPECIALIDADES PART ENDS HERE


#------------ICONICO PART STARTS HERE
def iconico(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(list_iconico))
updater.dispatcher.add_handler(CommandHandler('iconico', iconico))
#------------ICONICO PART ENDS HERE


#------------FRASES PART STARTS HERE
def frases(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(list_frases))
updater.dispatcher.add_handler(CommandHandler('frases', frases))
#------------FRASES PART ENDS HERE


#------------CURIOSIDADES PART STARTS HERE
def curiosidades(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(list_curiosidades))
updater.dispatcher.add_handler(CommandHandler('curiosidades', curiosidades))
#------------CURIOSIDADES PART ENDS HERE


#------------PERRITOS PART STARTS HERE
def get_url_perritos():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url_perritos()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


def perritos(update: Update, context: CallbackContext) -> None:
    url_perrito = get_image_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url_perrito, caption="Perritos para alegrar tu dia!")
updater.dispatcher.add_handler(CommandHandler('perritos', perritos))
#------------PERRITOS PART ENDS HERE


#------------GATITOS PART STARTS HERE
def get_url_gatitos():
    contents = requests.get('https://api.thecatapi.com/v1/images/search').json()    
    url = contents[0]['url']
    return url

def gatitos(update: Update, context: CallbackContext) -> None:
    url_gatito = get_url_gatitos()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url_gatito, caption="Gatitos cuchis para alegrar tu dia!")
updater.dispatcher.add_handler(CommandHandler('gatitos', gatitos))
#------------GATITOS PART ENDS HERE

#------------CANCIONES PART STARTS HERE
def canciones(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(list(songs.values())))
updater.dispatcher.add_handler(CommandHandler('canciones', canciones))
#------------CANCIONES PART ENDS HERE
## Fin del establecimiento de las funciones de los comandos

updater.start_polling()
updater.idle()
