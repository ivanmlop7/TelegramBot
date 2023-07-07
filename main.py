import telebot
import json
from configs.secrets import token
from libs.comandos import Commands


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
def cmd_handler(message):
    cmd.delete_list(message)

# @bot.message_handler(commands=['add', 'agregar'])
# def cmd_handler(message):
#     cmd.add_product_to_list(message)    


@bot.message_handler(commands=['add', 'agregar'])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, 'Agrega productos a la lista. Una vez finalizado usa el comando /end para salir del modo de agregación.')

        # Función para manejar el siguiente mensaje
        def handle_next_step(next_message):
            if next_message.text == '/end':
                bot.send_message(next_message.chat.id, 'Modo de agregación finalizado.')
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
                emoji_producto_agregado = "\u2705"
                bot.send_message(next_message.chat.id, emoji_producto_agregado)

                # Espera al siguiente mensaje
                bot.register_next_step_handler(next_message, handle_next_step)
            else:
                bot.send_message(next_message.chat.id, 'El producto no puede empezar con "/".')

        # Espera al siguiente mensaje
        bot.register_next_step_handler(message, handle_next_step)
    else:
        bot.send_message(message.chat.id, 'Comando inválido. Por favor, usa el comando /add o /agregar para iniciar el modo de agregación.')





if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
