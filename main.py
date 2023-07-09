import telebot
from configs.secrets import token
from libs.comandos import Commands
from libs.mensajes import msg_unauthorized
from libs.validations import check_user_id


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

@bot.message_handler(commands=['add', 'agregar'])
def cmd_handler(message):
    cmd.add_product_to_list(bot, message)


if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
