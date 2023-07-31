import json
import telebot
import openai
import emoji
from configs.secrets import token
from libs.mensajes import msg_help, msg_clear_list, msg_start_with, msg_add_product_end, msg_add_product_error_slash, msg_add_product_error
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(token)
shopping_list = 'data/shopping_list.json'


class Commands:
    @staticmethod
    def help(message):
        print(message)
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

    # @staticmethod
    # def chat_with_gpt(message):
    #     query = message.text  # Obtén la consulta del mensaje del usuario

    #     # Llama a la API de OpenAI para obtener una respuesta del modelo de ChatGPT
    #     response = openai.Completion.create(
    #         engine='text-davinci-003',
    #         prompt=query,
    #         max_tokens=50,
    #         n=1,
    #         stop=None,
    #         temperature=0.7
    #     )

    #     # Extrae la respuesta generada por el modelo
    #     answer = response.choices[0].text.strip()

    #     # Envía la respuesta al usuario
    #     bot.reply_to(message, answer)
        

    # @staticmethod
    # def get_weather_forecast(message):
    #     concello = message.text.split()[1]  # Obtén el nombre del concello del mensaje

    #     # Construye la URL de consulta utilizando el nombre del concello
    #     url = f"https://www.meteogalicia.gal/web/predicion/localidades/localidadesIndex.action?request_locale=gl&conc={concello}"

    #     # Realiza la solicitud GET a la URL y obtén el contenido HTML de la página
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         html_content = response.text

    #         # Analiza el contenido HTML utilizando BeautifulSoup
    #         soup = BeautifulSoup(html_content, 'html.parser')

    #         # Encuentra y extrae la información de la previsión meteorológica
    #         prevision_div = soup.find("div", class_="prevision_dia")
    #         print(prevision_div)
    #         if prevision_div:
    #             # Extraer los datos de la previsión meteorológica
    #             fecha = prevision_div.find("h4").get_text()
    #             tiempo = prevision_div.find("p").get_text()

    #             # Imprimir los datos extraídos
    #             print("Fecha:", fecha)
    #             print("Tiempo:", tiempo)

    #         # ... código para extraer la información ...

    #         # Envía la información de la previsión meteorológica al usuario
    #         bot.reply_to(message, "Aquí está la previsión meteorológica para el concello de " + concello + ":")
    #         # ... código para enviar la información ...

    #     else:
    #         bot.reply_to(message, "No se pudo obtener la previsión meteorológica en este momento.")        