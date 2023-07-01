from configs.secrets import token
from libs.mensajes import mensaje_help
import telebot
import json

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'ayuda'])
def cmd_help(message):
    bot.reply_to(message, mensaje_help)

@bot.message_handler(commands=['list', 'lista'])
def cmd_list(message):
    with open("datos.json", "r") as archivo:
        datos_recuperados = json.load(archivo)

    if len(datos_recuperados)<= 0:
        bot.reply_to(message, 'La lista esta vacia')
    else:
        productos = datos_recuperados['Productos']
        print(productos)   
        bot.reply_to(message, str(productos))

@bot.message_handler(commands=['clear', 'borrar'])
def cmd_list(message):
    with open("datos.json", "w") as archivo:
        json.dump({}, archivo)
    bot.reply_to(message, 'Se ha borrado el contenido de la lista')
    
    

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, 'Comando no disponible')
    else:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
        if 'Productos' in datos:        
            datos["Productos"].append(message.text)
        else:
            datos["Productos"] = [message.text]

        with open('datos.json', 'w') as archivo:
            json.dump(datos,archivo)       



if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')