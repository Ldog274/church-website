# Church Website

Static site for [CHURCH NAME], hosted free on GitHub Pages.

## How it is published

Every push to `main` updates the live website within about a minute. There is no
build step, no framework, and no dependencies - just HTML and one CSS file.

- `index.html` - home
- `about.html` - about us / plan a visit
- `beliefs.html` - what we believe
- `ministries.html` - ministries
- `sermons.html` - sermons
- `give.html` - giving
- `contact.html` - contact and directions
- `404.html` - shown for a bad URL
- `css/styles.css` - all styling, one file
- `CNAME` - the custom domain, once it is configured

## Placeholders

Every value that needs real information is written as a bracketed placeholder,
for example `[CHURCH NAME]` or `[9:30 AM]`. Find them all with:

```bash
grep -rn '\[' --include='*.html' .
```

Blocks marked **TO FILL IN** render as a yellow note on the page so nothing goes
live half-finished. Delete the `<div class="todo">...</div>` wrapper once filled.

## Editing

Edit the file, commit, push. That is the whole workflow.

```bash
git add -A && git commit -m "Update service times" && git push
```

## Notes

- No fonts, scripts, or images are loaded from third-party servers. Pages include
  no tracking, no cookies, and no analytics, so there is nothing to disclose in a
  privacy notice.
- Do not put bank details, giving account numbers, or member information in this
  repository. It is a public repository.
