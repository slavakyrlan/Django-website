from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','get_html_photo','is_published') #определяет поля модели, которые будут отображаться в списке объектов модели в административной панели Django.
    list_display_links = ('id','title') # определяет поля модели, которые будут являться ссылками на редактирование объекта модели в списке объектов модели.
    search_fields = ('title','content') # определяет поля модели, по которым можно выполнять поиск объектов модели в административной панели Django.

    list_editable = ('is_published',) # определяет поля модели, которые можно редактировать прямо из списка объектов модели в административной панели Django.
    list_filter = ('is_published','time_create') # определяет поля модели, по которым можно фильтровать объекты модели в списке объектов модели в административной панели Django.

    prepopulated_fields = {'slug': ('title',)} #определяет поля модели, для которых значения будут автоматически заполняться на основе других полей модели.
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'is_published', 'time_create', 'time_update') #определяет порядок отображения полей модели при редактировании объекта модели в административной панели Django.

    readonly_fields = ('time_create', 'time_update', 'get_html_photo') # определяет поля модели, которые будут только для чтения и недоступны для редактирования в административной панели Django.
    save_on_top = True #определяет, будет ли кнопка "Сохранить" отображаться вверху формы редактирования объекта модели в административной панели Django.

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "Миниатюра"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Film, FilmAdmin) # регистрирует модель Film в административной панели Django с использованием класса FilmAdmin в качестве настройки.
admin.site.register(Category, CategoryAdmin) #admin.site.register(Category, CategoryAdmin) регистрирует модель Category в административной панели Django с использованием класса CategoryAdmin в качестве настройки.


admin.site.site_title = 'Админ-панель сайта c статьями'
admin.site.site_header = 'Админ-панель сайта c статьями'