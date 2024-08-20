import os
from telegram import ReplyKeyboardMarkup, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import requests

bot_token = ''

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

aaa = 0
bbb = 1
ccc = 2
TEXT = ''


# все персонажи для который нужно сделать кнопки
def pers(update, context):
    keyboard = [
        ["Аято", "Яэ Мико", "Шэнь Хэ", 'Беннет', 'Барбара'],
        ["Итто", "Кокоми", "Сёгун Райдэн", 'Лиза', 'Кэйа', 'Бэй Доу'],
        ["Элой", "Ёимия", "Аяка", 'Рэйзор', 'Ноэлль', 'Нин Гуан'],
        ["Кадзуха", "Эола", "Ху Тао", 'Сян Лин', 'Син Цю', 'Сахароза'],
        ["Сяо", "Гань Юй", "Альбедо", 'Эмбер', 'Чун Юнь', 'Фишль'],
        ["Чжун Ли", "Тарталья", "Кли", 'Розария', 'Синь Янь', 'Диона'],
        ["Венти", "Ци Ци", "Мона", 'Сара', 'Саю', 'Янь Фэй'],
        ["Кэ Цин", "Дилюк", "Джинн", 'Юнь Цзинь', 'Горо', 'Тома']
    ]
    update.message.reply_text('Привет. Я помогу тебе со сборками для геншина. Выбирай персонажа',
                              reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return aaa


def photo(update, context):
    pers_name = update.message.text
    a = os.listdir(f'heroes/{pers_name}')
    for i in a:
        sending_image = open(f"heroes/{pers_name}/{i}", 'rb')
        context.bot.send_document(update.effective_chat.id, sending_image)
    return aaa



def alarm(context):
    job = context.job
    context.bot.send_message(job.context, TEXT)


#def gift(update, context):
#    context.bot.send(requests.get('https://api.waifu.pics/sfw/waifu').json()['url'])


#не важно зачем просто оно нужно правдо хз для чего это,но пусть будет

pers_handler = CommandHandler('start', pers)
photo_handler = MessageHandler(Filters.text, photo)


conv_handler = ConversationHandler(
    entry_points=[pers_handler],
    states={
        aaa: [photo_handler],
    }, fallbacks=[])
# ну тут просто последовательность действий

dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()
