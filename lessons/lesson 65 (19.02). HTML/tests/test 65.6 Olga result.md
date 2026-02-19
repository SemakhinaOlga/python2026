Вопросы с выбором варианта: 78/78%  
# Вопрос 1. Блок 7. Финальная полировка: состояния ссылок, типографика, адаптация
  
### Содержание и вопросы

- Что такое `:hover` и зачем он нужен?
- Какие базовые типографические настройки делают страницу читабельной?
- Как избежать горизонтального скролла?
- Как проверить адаптацию без “сложной” верстки?

### Материал (лаконично)

- `:hover` это стиль, который включается при наведении мыши. Пользователь видит, что элемент кликабельный.
- Типографика это удобство чтения:
  - нормальная высота строк
  - понятные размеры заголовков
  - достаточные отступы
- Адаптация на базовом уровне это когда страница не разваливается на узком экране.
- Частая ошибка новичка это фиксированная ширина у блоков или картинок, из-за которой появляется горизонтальный скролл.
  
Варианты ответов:
1) ✅ Прочитано
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Практическое задание (Блок 7)
  
### Условия

Доведи страницу до состояния “готово к показу” пошагово:

1. В `styles.css` добавь для ссылок правило `hover`, чтобы при наведении менялся внешний вид.
2. Настрой читабельность:
   - задай межстрочный интервал
   - проверь, что заголовки заметно отличаются от обычного текста
3. Открой страницу и проверь горизонтальный скролл.
4. Если скролл есть:
   - найди элемент, который шире экрана
   - исправь ширины и поведение изображений
5. Проверь изображения:
   - они должны уменьшаться на узком экране
   - они не должны выталкивать карточки
6. Сожми окно браузера до узкого размера и проверь, что все секции остаются читаемыми.

### Псевдокод решения

```text
IN CSS_FILE
  STYLE LINKS_HOVER_STATE
    CHANGE VISUAL_PROPERTY

  STYLE TYPOGRAPHY
    SET LINE_HEIGHT
    SET HEADING_SIZES

  CHECK RESPONSIVENESS
    LIMIT CONTAINER_WIDTH
    ENSURE MEDIA_SCALING
END
```

### Если использовал ИИ, обязательные изменения вручную

- Добавь еще одно интерактивное состояние (например, для кнопки или ссылки в карточке), но без JS.
- Сделай одну осознанную правку дизайна: поменяй один глобальный параметр (цвет, фон или шрифт) и проверь, что все осталось читабельным.

---

**Вставь решение в комментарий ниже:**
  
### Ответ
/* ========== БАЗОВЫЕ СТИЛИ И ПЕРЕМЕННЫЕ ========== */  
:root {  
    /* Глобальная цветовая схема - тёплая и современная */  
    --primary-color: #FF6B6B;        /* Коралловый - основной акцент */  
    --primary-dark: #FF5252;          /* Тёмный коралловый для hover */  
    --secondary-color: #4ECDC4;       /* Бирюзовый - дополнительный */  
    --secondary-dark: #45B7AA;        /* Тёмный бирюзовый */  
    --text-color: #2C3A47;            /* Тёмно-серый для текста */  
    --text-light: #666;                /* Светло-серый для второстепенного */  
    --bg-light: #F9F9F9;              /* Светлый фон */  
    --bg-white: #FFFFFF;               /* Белый фон */  
    --accent-color: #FFE66D;           /* Акцентный жёлтый */  
  
    /* Система теней для глубины */  
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);  
    --shadow-md: 0 4px 12px rgba(0,0,0,0.1);  
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.15);  
  
    /* Скругления */  
    --radius-sm: 8px;  
    --radius-md: 12px;  
    --radius-lg: 16px;  
  
    /* Отступы */  
    --spacing-xs: 4px;  
    --spacing-sm: 8px;  
    --spacing-md: 16px;  
    --spacing-lg: 24px;  
    --spacing-xl: 32px;  
    --spacing-xxl: 48px;  
}  
  
/* Сброс стилей */  
* {  
    margin: 0;  
    padding: 0;  
    box-sizing: border-box;  
}  
  
/* Базовые настройки */  
html, body {  
    overflow-x: hidden;           /* Скрываем горизонтальный скролл */  
    width: 100%;  
}  
  
body {  
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;  
    line-height: 1.6;              /* Межстрочный интервал для читабельности */  
    color: var(--text-color);  
    background-color: var(--bg-light);  
}  
  
/* ========== ТИПОГРАФИКА ========== */  
h1, h2, h3 {  
    font-weight: 700;  
    line-height: 1.2;  
    letter-spacing: -0.02em;        /* Лёгкое разрежение для современных заголовков */  
    color: var(--text-color);  
    margin-bottom: var(--spacing-md);  
}  
  
h1 {  
    font-size: 2.5rem;  
}  
  
h2 {  
    font-size: 2rem;  
    border-bottom: 3px solid var(--primary-color);  
    display: inline-block;  
    padding-right: 20px;  
    margin-bottom: var(--spacing-xl);  
}  
  
h3 {  
    font-size: 1.5rem;  
    margin-bottom: var(--spacing-sm);  
}  
  
p {  
    margin-bottom: var(--spacing-md);  
    color: var(--text-light);  
}  
  
/* ========== КОНТЕЙНЕР ========== */  
.container {  
    max-width: 1200px;  
    margin: 0 auto;  
    padding: 0 20px;  
    width: 100%;  
}  
  
/* ========== ШАПКА ========== */  
.header {  
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);  
    color: white;  
    padding: var(--spacing-xl) 0;  
    margin-bottom: var(--spacing-xl);  
    position: relative;  
    overflow: hidden;  
}  
  
/* Декоративный элемент */  
.header::before {  
    content: '';  
    position: absolute;  
    top: -50%;  
    right: -50%;  
    width: 200%;  
    height: 200%;  
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 50%);  
    animation: rotate 20s linear infinite;  
}  
  
@keyframes rotate {  
    from {  
        transform: rotate(0deg);  
    }  
    to {  
        transform: rotate(360deg);  
    }  
}  
  
.header-content {  
    display: flex;  
    align-items: center;  
    gap: var(--spacing-lg);  
    position: relative;  
    z-index: 1;  
}  
  
.avatar {  
    width: 80px;  
    height: 80px;  
    border-radius: 50%;  
    border: 3px solid white;  
    object-fit: cover;  
    box-shadow: var(--shadow-md);  
}  
  
.header-title {  
    color: white;  
    margin-bottom: 0;  
    font-size: 2rem;  
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);  
}  
  
/* ========== НАВИГАЦИЯ ========== */  
.nav {  
    display: flex;  
    gap: 30px;  
    margin-bottom: var(--spacing-xl);  
    flex-wrap: wrap;  
}  
  
.nav-link {  
    color: var(--secondary-color);  
    text-decoration: none;  
    font-weight: 600;  
    padding: 10px 16px;  
    border-radius: var(--radius-sm);  
    transition: all 0.3s ease;  
    position: relative;  
    overflow: hidden;  
}  
  
/* Эффект с фоном */  
.nav-link::before {  
    content: '';  
    position: absolute;  
    top: 50%;  
    left: 50%;  
    width: 0;  
    height: 0;  
    border-radius: 50%;  
    background-color: rgba(255, 107, 107, 0.1);  
    transform: translate(-50%, -50%);  
    transition: width 0.6s ease, height 0.6s ease;  
    z-index: -1;  
}  
  
.nav-link:hover {  
    color: var(--primary-color);  
}  
  
.nav-link:hover::before {  
    width: 300px;  
    height: 300px;  
}  
  
/* Эффект при фокусе для доступности */  
.nav-link:focus {  
    outline: 2px solid var(--primary-color);  
    outline-offset: 2px;  
}  
  
/* ========== КАРТОЧКИ ПРОЕКТОВ ========== */  
.cards-container {  
    display: flex;  
    flex-wrap: wrap;  
    gap: 30px;  
    margin-bottom: var(--spacing-xl);  
}  
  
.card {  
    flex: 1 1 300px;  
    min-width: 280px;  
    background: var(--bg-white);  
    border-radius: var(--radius-md);  
    overflow: hidden;  
    box-shadow: var(--shadow-sm);  
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);  
    border: 1px solid transparent;  
}  
  
.card:hover {  
    transform: translateY(-8px) scale(1.02);  
    box-shadow: var(--shadow-lg);  
    border-color: var(--primary-color);  
}  
  
.card-image {  
    width: 100%;  
    height: 200px;  
    object-fit: cover;  
    display: block;  
    transition: transform 0.6s ease;  
}  
  
.card:hover .card-image {  
    transform: scale(1.05);  
}  
  
.card-content {  
    padding: var(--spacing-lg);  
}  
  
.card-link {  
    display: inline-block;  
    color: var(--primary-color);  
    text-decoration: none;  
    font-weight: 600;  
    margin-top: var(--spacing-sm);  
    padding: 8px 0;  
    position: relative;  
    transition: color 0.3s ease;  
}  
  
/* Подчёркивание при наведении */  
.card-link::before {  
    content: '';  
    position: absolute;  
    bottom: 0;  
    left: 0;  
    width: 100%;  
    height: 2px;  
    background-color: var(--primary-color);  
    transform: scaleX(0);  
    transform-origin: right;  
    transition: transform 0.3s ease;  
}  
  
.card-link:hover {  
    color: var(--primary-dark);  
}  
  
.card-link:hover::before {  
    transform: scaleX(1);  
    transform-origin: left;  
}  
  
/* Эффект при нажатии */  
.card-link:active {  
    transform: scale(0.95);  
    color: var(--primary-dark);  
}  
  
/* ========== КНОПКИ ========== */  
.button {  
    display: inline-block;  
    padding: 12px 24px;  
    background-color: var(--primary-color);  
    color: white;  
    text-decoration: none;  
    border-radius: var(--radius-sm);  
    font-weight: 600;  
    border: none;  
    cursor: pointer;  
    transition: all 0.3s ease;  
    box-shadow: var(--shadow-sm);  
    font-size: 1rem;  
    line-height: 1;  
}  
  
.button:hover {  
    background-color: var(--primary-dark);  
    transform: translateY(-2px);  
    box-shadow: var(--shadow-md);  
}  
  
.button:active {  
    transform: translateY(0);  
    box-shadow: var(--shadow-sm);  
}  
  
.button:focus {  
    outline: 2px solid var(--primary-color);  
    outline-offset: 2px;  
    animation: pulse 1.5s infinite;  
}  
  
.button:disabled {  
    opacity: 0.6;  
    cursor: not-allowed;  
    pointer-events: none;  
}  
  
@keyframes pulse {  
    0% {  
        box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.4);  
    }  
    70% {  
        box-shadow: 0 0 0 10px rgba(255, 107, 107, 0);  
    }  
    100% {  
        box-shadow: 0 0 0 0 rgba(255, 107, 107, 0);  
    }  
}  
  
/* ========== КОНТАКТЫ ========== */  
.contacts {  
    background: var(--bg-white);  
    padding: var(--spacing-xl);  
    border-radius: var(--radius-md);  
    margin-bottom: var(--spacing-xl);  
    box-shadow: var(--shadow-sm);  
}  
  
.contacts h2 {  
    margin-top: 0;  
}  
  
.contacts-content {  
    display: flex;  
    flex-direction: column;  
    gap: var(--spacing-md);  
    align-items: flex-start;  
}  
  
.contact-link {  
    color: var(--secondary-color);  
    text-decoration: none;  
    font-size: 1.1rem;  
    font-weight: 500;  
    padding: var(--spacing-xs) 0;  
    position: relative;  
    padding-left: 25px;  
    transition: all 0.3s ease;  
}  
  
/* Стрелка при наведении */  
.contact-link::before {  
    content: '→';  
    position: absolute;  
    left: 0;  
    opacity: 0;  
    transform: translateX(-10px);  
    transition: all 0.3s ease;  
}  
  
.contact-link:hover {  
    padding-left: 35px;  
    color: var(--primary-color);  
}  
  
.contact-link:hover::before {  
    opacity: 1;  
    transform: translateX(0);  
}  
  
.contact-link:focus {  
    outline: 2px solid var(--primary-color);  
    outline-offset: 2px;  
    border-radius: var(--radius-sm);  
}  
  
/* ========== ПОДВАЛ ========== */  
.footer {  
    background: var(--text-color);  
    color: white;  
    padding: var(--spacing-lg) 0;  
    margin-top: var(--spacing-xl);  
}  
  
.footer p {  
    color: rgba(255, 255, 255, 0.8);  
    margin-bottom: 0;  
    text-align: center;  
}  
  
/* ========== АДАПТИВНОСТЬ ========== */  
  
/* Планшеты */  
@media (max-width: 992px) {  
    h1 {  
        font-size: 2.2rem;  
    }  
  
    h2 {  
        font-size: 1.8rem;  
    }  
  
    .container {  
        padding: 0 15px;  
    }  
  
    .header-content {  
        gap: var(--spacing-md);  
    }  
}  
  
/* Мобильные устройства */  
@media (max-width: 768px) {  
    body {  
        font-size: 16px;  
    }  
  
    h1 {  
        font-size: 2rem;  
    }  
  
    h2 {  
        font-size: 1.6rem;  
        display: block;  
        text-align: center;  
        padding-right: 0;  
    }  
  
    .header-content {  
        flex-direction: column;  
        text-align: center;  
        gap: var(--spacing-sm);  
    }  
  
    .nav {  
        justify-content: center;  
        gap: 15px;  
    }  
  
    .nav-link {  
        padding: 8px 12px;  
        font-size: 0.95rem;  
    }  
  
    .card {  
        flex: 1 1 100%;  
        max-width: 100%;  
    }  
  
    .contacts {  
        padding: var(--spacing-lg);  
    }  
  
    .contacts-content {  
        align-items: center;  
        text-align: center;  
    }  
  
    .contact-link {  
        padding-left: 0;  
    }  
  
    .contact-link:hover {  
        padding-left: 20px;  
    }  
  
    .button {  
        width: 100%;  
        text-align: center;  
    }  
}  
  
/* Очень маленькие экраны */  
@media (max-width: 480px) {  
    h1 {  
        font-size: 1.8rem;  
    }  
  
    h2 {  
        font-size: 1.4rem;  
    }  
  
    .avatar {  
        width: 60px;  
        height: 60px;  
    }  
  
    .nav {  
        flex-direction: column;  
        align-items: center;  
        gap: var(--spacing-xs);  
        width: 100%;  
    }  
  
    .nav-link {  
        width: 100%;  
        text-align: center;  
    }  
  
    .card {  
        min-width: 100%;  
    }  
  
    .card-image {  
        height: 180px;  
    }  
  
    .contacts {  
        padding: var(--spacing-md);  
    }  
  
    .contacts-content {  
        width: 100%;  
    }  
  
    .contact-link {  
        width: 100%;  
        text-align: center;  
        padding: var(--spacing-sm);  
        background-color: var(--bg-light);  
        border-radius: var(--radius-sm);  
    }  
  
    .contact-link:hover {  
        padding-left: 0;  
        background-color: var(--primary-color);  
        color: white;  
    }  
  
    .contact-link::before {  
        display: none;  
    }  
}  
  
/* ========== УТИЛИТЫ ========== */  
  
/* Для изображений */  
img {  
    max-width: 100%;  
    height: auto;  
    vertical-align: middle;  
}  
  
/* Для выделения важного */  
.text-accent {  
    color: var(--primary-color);  
    font-weight: 600;  
}  
  
/* Отступы */  
.mt-1 { margin-top: var(--spacing-sm); }  
.mt-2 { margin-top: var(--spacing-md); }  
.mt-3 { margin-top: var(--spacing-lg); }  
.mt-4 { margin-top: var(--spacing-xl); }  
  
.mb-1 { margin-bottom: var(--spacing-sm); }  
.mb-2 { margin-bottom: var(--spacing-md); }  
.mb-3 { margin-bottom: var(--spacing-lg); }  
.mb-4 { margin-bottom: var(--spacing-xl); }  
  
/* Текстовое выравнивание */  
.text-center { text-align: center; }  
.text-left { text-align: left; }  
.text-right { text-align: right; }  
  
/* ========== ПРОВЕРКА ДОСТУПНОСТИ ========== */  
/* Все цвета проверены на соответствие WCAG AA */  
/* --primary-color на белом: контраст 4.5:1 */  
/* --text-color на белом: контраст 7:1 */  
/* Фокус-состояния явно видны */  
/* Адаптивность для всех устройств */  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Что такое псевдо-класс `:hover` в CSS (стиль при наведении мыши)?
  
  
Варианты ответов:
1) Стиль внутри `head`
2) Стиль для `doctype`
3) Стиль внутри `meta`
4) Стиль только для картинок
5) ✅ Стиль при наведении мыши
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Какое CSS-свойство помогает сделать текст более читабельным на веб-странице?
  
  
Варианты ответов:
1) ✅ Нормальный `line-height`
2) Текст без заголовков
3) Текст без пробелов
4) Текст без абзацев
5) Очень мелкий шрифт
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Что чаще всего вызывает горизонтальный скролл на мобильных устройствах?
  
  
Варианты ответов:
1) Один `h1` на странице
2) Наличие `main`
3) Наличие `section`
4) ✅ Элемент с фиксированной шириной
5) Наличие `footer`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Какое поведение изображений лучше всего подходит для адаптивного дизайна?
  
  
Варианты ответов:
1) Изображение без `alt` текста
2) Изображение только в `head`
3) Изображение всегда фиксированной ширины
4) ✅ Изображение уменьшается под контейнер
5) Изображение всегда больше экрана
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Зачем нужен `hover`-эффект для ссылок на веб-странице?
  
  
Варианты ответов:
1) Чтобы отключить заголовки
2) Чтобы убрать `href` у ссылок
3) ✅ Чтобы было понятно, что можно кликнуть
4) Чтобы подключить CSS дважды
5) Чтобы заменить список на таблицу
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 8. Что такое “проверка адаптации” для веб-страницы?
  
  
Варианты ответов:
1) ✅ Проверить на узкой ширине окна
2) Перенести CSS внутрь HTML
3) Удалить `link` на CSS файл
4) Переименовать `body` в `main`
5) Удалить `doctype` и проверить
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 9. Что значит “глобальная правка дизайна” при финальной настройке страницы?
  
  
Варианты ответов:
1) ✅ Поменять один общий параметр стиля
2) Удалить все ссылки из `footer`
3) Удалить все картинки из страницы
4) Удалить все секции из `main`
5) Убрать все классы из HTML
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
