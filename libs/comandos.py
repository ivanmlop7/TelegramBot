import json
import telebot
import emoji
from configs.secrets import token
from libs.mensajes import msg_help, msg_clear_list, msg_start_with, msg_add_product_end, msg_add_product_error_slash, msg_add_product_error

bot = telebot.TeleBot(token)
shopping_list = 'data/shopping_list.json'


class Commands:
    @staticmethod
    def help(message):
        bot.reply_to(message, msg_help)

    @staticmethod
    def show_list(message):
        with open(shopping_list, "r") as file:
            products = json.load(file)

        if len(products) <= 0:
            bot.reply_to(message, 'La lista esta vacia')
        else:
            products_list = products['Productos']
            print(products_list)
            for product in products_list:
                bot.send_message(chat_id=message.chat.id, text=product)

    @staticmethod
    def delete_list(message):
        with open(shopping_list, "w") as file:
            json.dump({}, file)
        bot.reply_to(message, msg_clear_list)


    @staticmethod
    def add_product_to_list(bot, message):
        if message.text.startswith("/"):
            bot.send_message(message.chat.id, msg_start_with)

            # Función para manejar el siguiente mensaje
            def handle_next_step(next_message, bot=bot):
                if next_message.text == '/end':
                    bot.send_message(next_message.chat.id, msg_add_product_end)
                elif not next_message.text.startswith("/"):
                    with open(shopping_list, "r") as archivo:
                        datos = json.load(archivo)
                    if 'Productos' in datos:
                        datos["Productos"].append(next_message.text)
                    else:
                        datos["Productos"] = [next_message.text]

                    with open(shopping_list, 'w') as archivo:
                        json.dump(datos, archivo)

                    # Responder con un emoji
                    emoji_product_added = "\u2705"
                    bot.send_message(next_message.chat.id, emoji_product_added)

                    # Espera al siguiente mensaje
                    bot.register_next_step_handler(next_message, handle_next_step)
                else:
                    bot.send_message(next_message.chat.id, msg_add_product_error_slash)

            # Espera al siguiente mensaje
            bot.register_next_step_handler(message, handle_next_step)
        else:
            bot.send_message(message.chat.id, msg_add_product_error)
        