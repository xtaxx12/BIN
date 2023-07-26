import logging
import os
import requests
import time
import string
import random

from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

ejecucion = "/."

enviar = bool(os.environ.get('enviar', True))
tokenbot = os.environ.get("tokenbot", None)

# Configure logging
logging.basicConfig(level=logging.INFO)

#///token bot///
bot = Bot(token="6041519628:AAGJhLI6gP6MJiPERp2yNnePF9PN79A5kI8", parse_mode=types.ParseMode.HTML)
llamadodelbot = Dispatcher(bot)

###USE YOUR ROTATING PROXY### NEED HQ PROXIES ELSE WON'T WORK UPDATE THIS FIELD

session = requests.session()

def get_country_flag(country):
    base_offset = 127397
    code_points = '-'.join([str(ord(c)) for c in country.upper()])
    return code_points

def format_country_flag(code_points):
    base_offset = 127397
    code_points = code_points.split("-")
    emoji = "".join([chr(int(c) + base_offset) for c in code_points])
    return emoji


@llamadodelbot.message_handler(commands=['start','iniciar'], commands_prefix=ejecucion)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply (f"""
ME HAS INICIADO...
 
""")

@llamadodelbot.message_handler(commands=["bin"], commands_prefix=ejecucion)
async def binio(message: types.Message):
    await message.answer_chat_action("typing")
    BIN = message.text[len("/bin "):][:6]  # Tomar solo los primeros 6 dígitos del BIN
    if not BIN:
        return await message.reply("Por favor, ingresa un BIN válido.")
    req = requests.get(f"https://binlist.io/lookup/{BIN}").json()
    brand = req.get("brand", "Desconocido")
    tipo = req.get("type", "Desconocido")
    bank = req.get("bank", {}).get("name", "Desconocido")
    country = req.get("country", {}).get("name", "Desconocido")
    currency = req.get("country", {}).get("currency", "Desconocido")
    
    country_flag = get_country_flag(country)  # Obtener el código de punto Unicode de la bandera del país
    country_flag_emoji = format_country_flag(country_flag)  # Formatear el emoji de la bandera del país
    
    INFO = (f"""
<b><a href="tg://user?id={message.chat.id}">B I N     I N F O ✿</a></b>

<b>Bin :</b> <code>{BIN}</code>
<b>Estado : Enlinea [✅]</b>
<b>Marca : </b>{brand}
<b>Tipo : </b>{tipo}
<b>Banco: </b>{bank}
<b>País : </b>{country}   {country_flag_emoji}
<b>Moneda : </b>{currency}

𝗖𝗿𝗲𝗮𝘁𝗲 𝗕𝗬 𝗕𝗼𝘁 ✿: @PeePGOD23 <b><a href="https://t.me/refespeep">C L I C K</a></b>

""")
    await message.reply(INFO)

if __name__ == '__main__':
    executor.start_polling(llamadodelbot, skip_updates=True)
