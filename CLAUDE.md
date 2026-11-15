# Dial Studio

A single-page static web app (`index.html`, no build step) deployed on Vercel from `main`.

## Every change ships to two places

Whenever you change the app, update **both**:

1. **GitHub / Vercel**: commit and push to `main`. Vercel redeploys automatically.
2. **The claude.ai artifact** at https://claude.ai/artifact/Ekpjtyeivv6z5p7EvDjwaT:
   build the artifact copy, then publish it to that URL (same link, new version):

   ```bash
   python3 scripts/build-artifact.py <scratchpad>/dial-studio.html
   ```

   The script strips the PWA-only parts (manifest, icons, service worker), which don't apply inside claude.ai.

## Notes

- Keep internal identifiers stable so existing files keep working: the design file tag `app: 'guilloche-studio'`, the Fusion export tag `guilloche-studio-fusion`, the `GuillocheDial` Fusion script folder, and the autosave key `guilloche-studio-v1`.
- When `sw.js` changes meaningfully, bump its `CACHE` name.
- Test in Chromium (Playwright) by serving the folder, e.g. `python3 -m http.server`, and check for page errors.
