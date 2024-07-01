import telebot
from telebot import types
TOKEN = '6642468718:AAFLbN7L6_gMd_iDufD9E6U9L6pvb7U4H38'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()    
    markup.add(types.InlineKeyboardButton('Наши продукты', callback_data='game_products'))
    bot.send_message(message.chat.id, 'Выберете варианты', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'game_products':
        show_game_products(call.message)
    elif call.data == 'back_to_menu':
        send_welcome(call.message)
def show_game_products(message):
    markup = types.InlineKeyboardMarkup()    
    markup.add(types.InlineKeyboardButton('Baldi',url = 'https://store.steampowered.com/app/1712830/Baldis_Basics_Classic_Remastered/'))
    markup.add(types.InlineKeyboardButton('Bodycam', url = 'https://store.steampowered.com/app/2406770/Bodycam/'))
    markup.add(types.InlineKeyboardButton('Content Warning', url = 'https://store.steampowered.com/app/2881650/Content_Warning/'))
    markup.add(types.InlineKeyboardButton('Назад',callback_data='back_to_menu'))
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Вот все наши продукты',reply_markup=markup)

def get_back_to_menu(message):
    markup = types.InlineKeyboardMarkup()    
    markup.add(types.InlineKeyboardButton('Наши продукты', callback_data='game_products'))
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Выберете варианты',reply_markup=markup)
if __name__ == '__main__':
    bot.polling(none_stop=True)