from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btnMain = KeyboardButton('Назад')

# --- Главное меню ---

btnMain1 = KeyboardButton('Вопросы по конкурсу')
btnMain2 = KeyboardButton('Вопросы по заявке на конкурс')
btnMain3 = KeyboardButton('Вопросы по регистрации в ИС')
btnMain4 = KeyboardButton('Вопросы по разделу "Бюджет"')
btnMain5 = KeyboardButton('Обратная связь с АО "НЦГНТЭ"')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnMain1,btnMain2,btnMain3,btnMain4,btnMain5)

# --- Подменю "Вопросы по конкурсу" ---

btn1menu1 = KeyboardButton('Кто может участвовать в конкурсе для молодых ученых?')
btn1menu2 = KeyboardButton('Какие возрастные ограничения для участников на конкурс для молодых ученых?')
btn1menu3 = KeyboardButton('Могут ли студенты последних курсов бакалавра участвовать в конкурсе для молодых ученых?')
menu1 = ReplyKeyboardMarkup(resize_keyboard= True).add(btn1menu1,btn1menu2,btn1menu3,btnMain)

# --- Подменю "Вопросы по заявке на конкурс" ---

btn2menu1 = KeyboardButton('Как подать заявку?')
btn2menu2 = KeyboardButton('Можно ли повторно подавать заявку, неодобренную к финансированию в прошедших конкурсах?')
btn2menu3 = KeyboardButton('Можно ли подать заявку если я исполнитель в одном проекте и научный руководитель в другом?')
btn2menu4 = KeyboardButton('Как выглядит и где посмотреть ИРН заявку??')
btn2menu5 = KeyboardButton('Члены исследовательской группы должны ли подписывать через ЭЦП свое участие в проекте')
menu2 = ReplyKeyboardMarkup(resize_keyboard= True).add(btn2menu1,btn2menu2,btn2menu3,btn2menu4,btn2menu5,btnMain)

# --- Подменю "Вопросы по регистрации в ИС" ---

btn3menu1 = KeyboardButton('Необходима ли регистрация в системе всех членов исследовательской группы?')
btn3menu2 = KeyboardButton('Забыл электронную почту, указанную при регистрации')
btn3menu3 = KeyboardButton('Забыл пароль от личного кабинета')
menu3 = ReplyKeyboardMarkup(resize_keyboard= True).add(btn3menu1,btn3menu2,btn3menu3,btnMain)

# --- Подменю "Вопросы по разделу "Бюджет"" ---

btn4menu1 = KeyboardButton('Ошибка о превышении 60% фонда заработной платы')
btn4menu2 = KeyboardButton('Учитывать ли в налогах ОПВ и ИПН?')
btn4menu3 = KeyboardButton('Почему в таблице «Налоги и другие обязательные платежи в бюджет» указаны ОПВ работодателя?')
btn4menu4 = KeyboardButton('В какой валюте указывать суммы в заявках на разных языках?')
menu4 = ReplyKeyboardMarkup(resize_keyboard= True).add(btn4menu1,btn4menu2,btn4menu3,btn4menu4,btnMain)