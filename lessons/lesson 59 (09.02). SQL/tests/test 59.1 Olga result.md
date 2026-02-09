Вопросы с выбором варианта: 100/100%  
# Вопрос 1. Тема: Основы SQL
  
**1. Какая команда используется для извлечения всех записей из таблицы в SQL?**
  
Варианты ответов:
1) SELECT all FROM table_name;
2) ✅ SELECT * FROM table_name;
3) SELECT FROM table_name;
4) SELECT 1 FROM table_name;
  
### ИИ анализ
Команда `SELECT * FROM table_name;` является стандартным синтаксисом SQL для выбора всех столбцов из указанной таблицы.  Символ `*` является специальным оператором, обозначающим "все столбцы".  Другие варианты либо неполны, либо используют несуществующий синтаксис.  

# Вопрос 2. Тема: Основы SQL
  
**2. Как ограничить выборку по конкретному условию?**
  
Варианты ответов:
1) SELECT * WHERE condition FROM table_name;
2) SELECT WHERE condition FROM table_name;
3) SELECT * FROM table_name ORDER BY condition;
4) ✅ SELECT * FROM table_name WHERE condition;
  
### ИИ анализ
Для фильтрации записей по условию в SQL используется предложение `WHERE`.  Оно должно располагаться после `FROM table_name` и перед любым предложением `ORDER BY`.  Правильный порядок ключевых слов: `SELECT` -> `FROM` -> `WHERE`.  

# Вопрос 3. Тема: Основы SQL
  
**3. Как отсортировать результаты по убыванию значения в столбце age?**
  
Варианты ответов:
1) SELECT * FROM table_name WHERE age ORDER BY DESC;
2) ✅ SELECT * FROM table_name ORDER BY age DESC;
3) SELECT * FROM table_name ORDER BY DESC age;
4) SELECT * ORDER BY age FROM table_name;
  
### ИИ анализ
Сортировка выполняется с помощью предложения `ORDER BY`, за которым следует имя столбца и ключевое слово `DESC` для указания порядка по убыванию.  Ключевое слово `DESC` должно стоять после имени столбца.  Предложение `ORDER BY` обычно является последним в запросе.  

# Вопрос 4. Тема: Основы SQL
  
**4. Как выбрать записи, где age меньше 30 или salary больше 50000, и отсортировать их по name?**
  
Варианты ответов:
1) SELECT * FROM table_name WHERE age < 30 OR salary > 50000 name;
2) SELECT * FROM table_name ORDER BY age < 30 OR salary > 50000, name;
3) SELECT * FROM table_name WHERE age < 30 AND salary > 50000 ORDER BY name;
4) ✅ SELECT * FROM table_name WHERE age < 30 OR salary > 50000 ORDER BY name;
  
### ИИ анализ
Для объединения условий используется логический оператор `OR`.  Предложение `ORDER BY` для сортировки по столбцу `name` должно быть отделено от условия `WHERE`.  Вариант с `AND` неверен, так как он требует одновременного выполнения обоих условий, что не соответствует постановке задачи.  

# Вопрос 5. Тема: Основы SQL
  
**5. Как выбрать записи, где salary больше 50000 и age больше 25?**
  
Варианты ответов:
1) SELECT * FROM table_name WHERE salary > 30000 NOT age > 25;
2) ✅ SELECT * FROM table_name WHERE salary > 30000 AND age > 25;
3) SELECT * FROM table_name WHERE salary > 30000 OR age > 25;
4) SELECT * FROM table_name WHERE salary > 30000, age > 25;
  
### ИИ анализ
Для одновременного выполнения двух условий используется логический оператор `AND`.  Оператор `OR` вернул бы записи, удовлетворяющие хотя бы одному условию, что не соответствует требованию "и".  В SQL условия перечисляются через логические операторы, а не через запятую.
