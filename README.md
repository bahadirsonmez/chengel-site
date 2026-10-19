# chengel.bahadirsonmez.com

Static site for Chengel, served by GitHub Pages from `main` (custom domain in `CNAME`).

## Launch day: App Store links

Until Chengel is on the App Store the site shows "Coming soon" and has no App Store link.
On launch day it is one step:

```sh
git revert 4c3a607   # "Back to coming soon until launch day: no App Store links"
```

That commit is the only place the links were taken out, so reverting it restores all of them
(App Store id `6819309538`, `https://apps.apple.com/app/id6819309538`) in `index.html`:

- the `apple-itunes-app` Smart App Banner meta in `<head>`
- `downloadUrl` in the JSON-LD
- the menu pill (`Get Chengel`)
- the hero button (`Download on the App Store`) and the kicker / meta description wording
- the FAQ answer (`Get Chengel on the App Store`)

Check `curl -sI https://apps.apple.com/app/id6819309538` no longer returns 404 before pushing.
The other sites (bahadirsonmez.com, the app sites' "More apps" footers, the blog) list Chengel as
"coming soon" too; update those on the same day.
