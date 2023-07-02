from configs.secrets import token
from libs.mensajes import mensaje_help
import telebot
import json

bot = telebot.TeleBot(token)
shopping_list = 'data/shopping_list.json'


class Commands:
    @staticmethod
    def help(message):
        bot.reply_to(message, mensaje_help)

    @staticmethod
    def show_list(message):
        with open(shopping_list, "r") as file:
            products = json.load(file)

        if len(products) <= 0:
            bot.reply_to(message, 'La lista esta vacia')
        else:
            products_list = products['Productos']
            print(products_list)
            bot.reply_to(message, str(products_list))

    @staticmethod
    def delete_list(message):
        with open(shopping_list, "w") as file:
            json.dump({}, file)
        bot.reply_to(message, 'Se ha borrado el contenido de la lista')
