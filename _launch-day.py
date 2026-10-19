#!/usr/bin/env python3
"""Launch day for Chengel on the App Store: put the App Store links back in index.html.

Run from this folder:  python3 _launch-day.py
It undoes the "coming soon" state from commit 4c3a607 (menu pill, hero kicker and button,
FAQ answer, meta description, Smart App Banner meta, JSON-LD downloadUrl) and leaves
everything else alone, including the Android "coming later" lines. Each replacement must
match exactly once, otherwise nothing is written. The leading underscore keeps GitHub
Pages (Jekyll) from publishing this file.
"""
import pathlib, sys

APP_STORE = "https://apps.apple.com/app/id6819309538"
APP_ID = "6819309538"

REPLACEMENTS = [
    ("from A1 to C1. Coming soon to iPhone and iPad.\">",
     "from A1 to C1. Free on iPhone and iPad.\">"),
    ('  <meta name="theme-color" content="#ecf2fe">\n',
     f'  <meta name="theme-color" content="#ecf2fe">\n  <meta name="apple-itunes-app" content="app-id={APP_ID}">\n'),
    ('"applicationCategory":"EducationalApplication",',
     f'"applicationCategory":"EducationalApplication","downloadUrl":"{APP_STORE}",'),
    ('<a class="pill" href="#launch">Coming soon &middot; iPhone &amp; iPad</a>',
     f'<a class="pill" href="{APP_STORE}">Get Chengel</a>'),
    ('<p class="kicker">Coming soon &middot; iPhone &amp; iPad</p>',
     '<p class="kicker">Free &middot; iPhone &amp; iPad</p>'),
    ('<span class="button soon"><img src="assets/illo/sprout.svg" alt="" width="28" height="28">Coming soon to the App Store</span>',
     f'<a class="button" href="{APP_STORE}"><img src="assets/illo/sprout.svg" alt="" width="28" height="28">Download on the App Store</a>'),
    ('''        <details id="launch">
          <summary>When does it launch?</summary>
          <p>Soon, on the App Store for iPhone and iPad (iOS 17 or later). This page will link to it on launch day.</p>''',
     f'''        <details id="launch">
          <summary>Which devices does it run on?</summary>
          <p>iPhone and iPad with iOS 17 or later. <a href="{APP_STORE}">Get Chengel on the App Store</a>.</p>'''),
]

page = pathlib.Path(__file__).with_name("index.html")
html = page.read_text(encoding="utf-8")
for old, new in REPLACEMENTS:
    if html.count(old) != 1:
        sys.exit(f"index.html: expected exactly one match for:\n{old}\nNothing was changed.")
    html = html.replace(old, new)
page.write_text(html, encoding="utf-8")
print("App Store links restored in index.html. Check the page, then commit and push.")
