# Quick Start Checklist ✅

Follow these steps in order to get your Mini App running:

## ☑️ Step 1: Create Telegram Bot (5 minutes)

- [ ] Open Telegram
- [ ] Search for `@BotFather`
- [ ] Send `/newbot` command
- [ ] Choose a name for your bot
- [ ] Choose a username (must end with 'bot')
- [ ] **Copy and save the bot token** (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

---

## ☑️ Step 2: Host index.html (5 minutes)

Choose ONE method:

### Option A: Netlify (Fastest)
- [ ] Go to [netlify.com](https://www.netlify.com/)
- [ ] Drag `index.html` file to the deploy box
- [ ] Wait 10 seconds
- [ ] Copy the URL you get (e.g., `https://xyz.netlify.app/index.html`)

### Option B: GitHub Pages
- [ ] Create GitHub account at [github.com](https://github.com)
- [ ] Create new repository
- [ ] Upload `index.html`
- [ ] Enable Pages in Settings
- [ ] Copy URL: `https://username.github.io/repo-name/index.html`

📝 **Your hosted URL:** `_______________________________________`

---

## ☑️ Step 3: Configure Menu Button in BotFather (3 minutes)

- [ ] Open `@BotFather` in Telegram
- [ ] Send `/mybots`
- [ ] Select your bot
- [ ] Tap "Bot Settings"
- [ ] Tap "Menu Button"
- [ ] Tap "Edit Menu Button URL"
- [ ] Paste your hosted URL from Step 2
- [ ] Send a button name (e.g., "Math Keyboard")

---

## ☑️ Step 4: Configure Local Environment (2 minutes)

```bash
# In terminal, navigate to your project folder
cd /Users/samar/Documents/testchi/tg-app

# Copy environment file
cp .env.example .env

# Edit .env file with your values
# (Use any text editor or run: nano .env)
```

Edit `.env` and add:
```
BOT_TOKEN=paste_your_bot_token_here
WEB_APP_URL=paste_your_hosted_url_here
```

**Example .env:**
```
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_APP_URL=https://myapp.netlify.app/index.html
```

---

## ☑️ Step 5: Run the Bot (1 minute)

```bash
# Activate virtual environment
source venv/bin/activate

# Run the bot
python main.py
```

You should see:
```
✅ Math Keyboard Bot is running!
Press Ctrl+C to stop
```

**Keep this terminal window open!**

---

## ☑️ Step 6: Test Your Mini App (2 minutes)

- [ ] Open Telegram on your phone or computer
- [ ] Search for your bot (use the username you created)
- [ ] Click "Start" button
- [ ] Look for the **☰ menu icon** next to the message input field
- [ ] Click the menu icon
- [ ] Your Mini App should open! 🎉
- [ ] Test the math keyboard
- [ ] Click "Send to Bot"
- [ ] Expression should appear in chat

---

## ✅ Success Checklist

If everything works, you should be able to:

- [ ] Open your bot in Telegram
- [ ] See the menu button (☰)
- [ ] Click menu button and Mini App opens
- [ ] See the math keyboard interface
- [ ] Type math expressions using custom keyboard
- [ ] Mobile phone keyboard does NOT appear
- [ ] Send expression back to bot
- [ ] Bot receives and displays the expression

---

## 🚨 Troubleshooting

### Bot token error?
- Check `.env` file has correct token
- Make sure no spaces or quotes around token
- Token should be one continuous string

### Menu button not showing?
- Did you configure it in BotFather? (Step 3)
- Try restarting Telegram app
- Make sure you completed ALL steps in Step 3

### Mini App doesn't open?
- Check URL is HTTPS (not HTTP)
- Open URL in browser - does it work?
- Make sure URL in `.env` matches URL in BotFather

### Mobile keyboard still appears?
- This is normal on desktop browsers
- Test on actual mobile device in Telegram
- The prevention only works in Telegram app

### Bot not receiving data?
- Check terminal for errors
- Make sure bot is running (Step 5)
- Check `WEB_APP_URL` in `.env` is correct

---

## 📱 How Users Will Use Your App

Once everything is set up:

1. User opens your bot
2. User clicks ☰ menu icon
3. Mini App opens with math keyboard
4. User types math expression
5. User clicks "Send to Bot"
6. Bot receives expression in chat

**No mobile keyboard interference! ✨**

---

## 🎯 Next Steps

After your Mini App works:

- [ ] Customize the keyboard buttons in `index.html`
- [ ] Add more math functions (sin, cos, log, etc.)
- [ ] Change colors and styling
- [ ] Add expression history
- [ ] Share with friends!

---

## 📚 Additional Resources

- **Detailed setup**: See [README.md](README.md)
- **Hosting help**: See [HOSTING_GUIDE.md](HOSTING_GUIDE.md)
- **Mini App info**: See [MINI_APP_SETUP.md](MINI_APP_SETUP.md)

---

## 🆘 Need Help?

Common issues:
1. Token problems → Check `.env` file format
2. Menu button missing → Reconfigure in BotFather
3. URL issues → Verify HTTPS and public access
4. Bot errors → Check terminal output

**Remember:** Keep the terminal window running while testing!

---

**Estimated total time:** 15-20 minutes
**Difficulty:** Beginner-friendly ⭐⭐

Good luck! 🚀
