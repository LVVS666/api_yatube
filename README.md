<h1>Проект Api_Yatube</h1>
Описание проекта: Благодаря этому проекту зарегистрированные пользователи могут:
<ul>
  <li>создавать новые посты, комментировать посты других авторов</li>
<li>получать информацию о постах, группах постов и комментариев к постам, оставленные пользвателями</li>
  <li>вносить изменения и удалять свои посты и комментарии</li>
</ul>
 
<b>Технологии: Python 3.7.9 Django 2.2.16</b>

  <h2>Запуск проекта в dev-режиме</h2>
<ul>
<li>Установите и активируйте виртуальное окружение python3 -m venv venv source venv/bin/activate</li>
<li>Установите зависимости из файла requirements.txt</li>
<li>pip3 install -r requirements.txt</li>
<li>Примените миграции - python3 manage.py makemigrations python manage.py migrate</li>
<li>Запустите сервер: python3 manage.py runserver</li>

Использовать проект можно при помощи Postman Проект доступен только для зарегистированных пользователей Создать пользователя в БД можно командой createsuperuser
