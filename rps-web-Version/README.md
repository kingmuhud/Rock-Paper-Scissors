# Rock · Paper · Scissors (Web)

Static site — ready to host. No build step, no backend.

## Files

```
rps-web/
├── index.html    # full game + AdSense slot
├── favicon.svg   # site icon
└── README.md
```

## Play locally

Open `index.html` in a browser, or:

```bash
# Python
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Add Google AdSense

1. Get approved at https://www.google.com/adsense/
2. Create an ad unit (Display / responsive).
3. In `index.html`, find the block marked **ADSENSE PLACEHOLDER**.
4. Replace the inner content of `.ad-slot-inner` with your AdSense snippet  
   (the `<script>` + `<ins class="adsbygoogle">` + push script).
5. Also add your AdSense account meta/script in `<head>` if AdSense provides one.

Until you paste real code, visitors only see a dashed “Ad space” box.

## Free hosting (recommended)

| Service | Why | How |
|---------|-----|-----|
| **Cloudflare Pages** | Fast CDN, free SSL, custom domain | Connect GitHub repo or drag-and-drop folder |
| **Netlify** | Drag-and-drop, free SSL, easy | netlify.com → Add new site → Deploy manually |
| **GitHub Pages** | Free with GitHub account | Repo → Settings → Pages → deploy `/` or `/docs` |
| **Vercel** | Free tier, simple | vercel.com → Import or CLI |

### Fastest path (no Git)

1. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)  
2. Drag the entire `rps-web` folder onto the page  
3. Get a live URL like `https://random-name.netlify.app`  
4. Optional: set a custom domain in Netlify settings  

### GitHub Pages

1. Create a repo, upload `index.html` + `favicon.svg`  
2. Settings → Pages → Source: Deploy from branch `main` / root  
3. Site at `https://YOURUSER.github.io/REPO/`  

## Tips

- AdSense usually needs a real domain and some content/traffic before approval.
- Keep the game playable above the ad; don’t cover buttons with ads.
- For a custom domain, Cloudflare Pages or Netlify free tiers both work well.
