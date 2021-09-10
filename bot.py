import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(filename ="bot.log", level = logging.INFO)

import settings

PROXY = {"proxy_url": settings.PROXY_URL,
"urllib3_proxy_kwargs":{"username": settings.PROXY_USERNAME, "password": settings.PROXY_PASSWORD}} #

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет пользователь!")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet(update, context):
    message = update.message.text
     
    divided_in_message = message.split()
   
    planet = divided_in_message[1].lower()
    current_date =date.today()
    if planet.lower() == 'mercury':
        current_planet = ephem.Mercury(current_date)
    elif planet == 'venus':
        current_planet = ephem.Venus(current_date)
    elif planet == 'mars':
        current_planet = ephem.Mars(current_date)
    elif planet == 'jupiter':
        current_planet = ephem.Jupiter(current_date)
    elif planet == 'saturn':
        current_planet = ephem.Saturn(current_date)
    elif planet == 'uranus':
        current_planet = ephem.Uranus(current_date)
    elif planet == 'neptune':
        current_planet = ephem.Neptune(current_date)
    elif planet == 'pluto':
        current_planet = ephem.Pluto(current_date)
        update.message.reply_text('Плутон не планета, но так уж и быть держи созвездие')
   
    const = ephem.constellation(current_planet)
    print(const)
    update.message.reply_text(f'Планета {divided_in_message[1]} сейчас находится в созвездии {const}')


def main():
    mybot = Updater(settings.API_KEY, use_context = True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    logging.info("Bot start")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

