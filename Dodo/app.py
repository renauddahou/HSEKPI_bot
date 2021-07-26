# - *- coding: utf- 8 - *-

#Production by Famaxth
#Telegram - @famaxth


import telebot
import time
from datetime import datetime
import random
import menu
import urllib
import config
from io import BytesIO
from telebot import types


bot = telebot.TeleBot(config.token, parse_mode=None)
print("Start")


joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(str(message.chat.id))
        bot.send_message(message.chat.id, "La chaîne de pizzas numéro un en Russie.\n\nVous pouvez commander une pizza sur dodopizza.ru DoDo Pizza est une chaîne internationale de pizzerias née à Syktyvkar et déjà présente dans treize pays du monde. En général, les gens viennent chez Dodo Pizza juste pour manger. Mais pour nous, Dodo n'est pas seulement une pizza, mais une grande entreprise, qui nous inspire, nous fait nous lever chaque matin et continuer à travailler avec intérêt.\n\nNous sommes en train de créer une entreprise innovante en Russie, fondée sur le principe de l'ouverture totale. Nous n'avons pas peur d'admettre nos erreurs et de partager nos réussites avec vous. Mais notre objectif principal est de vous livrer la pizza la plus savoureuse le plus rapidement possible.", reply_markup=menu.start)
    else:
        bot.send_message(message.chat.id, "La chaîne de pizzas numéro un en Russie.\n\nVous pouvez commander une pizza sur le site web dodopizza.ru\n\nDodo Pizza est une chaîne internationale de pizzerias née à Syktyvkar et déjà présente dans treize pays du monde. En général, les gens viennent chez Dodo Pizza juste pour manger. Mais pour nous, Dodo n'est pas qu'une simple pizza, c'est une grande entreprise, qui nous inspire et nous pousse à nous réveiller chaque matin et à poursuivre notre travail avec intérêt.\n\nNous construisons depuis la Russie une entreprise innovante basée sur le principe de la divulgation complète. Nous n'avons pas peur d'admettre nos erreurs et de partager nos succès avec vous. Mais notre objectif principal est de vous livrer la pizza la plus savoureuse le plus rapidement possible.", reply_markup=menu.start)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'Pizza':
            url = 'https://telegra.ph/dodo-2077-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Dodo 2077</a>\n\nIngrédients: pizza de 30 cm, sauce barbecue cybercola, bacon, boulettes de bœuf, pepperoni épicé, tomates cerises, mozzarella, champignons, poivrons, oignon rouge, ail, sauce tomate\n\nPrix : 745 roubles.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza1)
        elif call.data == 'Avantage1':
            url = 'https://telegra.ph/dodo-fresh-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Pepperoni frais</a>\n\nIngrédients : 30 cm, pâte traditionnelle, 610 g, pepperoni épicé, portion accrue de mozzarella, tomates, coque de tomates\n\nPrix : 435 roubles.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza2)
        elif call.data == 'Retour1':
            url = 'https://telegra.ph/dodo-2077-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Dodo 2077</a>\n\nIngrédients : pizza de 30 cm, sauce barbecue cybercola, bacon, boulettes de bœuf, pepperoni épicé, tomates cerises, mozzarella, champignons, poivrons, oignon rouge, ail, sauce tomate\n\nPrix : 745 roubles.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza1)
        elif call.data == 'Avantage2':
            url = 'https://telegra.ph/dodo-peperoni-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Pepperoni</a>\n\nIngrédients: 30 cm, pâte traditionnelle, 570 g, pepperoni épicé, portion élargie de mozzarella, sauce tomate\n\nPrix : 625 roubles.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza3)
        elif call.data == 'Retour2':
            url = 'https://telegra.ph/dodo-fresh-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Pepperoni frais</a>\n\nIngrédients : 30cm, pâte traditionnelle, 610g, pepperoni épicé, très grande portion de mozzarella, tomates, sauce tomate\n\nPrix : 435 roubles.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza2)
        elif call.data == 'Combo':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Désolé, ce produit est en rupture de stock")
        elif call.data == 'Snacks':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Désolé, ce produit est en rupture de stock")
        elif call.data == 'Desserts':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Désolé, ce produit est en rupture de stock")
        elif call.data == 'Boissons':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Désolé, ce produit est en rupture de stock")
        else:
            bot.send_message(call.message.chat.id, "Ça n'a aucun sens!")



@bot.message_handler(content_types=["text"])
def send(message):
    if message.text == 'Nourriture et boisson':
        bot.send_message(message.chat.id, "Sélectionnez une catégorie:", reply_markup=menu.eda_napitki)
    elif message.text == '💌 A propos de nous':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Lire la suite", url="https://dodopizza.ru/moscow/about")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "💌 A propos de nous\n\nMais pour nous, Dodo, ce n'est pas que de la pizza. C'est aussi de la pizza, mais c'est avant tout une grande cause qui nous inspire, qui nous fait nous lever chaque matin et...", reply_markup=keyboard)
    elif message.text == 'Notre site web':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Aller sur le site", url="https://dodopizza.ru")
        keyboard.add(url_button)
        photo = open('huthgutgh.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=keyboard)
    elif message.text == 'Facebook':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Cliquez sur le lien', url='https://vk.com/dodo')
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "❤️Nous sommes apparus sur VKontakte", reply_markup=keyboard)
    elif message.text == '🏛 Actualités':
        photo = open('novosti_dodo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption="15 premiers prix 🤩\n\nKnight City a ouvert ses portes au public aujourd'hui, et nous lançons un cyber-concours ! Tirage au sort de produits dérivés de Cyberpunk 2077 : 10 t-shirts, 4 blousons et une console Xbox Series X fournie avec le jeu.\n\nCe qu'il faut faire:\n1. Commandez une pizza Dodo 2077.\n2. Retrouvez-le sur notre compte Instagram (https://www.instagram.com/dodopizza/) Insta-masque Dodo 2077. Dirigez-le vers la boîte à pizza et prenez une photo/vidéo du cyberhologramme.\n3. Mettez-le dans votre storie.\n4. Tic-tac @dodopizza.\n\nLes résultats seront résumés en direct le 26 décembre à l'aide d'un randomiseur. Un compte Instagram ouvert est une condition préalable. Bonne chance à tous !\n\nRègles détaillées de la campagne — https://vk.cc/bVOsIv")
    else:
        bot.send_message(message.chat.id, "Ça n'a aucun sens!")



#Start Bot
if __name__ == '__main__':
    bot.polling(none_stop=True)
