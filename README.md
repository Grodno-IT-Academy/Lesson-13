Продолжаем работать с демо проектом.
## Bootstrap стилизация
https://getbootstrap.com

Как сильная альтернатива можно пользоваться Foundation. Ей пользуються ведущие компании как Amazon & eBay.

https://get.foundation

Но мы сегодня будем пользоваться BOOTSTRAP.
Он создан и поддерживаеться программистами из Twitter.
Бутстрап состоит из css и js элементов.  
- Кто может расказать для чего css?  
- js?  
https://getbootstrap.com/docs/5.0/getting-started/introduction/
  
```html
<!--Добавте в HEAD нашего base.html файла-->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
```
Это css компонент бутстрапа. 
CSS это стилистический програмный язык.
Нам как питонистам не обязательно его знать скажу лишь что из-за разных браузеров и платформ то как будет выглядеть сайт в хроме не обязательно будет соответствовать тому как его будет видеть ваш пользователь!
Поэтому мы пользуемся фреймами для фронтенда чтобы наш сайт соответствовал требованиям современных браузеров!
Обращаем внимание на то что это будет подгружаться из ссылки каждый раз что замедлит подгрузку сайта в браузере!
Когда будем думать о выпуске то надо будет скачать этот файл тоже самое косаеться js файла.
```html
<!--Добавте это в конец <body>  элемента-->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
```
JS файл так-же подгружаеться на фронтенде хотя мы можем его включить в наш bundle.

https://getbootstrap.com/docs/5.0/getting-started/download/

дальше можем перенести файлы в templates папку и сослаться на них по другомy.
Скачиваем файлы и получаем папку bootstrap с папками css и js. удобно?
Bootstrap так-же пользуеться фреймом jQuery. 
- Кто знает о jQuery?

Опять для нас лишние знания но надо подгрузить и его на сайт.

https://jquery.com/download/

Нам нужно пометсть папку в static папку которую понимает django и тогда можем делать ссылку используя django href в base.html файле:
```html
<!-- Bootstrap core CSS -->
    <link href="{% static 'vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">
<!-- Bootstrap core JavaScript -->
    <script src="{% static 'vendor/jquery/jquery-3.6.0.js' %}"></script>
    <script src="{% static   'vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
```
Нужно подгрузить static таг в начале файла с помощю load
```html
{% load static %}
```
Так-же в нашем settings файле нужно создать список STATIC_DIRS
```python
STATICFILES_DIRS = [
    BASE_DIR.joinpath('static/')
]
```

https://docs.djangoproject.com/en/3.2/howto/static-files/

и теперь всё должно заработать
### Зачем?
чтобы подгружалось быстрее и чтобы не зависеть от состояния серверов twitter & jQuery!
Иногда Django сайт будет работать на закрытом сервере как например в лаборатории фармацептической компании где не будет доступа к интернету чтобы предотвращать взломы по сети.
### Двигаем далее
У нас немного другой фонт и что?

Работая с bootstrap у нас есть доступ к стилям которые будут работать почти на всех браузерах одинаково*
почти потому-что всё равно в плане защиты информации пользователей мы теряем доступ к некоторым функциям наших зависимостей.

Начнём с навигации!
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">DemoDjangoProject</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/products/">Products</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/admin/">Admin</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```
В Bootstrap мы пользуемся классами для стилизации html обьектов.

Поместить всё в контэйнер!
## Линки
Обращаем внимание на href!
Это называются абсолютные внутренние линки(мой лучший превод) они не имеют сайта в названиях.

## Django линки
https://www.youtube.com/watch?v=CFO4aAsUuUk

но при изменении компонентов в джанго линки не поменяються!

чтобы линки были привязаны к конкретным страницам нам нужно изменить url.py файлы наименовывая name
```python

urlpatterns = [
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
```
```python
#products/urls.py
from django.urls import path
from .models import Product
from products.views import product_detail_view, products_view

urlpatterns = [
    path('',products_view,name='products'),
    path('<int:product_id>/', product_detail_view, name='detail'),
]

```
и в nav темплейте можно изменить href на:
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">DemoDjangoProject</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="{% url 'home' %}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'products' %}">Products</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/admin/">Admin</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```
## Формы фронтенд

## Django формы