# test_validations.py

import pytest
from unittest.mock import MagicMock
from libs.validations import check_user_id

def test_check_user_id_valid():
    # Creamos un objeto message simulado con un atributo from_user.id válido
    message = MagicMock()
    message.from_user.id = 12345

    # Establecemos el valid_user_id esperado para la prueba
    valid_user_id = 12345

    # Ejecutamos la función check_user_id y verificamos si el resultado es True
    resultado = check_user_id(message)
    assert resultado is True

def test_check_user_id_invalid():
    # Creamos un objeto message simulado con un atributo from_user.id inválido
    message = MagicMock()
    message.from_user.id = 54321

    # Establecemos el valid_user_id esperado para la prueba
    valid_user_id = 12345

    # Ejecutamos la función check_user_id y verificamos si el resultado es False
    resultado = check_user_id(message)
    assert resultado is False
