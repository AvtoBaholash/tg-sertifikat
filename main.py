#!/usr/bin/env python3
"""
Telegram Mini App Bot - Math Keyboard
This bot serves a custom math keyboard interface as a Telegram Web App
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
WEB_APP_URL = os.getenv('WEB_APP_URL', 'https://your-domain.com/index.html')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message with buttons to open the Web App."""
    user = update.effective_user

    # Create BOTH inline button (shows user data) AND keyboard button (sends data to bot)
    inline_keyboard = [
        [InlineKeyboardButton(
            text="🧮 Matematik Klaviaturani Ochish (Ma'lumot bilan)",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    # Send message with inline button
    await update.message.reply_text(
        f"👋 Salom {user.first_name}!\n\n"
        "Matematika Klaviaturasi Mini Ilovasiga xush kelibsiz!\n\n"
        "📱 **Quyidagi tugmani bosing:**\n"
        "• '🧮 Matematik Klaviaturani Ochish' - Foydalanuvchi ma'lumotlari bilan\n\n"
        "Siz telefoningizning oddiy klaviaturasi aralashmasdan maxsus matematik klaviaturani ko'rasiz!",
        parse_mode='Markdown',
        reply_markup=inline_markup
    )

async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle data sent from the Web App."""
    try:
        import json
        from datetime import datetime

        # Get the data sent from the Web App
        data = update.message.web_app_data.data

        # Parse the JSON data
        parsed_data = json.loads(data)

        # Log the raw data for debugging
        logger.info(f"Received Web App data: {data}")

        # Extract information
        latex = parsed_data.get('latex', 'N/A')
        text = parsed_data.get('text', 'N/A')
        user_info = parsed_data.get('user', {})
        timestamp = parsed_data.get('timestamp', 'N/A')
        platform = parsed_data.get('platform', 'unknown')
        version = parsed_data.get('version', 'unknown')

        # Format the timestamp
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            formatted_time = timestamp

        # Get user info from Telegram's update object as fallback
        telegram_user = update.effective_user

        # Build user information string - prefer Web App data, fallback to Telegram data
        user_name = f"{user_info.get('first_name', '')} {user_info.get('last_name', '')}".strip()
        if not user_name:
            user_name = f"{telegram_user.first_name or ''} {telegram_user.last_name or ''}".strip()

        username = user_info.get('username') or telegram_user.username or 'N/A'
        user_id = user_info.get('id') or telegram_user.id or 'N/A'
        language = (user_info.get('language_code') or telegram_user.language_code or 'N/A').upper() if user_info.get('language_code') or telegram_user.language_code else 'N/A'
        is_premium = "✨ Ha" if (user_info.get('is_premium') or telegram_user.is_premium) else "Yo'q"

        # Create a detailed response message
        response_message = (
            "✅ *Matematik Ifoda Qabul Qilindi!*\n\n"
            "📊 *Ifoda Tafsilotlari:*\n"
            f"• LaTeX: `{latex}`\n"
            f"• Oddiy Matn: `{text}`\n\n"
            "👤 *Foydalanuvchi Ma'lumotlari:*\n"
            f"• Ism: {user_name}\n"
            f"• Foydalanuvchi nomi: @{username if username != 'N/A' else 'yoq'}\n"
            f"• Foydalanuvchi ID: `{user_id}`\n"
            f"• Til: {language}\n"
            f"• Premium: {is_premium}\n\n"
            "🕐 *Metadata:*\n"
            f"• Vaqt: {formatted_time}\n"
            f"• Platforma: {platform}\n"
            f"• WebApp Versiyasi: {version}\n\n"
            "🎯 Siz istalgan vaqtda boshqa ifoda yuborishingiz mumkin!"
        )

        # Send a confirmation message with all details
        await update.message.reply_text(
            response_message,
            parse_mode='Markdown'
        )

        # Log the detailed information
        logger.info(
            f"User {update.effective_user.id} ({user_name}) sent expression: {text} "
            f"[LaTeX: {latex}] from platform: {platform}"
        )

    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        await update.message.reply_text(
            "❌ Kechirasiz, ma'lumotlarni tahlil qilishda xatolik yuz berdi.\n"
            "Iltimos, qaytadan urinib ko'ring.",
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error handling web app data: {e}")
        await update.message.reply_text(
            "❌ Kechirasiz, ma'lumotlarni qayta ishlashda kutilmagan xatolik yuz berdi.\n"
            "Iltimos, keyinroq qaytadan urinib ko'ring.",
            parse_mode='Markdown'
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message."""
    await update.message.reply_text(
        "📚 *Matematik Klaviatura Boti - Yordam*\n\n"
        "Ushbu bot maxsus matematik klaviatura interfeysini taqdim etadi.\n\n"
        "*Buyruqlar:*\n"
        "/start - Matematik klaviaturani ochish\n"
        "/help - Ushbu yordam xabarini ko'rsatish\n\n"
        "*Foydalanish bo'yicha ko'rsatma:*\n"
        "1. '🧮 Matematik Klaviaturani Ochish' tugmasini bosing\n"
        "2. Matematik ifodangizni kiritish uchun maxsus klaviaturadan foydalaning\n"
        "3. Mobil klaviaturangiz aralashmaydi\n"
        "4. Tayyor bo'lganda ifodangizni yuboring\n\n"
        "Matematikadan bahramand bo'ling! 🎯",
        parse_mode='Markdown'
    )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")

def main() -> None:
    """Start the bot."""
    # Validate configuration
    if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        logger.error("Please set your BOT_TOKEN in the environment or in the script!")
        print("\n⚠️  ERROR: BOT_TOKEN not configured!")
        print("Please set your bot token:")
        print("  export BOT_TOKEN='your-token-here'")
        print("\nOr create a .env file with:")
        print("  BOT_TOKEN=your-token-here")
        print("  WEB_APP_URL=https://your-domain.com/index.html\n")
        return

    if WEB_APP_URL == 'https://your-domain.com/index.html':
        logger.warning("WEB_APP_URL is not configured! Using default.")
        print("\n⚠️  WARNING: WEB_APP_URL not configured!")
        print("Please set your web app URL:")
        print("  export WEB_APP_URL='https://your-domain.com/index.html'")
        print("\nYou need to host index.html on a public HTTPS server\n")

    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data))

    # Register error handler
    application.add_error_handler(error_handler)

    # Start the Bot
    logger.info("Bot is starting...")
    print("\n✅ Math Keyboard Bot is running!")
    print("Press Ctrl+C to stop\n")

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
