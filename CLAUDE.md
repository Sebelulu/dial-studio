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

- Data model: `state.bodies` (base first; later bodies sit on top), `state.cur` = selected body. `state.layers`, `state.sel` and `state.dial` are non-enumerable accessors for the selected body (set up by `withBodyAccess`), so always create state through `restoreState`/`defaultState`. Geometry, exports and 3D work on `bodyView(state, i)`, which adds the automatic pockets (`pocketsFor`) and leaves out holes/indents that a higher body covers (`coveredHoles`). Old single-dial files (`dial` + `layers`) load as one round body.
- Bodies can rotate (`rotation`, degrees, about the body centre; patterns rotate with the body). Use `bodyToWorld`/`worldToBody`, and `bodyShapeIn(U, L)` for one body's outline in another's coordinates. Shape `custom` is an imported SVG outline stored in `custom.loop` (unit box), sized by width/height and moved by `shapeX/shapeY`. SVG/DXF export a body in its own unrotated frame.
- The graver (angle, cut depth) is per body (`graverAngle`, `cutDepth`); `bodyView`/`outFor` merge it into `out`. Material is per body too (`metal`, a key of `METALS`, which also lists the Fusion material/appearance names). `state.out` holds only whole-design export settings (its old angle/depth just seed bodies of older files).
- Finishes are a layer type (`finish`, `GEN.finish`, styles in `FINISH_STYLES`): seeded fine strokes that go through the normal clip/mask pipeline. `layerCut` gives them a shallow texture depth and stroke width instead of a graver cut; `exportable()` keeps them out of SVG/DXF/Fusion unless `exportLines`, and the Fusion script never cuts them as grooves.
- 3D faces are built with the inlined polygon-clipping library (`window.polygonClipping`): top = body − openings, floors per depth, walls split where the surface level changes (`levelAt`). Don't go back to THREE.Shape holes: they break when openings overlap or cross an edge.
- The Fusion script's data has `bodies[]` (version 2 design files); top-level single-dial fields are kept for older installed copies of the script.

- Keep internal identifiers stable so existing files keep working: the design file tag `app: 'guilloche-studio'`, the Fusion export tag `guilloche-studio-fusion`, the `GuillocheDial` Fusion script folder, and the autosave key `guilloche-studio-v1`.
- When `sw.js` changes meaningfully, bump its `CACHE` name.
- Test in Chromium (Playwright) by serving the folder, e.g. `python3 -m http.server`, and check for page errors.
