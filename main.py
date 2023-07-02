from configs.secrets import token
from libs.comandos import Commands
import telebot
import json

bot = telebot.TeleBot(token)
cmd = Commands()

shopping_list = 'data/shopping_list.json'


@bot.message_handler(commands=['help', 'ayuda'])
def cmd_handler(message):
    cmd.help(message)


@bot.message_handler(commands=['list', 'lista'])
def cmd_handler(message):
    cmd.show_list(message)


@bot.message_handler(commands=['clear', 'borrar'])
def cmd_list(message):
    cmd.delete_list(message)


# Cambiar esta entrada por un comando para agregar elementos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, 'Comando no disponible')
    else:
        with open(shopping_list, "r") as archivo:
            datos = json.load(archivo)
        if 'Productos' in datos:
            datos["Productos"].append(message.text)
        else:
            datos["Productos"] = [message.text]

        with open(shopping_list, 'w') as archivo:
            json.dump(datos, archivo)


if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
