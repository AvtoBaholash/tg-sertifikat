#!/usr/bin/env python3
"""
Telegram Mini App Bot - Math Keyboard
This bot serves a custom math keyboard interface as a Telegram Web App
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

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
    """Send a welcome message. The Mini App is opened via the menu button."""
    user = update.effective_user

    await update.message.reply_text(
        f"👋 Hello {user.first_name}!\n\n"
        "Welcome to the Math Keyboard Mini App!\n\n"
        "📱 **To open the Math Keyboard:**\n"
        "• Click the menu icon (☰) next to the message input\n"
        "• Or tap the keyboard icon in the attachment menu\n\n"
        "You'll see a custom mathematical keyboard without your phone's native keyboard interfering!",
        parse_mode='Markdown'
    )

async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle data sent from the Web App."""
    try:
        # Get the data sent from the Web App
        data = update.message.web_app_data.data

        # Send a confirmation message
        await update.message.reply_text(
            f"✅ Received your math expression:\n\n"
            f"`{data}`\n\n"
            "Great job! You can send another expression anytime.",
            parse_mode='Markdown'
        )

        logger.info(f"User {update.effective_user.id} sent: {data}")
    except Exception as e:
        logger.error(f"Error handling web app data: {e}")
        await update.message.reply_text(
            "❌ Sorry, there was an error processing your data."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message."""
    await update.message.reply_text(
        "📚 *Math Keyboard Bot - Help*\n\n"
        "This bot provides a custom math keyboard interface.\n\n"
        "*Commands:*\n"
        "/start - Open the math keyboard\n"
        "/help - Show this help message\n\n"
        "*How to use:*\n"
        "1. Click the '🧮 Open Math Keyboard' button\n"
        "2. Use the custom keyboard to input your math expression\n"
        "3. The mobile keyboard won't interfere with your input\n"
        "4. Submit your expression when ready\n\n"
        "Enjoy mathematical typing! 🎯",
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
