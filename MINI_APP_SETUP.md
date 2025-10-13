# Quick Mini App Setup Guide

## What is a Telegram Mini App?

A Mini App is a web application that opens directly inside Telegram. Users access it through a menu button (☰) in the bot chat - **no keyboard buttons needed!**

## Visual Guide: Where to Find the Menu Button

When users open your bot:
```
┌─────────────────────────────┐
│  Your Bot Name         [×]  │
├─────────────────────────────┤
│                             │
│  Welcome message...         │
│                             │
├─────────────────────────────┤
│ [☰] [📎] Type a message...  │ ← Click the ☰ menu icon
└─────────────────────────────┘
```

## Setup Steps (Summary)

### 1. Get Bot Token
- Message [@BotFather](https://t.me/BotFather)
- Send: `/newbot`
- Save your token

### 2. Host index.html
Upload `index.html` to any of these (must be HTTPS):
- **GitHub Pages**: `https://username.github.io/repo/index.html`
- **Netlify**: Drag & drop file → get URL
- **Vercel**: `vercel` command → get URL

### 3. Configure Menu Button in BotFather
⭐ **This is the key step:**

```
1. Open @BotFather
2. Send: /mybots
3. Select your bot
4. Bot Settings → Menu Button → Edit Menu Button URL
5. Paste your index.html URL
6. Enter button name (e.g., "Math Keyboard")
```

### 4. Set Environment Variables
```bash
cp .env.example .env
# Edit .env:
BOT_TOKEN=your_token_here
WEB_APP_URL=https://your-hosted-url.com/index.html
```

### 5. Run Bot
```bash
source venv/bin/activate
python main.py
```

## Testing

1. Find your bot in Telegram
2. Start a chat with it
3. Look for **☰ icon** next to message input
4. Click it → Mini App opens!
5. Use the math keyboard
6. Submit → bot receives the expression

## Differences: Mini App vs Button Approach

| Feature | Mini App (☰ Menu) | Button Approach |
|---------|------------------|-----------------|
| Access | Menu icon (☰) | Button in chat |
| Setup | Configure in BotFather | Sent by bot code |
| User Experience | Clean, native feel | Button takes chat space |
| Recommended | ✅ Yes | For specific cases |

## Troubleshooting

**Menu button doesn't appear?**
- Make sure you configured it in BotFather (Step 3)
- Restart your Telegram app
- Check if URL is HTTPS (HTTP won't work)

**Mini App shows blank page?**
- Verify index.html is accessible in browser
- Check browser console for errors
- Ensure WEB_APP_URL matches hosted URL exactly

**Mobile keyboard still appears?**
- Test on actual mobile device (not desktop)
- Clear Telegram cache
- The keyboard is prevented through CSS/JS in index.html

## Additional Features You Can Add

Once working, you can enhance your Mini App:

1. **Save expressions** - Store in database
2. **History** - Show previous calculations
3. **Share** - Let users share expressions
4. **More functions** - Add sin, cos, log, etc.
5. **Themes** - Custom color schemes
6. **Multi-language** - Support different languages

## Mini App Best Practices

✅ **DO:**
- Keep it responsive (works on all screen sizes)
- Use Telegram theme colors (already implemented)
- Test on real mobile devices
- Keep load times fast

❌ **DON'T:**
- Use HTTP (only HTTPS works)
- Make users wait (show loading states)
- Ignore mobile optimization
- Forget error handling

## Resources

- [Telegram Mini Apps Documentation](https://core.telegram.org/bots/webapps)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [MathQuill Documentation](http://docs.mathquill.com/)

---

Need help? Check the main [README.md](README.md) for detailed information.
