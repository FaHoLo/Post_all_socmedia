# Публикация комиксов

Проект предназначен для публикации постов во все социальные сети за один запуск.

Поддерживаемые сети:
- Вконтакте
- Facebook
- Telegram

### Как установить

1. Python3 должен быть уже установлен.  
2. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
3. Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
4. Для работы с Api Вконтакте требуется: 
    * `Access Token`, чтобы его получить:
        * Зарегистрируйте Standalone-приложение на [vk.com/dev](https://vk.com/dev)
        * Получите ключ доступа пользователя с помощью процедуры [Implict Flow](https://vk.com/dev/implicit_flow_user). Потребуются права: photos, groups, wall и offline
        * Полученный ключ следует положить в файл `.env` под именем `VK_ACCESS_TOKEN`.
    * `id альбома` и `id группы` Вконтакте, в которой будет публиковаться запись. Они кладутся в файл `.env` под именами `VK_ALBUM_ID` и `VK_GROUP_ID` соответственно. Узнать `id группы` можно [здесь](http://regvk.com/id/).

5. Для работы с Telegram потребуется:
    * Включить `VPN`, если мессенджер заблокирован в вашей стране 
    * Получить `bot token` и положить его в `.env` под именем `TG_BOT_TOKEN`, об этом [здесь](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
    * Добавить имя канала  в `.env` в виде `@chanel_name` под именем `TG_CHAT_URL`.

6. Для работы с Facebook потребуется:
    * `User Access Token` с правом `publish_to_groups`, проще получить его с помощью [Graph API Explorer](https://developers.facebook.com/tools/explorer/). Полученный токен положить в `.env`, имя `FB_TOKEN`. Руководство по GAE [тут](https://developers.facebook.com/docs/graph-api/explorer/). Продление токена с 2 часов до 2 месяцев [тут](https://developers.facebook.com/tools/debug/accesstoken/)
    * `id группы` Facebook, в которой будет публиковаться запись. Занести в `.env`, имя `FB_GROUP_ID`.

7. Запустите файл `post_all_sm.py` с двумя аргументами:
    1. Путь к изображению
    2. Путь к тексту
    ```
    python post_all_sm.py /images/image.jpg /texts/text.txt
    ``` 

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).