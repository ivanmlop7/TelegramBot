import telebot
import json
from configs.secrets import token
from libs.comandos import Commands
from libs.mensajes import msg_start_with, msg_add_product_end, msg_add_product_error, msg_add_product_error_slash, msg_unauthorized


bot = telebot.TeleBot(token)
cmd = Commands()

shopping_list = 'data/shopping_list.json'


@bot.message_handler(commands=['help', 'ayuda'])
def cmd_handler(message):
        cmd.help(message)


@bot.message_handler(commands=['list', 'lista'])
def cmd_handler(message):
    if check_user_id(message):
        cmd.show_list(message)
    else:
        bot.send_message(message.chat.id, msg_unauthorized)


@bot.message_handler(commands=['clear', 'borrar'])
def cmd_handler(message):
    if check_user_id(message):
        cmd.delete_list(message)
    else:
        bot.send_message(message.chat.id, msg_unauthorized)

# @bot.message_handler(commands=['add', 'agregar'])
# def cmd_handler(message):
#     cmd.add_product_to_list(message)    


@bot.message_handler(commands=['add', 'agregar'])
def add_product_to_list(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, msg_start_with)

        # Función para manejar el siguiente mensaje
        def handle_next_step(next_message):
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



def check_user_id(message):
    if message.from_user and message.from_user.id == 504727906:
        return True
    else:
        return False


if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
