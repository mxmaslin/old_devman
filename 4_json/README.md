# Prettify JSON

JSON – популярный формат передачи данных. Он универсальный, текстовый, удобный и распространённый.

В "сыром" виде он выглядит так:

```bash
[{'Cells':{'Address': 'улица Академика Павлова, дом 10','AdmArea':'Западный административный округ','ClarificationOfWorkingHours':None,'District':'район Кунцево','IsNetObject':'да','Name':'Ароматный Мир','OperatingCompany':'Ароматный Мир','PublicPhone':[{'PublicPhone':'(495) 777-51-95'}],'TypeService':'реализация продовольственных товаров','WorkingHours':[{'DayOfWeek':'понедельник','Hours': '09:30-22:30'},{'DayOfWeek': 'вторник', 'Hours': '09:30-22:30'},{'DayOfWeek': 'среда', 'Hours': '09:30-22:30'},{'DayOfWeek': 'четверг', 'Hours': '09:30-22:30'},{'DayOfWeek': 'пятница', 'Hours': '09:30-22:30'},{'DayOfWeek': 'суббота', 'Hours': '09:30-22:30'},{'DayOfWeek': 'воскресенье','Hours': '09:30-22:30'}],'geoData': {'coordinates': [37.39703804817934, 55.740999719549094],'type': 'Point'},'global_id': 14371450},'Id': '79742784-9ef3-4543-bc98-a219a8903c18','Number': 1}]
```

# Quickstart

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.

Запуск на Linux:

```bash

$ python pprint_json.py <path to file> # possibly requires call of python3 executive instead of just python

[{'Cells': {'Address': 'улица Академика Павлова, дом 10',
            'AdmArea': 'Западный административный округ',
            'ClarificationOfWorkingHours': None,
            'District': 'район Кунцево',
            'IsNetObject': 'да',
            'Name': 'Ароматный Мир',
            'OperatingCompany': 'Ароматный Мир',
            'PublicPhone': [{'PublicPhone': '(495) 777-51-95'}],
            'TypeService': 'реализация продовольственных товаров',
            'WorkingHours': [{'DayOfWeek': 'понедельник',
                              'Hours': '09:30-22:30'},
                             {'DayOfWeek': 'вторник', 'Hours': '09:30-22:30'},
                             {'DayOfWeek': 'среда', 'Hours': '09:30-22:30'},
                             {'DayOfWeek': 'четверг', 'Hours': '09:30-22:30'},
                             {'DayOfWeek': 'пятница', 'Hours': '09:30-22:30'},
                             {'DayOfWeek': 'суббота', 'Hours': '09:30-22:30'},
                             {'DayOfWeek': 'воскресенье',
                              'Hours': '09:30-22:30'}],
            'geoData': {'coordinates': [37.39703804817934, 55.740999719549094],
                        'type': 'Point'},
            'global_id': 14371450},
  'Id': '79742784-9ef3-4543-bc98-a219a8903c18',
  'Number': 1}
]
```

# Цели проекта

Код создан в учебных целях в рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
