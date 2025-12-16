# نصب کتابخانه‌ها
!pip install python-telegram-bot --upgrade
!pip install nest_asyncio

# ===========================
import nest_asyncio
nest_asyncio.apply()  # حل مشکل event loop در Colab

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ======= توکن ربات =======
TOKEN = "8315887553:AAFOMUdCE61liLlntj7dwHK7d1NqJDgSQ7E"

# ======= پیام‌ها =======
MSG_WELCOME = "سلام! 👋\nاین ربات راهنمای ثبت‌نام و عضویت در سایت Kevin Trudeau Fan Club را ارائه می‌دهد.\nلطفاً یکی از گزینه‌ها را انتخاب کنید:"

MSG_FREE = (
    "📌 ثبت‌نام رایگان برای دریافت آموزش‌های رایگان:\n\n"
    "1️⃣ وارد سایت رسمی شوید:\nhttps://kevintrudeaufanclub.com/\n\n"
    "2️⃣ به بخش Subscribe / Free Training Form بروید\n"
    "3️⃣ فرم را کامل کنید:\n"
    "- نام (First Name)\n- نام خانوادگی (Last Name)\n- ایمیل\n- تلفن\n- تأیید ایمیل\n- آدرس کامل (ترجیحاً ترکیه)\n"
    "4️⃣ تیک قبول قوانین و دریافت ایمیل/پیام‌ها را بزنید (Consent)\n"
    "5️⃣ دکمه Submit را بزنید.\n"
    "✔️ آموزش‌ها و نکات رایگان برایتان ایمیل می‌شود."
)

MSG_PAID = (
    "💳 عضویت پولی Partner / حمایت مالی:\n\n"
    "1️⃣ در منو یا قسمت Become a Partner / Partner کلیک کنید.\n"
    "2️⃣ سطح عضویت را انتخاب کنید:\n"
    "- Bronze: 25$/ماه\n- Silver: 50$/ماه\n- Gold: 100$/ماه\n- Platinum: 250$/ماه\n- Diamond: 500$/ماه\n- Patron: 1000$/ماه\n"
    "3️⃣ وارد صفحه پرداخت شوید و اطلاعات کارت/پرداخت را وارد کنید.\n"
    "📌 برای ایران: متن توضیحات ایرانیکارت:\n"
    "سلام، از این سایت وارد شوید: https://kevintrudeaufanclub.com/ - قسمت Partner Contribution - سطح برنز (25$) را انتخاب کنید. اطلاعات را از ترکیه وارد کنید. ممنون\n"
    "4️⃣ پس از پرداخت، حسابتان فعال می‌شود."
)

MSG_ONE_TIME = (
    "💰 کمک یک‌باره مالی (One-Time Contribution):\n\n"
    "می‌توانید بدون عضویت پولی یک کمک مالی انجام دهید.\n"
    "برای ایرانیکارت: بجای قسمت Partner Contribution گزینه One-Time Contribution را انتخاب کنید و مبلغ دلخواه را پرداخت کنید."
)

MSG_CHANNELS = (
    "🌐 کانال‌های رسمی Kevin Trudeau Fan Club:\n\n"
    "Persian Channel:\nhttps://t.me/+VS-k0OOjYudiMDEy\n"
    "English Channel:\nhttps://t.me/TheKevinTrudeauFanClubChannel"
)

# ======= دکمه‌ها =======
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("ثبت‌نام رایگان", callback_data="free")],
        [InlineKeyboardButton("عضویت پولی", callback_data="paid")],
        [InlineKeyboardButton("کمک یک‌باره مالی", callback_data="one_time")],
        [InlineKeyboardButton("کانال‌ها", callback_data="channels")],
    ]
    return InlineKeyboardMarkup(keyboard)

def back_to_menu_keyboard():
    keyboard = [[InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="menu")]]
    return InlineKeyboardMarkup(keyboard)

# ======= فرمان /start =======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MSG_WELCOME, reply_markup=main_menu_keyboard())

# ======= پاسخ به دکمه‌ها =======
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "free":
        await query.message.reply_text(MSG_FREE, reply_markup=back_to_menu_keyboard())
    elif query.data == "paid":
        await query.message.reply_text(MSG_PAID, reply_markup=back_to_menu_keyboard())
    elif query.data == "one_time":
        await query.message.reply_text(MSG_ONE_TIME, reply_markup=back_to_menu_keyboard())
    elif query.data == "channels":
        await query.message.reply_text(MSG_CHANNELS, reply_markup=back_to_menu_keyboard())
    elif query.data == "menu":
        await query.message.reply_text(MSG_WELCOME, reply_markup=main_menu_keyboard())

# ======= ساخت اپلیکیشن =======
app = ApplicationBuilder().token(TOKEN).build()

# اضافه کردن فرمان‌ها و دکمه‌ها
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

# ======= اجرای ربات =======
print("ربات فعال است! به تلگرام برو و /start را امتحان کن.")
app.run_polling()
