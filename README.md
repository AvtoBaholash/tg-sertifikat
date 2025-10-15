# Telegram Math Keyboard Mini App

A Telegram Mini App that provides a custom mathematical keyboard interface using MathQuill. Users can input mathematical expressions using a special on-screen keyboard without triggering their mobile phone's native keyboard.

## Features

- **Custom Math Keyboard**: Full-featured mathematical keyboard with numbers, operators, and special functions
- **No Mobile Keyboard Interference**: The native mobile keyboard is prevented from appearing
- **MathQuill Integration**: Beautiful mathematical notation rendering
- **Telegram Theme Support**: Automatically adapts to user's Telegram theme
- **LaTeX Output**: Generates LaTeX code for mathematical expressions

## Quick Start

**New to this project?** Start here: **[QUICK_START.md](QUICK_START.md)** - Complete setup in 15 minutes with step-by-step checklist!

### 30 Second Overview

1. Create bot with @BotFather → Get token
2. Host `index.html` on GitHub Pages/Netlify → Get URL
3. Configure Menu Button in BotFather with your URL
4. Create `.env` file with token and URL
5. Run `python main.py`
6. Open bot → Click ☰ menu → Mini App opens!

## Documentation

This project includes several guides for different needs:

### 📘 [QUICK_START.md](QUICK_START.md)
**Best for beginners** - Step-by-step checklist with all commands and troubleshooting. Start here if you've never created a Telegram bot before.

### 🌐 [HOSTING_GUIDE.md](HOSTING_GUIDE.md)
**Need to host your HTML file?** - Detailed instructions for GitHub Pages, Netlify, Vercel, and Cloudflare Pages. Explains HTTPS requirements and testing.

### 📱 [MINI_APP_SETUP.md](MINI_APP_SETUP.md)
**Understanding Mini Apps** - Explains what Telegram Mini Apps are, how they work, and best practices. Includes visual guides for the menu button location.

### 📄 This README
**Technical overview** - Full project documentation, troubleshooting, and detailed setup instructions.

## Prerequisites

- Python 3.7+
- A Telegram Bot Token (get it from [@BotFather](https://t.me/BotFather))
- A public HTTPS server to host `index.html` (see [HOSTING_GUIDE.md](HOSTING_GUIDE.md))

## Setup Instructions

### 1. Create Your Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Save the bot token you receive

### 2. Host Your Web App

You need to host the `index.html` file on a public HTTPS server.

**Quick options:**
- **Netlify**: Go to [netlify.com](https://www.netlify.com/), drag & drop `index.html`, get URL
- **GitHub Pages**: Upload to repo, enable Pages in Settings

👉 **Detailed instructions:** [HOSTING_GUIDE.md](HOSTING_GUIDE.md)

### 3. Configure Mini App in BotFather ⭐

**This is the key step to enable the menu button:**

1. Open [@BotFather](https://t.me/BotFather) in Telegram
2. Send `/mybots`
3. Select your bot
4. Bot Settings → Menu Button → Edit Menu Button URL
5. Send the URL where you hosted `index.html`
6. Send a name for your button (e.g., "Math Keyboard")

### 4. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your values:
# BOT_TOKEN=your_bot_token_from_botfather
# WEB_APP_URL=https://your-hosted-url.com/index.html
```

### 5. Install Dependencies

```bash
# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows

# Install dependencies (already done if using existing venv)
pip install -r requirements.txt
```

### 6. Run the Bot

```bash
python main.py
```

You should see:
```
✅ Math Keyboard Bot is running!
```

### 7. Test Your Mini App

1. Open your bot in Telegram
2. Send `/start` command
3. **Look for the menu icon (☰)** next to the message input field
4. Click it → Your Mini App opens!
5. Use the custom keyboard to input expressions
6. Click "📤 Send to Bot" to submit

## How It Works

```
User → Opens bot → Clicks ☰ menu → Mini App loads → Custom keyboard (no native mobile keyboard!)
```

1. **Bot Backend**: Python bot using `python-telegram-bot` library
2. **Web App**: HTML page with MathQuill and Telegram Web App SDK
3. **Communication**: Telegram Web App API sends data back to the bot
4. **Mobile Keyboard Prevention**: CSS and JavaScript prevent native keyboard from appearing

## Math Keyboard Features

- **Numbers**: 0-9
- **Basic Operators**: +, −, ×, ÷, =, <, >
- **Variables**: x, y, z, a, b, c, e
- **Special Functions**:
  - `x^n`: Power/Exponent
  - `a/b`: Fraction
  - `√`: Square root
  - `π`: Pi constant
- **Backspace**: Delete last character

## Project Structure

```
tg-app/
├── venv/                    # Virtual environment (dependencies installed)
├── index.html               # Web App frontend (custom keyboard)
├── main.py                  # Bot backend (Python)
├── requirements.txt         # Python dependencies
├── .env.example             # Configuration template
├── .env                     # Your configuration (create this)
├── .gitignore               # Git ignore rules
├── README.md                # This file (overview)
├── QUICK_START.md           # Step-by-step setup checklist
├── HOSTING_GUIDE.md         # How to host index.html
└── MINI_APP_SETUP.md        # Mini App explanation & best practices
```

## Troubleshooting

### Bot doesn't start
- Check that `BOT_TOKEN` is correctly set in `.env`
- Verify the token with [@BotFather](https://t.me/BotFather)
- Make sure no extra spaces or quotes in `.env`

### Menu button (☰) doesn't appear
- Did you configure it in BotFather? (Step 3)
- Try restarting Telegram app
- Make sure URL is HTTPS (not HTTP)

### Web App doesn't open
- Ensure `index.html` is hosted on a public HTTPS URL
- Open the URL in your browser - does it load?
- Verify `WEB_APP_URL` in `.env` matches the hosted URL exactly

### Mobile keyboard still appears
- This is normal on desktop browsers
- Test on actual mobile device in Telegram app
- The prevention only works in Telegram Mobile App

### Bot doesn't receive data
- Check that bot is running (terminal shows "Bot is running")
- Check browser console for errors (F12)
- Verify Telegram Web App SDK loaded correctly

👉 **More help:** See [QUICK_START.md](QUICK_START.md) troubleshooting section

## Technologies Used

- **Backend**: Python 3, python-telegram-bot 20.7
- **Frontend**: HTML5, JavaScript, MathQuill, jQuery
- **API**: Telegram Bot API, Telegram Web Apps API

## Next Steps

- Customize the keyboard layout in `index.html`
- Add more mathematical functions (sin, cos, log, etc.)
- Store expressions in a database
- Add expression history
- Implement sharing functionality
- Add multi-language support

## Resources

- [Telegram Mini Apps Documentation](https://core.telegram.org/bots/webapps)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [MathQuill Documentation](http://docs.mathquill.com/)
- [python-telegram-bot Library](https://python-telegram-bot.org/)

## License

This project is open source and available for educational purposes.

---

**Questions?** Check the documentation files above or review the troubleshooting sections.

**Ready to start?** Go to [QUICK_START.md](QUICK_START.md) now! 🚀

#### Jenkins config 
