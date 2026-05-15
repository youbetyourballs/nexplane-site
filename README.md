# nexplane.ai — Commercial Website

Static marketing site + interest capture for nexplane.ai.

## Structure

```
nexplane.ai/
  public/
    index.html    ← The website
    style.css     ← All styles
    form.js       ← Form submission logic
  src/
    google_apps_script.js  ← Paste into Google Apps Script (see below)
  README.md
```

---

## To publish (30 minutes total)

### Step 1 — Set up the Google Sheet + Apps Script (10 min)

1. Create a new Google Sheet at https://sheets.google.com
2. Name it **"Nexplane Interest Form Responses"**
3. Go to **Extensions → Apps Script**
4. Paste the contents of `src/google_apps_script.js` into the editor, replacing everything
5. Save (Ctrl+S), name the project "Nexplane Form Handler"
6. Click **Deploy → New deployment**
   - Type: **Web app**
   - Execute as: **Me**
   - Who has access: **Anyone**
7. Click **Deploy** → authorize → **copy the Web App URL**
8. In `public/index.html`, find the line near the bottom:
   ```html
   <script src="form.js"></script>
   ```
   Add this line BEFORE it:
   ```html
   <script>window.NEXPLANE_FORM_ENDPOINT = 'PASTE_YOUR_APPS_SCRIPT_URL_HERE';</script>
   ```

### Step 2 — Deploy to Netlify (5 min, free)

1. Go to https://netlify.com → sign up / log in
2. Click **Add new site → Deploy manually**
3. Drag the `public/` folder into the Netlify deploy dropzone
4. Site deploys instantly to a `*.netlify.app` URL — test the form works

### Step 3 — Connect nexplane.ai domain (15 min)

In Netlify:
1. **Site settings → Domain management → Add a custom domain**
2. Enter `nexplane.ai`
3. Netlify shows you the nameservers or CNAME to add

In your domain registrar (wherever nexplane.ai is registered):
1. Update nameservers to Netlify's, OR add a CNAME record:
   - Name: `@` (root) or `www`
   - Value: your `*.netlify.app` URL
2. Wait for DNS propagation (5 min – 2 hours)
3. In Netlify → enable **HTTPS** (free Let's Encrypt cert, one click)

### Step 4 — Verify

- Visit https://nexplane.ai
- Submit the form with your own email
- Check your Google Sheet for the row
- Check your inbox for the notification email

---

## Updating the site

Just drag a new `public/` folder to Netlify to redeploy. No build step needed — it's pure HTML/CSS/JS.

---

## What I need from you to publish

- [ ] Confirm who owns nexplane.ai and who controls DNS (registrar login)
- [ ] A Google account to own the Apps Script / Sheet
- [ ] Your preferred notification email (currently set to john.o.terrill@gmail.com in the script — change if different)
- [ ] Any copy changes to the site before it goes live
