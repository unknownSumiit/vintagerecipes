# The Vintage Recipe Box: Old-Fashioned Recipe Website

A fast, static recipe website of vintage and old-fashioned American recipes for US home cooks over 50. Each recipe includes the history behind the dish. It's built mobile-first for **iPhone Safari**, structured to meet **Google AdSense** site requirements, and ready to deploy to **Azure Static Web Apps** from **GitHub**.

## What's included

```
.
├── .github/workflows/azure-static-web-apps.yml   ← deploys to Azure automatically on every push
├── site/                                         ← THE WEBSITE (Azure publishes this folder)
│   ├── index.html                                ← home page with vintage kitchen hero
│   ├── recipes/            14 recipes, each with a history note, + searchable recipe index
│   ├── recipes-by-era.html the story behind every dish, from the 1800s to the 1960s
│   ├── category/           Supper Classics, Potluck Favorites, Grandma's Pies, Old-Fashioned Cakes
│   ├── articles/           4 guides: reading old recipe cards, Depression-era cooking,
│   │                       preserving family recipes, potluck food safety
│   ├── about, contact, privacy-policy, terms-of-use, disclaimer, 404
│   ├── sitemap.xml, robots.txt, ads.txt, site.webmanifest, apple-touch-icon.png
│   └── assets/  css, js, logo, icons, img/recipes/ (put your own food photos here)
├── tools/
│   ├── build.py              ← regenerates every page
│   ├── content_recipes.py    ← recipes, history notes and categories
│   ├── content_articles.py   ← guides
│   └── photos.py             ← photo for each recipe (Unsplash IDs)
└── brand/                    ← logo files (SVG + PNG, light and dark) and the script that draws them
```

**Built for readers over 50 on iPhone:** large text and a Text size button, Cook mode (keeps the screen awake), tap-to-check ingredients, Half / 1× / 2× batch buttons, a Share button that opens the iPhone share sheet, print-only-the-recipe, dark mode, and Google Recipe structured data on every recipe.

---

## Step 1: Add your details

| Placeholder | Replace with |
|---|---|
| `https://www.yourdomain.com` | your real domain |
| `contact@yourdomain.com` | your real email (ideally on your own domain) |
| `The Vintage Recipe Box` | your site name, if you choose a different one (also redraw the logo with `brand/make_logo.py`) |
| `the Vintage Recipe Box team` | your name or team name |

Edit the `SETTINGS` block at the top of `tools/build.py`, then run `python3 tools/build.py`. Or use **Edit → Replace in Files** in VS Code.

## Step 2: Photos

Every recipe shows a real food photo from **Unsplash**. The [Unsplash License](https://unsplash.com/license) allows free commercial use, and Unsplash+ (paid) photos were excluded. The home page uses a vintage kitchen photo.

Unsplash has few photos of specific vintage dishes, so four are **stand-ins** (close matches): Swedish meatballs, Salisbury steak, cabbage rolls and coffee cake. These are marked in `tools/photos.py`.

**Your own photos are best of all,** especially a dish made from a real family recipe card. Save the photo as `site/assets/img/recipes/<recipe-name>.jpg` (landscape, about 1200 × 900 px, under 250 KB), for example `swedish-meatballs.jpg`, and run `python3 tools/build.py`. It replaces the Unsplash photo everywhere.

## Step 3: Upload to GitHub

Create a new repository (branch **main**) and upload **everything**, including the hidden `.github` folder.

```bash
git init
git add .
git commit -m "First version of the website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/vintage-recipe-box.git
git push -u origin main
```

## Step 4: Create the Azure Static Web App

1. In the Azure Portal, search **Static Web Apps** → **Create** → **Free** plan.
2. Under **Deployment details**, choose **Other**. Then **Review + create** → **Create**.
3. Open the app → **Overview** → **Manage deployment token** → copy the token.
4. In GitHub, go to **Settings → Secrets and variables → Actions → New repository secret**. Name it `AZURE_STATIC_WEB_APPS_API_TOKEN` and paste the token.
5. In GitHub, go to **Actions → Deploy website to Azure Static Web Apps → Run workflow** (or push any change).

*Alternative:* choose **GitHub** as the source in Azure with **App location `/site`** and blank **Api location** and **Output location**. If you do this, delete the included workflow file so the site doesn't deploy twice.

## Step 5: Connect your domain

**Static Web App → Custom domains → Add**, then add the DNS record Azure shows you at your domain registrar. Azure sets up SSL for free. AdSense will not approve an `azurestaticapps.net` address.

## Step 6: Get indexed, then apply to AdSense

1. Add the site in [Google Search Console](https://search.google.com/search-console) and submit `/sitemap.xml`.
2. Wait until pages show as indexed, which usually takes 1 to 4 weeks.
3. Apply at [adsense.google.com](https://adsense.google.com). Put your `ca-pub-…` ID in `adsense_client` in `tools/build.py` and rebuild, and replace the publisher ID in `site/ads.txt`.
4. In AdSense, go to **Privacy & messaging** and turn on the **European regulations** message (required) and the **US state regulations** message (recommended).
5. Turn on **Auto ads**. Recipe pages have clear headings and sections, so Auto ads can place ads between them.

**Approval checklist**
- [x] 32 pages of original content: 14 recipes with history notes and photos, categories, guides, and policy pages
- [x] About, Contact, Privacy (with Google's required ad disclosures), Terms, and Disclaimer pages, all linked from every footer
- [x] No broken links, mobile-friendly, fast loading, sitemap, robots.txt, and ads.txt
- [ ] Your custom domain and a real contact email
- [x] Food photos on every recipe (replace the stand-ins with your own when you can)
- [ ] **Add more recipes before applying (aim for 25 or more).** Good next ones: chicken and dumplings, tuna noodle casserole, chicken à la king, Watergate salad, pineapple upside-down cake, rice pudding, snickerdoodles, banana pudding.
- [ ] Keep adding 2 to 3 recipes a week. Copy a recipe block in `tools/content_recipes.py`, edit it, and rebuild.

---

## Google Ads: reaching iPhone users over 50 in the US

Create a **Display campaign** with the goal **Website traffic**. Use these settings:

| Setting | What to choose |
|---|---|
| **Locations** | United States. Under *Location options*, choose **Presence: people in or regularly in your included locations**. |
| **Languages** | English |
| **Devices** | Show ads on **Mobile phones** only. Uncheck Computers, Tablets, and TV screens. |
| **Device targeting (advanced)** | **Operating systems → iOS**, and **Device models → Apple → iPhone**. |
| **Demographics → Age** | **55–64** and **65+**. Google has no 50–54 bracket. Add **45–54** only if you want to include people in their early 50s, knowing it also includes ages 45–49. |
| **Audience segments** | Affinity: **Food & Dining → Cooking Enthusiasts**. Also create a **custom segment** of people who searched terms such as *easy dinner recipes*, *meatloaf recipe*, *chicken pot pie recipe*, *slow cooker recipes*, or *recipes for two*. |
| **Optimized targeting** | **Off** at first, so your age, device, and audience settings stay strict. |
| **Content → Topics** (optional) | **Food & Drink → Cooking & Recipes** |
| **Content → Exclusions** | Exclude sensitive content categories. Under **Placements**, exclude **mobile app categories**, so ads appear on websites rather than inside iPhone games and apps, where accidental clicks are common. |
| **Bidding** | Start with **Maximize clicks** and a maximum CPC limit, on a small daily budget. Raise the budget only after you check the results. |
| **Landing pages** | Send each ad to a specific recipe page, not the home page. Pies and nostalgic dishes such as lemon meringue pie, Swedish meatballs and wacky cake make strong landing pages. |
| **Ads** | Responsive display ads with real food photos and short, plain headlines such as "Classic Meatloaf, Easy Steps." |

Add UTM tags to your ad URLs (for example `?utm_source=google&utm_medium=display&utm_campaign=iphone50`) so you can see in Analytics how ad visitors behave.

**Things to know before you buy traffic**
- **Invalid traffic:** if you pay for visitors to a site that shows AdSense ads, Google holds *you* responsible for the quality of that traffic. Start only after AdSense approval and with small budgets. Watch for very short visits or unusually high ad click rates, and never click your own ads.
- **Arbitrage policy:** Google limits AdSense on pages whose main purpose is to show ads to paid visitors. Real recipes, photos, and steady new content are what keep the site compliant.
- **iPhone privacy features:** Safari limits third-party cookies, so remarketing audiences built from iPhone visitors will be smaller than on other devices. Rely on demographic, affinity, and custom-segment targeting instead.

## Preview locally

```bash
cd site && python3 -m http.server 8000   # then open http://localhost:8000
```

## Legal note

The policy pages are a solid starting template that covers Google's requirements, but they are not legal advice. Review them for your situation. Food safety guidance follows USDA recommendations.
