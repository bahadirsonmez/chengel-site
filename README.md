# chengel.bahadirsonmez.com

Static site for Chengel, served by GitHub Pages from `main` (custom domain in `CNAME`).

## Launch day: App Store links

Until Chengel is on the App Store the site shows "Coming soon" and has no App Store link.
On launch day it is one step:

```sh
python3 _launch-day.py
```

The script puts every App Store link back (App Store id `6819309538`,
`https://apps.apple.com/app/id6819309538`) in `index.html` and changes nothing else:

- the `apple-itunes-app` Smart App Banner meta in `<head>`
- `downloadUrl` in the JSON-LD
- the menu pill (`Get Chengel`)
- the hero kicker (`Free · iPhone & iPad`), the hero button (`Download on the App Store`)
  and the meta description wording
- the FAQ answer (`Get Chengel on the App Store`)

Each replacement has to match exactly once or the script stops without writing, so it is safe to
run. The links were taken out in commit `4c3a607`; a plain `git revert 4c3a607` no longer applies
cleanly because the Android line now sits next to the hero kicker.
The leading underscore keeps GitHub Pages from publishing the script.

Check `curl -sI https://apps.apple.com/app/id6819309538` no longer returns 404 before pushing.
The trailer (`assets/promo/chengel-promo-v2.mp4` and its poster) also says "Coming soon" on its
closing card since commit `a0c39d4`; re-render it from `chengel-promo/trailer.html` on the same day.
The other sites (bahadirsonmez.com, the app sites' "More apps" footers, the blog) list Chengel as
"coming soon" too; update those on the same day.

## Android (not built yet)

There is no Android app and no date. The site only says it is coming later, in two places in
`index.html`; there is no Play Store link, badge or logo, and Android is not in the meta
description or the JSON-LD.

- hero: `<p class="kicker kicker-soft">Android &middot; coming later</p>` inside `.kickers`
  (style: `.kicker-soft` in `styles.css`)
- FAQ: `<details id="android">` "Is Chengel coming to Android?"

`_launch-day.py` does not touch these lines. When the Android version ships,
update or remove both by hand (and add the Play Store link, `downloadUrl` and description then).
