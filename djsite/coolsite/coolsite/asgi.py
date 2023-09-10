"""
ASGI config for coolsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
"""
Файл asgi.py - это точка входа для ASGI (Asynchronous Server Gateway Interface) сервера вашего Django-проекта.
ASGI - это интерфейс, который позволяет асинхронным серверам взаимодействовать с веб-приложениями, такими как Django.
Файл asgi.py содержит код, который инициализирует ASGI-приложение нашего проекта и создает экземпляр ASGI-сервера для его запуска.
"""
import os

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coolsite.settings') #в файле asgi.py устанавливает переменную окружения DJANGO_SETTINGS_MODULE, которая указывает на модуль настроек Django-проекта.
# 'coolsite.settings' - это значение, которое устанавливается в DJANGO_SETTINGS_MODULE. Здесь 'coolsite' - это имя вашего проекта, а 'settings' - это имя модуля настроек внутри вашего проекта.
#Эта строка кода гарантирует, что Django будет использовать правильный модуль настроек при запуске вашего ASGI-приложения.
# Это важно, потому что модуль настроек содержит конфигурацию вашего проекта, такую как база данных, статические файлы, шаблоны и другие настройки.


application = get_asgi_application()
