import warnings
warnings.filterwarnings("ignore")
import os
from dotenv import load_dotenv

import google.generativeai as genai
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm SageBot AI 🤖\nAsk me anything."
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    user_text = update.message.text

    try:
        response = model.generate_content(
            f"""
            You are SageBot, a friendly AI assistant.

            Rules:
            - Be helpful
            - Be friendly
            - Keep answers under 300 words
            - Explain technical topics simply

            User: {user_text}
            """
        )

        reply = response.text

        for i in range(0, len(reply), 4000):
            await update.message.reply_text(
                reply[i:i+4000]
            )

    except Exception as e:
        await update.message.reply_text(
            f"Error: {e}"
        )


def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN not found in .env")
        return

    if not GEMINI_API_KEY:
        print("❌ GEMINI_API_KEY not found in .env")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat
        )
    )

    print("✅ SageBot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
