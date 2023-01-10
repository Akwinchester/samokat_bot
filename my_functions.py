import json

from telebot import types
from settings import *
import os
import json
import csv
import datetime



def add_user_data(chat_id, second_key, value):
    chat_id = str(chat_id)
    user_data = update_user_data()
    if not(chat_id in user_data):
        user_data[chat_id] = {}
    user_data[chat_id][second_key] = value
    update_json_file(user_data)


def  update_json_file(data):
    if os.path.exists('./users.json'):
        with open('./users.json', 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


def update_user_data():
    if os.path.exists('./users.json'):
        with open('./users.json', 'r', encoding="utf-8") as f:
            user_data = json.load(f)
    return user_data


def past_link(text, link):
    rusult = f'=ГИПЕРССЫЛКА("{link}"; "{text}")'
    return rusult

def write_data_table_csv(headlines, data):
    check_existence_and_make_csv(headlines)
    data_1 = data[:]
    data_1[-1] =past_link(data[-1], f'./{data[-1]}')
    with open('./files/data.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')
        writer.writerow(data_1)


def check_existence_and_make_csv(headlines):
    if not os.path.exists('./files/data.csv'):
        with open('files/data.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\n')
            writer.writerow(headlines)

def make_data_for_writer_table(dict_data):
    data = []
    # dict_data['video_link'] = past_link(dict_data['video_link'], f'./{dict_data["video_link"]}')
    for i in dict_data:
        data.append(dict_data[i])
    return data


def download_video(message, bot):
    user_data = update_user_data()[str(message.chat.id)]
    file_id_time = str((datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()).split('.')[0]
    try:
        if message.video:
            file_info = bot.get_file(message.video.file_id)
            extension_file = file_info.file_path.split('/')[-1]
            extension_file = str(extension_file).split('.')[-1]
        elif message.document:
            file_info = file_info = bot.get_file(message.document.file_id)
            extension_file = file_info.file_path.split('/')[-1]
            extension_file = str(extension_file).split('.')[-1]
        downloaded_file = bot.download_file(file_info.file_path)

        with open(f'./files/{file_id_time}.{extension_file}', 'wb') as f:
            f.write(downloaded_file)

        bot.send_message(ADMIN_ID,
                            f'''пользователь: {user_data["name"]} отправил видео
Название: {file_id_time}
Телефон: {user_data["phone_number"]}
Видео загружено на сервер''')
        bot.copy_message(ADMIN_ID, message.chat.id, message.id)
        return (file_id_time, file_id_time + '.' + extension_file)
    except:
        bot.send_message(ADMIN_ID,
                            f'''пользователь: {user_data["name"]} отправил видео
Название: {file_id_time}
Телефон: {user_data["phone_number"]}
Необходимо скачать''')
        bot.copy_message(ADMIN_ID, message.chat.id, message.id)
        return (file_id_time, file_id_time+'.'+'mp4')

