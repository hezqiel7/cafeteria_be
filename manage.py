#!/usr/bin/env python
import os
import sys

import django
from django.contrib.auth import get_user_model


def change_password(username, new_password):
    # Cambiar la contraseña del usuario de forma programática
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        print(f"Contraseña cambiada exitosamente para el usuario {username}")
    except User.DoesNotExist:
        print(f"El usuario {username} no existe")

if __name__ == "__main__":
    # Configura Django antes de ejecutar cualquier cosa
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafeteria_be.settings")
    django.setup()

    # Aquí se puede pasar el nombre de usuario y la nueva contraseña a través de variables de entorno o argumentos
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    new_password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin')

    # Cambiar la contraseña
    change_password(username, new_password)

    # Ahora ejecutar el comando de Django
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
