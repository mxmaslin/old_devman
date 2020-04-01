# Ближайшие бары

На сайте data.mos.ru есть много разных данных, в том числе список московских баров. Его можно скачать в формате JSON. Для этого нужно:

1. зарегистрироваться на сайте и получить ключ API;
2. скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.

А можно не тратить на это время и воспользоваться [ранее скачанным файлом](https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json).

Требуется написать скрипт, который рассчитает:

- самый большой бар
- самый маленький бар
- самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py --lat latitude --lon longitude path_to_bars_data_file # possibly requires call of python3 executive instead of just python
Largest bar is: Спорт бар «Красная машина». It has 450 seats. Its location is Автозаводская улица, дом 23, строение 1
Smallest bar is: БАР. СОКИ. It has 0 seats. Its location is Дубравная улица, дом 34/29
Closest bar is: Staropramen. It has 50 seats. Its location is Садовая-Спасская улица, дом 19, корпус 1
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
