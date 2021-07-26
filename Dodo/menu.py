import config
import telebot
from telebot import types


start = telebot.types.ReplyKeyboardMarkup(True, False)
start.row("Nourriture et boisson")
start.row('Notre site web', 'Facebook')
start.row('💌 A propos de nous', '🏛 Actualités')


eda_napitki = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="🍕Pizza", callback_data="Pizza")
but_2 = types.InlineKeyboardButton(text="🍱 Combo", callback_data="Combo")
but_3 = types.InlineKeyboardButton(text="🥨Snacks", callback_data="Snacks")
but_4 = types.InlineKeyboardButton(text="🍦Desserts", callback_data="Desserts")
but_5 = types.InlineKeyboardButton(text="🍾Boissons", callback_data="Boissons")
eda_napitki.add(but_1)
eda_napitki.add(but_2)
eda_napitki.add(but_3)
eda_napitki.add(but_4)
eda_napitki.add(but_5)


pizza1 = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Passer une commande", url="https://t.me/Renaud17")
but_2 = types.InlineKeyboardButton(text="▶️", callback_data="Avantage1")
pizza1.add(but_2)
pizza1.add(but_1)


pizza2 = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="◀️", callback_data="Retour1")
but_3 = types.InlineKeyboardButton(text="Passer une commande", url="https://t.me/Renaud17")
but_2 = types.InlineKeyboardButton(text="▶️", callback_data="Avantage2")
pizza2.row(but_1, but_2)
pizza2.row(but_3)


pizza3 = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="◀️", callback_data="Retour2")
but_2 = types.InlineKeyboardButton(text="Passer une commande", url="https://t.me/Renaud17")
pizza3.add(but_1)
pizza3.add(but_2)
