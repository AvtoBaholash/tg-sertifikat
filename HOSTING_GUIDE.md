# How to Host Your index.html File

You need to host `index.html` on a **public HTTPS server**. Here are the easiest free options:

## Option 1: GitHub Pages (Recommended - Free & Easy)

### Step by step:

1. **Create a GitHub account** (if you don't have one)
   - Go to [github.com](https://github.com)
   - Sign up for free

2. **Create a new repository**
   - Click the "+" icon → "New repository"
   - Name it anything (e.g., "math-keyboard-app")
   - Make it **Public**
   - Click "Create repository"

3. **Upload index.html**
   - Click "uploading an existing file"
   - Drag and drop `index.html` from your computer
   - Click "Commit changes"

4. **Enable GitHub Pages**
   - Go to repository Settings
   - Scroll to "Pages" section (in left sidebar)
   - Under "Source", select "main" branch
   - Click "Save"

5. **Get your URL**
   - After a minute, refresh the page
   - You'll see: "Your site is live at `https://username.github.io/repo-name/`"
   - Your Mini App URL is: `https://username.github.io/repo-name/index.html`

**Example:**
- Username: `john`
- Repo: `math-keyboard-app`
- URL: `https://john.github.io/math-keyboard-app/index.html`

---

## Option 2: Netlify (Super Fast)

### Step by step:

1. **Go to [netlify.com](https://www.netlify.com/)**

2. **Drag and drop**
   - Find the big "Deploy" box
   - Drag your `index.html` file and drop it
   - Wait 10 seconds

3. **Get your URL**
   - Netlify will give you: `https://random-name.netlify.app/index.html`
   - Copy this URL

4. **Optional: Custom name**
   - Click "Site settings"
   - Click "Change site name"
   - Choose a custom name: `https://your-name.netlify.app/index.html`

---

## Option 3: Vercel (For Developers)

### If you have Node.js installed:

```bash
# Install Vercel CLI
npm i -g vercel

# Go to your project directory
cd /Users/samar/Documents/testchi/tg-app

# Deploy
vercel

# Follow the prompts (press Enter for defaults)
# You'll get a URL like: https://tg-app.vercel.app/index.html
```

---

## Option 4: Cloudflare Pages

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com/)
2. Sign up/login
3. Create a new project
4. Upload `index.html`
5. Get URL: `https://your-project.pages.dev/index.html`

---

## Important Notes

✅ **Requirements:**
- Must be **HTTPS** (not HTTP)
- Must be **publicly accessible**
- File must be named `index.html` (or use full path)

❌ **Won't work:**
- Local files: `file:///Users/...`
- HTTP: `http://example.com`
- Private servers requiring login
- Localhost: `http://localhost:8000`

---

## Testing Your Hosted File

Before using in Telegram:

1. **Open the URL in your browser**
   - You should see the math keyboard interface
   - If you see 404 error, check the URL

2. **Test on mobile**
   - Open URL on your phone's browser
   - Make sure it loads properly

3. **Check HTTPS**
   - URL must start with `https://`
   - You should see a lock icon 🔒 in browser

---

## Which Option Should I Choose?

| Service | Best For | Speed | Ease |
|---------|----------|-------|------|
| **GitHub Pages** | Beginners, free, reliable | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Netlify** | Fastest setup | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Vercel** | Developers with CLI | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Cloudflare** | Advanced users | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**My recommendation:** Start with **Netlify** (drag & drop) or **GitHub Pages** (if you want version control).

---

## After Hosting

Once you have your URL (e.g., `https://yoursite.com/index.html`):

1. ✅ Copy the full URL
2. ✅ Add it to `.env` file:
   ```
   WEB_APP_URL=https://yoursite.com/index.html
   ```
3. ✅ Configure it in BotFather (Menu Button URL)
4. ✅ Test your Mini App!

---

## Updating Your Hosted File

If you make changes to `index.html`:

- **GitHub Pages**: Commit new file to repository
- **Netlify**: Drag & drop new file (replaces old one)
- **Vercel**: Run `vercel` again
- **Cloudflare**: Upload new version

Changes usually appear within 1-5 minutes.

---

Need help? Check [MINI_APP_SETUP.md](MINI_APP_SETUP.md) for Mini App configuration.
