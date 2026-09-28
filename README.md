# East Side Free Will Baptist Church

Static site for East Side Free Will Baptist Church, Muldrow, Oklahoma.
Hosted free on GitHub Pages at <https://eastsidefwbc.org/>.

## How it is published

Every push to `main` updates the live website within about a minute. There is no build step,
no framework and no dependencies - just HTML and one CSS file.

- `index.html` - home
- `about.html` - about us, our pastors, planning a visit
- `beliefs.html` - what we believe
- `ministries.html` - ministries
- `calendar.html` - church calendar
- `sermons.html` - sermons and livestream
- `give.html` - giving
- `contact.html` - contact, directions, map
- `404.html` - shown for a bad URL
- `css/styles.css` - all styling, one file
- `assets/img/` - photographs, with credits in `assets/img/CREDITS.md`
- `CNAME` - the custom domain. GitHub manages this file; do not edit or delete it.

## Editing

Edit the file, commit, push. That is the whole workflow.

```bash
git add -A && git commit -m "Update service times" && git push
```

## The calendar

`calendar.html` is ready to be wired to the church's Google Calendar, so events added there
appear on the site automatically. To switch it on:

1. In Google Calendar, hover the church calendar, open **Settings and sharing**.
2. Under *Access permissions for events*, tick **Make available to public**.
3. Under *Integrate calendar*, copy the **Calendar ID**.
4. In `calendar.html`, replace `YOUR_CALENDAR_ID` in the commented-out iframe, delete the
   comment marks around that iframe, and delete the `callout--quiet` block beneath it.

The calendar must be public or the embed will not render, and only events on that calendar
are shown - so keep private appointments on a separate calendar.

## Privacy and third parties

The site loads no fonts, scripts or analytics from third-party servers. Two elements are
Google's, and they only load when the visitor scrolls to them:

- the Google Map on `contact.html`
- the Google Calendar on `calendar.html`, once enabled

Both set Google's own cookies when they load.

## Please keep out of this repository

It is a public repository. Do not commit bank details, giving account numbers, or member
information.
