from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Меню/Меню", callback_data='menu')],
        [InlineKeyboardButton("Години роботи ресторану", callback_data='restaurant_hours')],
        [InlineKeyboardButton("Години роботи SPA", callback_data='spa_hours')],
        [InlineKeyboardButton("Контакти", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌊 Ласкаво просимо до Lagodiv Lake Resort Complex! 🏖️\n\n"
        "Місце, де природа, комфорт та відпочинок об'єднуються в гармонії! 💫\n\n"
        "Ось що я можу для вас зробити:\n"
        "- /info - Дізнатися про нас.\n"
        "- /menu - Меню ресторану та години роботи.\n"
        "- /spa - Інформація про SPA та басейн.\n"
        "- /contact - Контакти нашого комплексу.\n\n"
        "Виберіть потрібну команду!",
        reply_markup=reply_markup
    )

# Інформація про комплекс
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 Ми пропонуємо комфортний відпочинок у мальовничому куточку.\n"
        "Наш комплекс включає:\n"
        "- Затишні номери\n"
        "- Ресторан зі смачними стравами\n"
        "- SPA-зона: басейн, джакузі, хамам, сауна\n"
        "- Простори для відпочинку з видом на озеро\n\n"
        "Детальніше на нашому сайті: https://lagodivrest.com.ua"
    )

# Меню ресторану та години роботи
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍽️ Ресторан Lagodiv:\n"
        "- Години роботи ресторану: 11:00 - 22:00\n"
        "- Сніданки подаються з 09:00 до 11:00\n\n"
        "📋 [Меню ресторану](https://restoran-koliba.choiceqr.com)\n\n"
        "Запрошуємо насолодитися вишуканими стравами!"
    )

# Інформація про SPA та басейн
async def spa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💆‍♀️ SPA та басейн:\n"
        "Розслабтеся та відновіть сили у нашій SPA-зоні:\n"
        "- Пн-Пт: 17:00 - 22:00\n"
        "- Сб-Нд: 13:00 - 22:00\n"
        "📞 Телефон для бронювання: 096 688 2577\n"
        "Чекаємо на вас!"
    )

# Контакти комплексу
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Контакти:\n"
        "- Рецепція: 096 337 2888\n"
        "- Басейн/SPA: 096 688 2577\n"
        "- Ресторан: 096 030 7888\n"
        "- Бронювання номерів: 096 337 2888\n\n"
        "🌍 Наш сайт: https://lagodivrest.com.ua\n"
        "Завітайте до нас!"
    )

# Налаштування бота
def main():
    app = ApplicationBuilder().token("7746083601:AAFsDixkcid_Mq71JZ0yEMf-7DzYv9lKP1A").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("spa", spa))
    app.add_handler(CommandHandler("contact", contact))

    app.run_polling()

if __name__ == "main":
    main()
