import os.path
import shutil
import telebot
import requests
from settings import *
from my_functions import *



bot = telebot.TeleBot(BOT_TOKEN)




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
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['two_button'])
def two_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['three_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['two_step'], reply_markup=markup)


#    'three_button': 'Ага, мы придумали продукт. Что с ним делать?',
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['three_button'])
def three_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['four_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['three_step'], reply_markup=markup)

#    'four_button': 'А что нужно знать перед съёмкой?'
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['four_button'])
def three_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['five_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['four_step'], reply_markup=markup)


#    'five_button': 'В каком формате и как отправлять видео?'
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['five_button'])
def six_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(BUTTON_TEXT['six_button'])
    markup.add(button)
    bot.send_message(message.chat.id, MESSAGE_TEXT['five_step'], reply_markup=markup)

#    'six_button': 'А когда посмотрим другие работы и узнаем победителей?'
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['six_button'])
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
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['block_button_1'])
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
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['block_button_2'])
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
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['block_button_3'])
def block_button_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)

    bot.send_message(message.chat.id, MESSAGE_TEXT['block_button_3'], reply_markup=markup)
    check_existence_and_make_csv(HEADLINES_FOR_TABLE)
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    add_user_data(message.chat.id, second_key='name', value=message.text)
    bot.send_message(message.chat.id, MESSAGE_TEXT['get_phone_number'])
    bot.register_next_step_handler(message, get_phone_number)


def get_phone_number(message):
    add_user_data(message.chat.id, second_key='phone_number', value=message.text)
    bot.send_message(message.chat.id, MESSAGE_TEXT['get_nick_teammate'])
    bot.register_next_step_handler(message, get_nick_teammate)


def get_nick_teammate(message):
    add_user_data(message.chat.id, second_key='nick_teammate', value=message.text)
    bot.send_message(message.chat.id, MESSAGE_TEXT['get_name_team_product'])
    bot.register_next_step_handler(message, get_name_team_product)


def get_name_team_product(message):
    add_user_data(message.chat.id, second_key='name_team_product', value=message.text)
    bot.send_message(message.chat.id, MESSAGE_TEXT['get_video'])
    bot.register_next_step_handler(message, get_video)



def get_video(message):
    data_video = download_video(message, bot)
    add_user_data(message.chat.id, second_key='id_video', value=data_video[0])
    add_user_data(message.chat.id, second_key='id_video_extension', value=data_video[1])

    data_for_writer = make_data_for_writer_table(update_user_data()[str(message.chat.id)])
    write_data_table_csv(HEADLINES_FOR_TABLE, data_for_writer)

    upload_to_folder(ID_FOLDER, PATH_LOCAL_FOLDER+data_video[1], data_for_writer)

    bot.send_message(message.chat.id, MESSAGE_TEXT['finish_collection_data'])


#    'block_button_4':'Нужна помощь'
@bot.message_handler(content_types=['text'], regexp=BUTTON_TEXT['block_button_4'])
def block_button_4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton(BUTTON_TEXT['block_button_1'])
    item_2 = types.KeyboardButton(BUTTON_TEXT['block_button_2'])
    item_3 = types.KeyboardButton(BUTTON_TEXT['block_button_3'])
    item_4 = types.KeyboardButton(BUTTON_TEXT['block_button_4'])

    markup.add(item_1, item_2)
    markup.add(item_3, item_4)
    bot.send_message(message.chat.id, MESSAGE_TEXT['block_button_4'], reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def body(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'Жаль, но я не знаю, что сказать по этому поводу :(')

if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)