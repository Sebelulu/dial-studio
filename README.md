# Guilloché Studio

Design rose-engine and straight-line guilloché patterns in the browser, then export them for CAD and CNC (SVG, DXF, and a Fusion script that builds a 3D dial).

The whole app is one static page (`index.html`) with no build step. It is also an installable web app (PWA): open it in Chrome or Edge and choose **Install**, or on iPhone use **Share → Add to Home Screen**. It keeps working offline after the first visit.

## Run locally

```bash
npx serve .
```

## Deploy on Vercel

1. In Vercel, choose **Add New → Project** and import this repository.
2. Framework preset: **Other**. Leave the build command and output directory empty.
3. Click **Deploy**. Every push to `main` redeploys automatically.

## Files

- `index.html`: the app
- `manifest.webmanifest`, `icons/`: app name and icons for installing
- `sw.js`: service worker for offline use (network-first, so updates show up right away)
- `vercel.json`: headers for the service worker and manifest
