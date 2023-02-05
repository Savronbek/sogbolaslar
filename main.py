import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as nav
from db import Database
from translations import _
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils import get_test_list_markup, get_test_questions
from data import msgs
import json
import string
from data import msgs, tests


TOKEN = "1993000522:AAHyDAquMqjnqc4KvT6y94tDRkZbF9dvjCk"

logging.basicConfig(level=logging.INFO)

# Initialize Bot
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

db = Database('database.db')

state_s = []


# global_state = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, '<b>Assalomu aleykum  |  Здравствуйте\n\nTilingizni tanlang  |  Выберите свой язык</b>', reply_markup=nav.subMenu, parse_mode='html')
    else:
        lang = db.get_lang(message.from_user.id)
        await bot.send_message(message.from_user.id, _('Xush kelibsiz!', lang), reply_markup=nav.mainMenu(lang))







# Language of user
@dp.callback_query_handler(text_contains = "lang_")
async def setlanguage(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    if not db.user_exists(callback.from_user.id):
        lang = callback.data[5:]
        db.add_user(callback.from_user.id, lang)
        await bot.send_message(callback.from_user.id, _('AKE Education botiga xush kelibsiz!', lang), reply_markup=nav.mainMenu(lang))



# Location of Learning centre
@dp.callback_query_handler(text='location')
async def Manzil(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_location(callback.from_user.id, latitude='41.275048', longitude='69.223709', reply_markup=nav.back(lang=db.get_lang(user_id=callback.from_user.id)))


# Contacts of Learning Centre
@dp.callback_query_handler(text='contact')
async def setcontact(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, _("Murojaat uchun\nUshbu raqamlarga qo'ng'iroq qilishingiz mumkin", lang=db.get_lang(user_id=callback.from_user.id)))
    
    await bot.send_contact(callback.from_user.id, phone_number='+998935527067', first_name='Ake Education 1')
    await bot.send_contact(callback.from_user.id, phone_number='+998935827067', first_name='Ake Education 2', reply_markup=nav.back(lang=db.get_lang(user_id=callback.from_user.id)))

@dp.callback_query_handler(text='back')
async def goback(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, _('Siz bosh menuga qayttingiz', lang=db.get_lang(user_id=callback.from_user.id)), reply_markup=nav.mainMenu(lang=db.get_lang(user_id=callback.from_user.id)))
    await callback.answer()
# Inline knopka bilanga esli chto
# @dp.callback_query_handler(text='kurs')
# async def Courses(callback: types.CallbackQuery):
#     await bot.delete_message(callback.from_user.id, callback.message.message_id)        
#     await bot.send_message(callback.from_user.id, _('Kursingizni tanlang', lang=db.get_lang(user_id=callback.from_user.id)), reply_markup=nav.)



# States
class Form(StatesGroup):
    name = State() 
    course = State()       
    phone = State()  
    gender = State()
    quiz = State()



@dp.callback_query_handler(text='kurs')
async def Courses(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)        

    await Form.name.set()

    await bot.send_message(callback.from_user.id, _('Ismingizni kiriting: ', lang=db.get_lang(user_id=callback.from_user.id)))





@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    """
    Обработка имени
    """
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    course1 = types.KeyboardButton('General English')
    course2 = types.KeyboardButton('IELTS')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(course1, course2)
    await message.reply(_("Kursingizni tanlang", lang=db.get_lang(user_id=message.from_user.id)), reply_markup=keyboard)




@dp.message_handler(state=Form.course)
async def process_course(message: types.Message, state: FSMContext):
    """
    Обработка курса
    """
    async with state.proxy() as data:
        data['course'] = message.text

    await Form.next()
    # markup = types.ReplyKeyboardRemove()
    await message.reply(_("Telefon raqamingizni kiriting", lang=db.get_lang(user_id=message.from_user.id)), reply_markup=nav.phoneBtn(lang=db.get_lang(user_id=message.from_user.id)))






# @dp.callback_query_handler(text='kurs')
# async def Courses(callback: types.CallbackQuery):
#     await bot.delete_message(callback.from_user.id, callback.message.message_id)        

#     await Form.course.set()

#     await bot.send_message(callback.from_user.id, _('Kursingizni tanlang', lang=db.get_lang(user_id=callback.from_user.id)), reply_markup=nav.courseMenu())


# Отмена стейта
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Отмена любого state
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # отмена стейта и оповещение юзера об отмене 
    await state.finish()
    # удаляем кнопку (если есть)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())



# @dp.message_handler(state=Form.course)
# async def process_course(message: types.Message, state: FSMContext):
#     """
#     Обработка курса
#     """
#     async with state.proxy() as data:
#         data['course'] = message.text

#     await Form.next()
#     markup = types.ReplyKeyboardRemove()
#     await message.reply(_("Ismingizni kiriting: ", lang=db.get_lang(user_id=message.from_user.id)), reply_markup=markup)



# @dp.message_handler(state=Form.name)
# async def process_name(message: types.Message, state: FSMContext):
#     """
#     Обработка имени
#     """
#     async with state.proxy() as data:
#         data['name'] = [message.text]

#     await Form.next()
#     await message.reply(_("Telefon raqamingizni kiriting", lang=db.get_lang(user_id=message.from_user.id)), reply_markup=nav.phoneBtn(lang=db.get_lang(user_id=message.from_user.id)))






# phone.isdigit()
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.phone)
async def process_phone_invalid(message: types.Message):
    """
    если номер не число
    """
    return await message.reply(_("Telefon raqam faqatgina sonda bo'lishi kerak!\nRaqamingizni kiriting", lang=db.get_lang(user_id=message.from_user.id)))



@dp.message_handler(content_types=types.ContentType.CONTACT, state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    # обновляем state и data
    await Form.next()
    await state.update_data(phone=message.contact['phone_number'])
    await message.reply(_("Jinsingizni tanlang", lang=db.get_lang(user_id=message.from_user.id)), reply_markup=nav.gender(lang=db.get_lang(user_id=message.from_user.id)))





@dp.message_handler(lambda message: message.text not in ["Мужской", "Женский", "Другой", "Erkak", "Ayol", "Boshqa"], state=Form.gender)
async def process_gender_invalid(message: types.Message):
    """
    Пол должен быть одним из в списке
    """
    return await message.reply("Неправильный пол. Выберите из клавиатуры.")



@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
      data['gender'] = message.text
      data['current_question'] = 0
    await message.reply('начнем тест', reply_markup=get_test_questions())
    await Form.next()


@dp.message_handler(state=Form.quiz)
# @dp.callback_query_handler(factory.filter(), state=Form.quiz)
async def process_quiz(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    global_state = {}
    await bot.send_message('test boshla mal')
    async def create_btn(text, data):
      await types.InlineKeyboardButton(text, callback_data=data)



    async def get_test_list_markup():
      test_list_markup = types.InlineKeyboardMarkup()

      for test in tests:
        test_list_markup.add(create_btn(test['name'], f"create_test_{test['name']}"))

      await test_list_markup


    async def get_test_questions(test_name: str):
      await next(item for item in tests if item["name"] == test_name)['questions']




    async def ask_question(msg: types.Message, data):
      question = get_test_questions(data['test_name'])[data['current_question']]

      alphabet = list(string.ascii_uppercase)

      question_msg = f"*№{data['current_question'] + 1} {question['content']}*\n\n"

      options_markup = types.InlineKeyboardMarkup()

      btn_list = []

      for i, option in enumerate(question['options']):
        question_msg += f"*{alphabet[i]}:* {option['content']}\n"
        btn_list.append(
          create_btn(alphabet[i], f"{i+1}_{alphabet[i]}_{'right' if option['is_right'] else 'wrong'}")
        )

      options_markup.row(*btn_list)

      await msg.answer(question_msg, parse_mode="MarkdownV2", reply_markup=options_markup)


    async def print_result(msg: types.Message, data):
      await msg.answer(f"{msgs['finish']} {data['score']}/{len(get_test_questions(data['test_name']))} 🎉")
          


    async def question_player(msg: types.Message, data):
      cid = msg.from_user.id
      global_state[cid] = data

      await ask_question(msg, global_state[cid])


    async def answer_question(msg: types.Message, option):
      
      cid = msg.from_user.id
      data = global_state[cid]

      is_right = option[2] in 'right'

      # hilight the right answer
      question = get_test_questions(data['test_name'])[
        data['current_question']]

      alphabet = list(string.ascii_uppercase)

      question_msg = f"*№{data['current_question'] + 1} {question['content']}*\n\n"

      for i, question_option in enumerate(question['options']):
        if alphabet[i] == option[1]:
          question_msg += f"*{alphabet[i]}: {question_option['content']}* {'✅' if is_right else '❌'}\n"
        else:
          question_msg += f"*{alphabet[i]}:* {question_option['content']} {'✅' if question_option['is_right'] else ''}\n"

      await msg.edit_text(question_msg, parse_mode="MarkdownV2", reply_markup=None)

      # manage state
      data['current_question'] += 1
      if is_right:
        data['score'] += 1
        # global state_s
        # state_s['score'] = data

      if data['current_question'] == len(get_test_questions(data['test_name'])):
        del global_state[cid]
        await print_result(msg, data)
        

        # await msg.answer(msgs['select'], reply_markup=get_test_list_markup())
        return

      global_state[cid] = data

      # continue test
      await question_player(msg, global_state[cid])













    lang = db.get_lang(user_id=message.from_user.id)
    await bot.send_message(
        message.from_user.id,
        md.text(
            md.text(_("Ismingiz: ", lang), f"{data['name']}"),
            md.text(_('Kursingiz: ', lang), f"{data['course']}"),
            md.text(_('Telefon raqamingiz: ', lang), f"{data['phone']}"),
            md.text(_('Jinsingiz: ', lang), f"{data['gender']}"),
            sep='\n',
        ),
        reply_markup=nav.back(lang),
        parse_mode=ParseMode.MARKDOWN,
    )
    # await bot.send_message(message.from_user.id, 'пройди тест', reply_markup=get_test_list_markup())
    state_z = data['name']
    state_c = data['course']
    state_p = data['phone']
    state_g = data['gender']
    # state_ad = state_s
    await bot.send_message(666358932, text=f"New person: {state_z}\nCourse: {state_c}\nPhone: {state_p}\nGender: {state_g}")
    # конец разговора
  await state.finish()


# TEST
# Actions
@dp.message_handler(commands=['go'])
async def start(msg: types.Message):
  await msg.answer(msgs['welcome'])
  await msg.answer(msgs['start'], reply_markup=get_test_list_markup())

# @dp.message_handler(commands=['help'])
# async def help(msg: types.Message):
#   await msg.answer(msgs['help'], parse_mode=ParseMode.MARKDOWN_V2)

@dp.message_handler(content_types=types.ContentType.ANY)
async def default_reply(msg: types.Message):
  await msg.delete()


async def question_player(msg: types.Message, data):
  cid = msg.from_user.id
  global_state[cid] = data

  await ask_question(msg, global_state[cid])


async def answer_question(msg: types.Message, option):
  cid = msg.from_user.id
  data = global_state[cid]

  is_right = option[2] in 'right'

  # hilight the right answer
  question = get_test_questions(data['test_name'])[
    data['current_question']]

  alphabet = list(string.ascii_uppercase)

  question_msg = f"*№{data['current_question'] + 1} {question['content']}*\n\n"

  for i, question_option in enumerate(question['options']):
    if alphabet[i] == option[1]:
      question_msg += f"*{alphabet[i]}: {question_option['content']}* {'✅' if is_right else '❌'}\n"
    else:
      question_msg += f"*{alphabet[i]}:* {question_option['content']} {'✅' if question_option['is_right'] else ''}\n"

  await msg.edit_text(question_msg, parse_mode="MarkdownV2", reply_markup=None)

  # manage state
  data['current_question'] += 1
  if is_right:
    data['score'] += 1
    # global state_s
    # state_s['score'] = data

  if data['current_question'] == len(get_test_questions(data['test_name'])):
    del global_state[cid]
    await print_result(msg, data)
    await msg.answer('данные запиши', reply_markup=nav.kursmenu())

    # await msg.answer(msgs['select'], reply_markup=get_test_list_markup())
    return

  global_state[cid] = data

  # continue test
  await question_player(msg, global_state[cid])

# Handlers
@dp.callback_query_handler()
async def btn_handler(query: types.CallbackQuery):
  cid = query.message.from_user.id

  if 'create_test' in query.data:
    await query.message.edit_reply_markup()  # clear btn
    await question_player(query.message, get_initial_state(query.data.split('_')[2]))
    await query.answer(msgs['begin'])

  elif 'wrong' in query.data or 'right' in query.data:
    # [№, char, 'wrong' | 'right']
    await answer_question(query.message, query.data.split('_'))
    await query.answer(msgs[query.data.split('_')[2]])

  else:
    await bot.send_message(cid, msgs['error'])























if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)