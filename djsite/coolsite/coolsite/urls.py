"""
URL configuration for coolsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Файл urls.py в Django является модулем, который содержит объявления URL-шаблонов вашего проекта. В этом файле определяются пути (URL) и соответствующие им обработчики представлений, которые обрабатывают запросы и возвращают ответы.
Файл urls.py играет важную роль в маршрутизации запросов в вашем Django-проекте. Он определяет, какие представления (views) должны быть вызваны для каждого URL-запроса и какие аргументы передаются представлениям.
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#Это позволяет организовать и разделить определение URL-шаблонов на несколько модулей, делая структуру проекта более модульной и понятной.
from coolsite import settings
from film.views import *

urlpatterns = [
    path('admin/', admin.site.urls), # этот путь относится к административной панели Django.
    path('captcha/', include('captcha.urls')), #этот путь включает URL-шаблоны для модуля Captcha, предоставляемого сторонней библиотекой.
    path('', include("film.urls")),#это пустой путь, который используется для включения URL-шаблонов из приложения film.

]
if settings.DEBUG: #используется для включения отладочной панели Django и для настройки обработки медиафайлов в режиме разработки
    import debug_toolbar # предоставляет отладочную панель Django для разработки.

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)), #Добавляется путь __debug__/ в список urlpatterns с помощью функции include() для включения URL-шаблонов отладочной панели.
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#К списку urlpatterns добавляются дополнительные пути для обработки медиафайлов. Используется функция static(), которая создает URL-шаблон для обслуживания медиафайлов во время разработки. Она использует значения MEDIA_URL и MEDIA_ROOT из настроек Django (settings.MEDIA_URL и settings.MEDIA_ROOT).

handler404 = pageNotFound
#ошибка 404