from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ["TOKEN"]
ADMIN_ID = 7855763034  # METTI QUI IL TUO TELEGRAM ID

async def inoltra_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=update.message.photo[-1].file_id,
            caption="📸 Foto ricevuta"
        )

    if update.message.video:
        await context.bot.send_video(
            chat_id=ADMIN_ID,
            video=update.message.video.file_id,
            caption="🎥 Video ricevuto"
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, inoltra_media))
app.run_polling()
