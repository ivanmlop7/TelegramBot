import unittest
from unittest.mock import patch, MagicMock
from libs.comandos import Commands
from libs.mensajes import msg_help, msg_start_with



class TestCommands(unittest.TestCase):
    def test_help(self):
        # Creamos un objeto message simulado
        message = MagicMock()
        message.text = "/help"
        message.chat.id = 123

        # Mock del bot para pasar como argumento al método
        bot_mock = MagicMock()

        # Llamamos al método help y verificamos que no lance excepciones
        with patch("libs.comandos.bot.reply_to") as mock_reply_to:
            Commands.help(message)

        # Verificamos que el método bot.reply_to haya sido llamado con los parámetros correctos
        mock_reply_to.assert_called_once_with(message, msg_help)


    def test_add_product_to_list_start_with_slash(self):
        # Creamos un objeto message simulado
        message = MagicMock()
        message.text = "/start_with_slash"
        message.chat.id = 101

        # Mock del bot para pasar como argumento al método
        bot_mock = MagicMock()

        # Llamamos al método add_product_to_list y verificamos la respuesta
        Commands.add_product_to_list(bot_mock, message)

        # Verificamos que el bot envíe el mensaje correcto
        bot_mock.send_message.assert_called_once_with(message.chat.id, msg_start_with)


if __name__ == '__main__':
    unittest.main()
