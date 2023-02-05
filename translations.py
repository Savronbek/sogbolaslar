

translations = {
    'ru': {
        'AKE Education botiga xush kelibsiz!': 'Добро пожаловать в бот AKE Education!',
        'Xush kelibsiz!': 'Добро пожаловать!',
        'Manzil': 'Локация',
        'Kurslarga Yozilish': 'Записаться на курсы',
        'Murojaat uchun': 'Контакты',
        "Murojaat uchun\nUshbu raqamlarga qo'ng'iroq qilishingiz mumkin": "Для связи с нами можете позвонить по номерам:",
        'Kursingizni tanlang': 'Выберите себе курс',
        'Ismingizni kiriting: ': 'Введите свое имя: ',
        "Telefon raqam faqatgina sonda bo'lishi kerak!\nRaqamingizni kiriting": "Номер должен быть в цифрах.\nВведите свой номер? (только цифры)",
        'Telefon raqamingizni kiriting': 'Отправьте ваш номер телефона',
        "Telefon raqamni jo'natish": 'Отправить свои контакты',
        "Jinsingizni tanlang": "Выберите свой пол",
        'Erkak': 'Мужской',
        'Ayol': 'Женский',
        'Boshqa': 'Другой',
        'Kursingiz: ': 'Ваш курс: ',
        'Ismingiz: ': 'Имя: ',
        'Telefon raqamingiz: ': 'Номер: ',
        'Jinsingiz: ': 'Пол: ',
        'Ortga': 'Назад',
        'Siz bosh menuga qayttingiz': 'Вы вернулись в главное меню',

    }
}



def _(text, lang='uz'):
    if lang == 'uz':
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text

