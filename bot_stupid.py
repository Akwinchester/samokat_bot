import os.path
import shutil
import telebot
import requests
from settings import *
from my_functions import *
import re



bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')




@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['one_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['start'], reply_markup=markup)


#    'one_button': 'Да, поехали 🚀'
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['one_button'])
def one_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['two_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['one_step'], reply_markup=markup)

#    'two_button':'Мы собрали команду. Что делать дальше?'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['two_button'][:-1:]))
def two_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['three_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['two_step'], reply_markup=markup)


#    'three_button': 'Ага, мы придумали продукт. Что с ним делать?',
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['three_button'][:-1:]))
def three_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['four_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['three_step'], reply_markup=markup)

#    'four_button': 'А что нужно знать перед съёмкой?'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['four_button'][:-1:]))
def three_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['five_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['four_step'], reply_markup=markup)


#    'five_button': 'В каком формате и как отправлять видео?'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['five_button'][:-1:]))
def six_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['six_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['five_step'], reply_markup=markup)

#    'six_button': 'А когда посмотрим другие работы и узнаем победителей?'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['six_button'][:-1:]))
def six_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    bot.send_message(message.chat.id, MESSAGE_TEXT['six_step'], reply_markup=markup)

#    'block_button_1':'Еще раз про сроки'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['block_button_1'][:-1:]))
def block_button_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    bot.send_message(message.chat.id, MESSAGE_TEXT['block_button_1'], reply_markup=markup)

#    'block_button_2':'Еще раз про формат видео'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['block_button_2'][:-1:]))
def block_button_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    bot.send_message(message.chat.id, MESSAGE_TEXT['block_button_2'], reply_markup=markup)

#    'block_button_3':'Готовы загрузить видео'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['block_button_3'][:-1:]))
def block_button_3(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1_1 = types.KeyboardButton(BUTTON_TEXT['block_button_5'])
    markup_1.add(item_1_1)

    bot.send_message(message.chat.id, MESSAGE_TEXT['block_button_3'], reply_markup=markup_1)
    check_existence_and_make_csv(HEADLINES_FOR_TABLE)
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1_1 = types.KeyboardButton(BUTTON_TEXT['block_button_5'])
    markup_1.add(item_1_1)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)

    if message.text == BUTTON_TEXT['block_button_5']:
        bot.send_message(message.chat.id, MESSAGE_TEXT['exit_data_collection'], reply_markup=markup)
    else:
        add_user_data(message.chat.id, second_key='name', value=message.text)
        bot.send_message(message.chat.id, MESSAGE_TEXT['get_phone_number'], reply_markup=markup_1)
        bot.register_next_step_handler(message, get_phone_number)


def get_phone_number(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1_1 = types.KeyboardButton(BUTTON_TEXT['block_button_5'])
    markup_1.add(item_1_1)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    if message.text == BUTTON_TEXT['block_button_5']:
        bot.send_message(message.chat.id, MESSAGE_TEXT['exit_data_collection'], reply_markup=markup)
    else:
        if re.search('[+][0-9]{11,11}', message.text) and len(message.text) == 12:
            add_user_data(message.chat.id, second_key='phone_number', value="'" + message.text)
            bot.send_message(message.chat.id, MESSAGE_TEXT['get_nick_teammate'], reply_markup=markup_1)
            bot.register_next_step_handler(message, get_nick_teammate)
        else:
            bot.send_message(message.chat.id,MESSAGE_TEXT['now_pattern_phone'], reply_markup=markup_1)
            bot.register_next_step_handler(message, get_phone_number)


def get_nick_teammate(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1_1 = types.KeyboardButton(BUTTON_TEXT['block_button_5'])
    markup_1.add(item_1_1)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)

    if message.text == BUTTON_TEXT['block_button_5']:
        bot.send_message(message.chat.id, MESSAGE_TEXT['exit_data_collection'], reply_markup=markup)
    else:
        add_user_data(message.chat.id, second_key='nick_teammate', value=message.text)
        bot.send_message(message.chat.id, MESSAGE_TEXT['get_name_team_product'], reply_markup=markup_1)
        bot.register_next_step_handler(message, get_name_team_product)


def get_name_team_product(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1_1 = types.KeyboardButton(BUTTON_TEXT['block_button_5'])
    markup_1.add(item_1_1)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)

    if message.text == BUTTON_TEXT['block_button_5']:
        bot.send_message(message.chat.id, MESSAGE_TEXT['exit_data_collection'], reply_markup=markup)
    else:
        add_user_data(message.chat.id, second_key='name_team_product', value=message.text)
        bot.send_message(message.chat.id, MESSAGE_TEXT['get_video'], reply_markup=markup_1)
        bot.register_next_step_handler(message, get_video)



def get_video(message):
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1_1 = types.KeyboardButton(BUTTON_TEXT['block_button_5'])
    markup_1.add(item_1_1)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    if message.text == BUTTON_TEXT['block_button_5']:
        bot.send_message(message.chat.id, MESSAGE_TEXT['exit_data_collection'], reply_markup=markup)
    else:
        if message.video or message.document:
            data_video = download_video(message, bot)
            add_user_data(message.chat.id, second_key='id_video', value=data_video[0])
            # add_user_data(message.chat.id, second_key='video_link', value=past_link(data_video[1], f'./{data_video[1]}'))
            add_user_data(message.chat.id, second_key='video_link',
                          value=data_video[1])

            data_for_writer = make_data_for_writer_table(update_user_data()[str(message.chat.id)])
            write_data_table_csv(HEADLINES_FOR_TABLE, data_for_writer)

            upload_to_folder(ID_FOLDER, PATH_LOCAL_FOLDER+data_video[1], data_for_writer)

            bot.send_message(message.chat.id, MESSAGE_TEXT['finish_collection_data'], parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, MESSAGE_TEXT['photo'], reply_markup=markup)
            bot.register_next_step_handler(message, get_video)


#    'block_button_4':'Нужна помощь'
@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['block_button_4'][:-1:]))
def block_button_4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    bot.send_message(message.chat.id, MESSAGE_TEXT['block_button_4'], reply_markup=markup)

@bot.message_handler(content_types=['text'], regexp=r'{}*'.format(BUTTON_TEXT['block_button_5'][:-1:]))
def block_button_4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    bot.send_message(message.chat.id, "Продолжим", reply_markup=markup)
# @bot.message_handler(content_types=['text'])
# def body(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'Жаль, но я не знаю, что сказать по этому поводу :(')

if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)