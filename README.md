# GameOFTeens2023_PYTHON
lifecell bot

ANONCMENT !!!
НА ЖАЛЬ, Я НЕ ВСТИГ ПОВНІСТЮ ЗАВЕРШИТИ ФУНКЦОНАЛ БОТА, ТОМУ  В КОДІ ПРИСУТНІ ПОМИЛКИ І  ПСЕВДОКОД (ДОДАВ АБИ ПОЯСНИТИ СВОЮ ІДЕЮ)



МОЯ МАТЕМАТИЧНА МОДЕЛЬ (МОДЕЛЬ КОРИСТУВАЧА І ТАРИФУ - у файлах з відповідною назвою)
На основі даних про тарифи я створив масиви, що їм відповідають (tariif_model). ОТже, тариф - собою являє набір числовмих значень, що можна вважати точкою в n-вимірному просторі

ТАРИФ _ ТОЧКА


ПРОФІЛЬ КОИСТУВАЧА:
В результаті опитування користувача формується так само масив з числових значень (user profile), але він не схожий на тириф, бо деякі властивості мають екстркмуми (максимальне й мінімальне значення), тобо є проміжками, або ж векторами. Виходячи з цього профіль користувача є сукупністю векторів, тензором або ж фігурою.

ПРОФІЛЬ _ ФІГУРА

РЕКОМЕНДАЦІЯ

Перед тим як дати користувачеві рекомендацію тарифу в програмі здійснюється процес підготовки даних до порівння. Значення деяких властивостей потрібно відрегуляювати. ВЕЛИКА підготовка чекає і на профіль користувача. У цій фігурі потрібно знайти геометричний центр мас, що буде являти союою сукупність середніх арифметичних усіх векторів . ТАким чином ми теж отримали точку (user_proffile_point) 

ДЛЯ встановлення рекомендації використаємо евклідову відстань між цими точками (тарифу і користувача). "Найближче" рекомендуємо. Також можна і косиносовою наближеністю
