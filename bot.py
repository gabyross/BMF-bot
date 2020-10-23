# Importamos las librerías necesarias
from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, CommandHandler, InlineQueryHandler, Filters
import random, ast


# Establecemos el token
updater = Updater('1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc')

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
#------------LISTAS PART ENDS HERE

##Primero se ejecuta el main, luego la parte del bot que hace polling, porque sino
##nunca se cargan las variables que quieres.

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


'''def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()  

def get_url_cat():
    contents = requests.get('').json()'''

#------------CANCIONES PART STARTS HERE
def canciones(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(songs))
updater.dispatcher.add_handler(CommandHandler('canciones', canciones))
#------------CANCIONES PART ENDS HERE
## Fin del establecimiento de las funciones de los comandos

updater.start_polling()
updater.idle()