Новости/Блог
============

Это модуль для ведение блога.

Категории
---------

Поля модели категории
~~~~~~~~~~~~~~~~~~~~~
    :name: Название
    :lang: Язык
    :parent (related_name='children'): Родительская категория
    :template (default='news/post_list.html'): Шаблон
    :slug: url
    :published: Опубликовать или снять с публикации
    :paginated (default=5): Количество новостей на странице

Template tags
~~~~~~~~~~~~~

Подключение тега. Если не указать шаблон, то будет взят по умолчанию.

.. code-block:: python

   {% load news_tags %}

   {% category_list %}

Изменение шаблона

.. code-block:: python

   {% category_list template="categories.html" %}

Шаблон для вывода списка категорий.

.. code-block:: python

    <ul>
        {% for category in category_list %}
            <li>
                <a href="{{ category.get_absolute_url }}">{{ category.name }}</a>
            </li>
        {% endfor %}
    </ul>


Статьи/новости
----------------

Вывод списка статей
~~~~~~~~~~~~~~~~~~~
Имя шаблона
    news/post_list.html

.. code-block:: python

    {% for post in post_list %}
        {% if post.image %}
            <img src="{{ post.image.url }}">
        {% endif %}
        <p>{{ post.published_date }}</p>
        <p>
            {{ post.title }}
        </p>
    {% endfor %}

Вывод полной статьи
~~~~~~~~~~~~~~~~~~~
Имя шаблона
    news/post_detail.html

.. code-block:: python

    <h1>{{ post.title }}</h1>
    {% if post.author %}
        <p>{{ post.author }}</p>
    {% endif %}
    <p>Опубликовано {{ post.created_date }}</p>
    {% if post.image %}
        <img src="{{ post.image.url }}" alt="{{ post.title }}">
    {% endif %}
    {{ post.text|safe }}
    Просмотренно - {{ post.viewed }}

Поля модели статей
~~~~~~~~~~~~~~~~~~
    :author: Автор (FK)
    :title: Заголовок
    :subtitle: Под заголовок
    :mini_text: Краткое содержание статьи
    :text: Полное содержание статьи
    :created_date: Дата создания
    :edit_date: Дата редактирования
    :published_date: Дата публикации - когда будет опубликованно
    :image: "Главная фотография"
    :tag: Теги (M2M)
    :category: Категория (FK)
    :template: Шаблон
    :slug: url
    :published: Опубликовать или снять с публикации
    :viewed: Просмотров
    :status: Отображать для зарегистрированных пользователей или нет


Template tags
~~~~~~~~~~~~~

    Подключение тега. Если не указать шаблон, то будет взят по умолчанию.

    .. code-block:: python

       {% load news_tags %}

       {% post_list %}

    Изменение шаблона

    .. code-block:: python

       {% post_list template="news_block_tags.html" %}

    Шаблон для вывода списка статей.

    .. code-block:: python

        {% for post in post_list %}
            <h2><a href="{{ post.get_absolute_url }}"> {{ post.title }} </a></h2>
            {% if post.image %}
                <img src="{{ post.image.url }}">
            {% endif %}
            <p>{{ post.published_date }}</p>
        {% endfor %}

Теги
---------

Поля модели тегов
~~~~~~~~~~~~~~~~~~~~~
    :name: Имя
    :slug: url
    :published: Опубликовать или снять с публикации

Комментарии
-----------

Поля модели комментариев
~~~~~~~~~~~~~~~~~~~~~~~~

    :user ForeignKey: Связь с моделью Пользователей
    :post ForeignKey: Связь с моделью Новость
    :text (max_length=2000): Сообщение
    :date: Дата
    :update: Изменен
    :parent TreeForeignKey(related_name='children'): Родительский комментарий
    :published: Опубликовать или снять с публикации