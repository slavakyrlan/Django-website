"""
WSGI config for coolsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#Функция get_wsgi_application() является частью Django и возвращает WSGI-совместимую функцию приложения, которую можно использовать для обслуживания вашего Django-проекта с помощью WSGI-совместимого сервера, такого как Gunicorn или uWSGI.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coolsite.settings')
# DJANGO_SETTINGS_MODULE для определения модуля настроек проекта. Она указывает на модуль, который содержит настройки Django, такие как база данных, маршрутизация URL и другие параметры проекта.
#В данном случае 'coolsite.settings' является значением переменной окружения DJANGO_SETTINGS_MODULE. Здесь 'coolsite' - это имя нашего проекта, а 'settings' - имя модуля, содержащего файл настроек settings.py.

application = get_wsgi_application()
# Присвоение возвращаемого значения get_wsgi_application() переменной application позволяет использовать это WSGI-приложение в конфигурации сервера. К примеру, в файле wsgi.py в Django-приложении, этот код устанавливает переменную application для запуска Django-приложения через WSGI-сервер.