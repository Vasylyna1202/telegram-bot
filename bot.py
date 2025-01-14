from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import os

TOKEN = "7746083601:AAFsDixkcid_Mq71JZ0yEMf-7DzYv9lKP1A"  # Ваш токен
USER_IDS_FILE = "user_ids.txt"

# Зчитування ID користувачів
def load_user_ids():
    if os.path.exists(USER_IDS_FILE):
        with open(USER_IDS_FILE, 'r') as file:
            return [int(line.strip()) for line in file.readlines()]
    return []

# Функція для збереження ID користувачів
def save_user_id(user_id):
    if user_id not in load_user_ids():
        with open(USER_IDS_FILE, 'a') as file:
            file.write(f"{user_id}\n")

# Функція для надсилання розсилки
async def send_broadcast_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == 770527682:  # Перевірка ID адміністратора (заміни на свій)
        message = " ".join(context.args)  # Текст для розсилки
        user_ids = load_user_ids()

        for user_id in user_ids:
            try:
                await context.bot.send_message(user_id, message)
                print(f"Повідомлення надіслано користувачу з ID: {user_id}")
            except Exception as e:
                print(f"Не вдалося надіслати повідомлення користувачу з ID {user_id}: {e}")

        await update.message.reply_text(f"Розсилку надіслано: {message}")
    else:
        await update.message.reply_text("Ви не маєте прав для відправки розсилки.")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    save_user_id(user_id)

    keyboard = [
        ["Про нас 🌿", "Меню 🍴"],
        ["СПА 💆🏻‍♀️", "Контакти 📞"],
        ["Проживання 🏡", "Баня з чаном 🧖🏻‍♀️"],  # Кнопка "Баня з чаном" вище
        ["Запустити бота ✨"]  # Кнопка "Запустити бота" в самому низу
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🌊 Ласкаво просимо до Lagodiv Lake Resort Complex! 🏖\n\n"
        "Натискайте на кнопки нижче для навігації або використовуйте команди вручну, якщо потрібно.",
        reply_markup=reply_markup
    )

# Реакція на кнопки
async def handle_menu_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Баня з чаном 🧖🏻‍♀️":
        inline_keyboard = [
            [InlineKeyboardButton("Прайс 💰", callback_data="bath_prices")],
            [InlineKeyboardButton("Бронювання 📅", callback_data="bath_booking")],
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await update.message.reply_text(
            "🧖🏻‍♀️ Баня з чаном 🧖🏻‍♀️\n\n"
            "Пориньте в гарячий чан і насолоджуйтесь теплом серед природи.\n"
            "Просторна баня з великими вікнами та захоплюючими пейзажами.\n"
            "Також ви можете замовити смачні страви з ресторану.\n\n"
            "Оберіть одну з опцій нижче для детальної інформації:",
            reply_markup=reply_markup
        )
    elif text == "СПА 💆🏻‍♀️":
        inline_keyboard = [
            [InlineKeyboardButton("Тарифи та умови 💵", callback_data="spa_rates")],
            [InlineKeyboardButton("Години роботи 🕒", callback_data="spa_hours")],
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await update.message.reply_text(
            "💆🏻‍♀️ СПА-зона Lagodiv 💆🏻‍♀️\n\n"
            "Розслабтеся та відновіть сили у нашій СПА-зоні!\n\n"
            "📞 Як з нами зв'язатися?\n"
            "Телефон: 096 688 2577\n\n"
            "Оберіть одну з опцій нижче для детальної інформації:",
            reply_markup=reply_markup
        )
    elif text == "Контакти 📞":
        inline_keyboard = [
            [InlineKeyboardButton("📱 ТікТок", url="https://www.tiktok.com/@kolybalagodiv")],
            [InlineKeyboardButton("📸 Інстаграм", url="https://www.instagram.com/kolybalagodiv?igsh=MTJuYnRxdzcwa2hkYw==")],
[InlineKeyboardButton("🌐 Наш сайт", url="https://lagodivrest.com.ua")],
            [InlineKeyboardButton("🏞 3D Тур комплексу", url="https://tourmkr.com/F1iQWlZ0pq/43287566p&314.12h&79.14t")],
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await update.message.reply_text(
            "📞 **Контакти:**\n"
            "- Рецепція: 096 337 2888\n"
            "- Басейн/SPA: 096 688 2577\n"
            "- Ресторан: 096 030 7888\n\n"
            "Оберіть одну з опцій нижче для детальної інформації:",
            reply_markup=reply_markup
        )
    elif text == "Про нас 🌿":
        await update.message.reply_text(
            "**Lagodiv Lake Resort Complex — ідеальне місце для вашого відпочинку! 🌿✨**\n\n"
            "🏡 Проживання: затишні номери, окремі будиночки та котедж до 14 осіб.\n"
            "💆‍♀️ СПА: басейн, хамам, джакузі та фінська сауна.\n"
            "🌊 Активний відпочинок: озеро, сапи, каяки, ліс.\n"
            "🍴 Ресторан: українська та європейська кухня."
        )
    elif text == "Меню 🍴":
        inline_keyboard = [
            [InlineKeyboardButton("📋 Відкрити меню", url="https://restoran-koliba.choiceqr.com")]
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await update.message.reply_text(
            "🍽 **Ресторан Lagodiv:**\n"
            "- Години роботи ресторану: 11:00 - 22:00\n"
            "- Сніданки подаються з 09:00 до 11:00\n\n"
            "Натисніть кнопку нижче, щоб переглянути меню:",
            reply_markup=reply_markup
        )
    elif text == "Проживання 🏡":
        inline_keyboard = [
            [InlineKeyboardButton("Час заїзду та виїзду 🕒", callback_data="checkin_checkout")],
            [InlineKeyboardButton("Правила бронювання 📋", callback_data="booking_rules")],
            [InlineKeyboardButton("Правила ануляції ❌", callback_data="cancellation_rules")],
            [InlineKeyboardButton("Бронюй номера тут 🛏", url="https://lagodivrest.com.ua/bronyuvannya/")],
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await update.message.reply_text(
            "🏡 Проживання Lagodiv:\n"
            "Комфортні номери, будиночки з чанами та просторий котедж для сімей або компаній. Відпочинок у гармонії з природою! 🌿✨\n\n"
            "📞 Рецепція: 096 337 2888\n"
            "📞 Бронювання номерів: 096 337 2888",
            reply_markup=reply_markup
        )
    elif text == "Запустити бота ✨":
        await start(update, context)

# Обробка інлайн-кнопок
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Тарифи для СПА
    if query.data == "spa_rates":
        await query.message.reply_text(
            "Тарифи СПА-зони:\n\n"
            "• **Будні (Понеділок - П’ятниця):**\n"
            "  - Дорослі: 3 години — 400 грн, кожна наступна година — 200 грн.\n"
            "  - Діти: 3 години — 300 грн, кожна наступна година — 100 грн.\n\n"
            "• **Вихідні (Субота, Неділя) та святкові дні:**\n"
            "  - Дорослі: 3 години — 500 грн, кожна наступна година — 200 грн.\n"
            "  - Діти: 3 години — 400 грн, кожна наступна година — 100 грн.\n\n"
            "Знижки:\n"
            "• Для військовослужбовців: Вхід зі знижкою 30% за наявності документа, що підтверджує статус.\n"
            "• Діти від 1 до 11 років: Можуть скористатися тарифом “Дитячий”.\n"
        )
    # Прайс для Бані з чаном
    elif query.data == "bath_prices":
        await query.message.reply_text(
            "🏷 Мінімальне замовлення — 2 години 🏷\n\n"
            "- Баня + чан: 1200 грн (1 год.)\n"
            "- Баня: 800 грн (1 год.)\n"
            "- Чан: 800 грн (1 год.)\n"
            "- Банний комплект (рушник, тапочки, простиня): 150 грн\n"
            "- Банна шапка одноразова: 50 грн\n"
            "- Оренда халата: 150 грн\n\n"
            "🍽 Замовлення з ресторану:\n"
"- Мінімальне замовлення з ресторану: 1000 грн\n"
            "- 10% від суми йде на обслуговування."
        )
    elif query.data == "bath_booking":
        await query.message.reply_text(
            "📅 Бронювання бані з чаном 📅\n\n"
            "Для бронювання зв'яжіться з нами за номером 0960307887."
        )
    elif query.data == "spa_hours":
        await query.message.reply_text(
            "🕒 Години роботи СПА 🕒\n\n"
            "СПА-зона працює з 17:00 до 22:00 з понеділка по пʼятницю.\n"
            "У вихідні дні та святкові — з 13:00 до 22:00."
        )
    elif query.data == "checkin_checkout":
        await query.message.reply_text(
            "🕒 Час заїзду та виїзду:\n"
            "- Заїзд: з 14:00\n"
            "- Виїзд: до 12:00"
        )
    elif query.data == "booking_rules":
        await query.message.reply_text(
            "📋 Правила бронювання:\n"
            "1. Бронювання вважається не гарантованим до внесення передоплати.\n"
            "2. Реквізити для оплати надсилаються протягом 3 днів у порядку черги.\n"
            "3. Передоплату необхідно здійснити протягом 3 днів із моменту отримання реквізитів.\n"
            "4. У разі відсутності передоплати бронювання буде скасовано.\n\n"
            "Дякуємо за розуміння!"
        )
    elif query.data == "cancellation_rules":
        await query.message.reply_text(
            "❌ Правила ануляції:\n"
            "• Своєчасне анулювання (до 14 і більше днів до дати заїзду) - оплачені кошти зберігаються на депозитному рахунку до 3 місяців або повертаємо кошти (рішення про повернення коштів розглядається протягом 3-х робочих днів).\n"
            "• Несвоєчасне анулювання (менше 14 днів до дати заїзду) - оплачена сума використовується як штраф."
        )

# Основна функція
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_buttons))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(CommandHandler("broadcast", send_broadcast_message))

    app.run_polling()

if __name__ == "__main__":
    main()

