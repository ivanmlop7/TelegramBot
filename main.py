import telebot
import openai
from configs.secrets import token, openai_key
from libs.comandos import Commands
from libs.mensajes import msg_unauthorized
from libs.validations import check_user_id


bot = telebot.TeleBot(token)
key = openai.api_key = openai_key
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

# @bot.message_handler(commands=['chat', 'conversar'])
# def cmd_handler(message):
#     cmd = Commands()

#     if message.text.startswith('/chat') or message.text.startswith('/conversar'):
#         cmd.chat_with_gpt(message)
#     else:
#         bot.reply_to(message, 'Comando no reconocido. Por favor, utiliza /chat <consulta> o /conversar <consulta> para conversar con ChatGPT.')

# @bot.message_handler(commands=['weather', 'tiempo'])
# def cmd_handler(message):
#     if message.text.startswith('/weather') or message.text.startswith('/tiempo'):
#         cmd.get_weather_forecast(message)
#     else:
#         bot.reply_to(message, 'Comando no reconocido. Por favor, utiliza /weather <concello> o /tiempo <concello> para consultar la previsión meteorológica.')




if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
