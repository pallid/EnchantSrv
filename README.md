# http-cервис проверки орфографии
Обвертка для использования библиотеки [PyEnchant](https://pythonhosted.org/pyenchant/) как http-сервис

# Установка 

- устанавливаем библиотеку [PyEnchant](https://pythonhosted.org/pyenchant/).
- добавляем словари для русского языка

>Файлы словаря "ru_RU.dic" и "ru_RU.aff" можно взять из офисных пакетов openoffice и libreoffice
>Их необходимо скопировать в папку `..Python36/Lib/site-packages/enchant/share/enchant/myspell`

- клонируем репозиторий

    `git clone git://github.com/pallid/EnchantSrv.git`

- запускаем сервис

    `python EnchantSrv.py`

# Примеры использования

Пример написан на [oscript](http://oscript.io/), при небольшой модификации портируется на 1С

- Запуск скрипта с примером

    `oscript ExampleClient.os`


