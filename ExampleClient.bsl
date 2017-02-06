#Использовать json

Функция ПроверкаСлова(Слово)

	Соединение = Новый HTTPСоединение("localhost",8080);
	Запрос = Новый HTTPЗапрос("/");
	
	ЗаписьJSON = Новый ЗаписьJSON;
	ЗаписьJSON.УстановитьСтроку(Новый ПараметрыЗаписиJSON);	
	ЗаписьJSON.ЗаписатьНачалоОбъекта();
	
	ЗаписьJSON.ЗаписатьИмяСвойства("word");
	ЗаписьJSON.ЗаписатьЗначение(Слово);
	
	ЗаписьJSON.ЗаписатьКонецОбъекта();
	Запрос.УстановитьТелоИзСтроки(ЗаписьJSON.Закрыть(), "UTF-8");
	
	РезультатЗапросаКСервису = Неопределено;
	Попытка
		РезультатЗапросаКСервису = Соединение.ОтправитьДляОбработки(Запрос);
	Исключение
		Сообщить("Не удалось выполнить склонение с помощью сервиса..");
	КонецПопытки;
	
	ПарсерJSON = Новый ПарсерJSON();	
	РезультатЧтения = ПарсерJSON.ПрочитатьJSON(РезультатЗапросаКСервису.ПолучитьТелоКакСтроку("UTF-8"));

	Если ТипЗнч(РезультатЧтения) = Тип("Булево") Тогда
	     Сообщить(РезультатЧтения);
	КонецЕсли;

	Если ТипЗнч(РезультатЧтения) = Тип("Массив") Тогда
		Сч = 0;
		Для Каждого Эл Из РезультатЧтения Цикл
			Сообщить(Эл);
			Сч = Сч + 1;
		КонецЦикла;
	КонецЕсли;

КонецФункции	

ПроверкаСлова("Привет");