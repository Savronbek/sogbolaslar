from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from translations import _


"""""""""""""""""""""""Start"""""""""""""""""""""""
subMenu = InlineKeyboardMarkup(row_width=2)
uzblang = InlineKeyboardButton(text="🇺🇿O'zbek tili", callback_data="lang_uz")
ruslang = InlineKeyboardButton(text="🇷🇺Русский язык", callback_data="lang_ru")
subMenu.insert(uzblang)
subMenu.insert(ruslang)





# """""""""""""""""""""""Main Menu"""""""""""""""""""""""
def mainMenu(lang):
    keyboard = InlineKeyboardMarkup(row_width=2)
    menu_sub_1 = InlineKeyboardButton(_('Kurslarga Yozilish', lang), callback_data='kurs')
    menu_sub_2 = InlineKeyboardButton(_('Manzil', lang), callback_data='location')
    menu_sub_3 = InlineKeyboardButton(_('Murojaat uchun', lang), callback_data='contact')
    keyboard.add(menu_sub_1, menu_sub_2, menu_sub_3)
    # keyboard.insert(menu_sub_2)
    # keyboard.insert(menu_sub_3)
    return keyboard



def phoneBtn(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    phone_btn = KeyboardButton(_("Telefon raqamni jo'natish", lang), request_contact=True)
    keyboard.add(phone_btn)
    return keyboard

def gender(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,selective=True)
    man = KeyboardButton(_('Erkak', lang))
    girl = KeyboardButton(_('Ayol', lang))
    another = KeyboardButton(_('Boshqa', lang))
    keyboard.add(man, girl)
    keyboard.add(another)
    return keyboard




# back buttons
def back(lang):
    keyboard = InlineKeyboardMarkup(row_width=1)
    menu_sub_1 = InlineKeyboardButton(_('Ortga', lang), callback_data='back')
    keyboard.add(menu_sub_1)
    # keyboard.insert(menu_sub_2)
    # keyboard.insert(menu_sub_3)
    return keyboard


def kursmenu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    menu_sub_1 = InlineKeyboardButton('Kurslarga Yozilish', callback_data='kurs')
    keyboard.add(menu_sub_1)
    return keyboard


