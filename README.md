Онлайн платформа-торговой сети электроники

Сеть представляет собой иерархическую структуру из трех уровней:

    завод;
    розничная сеть;
    индивидуальный предприниматель.

**Установка:**
    
1. Клонируйте репозитерий:

         https://github.com/SulAliya/ElectronRetail.git
    
2. Создайте виртуальное окружение:

         python -m venv env

         source env/bin/activate   # На Windows используйте `env\Scripts\activate`

3. Установите зависимости из файла requirements.txt:
            
        pip install -r requirements.txt

4. Создайте файл переменных окружения .env:

        В корневой директории проекта скопируйте файл env.sample в .env и заполните свои данные.

5. Примените миграции:

        python manage.py migrate

6. Создайте суперпользователя:

        python manage.py csu

7. Запуск приложения: 
            
        python manage.py runserver

