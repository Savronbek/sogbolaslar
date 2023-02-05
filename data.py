msgs = {
  "welcome": "Добро пожаловать! Вас приветствует бот. ",
  "start": "Ну что ж, начнем. Удачи",
  "begin": "Начинаем тест",
  "finish": "Конец! Ваш результат:",
  "select": "Выберите доступный тест",
  "wrong": "✖️",
  "right": "✔️",
  "is_ready": "Готовы?",
  "help": "Бот\-викторина по банкингу, Этот бот проверит ваши знания по банковской сфере\.\n\n Бот был создан при поддержке *«Billy\'s boys & Йожик»*\n\n работников банка 'Алокабанк' В\. В\.\nКостюченко А\. В\.",
  "error": "Эх жаль, случилась ошибка, попробуйте еще раз"
}

test1_questions = [
  {
    "content": "\_\_\_\_'s your name? Thomas\.",
    "options": [
      { "content": "How", "is_right": False },
      { "content": "Who", "is_right": False },
      { "content": "What", "is_right": True },
      { "content": " Where", "is_right": False },
    ]
  },
  {
    "content": "This is Lucy and her brother, Dan\. \_\_\_\_ my friends\.",
    "options": [
      { "content": "We're", "is_right": False },
      { "content": "I'm", "is_right": False },
      { "content": "You're", "is_right": False },
      { "content": "They're", "is_right": True },
    ]
  },
  {
    "content": "\_\_\_\_? I'm from Italy\.",
    "options": [
      { "content": "Where are you from?", "is_right": True },
      { "content": "Where you are from?", "is_right": False },
      { "content": "Where from you are?", "is_right": False },
      { "content": "From where you are?", "is_right": False },
    ]
  },
  {
    "content": "\_\_\_\_? No, he isn't\. ",
    "options": [
      { "content": "Are they teachers?", "is_right": False },
      { "content": "Are you from Italy?", "is_right": False },
      { "content": "Is Mr Banning a teacher?", "is_right": True },
      { "content": "Is this your phone?", "is_right": False },
    ]
  },
  {
    "content": "\_\_\_\_ is the school? It's 50 years old\. ",
    "options": [
      { "content": "How many years", "is_right": False },
      { "content": "How much years", "is_right": False },
      { "content": "What years", "is_right": False },
      { "content": "How old", "is_right": True },
    ]
  },
  {
    "content": "\_\_\_\_ to the cinema\. ",
    "options": [
      { "content": "We not often go", "is_right": False },
      { "content": "We don't go often", "is_right": False },
      { "content": "We don't often go", "is_right": True },
      { "content": "Often we don't go", "is_right": False },
    ]
  },
  {
    "content": "What \_\_\_\_\_ you \_\_\_\_\_ at the weekend?",
    "options": [
      { "content": "does / does ", "is_right": False },
      { "content": "do / does", "is_right": False },
      { "content": "does / do ", "is_right": False },
      { "content": "do / do", "is_right": True },
    ]
  },
  {
    "content": "What \_\_\_\_\_ Dick and Tom like \_\_\_\_\_?",
    "options": [
      { "content": "do / doing ", "is_right": True },
      { "content": "doing / \* ", "is_right": False },
      { "content": "do / do ", "is_right": False },
      { "content": "does / doing", "is_right": False },
    ]
  },
  {
    "content": "Do boys like \_\_\_\_\_ jeans?",
    "options": [
      { "content": "wear ", "is_right": False },
      { "content": "wearing", "is_right": True },
      { "content": "to wear ", "is_right": False },
      { "content": "worn", "is_right": False },
    ]
  },
  {
    "content": "My classmates \_\_\_\_\_ on picnic every month\.",
    "options": [
      { "content": "went", "is_right": False },
      { "content": "goes ", "is_right": False },
      { "content": "going ", "is_right": False },
      { "content": "go", "is_right": True },
    ]
  },
  {
    "content": "Mary \_\_\_\_\_ face every morning\.",
    "options": [
      { "content": "washes his ", "is_right": False },
      { "content": "wash my ", "is_right": False },
      { "content": "washes her ", "is_right": True },
      { "content": "washes their", "is_right": False },
    ]
  },
  {
    "content": "I \_\_\_\_\_ a cigarette, but my teacher \_\_\_\_\_ smoke\.",
    "options": [
      { "content": "don’t / smokes ", "is_right": False },
      { "content": "smoke / doesn’t", "is_right": True },
      { "content": "smokes / smokes ", "is_right": False },
      { "content": "smoke / don’t", "is_right": False },
    ]
  },
  {
    "content": "I \_\_\_\_\_ lots of books every year\.",
    "options": [
      { "content": "will read ", "is_right": False },
      { "content": "am reading ", "is_right": False },
      { "content": "read ", "is_right": True },
      { "content": "am going to read", "is_right": False },
    ]
  },
  {
    "content": "Nurses \_\_\_\_\_ after people in hospital\.",
    "options": [
      { "content": "looks", "is_right": True },
      { "content": "is looking ", "is_right": False },
      { "content": "will look ", "is_right": False },
      { "content": "look", "is_right": False },
    ]
  },
  {
    "content": "Turkish is \_\_\_\_\_\_ in Turkey\.",
    "options": [
      { "content": "speaks ", "is_right": False },
      { "content": "spoke ", "is_right": False },
      { "content": "spoken ", "is_right": True },
      { "content": "be spoken", "is_right": False },
    ]
  },
  {
    "content": "That’s the palace \_\_\_\_\_ the King lives\.",
    "options": [
      { "content": "who ", "is_right": False },
      { "content": "which ", "is_right": False },
      { "content": "where  ", "is_right": True },
      { "content": "when", "is_right": False },
    ]
  },
  {
    "content": "It’s our anniversary today\. We’ve been \_\_\_\_\_ for fifteen years\.",
    "options": [
      { "content": "at last ", "is_right": False },
      { "content": "exactly ", "is_right": False },
      { "content": "together", "is_right": True },
      { "content": "nearly", "is_right": False },
    ]
  },
  {
    "content": "Your clothes smell, and you’ve got a cough\. You \_\_\_\_\_ smoke\. ",
    "options": [
      { "content": "don’t have to ", "is_right": False },
      { "content": "should", "is_right": False },
      { "content": "shouldn’t ", "is_right": True },
      { "content": "have to", "is_right": False },
    ]
  },
  {
    "content": "She \_\_\_\_\_ a shower every morning before school\.",
    "options": [
      { "content": "does", "is_right": False },
      { "content": "has ", "is_right": True },
      { "content": "did ", "is_right": False },
      { "content": "is", "is_right": False },
    ]
  },
  {
    "content": '"What did you talk \_\_\_\_\_ ?"\n"Oh, this and that\."',
    "options": [
      { "content": "to", "is_right": False },
      { "content": "on ", "is_right": False },
      { "content": "with ", "is_right": False },
      { "content": "about", "is_right": True },
    ]
  },
  {
    "content": "Our kitchen \_\_\_\_\_ decorated at the moment\.",
    "options": [
      { "content": "is", "is_right": False },
      { "content": "is being", "is_right": True },
      { "content": "being ", "is_right": False },
      { "content": "was being", "is_right": False },
    ]
  },
  {
    "content": "The doctor says I \_\_\_\_\_ walk again in two weeks’ time\.",
    "options": [
      { "content": "can", "is_right": False },
      { "content": "could", "is_right": False },
      { "content": "will be able to", "is_right": True },
      { "content": "to be able to", "is_right": False },
    ]
  },
  {
    "content": "Did \_\_\_\_\_ phone me while I was out?",
    "options": [
      { "content": "someone ", "is_right": False },
      { "content": "anyone ", "is_right": True },
      { "content": "no one ", "is_right": False },
      { "content": "everyone", "is_right": False },
    ]
  },
  {
    "content": "She refused \_\_\_\_\_ the phone\.",
    "options": [
      { "content": "answer", "is_right": False },
      { "content": "to answer", "is_right": True },
      { "content": "answered", "is_right": False },
      { "content": "answering", "is_right": False },
    ]
  },
  {
    "content": "Since divorce became easier to obtain in Europe, the divorce rate has gone up \_\_\_\_\_\_\.",
    "options": [
      { "content": "dramatic ", "is_right": False },
      { "content": "dramatically ", "is_right": True },
      { "content": "dramatics", "is_right": False },
      { "content": "to be dramatic", "is_right": False },
    ]
  },
  {
    "content": "He \_\_\_\_\_\_ my name, so I reminded him\.",
    "options": [
      { "content": "forgets ", "is_right": False },
      { "content": "has forgotten", "is_right": False },
      { "content": "had forgotten ", "is_right": True },
      { "content": "forgot", "is_right": False },
    ]
  },
  {
    "content": "By 5\.30 this afternoon, Tom \_\_\_\_\_\_ at work for eight hours\.",
    "options": [
      { "content": "had been ", "is_right": False },
      { "content": "would have been", "is_right": False },
      { "content": "will have been ", "is_right": True },
      { "content": "has been", "is_right": False },
    ]
  },
  {
    "content": "It rained\! I didn’t think it \_\_\_\_\_\_\.",
    "options": [
      { "content": "is going to rain ", "is_right": False },
      { "content": "was going to rain", "is_right": True },
      { "content": "was raining ", "is_right": False },
      { "content": "had rained", "is_right": False },
    ]
  },
  {
    "content": "I\_\_\_\_\_\_ hungry at four because I \_\_\_\_\_\_ a big lunch at one\.",
    "options": [
      { "content": "wasn’t / had had ", "is_right": True },
      { "content": "am not / had", "is_right": False },
      { "content": "was / had had ", "is_right": False },
      { "content": "wouldn’t be / had", "is_right": False },
    ]
  },
  {
    "content": "Last night I \_\_\_\_\_\_ you, but the phone was out of order\.",
    "options": [
      { "content": "wasn’t / had had ", "is_right": True },
      { "content": "am not / had", "is_right": False },
      { "content": "was / had had ", "is_right": False },
      { "content": "wouldn’t be / had", "is_right": False },
    ]
  }  

]

# test2_questions = [
#   {
#     "content": "Центральный банк:",
#     "options": [
#       { "content": "собирает налоги;", "is_right": False },
#       { "content": "хранит все наличные деньги;", "is_right": False },
#       { "content": "обеспечивает устойчивость сума;", "is_right": True },
#     ]
#   },
#   {
#     "content": "Ниже приведён перечень функций, выполняемых банками\. Все они, за исключением двух, относятся к сфере деятельности коммерческих банков",
#     "options": [
#       { "content": "открытие и обслуживание пластиковых карт;", "is_right": False },
#       { "content": "покупка и продажа валюты;", "is_right": False },
#       { "content": "выдача кредитов гражданам;", "is_right": False },
#       { "content": "обслуживание счетов фирм;", "is_right": False },
#       { "content": "назначение учётной ставки;", "is_right": True },
#       { "content": "эмиссия денег;", "is_right": True },
#     ]
#   },
#   {
#     "content": "Сергей решил открыть своё дело и обратился в банк за предоставлением кредита на приобретение материалов\. Какие ещё функции выполняют коммерческие банки? Выберите из приведённого списка нужные позиции и запишите цифры, под которыми они указаны: ",
#     "options": [
#       { "content": " осуществление расчётов и платежей", "is_right": True },
#       { "content": " предоставление страховых услуг", "is_right": False },
#       { "content": "приём вкладов", "is_right": True },
#       { "content": "регулирование денежного обращения", "is_right": False },
#       { "content": "денежная эмиссия", "is_right": False },
#       { "content": " поддержка курса национальной валюты", "is_right": False },
#     ]
#   },
#   {
#     "content": "Укажите основные условия выдачи кредита: ",
#     "options": [
#       { "content": "срочность", "is_right": True },
#       { "content": " выгодность", "is_right": False },
#       { "content": "безвозмездность", "is_right": False },
#       { "content": "бессрочность", "is_right": False },
#       { "content": "платность", "is_right": True },
#       { "content": "возвратность", "is_right": True },
#     ]
#   },
#   {
#     "content": "Ссудный процент \– это: ",
#     "options": [
#       { "content": "долг заемщика кредитору;", "is_right": False },
#       { "content": "сумма кредита, которую заемщик обязан вернуть кредитору;", "is_right": False },
#       { "content": "плата за кредит;", "is_right": False },
#       { "content": "прибыль банка;", "is_right": True },
#     ]
#   },
#   {
#     "content": "Главной формой отчетности центрального банка является: ",
#     "options": [
#       { "content": "отчет о прибылях и убытках", "is_right": False },
#       { "content": "платежный баланс", "is_right": False },
#       { "content": "баланс", "is_right": True },
#       { "content": "годовой отчет", "is_right": False },
#     ]
#   },
  # {
  #   "content": "Золотовалютными резервами Великобритании управляет: ",
  #   "options": [
  #     { "content": "и владеет Королевский двор", "is_right": False; },
  #     { "content": "ЕЦБ", "is_right": False; },
  #     { "content": "Банк Англии от имени Казначейства", "is_right": True },
  #     { "content": "Европейский Экономический и Валютный Союз", "is_right": False },
  #   ]
  # },
  # {
  #   "content": "Где расположена штаб-квартира Совета по исламским финансовым услугам(IFSB):",
  #   "options": [
  #     { "content": " Турция", "is_right": False },
  #     { "content": " Бахрейн", "is_right": False },
  #     { "content": " Саудовская Аравия", "is_right": False },
  #     { "content": " Малайзия", "is_right": True },
  #   ]
  # },
  # {
  #   "content": "Банковская система, свойственная административно-командной экономике и полностью зависящая от указаний правительства",
  #   "options": [
  #     { "content": "децентрализованная банковская система", "is_right": False },
  #     { "content": "банковская система с линейно-штабной структурой управления", "is_right": False },
  #     { "content": "централизованная банковская система", "is_right": False },
  #     { "content": "распределительная банковская система", "is_right": True },
  #   ]
  # },
  # {
  #   "content": "Развитие вторичного рынка исламских ценных бумаг и разработка новых финансовых инструментов для исламского финансового рынка является функционалом",
  #   "options": [
  #     { "content": "Council for Islamic Banks and Financial Institutions (CIBAFI)", "is_right": False },
  #     { "content": "The Islamic Finance Service Board»(IFSB)", "is_right": False },
  #     { "content": "Международного центра по управлению ликвидностью", "is_right": True },
  #     { "content": "The International Islamic Financial Market", "is_right": False },
  #   ]
  # }
# ]

tests = [
  {
    "name": "Тест №1",
    "questions": test1_questions
  },
  # {
  #   "name": "Тест №2",
  #   "questions": test2_questions
  # }
]
