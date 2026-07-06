from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

CHANNEL = "@prompt_balochi"

PROMPTS = {
    "1": "اینجا متن پرامپت شماره ۱ را قرار بده",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    args = context.args
    if not args:
        await update.message.reply_text("سلام 👋")
        return

    prompt_id = args[0]

    member = await context.bot.get_chat_member(
        CHANNEL,
        user.id
    )

    if member.status in ["member", "administrator", "creator"]:
        await update.message.reply_text(
            PROMPTS.get(prompt_id, "پرامپت پیدا نشد.")
        )
    else:
        keyboard = [
            [InlineKeyboardButton(
                "📢 عضویت در کانال",
                url="https://t.me/prompt_balochi"
            )],
            [InlineKeyboardButton(
                "✅ بررسی عضویت",
                callback_data=f"check_{prompt_id}"
            )]
        ]

        await update.message.reply_text(
            "برای دریافت پرامپت ابتدا عضو کانال شوید.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


app = Application.builder().token("TOKEN").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
