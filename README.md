# Dial Studio

Design rose-engine and straight-line guilloché patterns in the browser, then export them for CAD and CNC (SVG, DXF, and a Fusion script that builds a 3D dial).

The whole app is one static page (`index.html`) with no build step. It is also an installable web app (PWA): open it in Chrome or Edge and choose **Install**, or on iPhone use **Share → Add to Home Screen**. It keeps working offline after the first visit.

## Finishes

Besides guilloché patterns, a layer can be a **finish**: brushed (satin), circular brushed, sunray (soleil), grained / frosted (sablé), circular graining (perlage) or Côtes de Genève. Finishes are placed, stacked and masked like any other layer and show in 2D and 3D; they are left out of exports unless a layer is set to export its strokes.

## Text, markers and tracks

**Text** is its own layer: straight or on an arc, or following a **badge** (a frame) so it moves with it. *Spread words evenly* makes the gaps between words equal while letters stay together. **Markers & tracks** space ticks, batons, dots and shapes along a circle or arc, a rounded rectangle (square tracks), the body outline or a line, by equal angle (where the hands point) or equal distance, with major marks, railway rails and labels (numbers, Roman numerals or a custom list). Elements can be engraved or printed (ink, never cut).

## Bodies (sub-assembled dials)

A design is a stack of **bodies**: plates with their own outline (round, square, tonneau, cushion, or a custom outline imported from an SVG), size, position, rotation, thickness, material and layers. **Height** moves a body up or down relative to the base dial's top; a body set down into the one below gets a pocket cut for it automatically. SVG and DXF export the selected body; **Fusion model** builds the whole assembly, one component per body.

## Saving your work

- **Save to browser** (Ctrl+S) keeps designs in this browser's IndexedDB storage, uploaded fonts included. They are listed under *Saved in this browser*. Saving again with the same design name updates that save.
- **Download design** saves a `.json` file you can open on any device with **Open design…**.
- **Undo / Redo** (Ctrl+Z, Ctrl+Shift+Z or Ctrl+Y) step through your edits.

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
