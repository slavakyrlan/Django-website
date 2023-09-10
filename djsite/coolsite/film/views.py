from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
'''
logout: функция для выхода пользователя из системы.
login: функция для входа пользователя в систему.
login_required: декоратор, который требует, чтобы пользователь был аутентифицирован для доступа к определенному представлению.
LoginView: класс представления, который предоставляет функциональность входа пользователя в систему.
Paginator: класс, который позволяет разбить коллекцию объектов на страницы.
HttpResponse, HttpResponseNotFound, Http404: классы для создания HTTP-ответов и обработки ошибок.
render: функция для отображения шаблона с переданными данными в ответ на HTTP-запрос.
redirect: функция для перенаправления на другую страницу.
get_object_or_404: функция для получения объекта из базы данных или генерации исключения Http404, если объект не найден.
reverse_lazy: функция для получения URL по имени маршрута в момент выполнения.
ListView: класс представления для отображения списка объектов из базы данных.
DetailView: класс представления для отображения подробной информации об объекте.
CreateView: класс представления для создания нового объекта.
FormView: класс представления для обработки формы.
LoginRequiredMixin: класс-миксин, который требует, чтобы пользователь был аутентифицирован для доступа к представлению.
'''
from .forms import *
from .models import *
from .utils import *

class FilmHome(DataMixin,ListView):

    model = Film
    template_name = 'film/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Film.objects.filter(is_published=True).select_related('cat')


def index(request): #HttpResponse
    posts = Film.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cats_selected': 0,
    }

    return render(request, 'film/index.html', context=context)


#@login_required - доступ только для админов
def about(request):
    #contact_list = Film.objects.all()
    #paginator = Paginator(contact_list, 1)

    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    return render(request, 'film/about.html', { 'menu': menu, 'title': 'О сайте'})



class AddPage(LoginRequiredMixin, DataMixin,CreateView):
    form_class = AddPostForm
    template_name = 'film/addpage.html'
    success_url = reverse_lazy('home') # перенаправление на гл окно
    login_url = reverse_lazy('home')
    raise_exception = True
    # используется в Django для настройки поведения при возникновении ошибки аутентификации пользователя. Если значение raise_exception установлено на True, то Django будет генерировать исключение PermissionDenied при попытке доступа неаутентифицированного пользователя к защищенному представлению, что приведет к отображению страницы ошибки 403 (Forbidden).
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             #Film.objects.create(**form.cleaned_data)
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'film/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

# def contact(request):
#     return HttpResponse("Обратная связь")

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'film/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
'''
form_class: Указывает класс формы, который будет использоваться для отображения и обработки формы обратной связи. В данном случае, используется класс ContactForm.
template_name: Указывает путь к шаблону, который будет использоваться для отображения страницы обратной связи.
success_url: Указывает URL, на который будет перенаправлен пользователь после успешной отправки формы.
get_context_data(): Метод, который добавляет дополнительные данные в контекст шаблона. В данном случае, метод использует метод get_user_context() из класса DataMixin для получения контекста пользователя и объединяет его с общим контекстом представления.
form_valid(): Метод, вызываемый при успешной валидации формы. В данном случае, метод просто выводит очищенные данные формы на консоль и перенаправляет пользователя на указанный success_url.
Класс ContactFormView использует множественное наследование, где DataMixin предоставляет дополнительные методы и атрибуты для работы с контекстом и данными пользователя.
'''
# def login(request):
#     return HttpResponse("Авторизация")

# def show_post(request, post_slug):
#     post = get_object_or_404(Film, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'film/post.html', context=context)

class ShowPost(DataMixin,DetailView):
    model = Film
    template_name = 'film/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        #context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



class FilmCategory(DataMixin, ListView):

    model = Film
    template_name = 'film/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Film.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))
'''
model: Указывает модель, на основе которой будет строиться список фильмов. В данном случае, используется модель Film.
template_name: Указывает путь к шаблону, который будет использоваться для отображения списка фильмов.
context_object_name: Указывает имя переменной контекста, в которой будет доступен список фильмов.
allow_empty: Указывает, разрешено ли отображение пустого списка фильмов.
get_queryset(): Метод, который возвращает queryset (запрос к базе данных) для получения списка фильмов определенной категории. В данном случае, фильмы фильтруются по полю cat__slug (slug категории) и is_published=True (опубликованные фильмы), и используется метод select_related() для выполнения предварительной выборки связанных объектов категорий.
get_context_data(): Метод, который добавляет дополнительные данные в контекст шаблона. В данном случае, метод использует метод get_user_context() из класса DataMixin для получения контекста пользователя, а также добавляет название категории и идентификатор выбранной категории в контекст.
'''
# def show_category(request, cat_id):
#     posts = Film.objects.filter(cat_id=cat_id)
#
#
#     if len(posts) ==0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по жанрам',
#         'cats_selected': cat_id,
#     }
#
#     return render(request, 'film/index.html', context=context)




class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'film/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'film/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


#python manage.py runserver
#python manage.py migrate
#python manage.py makemigrations
