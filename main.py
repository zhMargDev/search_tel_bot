import telebot
import CONFIG

import data
import search_engine.google_parser as google_parser

from telebot import types

bot = telebot.TeleBot(CONFIG.TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.InlineKeyboardMarkup(row_width=1) # Add buttons type

    google_btn = types.InlineKeyboardButton('Поиск через Google.', callback_data='google') # First button
    AI_button = types.InlineKeyboardButton('Поиск через ИИ.', callback_data='ai') # Second button

    markup.add(google_btn, AI_button) # Add to markp
    
    # Send message and add buttons to message
    bot.send_message(message.chat.id, 'Привет. Я бот созданный для поиска информации. Выберите способ поиска.', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(content_types=['text'])
def echo_handler(message):
    if data.search_type == 'google':
        bot.send_message(message.chat.id, 'По вашему запросу было найдено:')
        returned_info = google_parser.search_by_text(message.text)
        for w_sites in returned_info:
            bot.send_message(message.chat.id, w_sites, parse_mode='html')
    elif message.text == 'Поиск через Google.':
        bot.send_message(message.chat.id, 'Поиск через Google.')
        bot.send_message(message.chat.id, 'Напишите ваш текст для поиска.')
        data.search_type = 'google'
    elif message.text == 'Поиск через ИИ.':
        bot.send_message(message.chat.id, 'Поиск через ИИ.')
        bot.send_message(message.chat.id, 'Напишите ваш текст для поиска.')
        data.search_type = 'ai'
    else:
        markup = types.InlineKeyboardMarkup(row_width=1) # Add buttons type

        google_btn = types.InlineKeyboardButton('Поиск через Google.', callback_data='google') # First button
        AI_button = types.InlineKeyboardButton('Поиск через ИИ.', callback_data='ai') # Second button
    
        markup.add(google_btn, AI_button) # Add to markp
    
        # Send message and add buttons to message
        bot.send_message(message.chat.id, 'Сначал выберите способ поиска.', parse_mode='html', reply_markup=markup)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'google':
                bot.send_message(call.message.chat.id, 'Поиск по Google активирован. **Введите текст для поиска:**', parse_mode='html')
                data.search_type = 'google'
            elif call.data == 'ai':
                bot.send_message(call.message.chat.id, 'Поиск по ИИ активирован. **Введите текст для поиска:**', parse_mode='html')
                data.search_type = 'ai'
    except Exception as e:
            print(repr(e))


bot.polling(none_stop=True)