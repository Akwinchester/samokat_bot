from settings import *
from telethon import events, TelegramClient, Button


bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='привет'))
async def start(event):
    # my_button = Button.text('кнопка')
    await event.respond(event.text)


def main():

    bot.run_until_disconnected()


if __name__ == '__main__':
    main()