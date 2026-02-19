Вопросы с выбором варианта: 78/78%  
# Вопрос 1. Блок 3. Текстовый контент, ссылки, списки, изображения
  
### Содержание и вопросы

- Как сделать ссылку и какие бывают `href`?
- Чем `ul` отличается от `ol`?
- Зачем нужен `alt` у изображения?
- Как структурировать “карточку” проекта только HTML-ом?

### Материал (лаконично)

- Ссылка это тег `a`. Внутри должен быть текст, по которому понятно, куда ведет ссылка.
- `href` может быть:
  - обычным адресом сайта
  - якорем внутри страницы
  - `mailto:` для письма
- Списки:
  - `ul` когда порядок не важен, например “навыки”
  - `ol` когда это шаги, порядок важен
- Картинка это `img`. `alt` обязателен. Если картинка не загрузится, текст `alt` подскажет, что там должно быть.
- “Карточка” проекта это просто блок. Обычно внутри: заголовок, текст, ссылка.
  
Варианты ответов:
1) ✅ Прочитано
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Практическое задание (Блок 3)
  
### Условия

Добавь контент в `index.html` пошагово:

1. В одной из секций добавь заголовок и под ним список.
2. Заполни список из 5 пунктов.
3. В секции с проектами создай контейнер для карточек.
4. Создай минимум 3 карточки. В каждой карточке сделай:
   - заголовок карточки
   - короткий текст-описание
   - ссылку
5. В шапке добавь изображение-аватар.
6. В подвале сделай блок контактов и добавь минимум 3 ссылки.
7. Проверь, что у всех `img` есть `alt`, а у всех `a` есть `href`.

Проверка:

- Все ссылки кликабельны.
- Все изображения имеют `alt`.

### Псевдокод решения

```text
IN SECTION_B
  CREATE LIST
    ADD LIST_ITEM (REPEAT 5 TIMES)

IN SECTION_C
  CREATE CARDS_CONTAINER
    REPEAT 3 TIMES
      CREATE CARD
        ADD CARD_TITLE
        ADD CARD_TEXT
        ADD CARD_LINK

IN HEADER
  ADD IMAGE_WITH_ALT

IN FOOTER
  CREATE CONTACTS_LIST
    ADD LINK_ITEM (REPEAT 3 TIMES)
END
```

### Если использовал ИИ, обязательные изменения вручную

- Замени один тип списка на другой (например, `ul` на `ol` или наоборот) и объясни почему это подходит.
- Добавь еще одну ссылку с другим типом `href` (например, `mailto:`).

---

**Вставь решение в комментарий ниже:**
  
### Ответ
<!doctype html>  
<html lang="ru">  
<head>  
  <meta charset="UTF-8" />  
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>  
  <title>Страница-визитка</title>  
  <link rel="stylesheet" href="styles.css" />  
</head>  
<body>  
  
  <header>  
    <!-- Добавлено изображение-аватар с alt -->  
    <img src="avatar.jpg" alt="Аватар пользователя" width="80" height="80" />  
    <h1>Главный заголовок страницы</h1>  
    <p>Короткая строка-описание</p>  
  </header>  
  
  <main>  
  
    <section>  
      <h2>Секция 1</h2>  
      <p>Краткое описание или текст в первой секции.</p>  
    </section>  
  
    <section>  
      <h2>Секция 2</h2>  
      <!-- Заголовок и под ним список из 5 пунктов -->  
      <h3>Навыки</h3>  
      <ol>  
        <li>HTML</li>  
        <li>CSS</li>  
        <li>JavaScript</li>  
        <li>Git</li>  
        <li>React</li>  
      </ol>  
    </section>  
  
    <section>  
      <h2>Секция 3</h2>  
      <p>Дополнительный текст или элементы страницы.</p>  
      <!-- Контейнер для карточек с проектами -->  
      <div class="cards-container">  
  
        <article class="card">  
          <h3>Проект 1</h3>  
          <p>Краткое описание первого проекта.</p>  
          <a href="https://example.com/project1">Подробнее</a>  
        </article>  
  
        <article class="card">  
          <h3>Проект 2</h3>  
          <p>Описание второго проекта в двух словах.</p>  
          <a href="https://example.com/project2">Подробнее</a>  
        </article>  
  
        <article class="card">  
          <h3>Проект 3</h3>  
          <p>Краткий текст о третьем проекте.</p>  
          <a href="https://example.com/project3">Подробнее</a>  
        </article>  
  
      </div>  
    </section>  
  
  </main>  
  
  <footer>  
    <!-- Блок контактов с минимум 3 ссылками -->  
    <div class="contacts">  
      <a href="mailto:email@example.com">Email</a> |  
      <a href="mailto:email@example.com">Email</a> |  
      <a href="https://t.me/username" target="_blank" rel="noopener">Telegram</a> |  
      <a href="https://github.com/username" target="_blank" rel="noopener">GitHub</a>  
    </div>  
  </footer>  
  
</body>  
</html>  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Какой HTML-тег используется для создания обычной ссылки на другую страницу?
  
  
Варианты ответов:
1) `span`
2) `p`
3) `div`
4) `img`
5) ✅ `a`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Какой тип списка лучше подходит для раздела “навыки”, где порядок элементов не имеет значения?
  
  
Варианты ответов:
1) ✅ `ul`
2) `ol`
3) `form`
4) `nav`
5) `table`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Зачем нужен атрибут `alt` у тега изображения `img`?
  
  
Варианты ответов:
1) Для выравнивания текста
2) Для подключения CSS
3) Для создания отступов
4) ✅ Для текстового описания картинки
5) Для изменения размера картинки
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Какое значение атрибута `href` используется для создания ссылки, которая открывает почтовую программу?
  
  
Варианты ответов:
1) `css:`
2) `http:`
3) `file:`
4) ✅ `mailto:`
5) `ftp:`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Какие элементы обычно должны быть внутри “карточки проекта” на странице-визитке?
  
  
Варианты ответов:
1) Только картинка без текста
2) Только таблица с данными
3) Только `meta` теги
4) Только `script` код
5) ✅ Заголовок, текст, ссылка
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 8. Что нужно проверить после добавления ссылок и изображений на страницу?
  
  
Варианты ответов:
1) ✅ Что все ссылки имеют `href`
2) Что нет `main`
3) Что нет `section`
4) Что `head` пустой
5) Что нет `footer`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 9. Какое главное требование к тексту внутри ссылки для удобства пользователей?
  
  
Варианты ответов:
1) Чтобы он был на одной букве
2) ✅ Чтобы он был понятным
3) Чтобы он был скрыт стилями
4) Чтобы он был только цифрами
5) Чтобы он был пустым
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
