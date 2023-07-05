# Telegram Bot

Este repositorio contiene un proyecto de ejemplo de un bot de Telegram utilizando Python y la biblioteca python-telegram-bot.

## Descripción

El objetivo de este proyecto es mostrar cómo crear un bot de Telegram utilizando Python. El bot es capaz de responder a comandos y realizar acciones específicas según las interacciones del usuario.

## Requisitos

- Python 3.6 o superior
- python-telegram-bot (instalable mediante `pip install python-telegram-bot`)

## Uso

1. Clona el repositorio: `git clone https://github.com/ivanmlop7/TelegramBot.git`
2. Ve al directorio del proyecto: `cd TelegramBot`
3. Crea y activa un entorno virtual (opcional, pero se recomienda): `python3 -m venv env` y `source env/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Obtén un token para tu bot de Telegram siguiendo las instrucciones de la documentación de python-telegram-bot.
6. Crea un archivo `configs/secrets.py` y define la variable `token` con tu token de Telegram.
7. Ejecuta el bot: `python bot.py`

## Estructura del proyecto

- `bot.py`: Archivo principal que contiene la lógica del bot.
- `configs/secrets.py`: Archivo de configuración para almacenar el token del bot.
- `libs/mensajes.py`: Módulo que contiene mensajes y respuestas predefinidas.
- `libs/comandos.py`: Módulo que define las acciones para cada comando del bot.
- `data/lista_compra.json`: Archivo JSON que almacena los datos del bot.
- `README.md`: Este archivo.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

1. Crea un fork del repositorio.
2. Crea una nueva rama para tu contribución: `git checkout -b mi_contribucion`
3. Realiza tus cambios y haz commit: `git commit -am "Descripción de mi contribución"`
4. Sube tus cambios a tu repositorio: `git push origin mi_contribucion`
5. Crea un pull request en el repositorio original.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
