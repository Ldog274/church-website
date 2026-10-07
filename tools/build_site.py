# -*- coding: utf-8 -*-
"""Generate the finished East Side FWB church site."""
import os, re, calendar, datetime

D = r"C:/Users/logan/church-website"

NAME   = "East Side Free Will Baptist Church"
STREET = "613 E Sequoyah St"
CITY   = "Muldrow, OK 74948"
TELD   = "(918) 427-5116"
TEL    = "tel:+19184275116"
FB     = "https://www.facebook.com/esfwbc"
VISION_URL = "https://eastsidefwb.churchcenter.com/giving/to/vision-fund"
CHAIR_URL  = "https://eastsidefwb.churchcenter.com/giving/to/chair-donation"
EMAIL  = "eastsidefwbc@gmail.com"
ACT    = "1302 S. Main St."
MAPDIR = "https://www.google.com/maps/dir/?api=1&destination=613+E+Sequoyah+St,+Muldrow,+OK+74948"
MAPEMB = "https://www.google.com/maps?q=613+E+Sequoyah+St,+Muldrow,+OK+74948&z=16&output=embed"
IMG    = "assets/img"
OG_IMG = "/assets/img/social-card.jpg"

# Structured data for search engines and local listings. Only facts we can stand
# behind: no coordinates or opening/closing times are invented here.
CHURCH_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Church",
  "name": "East Side Free Will Baptist Church",
  "alternateName": "East Side FWB Church",
  "url": "https://eastsidefwbc.org/",
  "description": "A Free Will Baptist congregation in Muldrow, Oklahoma. Sunday school 9:30 AM, morning worship 10:30 AM with children's church, Wednesday evening service 7:00 PM.",
  "image": "https://eastsidefwbc.org/assets/img/social-card.jpg",
  "logo": "https://eastsidefwbc.org/apple-touch-icon.png",
  "telephone": "+1-918-427-5116",
  "email": "eastsidefwbc@gmail.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "613 E Sequoyah St",
    "addressLocality": "Muldrow",
    "addressRegion": "OK",
    "postalCode": "74948",
    "addressCountry": "US"
  },
  "areaServed": { "@type": "City", "name": "Muldrow, Oklahoma" },
  "sameAs": ["https://www.facebook.com/esfwbc"]
}
</script>"""

NAV = [("index.html", "Home"), ("about.html", "About"), ("beliefs.html", "What We Believe"),
       ("ministries.html", "Ministries"), ("calendar.html", "Calendar"), ("announcements.html", "Announcements"),
       ("study-material.html", "Study Material"),
       ("give.html", "Give"), ("contact.html", "Contact")]

# Study Material is a section, not a single page: its subpages keep the section
# marked as the current one in the nav, so the menu still shows you where you are.
STUDY_PAGES = ("study-material.html", "sermons.html", "devotions.html")


def nav(page, base=""):
    if page in STUDY_PAGES or page.startswith("devotions/"):
        page = "study-material.html"
    rows = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ''
        rows.append('        <li><a href="%s%s"%s>%s</a></li>' % (base, href, cur, label))
    return "\n".join(rows)


FOOTER_TMPL = """<footer class="site-footer">
  <div class="wrap">
    <div>
      <h3>Service Times</h3>
      <ul>
        <li>Sunday School &mdash; 9:30 AM</li>
        <li>Morning Worship &mdash; 10:30 AM<span class="fine">Children&rsquo;s church at the same hour</span></li>
        <li>Wednesday &mdash; 7:00 PM<span class="fine">Youth meet at the Activities Center</span></li>
      </ul>
    </div>
    <div>
      <h3>Find Us</h3>
      <ul>
        <li>%(street)s</li>
        <li>%(city)s</li>
        <li><a href="%(tel)s">%(teld)s</a></li>
        <li><a href="mailto:%(email)s">%(email)s</a></li>
        <li><a href="%(base)scontact.html">Directions &amp; contact</a></li>
      </ul>
    </div>
    <div>
      <h3>Connect</h3>
      <ul>
        <li><a href="%(fb)s">Facebook</a></li>
        <li><a href="%(base)scalendar.html">Calendar</a></li>
        <li><a href="%(base)sstudy-material.html">Study Material</a></li>
        <li><a href="%(base)sdevotions.html">Devotions</a></li>
        <li><a href="%(base)sgive.html">Give</a></li>
      </ul>
    </div>
    <p class="legal">&copy; <span id="yr">2026</span> %(name)s</p>
  </div>
</footer>

<script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>"""


def footer(base=""):
    return FOOTER_TMPL % dict(street=STREET, city=CITY, tel=TEL, teld=TELD, fb=FB,
                              name=NAME, email=EMAIL, base=base)


def render(page, title, desc, body, schema="", base=""):
    url = "https://eastsidefwbc.org/" + ("" if page == "index.html" else page)
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">

<meta property="og:type" content="website">
<meta property="og:site_name" content="East Side Free Will Baptist Church">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="https://eastsidefwbc.org%(ogimg)s">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="East Side Free Will Baptist Church, Muldrow, Oklahoma">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="https://eastsidefwbc.org%(ogimg)s">

<meta name="theme-color" content="#14273a">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="%(base)scss/styles.css">
%(schema)s
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="%(base)sindex.html">East Side <small>Free Will Baptist Church</small></a>
    <nav class="site-nav" aria-label="Main">
      <ul>
%(nav)s
      </ul>
    </nav>
  </div>
</header>

<main id="main">

%(body)s
</main>

%(footer)s
""" % dict(title=title, desc=desc, url=url, nav=nav(page, base), body=body, footer=footer(base),
         ogimg=OG_IMG, schema=schema, base=base)


TIMES_BLOCK = """  <section class="times-section" id="this-week">
    <div class="wrap">
      <h2 class="center">Join us this week</h2>
      <dl class="times times--light">
        <div class="time-card">
          <dt>Sunday School</dt>
          <dd>9:30 AM<span>Classes for every age</span></dd>
        </div>
        <div class="time-card">
          <dt>Morning Worship</dt>
          <dd>10:30 AM<span>Children&rsquo;s church at the same hour</span></dd>
        </div>
        <div class="time-card">
          <dt>Wednesday Evening</dt>
          <dd>7:00 PM<span>Youth meet at the Activities Center</span></dd>
        </div>
      </dl>
    </div>
  </section>""" % dict(street=STREET, city=CITY, tel=TEL, teld=TELD)


# ----------------------------------------------------------------- index
index_body = """  <section class="hero hero--full">
    <img class="hero__bg" src="%(img)s/wheat-sunset.jpg" srcset="%(img)s/wheat-sunset-640.jpg 640w, %(img)s/wheat-sunset.jpg 1024w" sizes="100vw" alt="" aria-hidden="true">
    <div class="wrap wrap--narrow">
      <p class="eyebrow">Welcome to</p>
      <h1>East Side Free Will Baptist Church</h1>
      <p class="hero__actions">
        <a class="btn" href="about.html">Plan a Visit</a>
        <a class="btn btn--ghost" href="sermons.html">Watch a Service</a>
      </p>
    </div>
  </section>

  <section class="welcome">
    <div class="wrap wrap--narrow prose">
      <p class="lede">We are a church family committed to knowing Christ, growing together in His
      Word, and sharing the hope of the gospel with our community and beyond. At East Side, we
      believe the church is more than a place we gather&mdash;it is a family of believers walking
      through life together, encouraging one another, serving one another, and seeking to
      faithfully follow Jesus.</p>

      <p>Whether you have followed Christ for many years, are searching for answers, or are simply
      looking for a church to call home, there is a place for you here. Our desire is that every
      person who walks through our doors feels welcomed, hears the truth of God&rsquo;s Word, and
      has the opportunity to grow in a meaningful relationship with Christ and with others.</p>

      <p>For more than sixty years, East Side has been part of the Muldrow community, and our
      mission remains simple: to impact our world for Christ.</p>

      <p>We would love for you and your family to join us as we worship, grow, serve, and follow
      Christ together.</p>
    </div>
  </section>

%(times)s

  <section class="locate" id="find-us">
    <div class="wrap locate__wrap">
      <div class="locate__text">
        <p class="meta">Find us</p>
        <h2>Where we are</h2>
        <p><strong>%(street)s</strong><br>%(city)s</p>
        <p>We are in Muldrow, in Sequoyah County. The map shows the church, and the button below opens
        turn-by-turn directions.</p>
        <p><a class="btn" href="%(mapdir)s">Get directions</a></p>
      </div>
      <div class="map-wrap map-wrap--home">
        <iframe class="embed map-embed"
                title="Map showing East Side Free Will Baptist Church at %(street)s, Muldrow, Oklahoma"
                src="%(mapemb)s"
                loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
    <p class="fine-print wrap">Map data &copy; Google. <a href="%(mapdir)s">Open in Google Maps</a></p>
  </section>

  <section>
    <div class="wrap">
      <h2>Where to start</h2>
      <div class="grid">
        <article class="card">
          <p class="meta">New here?</p>
          <h3>Plan a visit</h3>
          <p>Where we are, where the children go, and what a Sunday morning looks like.</p>
          <p><a href="about.html">Read more &rarr;</a></p>
        </article>
        <article class="card">
          <p class="meta">This week</p>
          <h3>Church calendar</h3>
          <p>Services, youth, and upcoming events &mdash; kept in step with our own church calendar.</p>
          <p><a href="calendar.html">View the calendar &rarr;</a></p>
        </article>
        <article class="card">
          <p class="meta">Study</p>
          <h3>Sermons &amp; devotions</h3>
          <p>Missed a Sunday, or want something to read through the week? Our messages and our
          devotional writings live together under Study Material.</p>
          <p><a href="study-material.html">Read and watch &rarr;</a></p>
        </article>
        <article class="card">
          <p class="meta">Curious?</p>
          <h3>What we believe</h3>
          <p>What we hold to be true, in plain language &mdash; and where we stand as Free Will Baptists.</p>
          <p><a href="beliefs.html">See what we believe &rarr;</a></p>
        </article>
      </div>
    </div>
  </section>

  <section class="feature">
    <div class="wrap feature__wrap">
      <figure class="figure">
        <img src="%(img)s/praying.jpg" srcset="%(img)s/praying-640.jpg 640w, %(img)s/praying.jpg 1024w" sizes="(max-width: 46rem) 100vw, 45vw" alt="Hands clasped in prayer resting on an open Bible.">
      </figure>
      <div class="feature__text">
        <h2>A church that prays for its community</h2>
        <p>What holds this congregation together is a confidence that the Bible is God&rsquo;s Word and
        that the gospel is worth giving your life to.</p>
        <p>Much of the work of this church happens quietly &mdash; hospital and nursing home visits,
        meals carried to a house where someone is grieving, phone calls to those who can no longer get
        out. It is care given without a fuss, and it is as much the work of the church as the preaching
        is.</p>
        <p>If you need prayer, we would count it a privilege to pray with you.
        <a href="contact.html">Send us a prayer request &rarr;</a></p>
      </div>
    </div>
  </section>

  <section class="announce">
    <div class="wrap wrap--narrow">
      <p class="meta">Building Update</p>
      <h2>A new worship and ministry center</h2>
      <p>In October 2025 the church broke ground on a 14,000 square foot worship and ministry center at
      <strong>1302 South Main Street</strong>, expected to open in <strong>December 2026</strong>. We
      will keep this page updated as the work progresses.</p>
    </div>
  </section>

  <section class="band">
    <img src="%(img)s/stained-glass.jpg" srcset="%(img)s/stained-glass-640.jpg 640w, %(img)s/stained-glass.jpg 1024w" sizes="100vw" alt="" aria-hidden="true">
    <div class="wrap wrap--narrow">
      <blockquote class="band__quote">
        For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.
        <cite>&mdash; John 3:16</cite>
      </blockquote>
    </div>
  </section>
""" % dict(img=IMG, times=TIMES_BLOCK, street=STREET, city=CITY, mapdir=MAPDIR, mapemb=MAPEMB)

# Preserve the home-page feature draft until Logan has edited and approved it.
SHOW_COMMUNITY_PRAYER = False
if not SHOW_COMMUNITY_PRAYER:
    index_body = re.sub(r'\s*<section class="feature">.*?</section>', '', index_body, count=1, flags=re.S)

open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(render(
    "index.html",
    "East Side Free Will Baptist Church &mdash; Muldrow, Oklahoma",
    "A Free Will Baptist church family in Muldrow, Oklahoma. Sunday school 9:30 AM, morning worship 10:30 AM, Wednesday evening 7:00 PM. All are welcome.",
    index_body, schema=CHURCH_SCHEMA))
print("index.html written")


# ----------------------------------------------------------------- about
# Keep the draft in the source, but omit it from published HTML until verified.
SHOW_HISTORY = False
SHOW_WHAT_WE_ARE_ABOUT = False

about_body = """  <section>
    <div class="wrap wrap--narrow prose">
      <h1>About Us</h1>
      <p class="lede">East Side Free Will Baptist Church has served Muldrow and the surrounding area
      for more than sixty years &mdash; a congregation with a long memory and an open door.</p>

      <h2>Visiting for the first time</h2>
      <p>The first visit is the hardest part, so here is what you need to know.</p>
      <ul>
        <li><strong>Where we are</strong> &mdash; %(street)s, %(city)s.</li>
        <li><strong>Sunday morning</strong> &mdash; Sunday school for every age at <strong>9:30 AM</strong>, then morning worship at <strong>10:30 AM</strong>.</li>
        <li><strong>Children</strong> &mdash; children&rsquo;s church meets during the 10:30 AM worship hour, so parents can worship while the children are taught at their own level.</li>
        <li><strong>Wednesday</strong> &mdash; the church gathers at <strong>7:00 PM</strong> for Bible study and prayer, and our youth meet at the same hour at the Activities Center, %(act)s.</li>
      </ul>
      <p>If you have a question we have not answered here &mdash; about parking, about access, about
      anything at all &mdash; please call us at <a href="%(tel)s">%(teld)s</a>. We would far rather
      answer the phone than have you wonder.</p>

      <h2>Our pastors</h2>

      <h3>Pastor Anthony Williams</h3>
      <p>Pastor Anthony Williams has faithfully served East Side Free Will Baptist Church since
      <strong>2001</strong>. For more than two decades, he has walked alongside generations of
      families through some of life&rsquo;s most meaningful moments&mdash;baptizing new believers,
      officiating weddings, comforting families through loss, and faithfully serving the community.
      Through it all, his heart for people and commitment to Scripture have remained constant. Each
      week, Pastor Anthony continues to preach the Word of God plainly, faithfully, and with a desire
      to see lives changed by the gospel.</p>

      <h3>Associate Pastor Logan Williams</h3>
      <p>Logan Williams has served as associate pastor since <strong>2024</strong>. He is Pastor
      Williams&rsquo;s son, and his work centers on the nursing home, hospital, and shut-in ministry
      &mdash; visiting the sick, praying with them and their families, and keeping the church connected
      to members who can no longer come to us.</p>

      <h2>A new worship and ministry center</h2>
      <p>In October 2025 the church broke ground on a <strong>14,000 square foot worship and ministry
      center</strong> at 1302 South Main Street. It is expected to open in <strong>December 2026</strong>
      and will give us room to gather, teach, and host the community in a way the current building
      cannot.</p>

      <hr>
      <p><a class="btn" href="contact.html">Contact us</a></p>
    </div>
  </section>

  <section class="history">
    <div class="wrap wrap--narrow prose">
      <h2>Our history</h2>
      <p>East Side has been part of Muldrow for more than sixty years. A few of the milestones
      along the way:</p>
      <ol class="timeline">
        <li><strong>2001</strong><span>Anthony Williams is called as pastor of East Side.</span></li>
        <li><strong>2024</strong><span>Logan Williams joins the pastoral staff as associate pastor,
        taking up the nursing home, hospital, and shut-in ministry.</span></li>
        <li><strong>October 2025</strong><span>The church breaks ground on a 14,000 square foot
        worship and ministry center at 1302 South Main Street.</span></li>
        <li><strong>December 2026</strong><span>The new worship and ministry center is expected to
        open.</span></li>
      </ol>
    </div>
  </section>

  <section class="feature feature--reverse">
    <div class="wrap feature__wrap">
      <figure class="figure">
        <img src="%(img)s/open-bible.jpg" srcset="%(img)s/open-bible-640.jpg 640w, %(img)s/open-bible.jpg 1024w" sizes="(max-width: 46rem) 100vw, 45vw" alt="An open Bible resting outdoors.">
      </figure>
      <div class="feature__text">
        <h2>What we are about</h2>
        <p>We are ordinary people who believe the Bible is God&rsquo;s Word, that salvation is by grace
        through faith in Jesus Christ, and that a church is at its best when it is caring for the people
        around it.</p>
        <p>You will find us in the hospital room of one of our own, at the nursing home, and at the
        kitchen table of a family in a hard week &mdash; as much as you will find us on a Sunday
        morning.</p>
      </div>
    </div>
  </section>
""" % dict(street=STREET, city=CITY, tel=TEL, teld=TELD, act=ACT, img=IMG)

if not SHOW_HISTORY:
    about_body = re.sub(r'\s*<section class="history">.*?</section>', '', about_body, count=1, flags=re.S)

if not SHOW_WHAT_WE_ARE_ABOUT:
    about_body = re.sub(r'\s*<section class="feature feature--reverse">.*?</section>', '', about_body, count=1, flags=re.S)

open(os.path.join(D, "about.html"), "w", encoding="utf-8").write(render(
    "about.html",
    "About Us &mdash; East Side Free Will Baptist Church",
    "Our pastors, our church, and what to expect on a first visit at East Side Free Will Baptist Church in Muldrow, Oklahoma.",
    about_body))
print("about.html written")


# ----------------------------------------------------------------- beliefs
BELIEFS = [
    ("The Bible",
     "God used holy men to write the Scriptures. They are, in both the Old and New Testaments, the very "
     "words God intended us to have. They are, as given by God, without error and are our only rule of "
     "faith and practice. We profit from them by learning the truth about many things: they also speak "
     "to us about wrong doing, they correct us and get us back on course, and they instruct us in right "
     "living."),
    ("God",
     "We believe that God is the Creator, Sustainer, and Righteous Ruler of the universe. He has revealed "
     "Himself in nature, and in the Scriptures of the Holy Bible as Father, Son, and Holy Spirit: yet as "
     "one God."),
    ("Jesus Christ",
     "He is God&rsquo;s unique Son; the only one of a kind. The Scripture teaches that He is God revealed "
     "in flesh. In His divine nature He is truly God and in His human nature truly man. He is the One once "
     "crucified for man&rsquo;s sin, the now risen and glorified Savior and Lord who mediates between God "
     "and man and who gives us access to the Father through His intercession. None can come to the Father "
     "unless they come through Him."),
    ("The Holy Spirit",
     "All of the attributes of God are ascribed to the Holy Spirit by the Scriptures. It is He who convicts "
     "and convinces men of their sin. He also convinces man of that which is right, and that a final day of "
     "judgment will come. It is He who comes to live in us at conversion, to open our understanding to the "
     "Scripture, and to lead us into the truth."),
    ("Man",
     "God created man in a state of innocence. Man, being tempted by Satan, yielded and willfully disobeyed "
     "God, becoming a sinner and incurring God&rsquo;s judgment upon sin. All of Adam&rsquo;s descendants "
     "inherit his fallen nature and thus have a natural inclination to sin. When one comes to an age of "
     "accountability, he is guilty of sinning before God and in need of salvation."),
    ("God&rsquo;s Relationship to His Creatures and Creation",
     "God exercises a wise and benevolent providence over all beings and things. He maintains the laws of "
     "nature and performs special acts as the highest welfare of mankind and His created order of things "
     "require."),
    ("Salvation",
     "Man receives pardon and forgiveness for his sins when he admits to God that he is a sinner, when in "
     "godly sorrow he turns from them and trusts in the work of Christ as redemption for his sin. This "
     "acceptance of God&rsquo;s great salvation involves belief in Christ&rsquo;s death on the cross as "
     "man&rsquo;s substitute and the fact of God&rsquo;s raising Him from the dead as predicted. It is a "
     "salvation by grace alone and not of works."),
    ("Who Can Be Saved?",
     "It is God&rsquo;s will that all be saved, but since man has the power of choice, God saves only those "
     "who repent of their sin and believe in the work of Christ on the cross. Those who refuse in this life "
     "to repent and believe have no later chance to be saved and thus condemn themselves to eternal "
     "damnation by their unbelief."),
    ("Perseverance",
     "We believe that there are strong grounds to hope that the saved will persevere unto the end and be "
     "saved, because of the power of divine grace pledged for their support. We believe that any saved "
     "person who has sinned but has a desire to repent may do so and be restored to God&rsquo;s favor and "
     "fellowship. Since man, however, continues to have free choice, it is possible because of temptations "
     "and the weakness of human flesh for him to fall into the practice of sin and to make shipwreck of his "
     "faith and be lost."),
    ("Gospel Ordinances",
     "Free Will Baptists believe the Bible teaches three ordinances for the church to practice: baptism in "
     "water by immersion; the Lord&rsquo;s Supper, to be perpetuated until His return; and the washing of "
     "the saints&rsquo; feet, an ordinance teaching humility."),
    ("Resurrection",
     "Free Will Baptists believe the Scriptures teach the resurrection of the bodies of all men, each in its "
     "own order; they that have done good will come forth to the resurrection of life, and they that have "
     "done evil to the resurrection of damnation."),
    ("Church Government",
     "Free Will Baptist churches enjoy local church autonomy (self-governing). The local church is the "
     "highest authority in the denomination. Local churches voluntarily organize themselves into quarterly "
     "meetings, district, state, and national associations for the purpose of promoting the cause of Christ "
     "on the local, state, district, national, and world-wide level."),
    ("Christ&rsquo;s Second Coming",
     "The Bible teaches that Jesus Christ, who ascended on high and sits at the right hand of God, will come "
     "again to close the Gospel dispensation, glorify His saints, and judge the world."),
    ("Missions",
     "Free Will Baptists believe that Jesus commanded the church to go into all the world and preach the "
     "Gospel to every creature."),
]

def belief_slug(s):
    s = re.sub(r"&[a-z]+;", "", s)          # drop entities like &rsquo;
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


belief_rows = "\n".join(
    '      <h2 id="%s">%s</h2>\n      <p>%s</p>\n' % (belief_slug(t), t, b) for t, b in BELIEFS)

jump_items = "".join(
    '          <li><a href="#%s">%s</a></li>\n' % (belief_slug(t), t) for t, b in BELIEFS)

beliefs_body = """  <section>
    <div class="wrap wrap--narrow prose">
      <h1>What We Believe</h1>
      <p class="lede">East Side holds the doctrinal position of the <strong>National Association of Free
      Will Baptists</strong>. This page opens with the heart of it &mdash; the gospel, in plain words
      &mdash; and then sets out the fuller statement of what we teach and preach.</p>

      <nav class="jump" aria-label="Jump to a topic">
        <h2 class="jump__title">Jump to</h2>
        <ul>
          <li><a href="#the-gospel">The Gospel in short</a></li>
%(jump)s        </ul>
      </nav>

      <h2 id="the-gospel">The Gospel in short</h2>
      <p>God made everything, and He made it good. He made us in His own image, to know Him and to
      live with Him.</p>
      <p>We have all turned away from Him. Every one of us has done wrong, and done it knowing
      better. The Bible calls this sin, and sin separates us from God.</p>
      <p>God did not leave us there. He sent His Son, Jesus Christ, who lived the life we should
      have lived, died on a cross in our place, and rose from the dead three days later. Jesus took
      the penalty for our sin so that we would not have to.</p>
      <p>What God asks of us is repentance and faith &mdash; to admit our sin honestly, to turn from
      it, and to trust Jesus alone to save us. Salvation is God&rsquo;s gift, given by grace. It is not
      something we earn, and not something we can be good enough to deserve.</p>
      <p>Whoever comes to Him in that way is forgiven and received as God&rsquo;s own. You are not
      asked to tidy your life up first. If you would like to talk it over, please
      <a href="contact.html">get in touch</a>, or simply come to a service &mdash; someone would be
      glad to sit down with you.</p>

      <hr>

      <h2>What we teach and preach</h2>
      <p>What follows is the National Association&rsquo;s own summary of the Free Will Baptist
      position.</p>

      <blockquote>
        All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness.
        <cite>&mdash; 2 Timothy 3:16</cite>
      </blockquote>

%(rows)s
      <hr>
      <p><a class="btn" href="https://nafwb.org/site/treatise/">Read the full Free Will Baptist Treatise</a></p>
    </div>
  </section>
""" % dict(rows=belief_rows, jump=jump_items)

open(os.path.join(D, "beliefs.html"), "w", encoding="utf-8").write(render(
    "beliefs.html",
    "What We Believe &mdash; East Side Free Will Baptist Church",
    "The gospel in plain language, and the doctrinal position of East Side Free Will Baptist Church, Muldrow, Oklahoma, as held by the National Association of Free Will Baptists.",
    beliefs_body))
print("beliefs.html written")


# ----------------------------------------------------------------- ministries
ministries_body = """  <section>
    <div class="wrap">
      <h1>Ministries</h1>
      <p class="prose lede">There is a place here for every age, and a way for everyone to serve. Here
      is what actually goes on at East Side, week in and week out.</p>

      <h2 class="spaced">Children</h2>
      <div class="grid grid--loose">
        <article class="card">
          <p class="meta">Sunday</p>
          <h3>Children&rsquo;s Church</h3>
          <p>Children&rsquo;s church meets during the <strong>10:30 AM</strong> worship hour. Parents
          worship in the sanctuary while the children are taught at their own level.</p>
        </article>
        <article class="card">
          <p class="meta">Sunday</p>
          <h3>Sunday School for Children</h3>
          <p>Classes by age at <strong>9:30 AM</strong>, before the morning worship service.</p>
        </article>
      </div>

      <h2 class="spaced">Students</h2>
      <div class="grid grid--loose">
        <article class="card">
          <p class="meta">Wednesday</p>
          <h3>Youth Worship</h3>
          <p>Our youth meet on <strong>Wednesday evening at 7:00 PM</strong> at the
          <strong>Activities Center, %(act)s</strong> &mdash; the same hour as the midweek service, so
          families can come and go together.</p>
        </article>
      </div>

      <h2 class="spaced">Adults</h2>
      <div class="grid grid--loose">
        <article class="card">
          <p class="meta">Sunday</p>
          <h3>Sunday School</h3>
          <p>Classes for every age at <strong>9:30 AM</strong>, before the morning worship service.</p>
        </article>
        <article class="card">
          <p class="meta">Wednesday</p>
          <h3>Midweek Service</h3>
          <p>The church gathers on <strong>Wednesday at 7:00 PM</strong> for Bible study and prayer.</p>
        </article>
      </div>

      <h2 class="spaced">Care Ministries</h2>
      <div class="grid grid--loose">
        <article class="card">
          <p class="meta">All year</p>
          <h3>Nursing Home &amp; Shut-In Ministry</h3>
          <p>Associate Pastor Logan Williams leads this ministry on behalf of the church &mdash; nursing
          home services, hospital visits, and calls on members who can no longer come to us.</p>
          <p>It is how this congregation keeps faith with the people who have worshipped here for
          years, and it is work we take seriously.</p>
        </article>
      </div>

      <h2 class="spaced">Community Outreach</h2>
      <div class="grid grid--loose">
        <article class="card">
          <p class="meta">December</p>
          <h3>Tour of Christmas</h3>
          <p>Each December we open the Activities Center at %(act)s for our <strong>Tour of
          Christmas</strong> &mdash; a free evening of hayrides, live scenes depicting the life of Christ,
          hot chocolate and cookies, and a walk through Bethlehem. Everyone is welcome, and there is no
          charge.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="feature">
    <div class="wrap feature__wrap">
      <figure class="figure">
        <img src="%(img)s/open-bible.jpg" srcset="%(img)s/open-bible-640.jpg 640w, %(img)s/open-bible.jpg 1024w" sizes="(max-width: 46rem) 100vw, 45vw" alt="An open Bible on a table.">
      </figure>
      <div class="feature__text">
        <h2>Serving our neighbors</h2>
        <p>East Side has always been a community church as much as a Sunday church. Whether it is a meal
        for a family in a hard season, a ride to an appointment, or simply a visit to someone who has not
        been able to get out, this is work our people do without being asked.</p>
        <p>If you know of a need we should hear about, <a href="contact.html">tell us</a>.</p>
      </div>
    </div>
  </section>
""" % dict(act=ACT, tel=TEL, teld=TELD, img=IMG)

# Keep this draft unpublished until Logan approves its revised copy.
SHOW_SERVING_NEIGHBORS = False
if not SHOW_SERVING_NEIGHBORS:
    ministries_body = re.sub(r'\s*<section class="feature">.*?</section>', '', ministries_body, count=1, flags=re.S)

open(os.path.join(D, "ministries.html"), "w", encoding="utf-8").write(render(
    "ministries.html",
    "Ministries &mdash; East Side Free Will Baptist Church",
    "Sunday school, children's church, midweek service, youth worship, and the nursing home and shut-in ministry at East Side Free Will Baptist Church.",
    ministries_body))
print("ministries.html written")


# ----------------------------------------------------------------- calendar
# The church's own October-December 2026 calendar sheet, transcribed. Each
# month is a list of (day, [(time, title), ...]) in the order the sheet lists
# them. To update, edit this table and re-run the generator - never the HTML.
# Times the sheet left blank are recorded as None and simply omit the time.
MONTH_NUM = {"October": 10, "November": 11, "December": 12}

CHURCH_CALENDAR = [
    ("October 2026", [
        (1,  [("6:30&ndash;8:00 PM", "GriefShare in the Fellowship Hall")]),
        (4,  [(None,      "Vision Fund Sunday")]),
        (6,  [("10:00 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (7,  [(None,      "Bro. Trenton devotion at youth services"),
              ("7:00 PM",  "WAC"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (8,  [("6:30&ndash;8:00 PM", "GriefShare in the Fellowship Hall")]),
        (11, [("6:00 PM",  "PM service")]),
        (12, [(None,      "Ministers&rsquo; Retreat at Wewoka, Oklahoma (continues through the 14th)"),
              (None,      "Columbus Day / Indigenous Peoples&rsquo; Day")]),
        (13, [("10:00 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (14, [(None,      "Ministers&rsquo; Retreat at Wewoka, Oklahoma"),
              ("7:00 PM",  "Flanna Hills Nursing Home service"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (15, [("6:30&ndash;8:00 PM", "GriefShare in the Fellowship Hall"),
              (None,      "Muldrow Schools &mdash; no school (professional development day)")]),
        (16, [(None,      "Muldrow Schools &mdash; no school (fall break)")]),
        (20, [("10:00 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (21, [("7:00 PM",  "WAC"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (22, [("6:30&ndash;8:00 PM", "GriefShare in the Fellowship Hall")]),
        (23, [(None,      "East Side feeds the football and cheer squads (75)")]),
        (25, [(None,      "WAC &ldquo;Dollar Days for Missions&rdquo; offering"),
              (None,      "Family &ldquo;All-in-One&rdquo; worship"),
              (None,      "CAMO Sunday"),
              (None,      "Fall Festival at Ryan Barn")]),
        (27, [("10:00 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (28, [("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (29, [("6:30&ndash;8:00 PM", "GriefShare in the Fellowship Hall")]),
        (31, [(None,      "Halloween")]),
    ]),
    ("November 2026", [
        (1,  [(None,      "Vision Fund Sunday")]),
        (3,  [("10:00 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (4,  [("7:00 PM",  "WAC"),
              ("7:00 PM",  "Bro. Trenton devotion at youth services"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (5,  [("6:30&ndash;8:00 PM", "GriefShare in the Fellowship Hall")]),
        (8,  [("6:00 PM",  "PM services")]),
        (10, [("10:00 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (11, [("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (12, [("6:30&ndash;8:00 PM", "GriefShare in the Fellowship Hall &mdash; extra date if needed")]),
        (17, [("10:00 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (18, [("7:00 PM",  "WAC"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (22, [(None,      "WAC &ldquo;Dollar Days for Missions&rdquo; offering"),
              ("6:00 PM",  "Community Thanksgiving service")]),
        (23, [(None,      "Muldrow Schools &mdash; no school (Thanksgiving week)")]),
        (24, [("6:30 PM",  "BATTL"),
              (None,      "Muldrow Schools &mdash; no school (Thanksgiving week)")]),
        (25, [(None,      "No PM services"),
              (None,      "Muldrow Schools &mdash; no school (Thanksgiving week)")]),
        (26, [(None,      "Thanksgiving"),
              (None,      "Muldrow Schools &mdash; no school (Thanksgiving week)")]),
        (27, [(None,      "Muldrow Schools &mdash; no school (Thanksgiving week)")]),
        (29, [(None,      "Family &ldquo;All-in-One&rdquo; worship")]),
    ]),
    ("December 2026", [
        (1,  [("10:30 AM", "WWBS"),
              ("6:30 PM",  "BATIL")]),
        (2,  [("7:00 PM",  "TOC Walk-Through"),
              (None,      "No services")]),
        (5,  [("6:30&ndash;8:30", "Tour of Christmas at the Activities Center (tentative)")]),
        (6,  [(None,      "Vision Fund Sunday"),
              ("6:30&ndash;8:30", "Tour of Christmas at the Activities Center (tentative)")]),
        (8,  [("10:30 AM", "WWBS"),
              ("6:30 PM",  "BATIL")]),
        (9,  [("10:30", "Fianna Hills Nursing Home service")]),
        (13, [("6:00 PM",  "PM services")]),
        (15, [("10:30 AM", "WWBS"),
              ("6:30 PM",  "BATIL")]),
        (16, [("7:00 PM",  "WAC"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (19, [(None,      "Activities Center booked")]),
        (21, [(None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27")]),
        (22, [("6:30 PM",  "BATIL"),
              (None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27")]),
        (23, [(None,      "Services &mdash; to be announced"),
              (None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27")]),
        (24, [(None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27"),
              (None,      "Christmas Eve")]),
        (25, [(None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27"),
              (None,      "Christmas Day")]),
        (27, [(None,      "Family &ldquo;All-in-One&rdquo; worship service"),
              (None,      "WAC &ldquo;Dollar Days for Missions&rdquo; offering"),
              ("6:00 PM", "PM services")]),
        (28, [(None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27")]),
        (29, [("6:30 PM",  "BATIL"),
              (None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27")]),
        (30, [("7:00 PM", "Men&rsquo;s Bible Study"),
              (None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27")]),
        (31, [(None,      "Muldrow Schools Christmas Break 12/21/26-1/1/27"),
              (None,      "New Year&rsquo;s Eve")]),
    ]),
]

def cal_month_html(month, year, entries):
    """Render one month of the church calendar as a traditional month grid.

    Seven columns, Sunday first, with the events for each day inside its own
    cell. The day number is real text in a row-scoped cell position so screen
    readers and search engines both get a usable date out of it.
    """
    first = month.split()[0]
    mnum = MONTH_NUM[first]
    by_day = dict(entries)

    # Monday=0 .. Sunday=6 in datetime, but the grid starts on Sunday.
    lead = (datetime.date(year, mnum, 1).weekday() + 1) % 7
    ndays = calendar.monthrange(year, mnum)[1]

    out = ['    <div class="cal-month">',
           '      <h3 class="cal-month__name">%s</h3>' % month,
           '      <div class="cal-scroll" tabindex="0" role="region"',
           '           aria-label="%s %d month grid, scrolls sideways">' % (month, year),
           '      <table class="cal-grid">',
           '        <caption class="visually-hidden">%s %d</caption>' % (month, year),
           '        <thead>',
           '          <tr>']
    for dname in ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"):
        out.append('            <th scope="col" class="cal-grid__wd"><abbr title="%s">%s</abbr></th>'
                   % (dname, dname))
    out += ['          </tr>',
            '        </thead>',
            '        <tbody>']

    cells = ([None] * lead) + list(range(1, ndays + 1))
    while len(cells) % 7:
        cells.append(None)

    for wk in range(0, len(cells), 7):
        out.append('          <tr>')
        for day in cells[wk:wk + 7]:
            if day is None:
                out.append('            <td class="cal-cell cal-cell--empty"></td>')
                continue
            items = by_day.get(day, [])
            date = datetime.date(year, mnum, day)
            longname = "%s %s %d, %d" % (date.strftime("%A"), month.split()[0],
                                         day, year)
            cls = "cal-cell"
            if items:
                cls += " cal-cell--busy"
            out.append('            <td class="%s">' % cls)
            out.append('              <span class="visually-hidden">%s</span>' % longname)
            out.append('              <span class="cal-cell__day" aria-hidden="true">'
                       '<span class="cal-cell__num" data-weekday="%s">%d</span></span>'
                       % (date.strftime("%A"), day))
            if items:
                out.append('              <ul class="cal-cell__events">')
                for time, title in items:
                    if time:
                        out.append('                <li><span class="cal-cell__time">%s</span>%s</li>'
                                   % (time, title))
                    else:
                        out.append('                <li>%s</li>' % title)
                out.append('              </ul>')
            out.append('            </td>')
        out.append('          </tr>')

    out += ['        </tbody>',
            '      </table>',
            '      </div>',
            '    </div>']
    return "\n".join(out)


cal_sections = "\n".join(
    cal_month_html(m, 2026, e) for m, e in CHURCH_CALENDAR)

calendar_body = """  <section>
    <div class="wrap">
      <h1>Calendar</h1>
      <p class="prose lede">What is on at East Side for the next three months &mdash; services, studies,
      mission offerings, retreats, and the school-calendar dates families ask about most.</p>

      <h2 class="spaced">Every week at East Side</h2>
      <div class="callout">
        <p><strong>Sunday</strong> &mdash; Sunday School 9:30 AM &middot; Morning Worship 10:30 AM
        (children&rsquo;s church at the same hour)<br>
        <strong>Wednesday</strong> &mdash; Midweek service 7:00 PM &middot; Youth worship 7:00 PM at the
        Activities Center, %(act)s</p>
      </div>

      <h2 class="spaced">October, November, and December 2026</h2>
%(cal)s

      <p class="fine-print">A few entries on the church calendar carry no time listed; those show the
      event only. Dates and times can shift &mdash; call the church at <a href="%(tel)s">%(teld)s</a>
      if you are coming to something and want to be sure.</p>

      <h2 class="spaced">What you will find on the calendar</h2>
      <ul class="prose">
        <li>Regular services, studies, and ministry meetings</li>
        <li>Youth events at the Activities Center</li>
        <li>Mission offerings, revivals, and special services</li>
        <li>School closures and holidays that change the normal week</li>
      </ul>

      <h2>Coming to something?</h2>
      <p class="prose">You do not need to tell us you are coming, and you will not be singled out. If you
      would like someone to look out for you, call the church at <a href="%(tel)s">%(teld)s</a> and we
      will make sure you are expected.</p>
    </div>
  </section>
""" % dict(act=ACT, tel=TEL, teld=TELD, cal=cal_sections)

open(os.path.join(D, "calendar.html"), "w", encoding="utf-8").write(render(
    "calendar.html",
    "Calendar &mdash; East Side Free Will Baptist Church",
    "Services, studies, mission offerings, retreats, and school dates for the next three months at East Side Free Will Baptist Church, Muldrow, Oklahoma.",
    calendar_body))
print("calendar.html written")


# ------------------------------------------------------------- study material
# "Study Material" is the shelf. Sermons and devotions are what sits on it, each
# with a page of its own, so the section can grow without the menu growing with it.
study_body = """  <section>
    <div class="wrap">
      <h1>Study Material</h1>
      <p class="prose lede">Two things live here: the messages preached from this pulpit, and
      devotional writing to read through the week. Both are meant to be sat with rather than
      skimmed.</p>

      <div class="grid grid--loose">
        <article class="card card--study">
          <p class="meta">To watch</p>
          <h2>Sermons</h2>
          <p>Our Sunday morning services are streamed live and kept on our Facebook page, so you can
          watch a service you missed or hear a message a second time.</p>
          <p><a class="btn" href="sermons.html">Go to the sermons</a></p>
        </article>
        <article class="card card--study">
          <p class="meta">To read</p>
          <h2>Devotions</h2>
          <p>Short devotional writings on the Scriptures &mdash; a passage opened up, and a thought
          to carry into the week. New ones are added as they are written.</p>
          <p><a class="btn" href="devotions.html">Go to the devotions</a></p>
        </article>
      </div>
    </div>
  </section>

  <section class="band">
    <img src="assets/img/stained-glass.jpg" srcset="assets/img/stained-glass-640.jpg 640w, assets/img/stained-glass.jpg 1024w" sizes="100vw" alt="" aria-hidden="true">
    <div class="wrap wrap--narrow">
      <blockquote class="band__quote">
        All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness.
        <cite>&mdash; 2 Timothy 3:16</cite>
      </blockquote>
    </div>
  </section>
"""

open(os.path.join(D, "study-material.html"), "w", encoding="utf-8").write(render(
    "study-material.html",
    "Study Material &mdash; East Side Free Will Baptist Church",
    "Sermons to watch and devotions to read from East Side Free Will Baptist Church, Muldrow, Oklahoma.",
    study_body))
print("study-material.html written")


# ----------------------------------------------------------------- sermons
sermons_body = """  <section>
    <div class="wrap">
      <nav class="subnav" aria-label="Study Material">
        <p><a href="study-material.html">Study Material</a> <span aria-hidden="true">&rsaquo;</span> Sermons</p>
      </nav>

      <h1>Sermons</h1>
      <p class="prose lede">Every Sunday morning service is streamed live, and every message is kept on
      our Facebook page afterwards. If you missed a Sunday, or want to hear something again, it is
      there.</p>

      <h2 class="spaced">Watch a service</h2>
      <div class="callout">
        <p>We stream the Sunday morning service live each week at <strong>10:30 AM</strong>. Pastor
        Anthony Williams preaches from the Bible, and the service runs about an hour.</p>
        <p><a class="btn" href="%(fb)s">Watch on Facebook &rarr;</a></p>
      </div>

      <h2 class="spaced">The most recent service</h2>
      <p class="prose">Our newest messages sit at the top of our Facebook page, so the first thing you
      see there is always the most recent Sunday. Earlier services are in the same place, a little
      further down.</p>

      <h2 class="spaced">Finding a particular message</h2>
      <ul class="prose">
        <li>Open our <a href="%(fb)s">Facebook page</a> and choose <strong>Videos</strong>.</li>
        <li>Services are listed newest first.</li>
        <li>Sunday messages are also posted to the page as they go up, so the page itself is a useful
        record.</li>
      </ul>

      <h2 class="spaced">A searchable archive</h2>
      <p class="prose">Facebook is good for watching and poor for searching. So we are building a simple
      archive onto this page &mdash; each message listed with its title, the date it was preached, the
      speaker, and the Scripture passage, so that a series through a book of the Bible can be followed
      in order. It will appear below as it is filled in.</p>

      <p class="prose">As messages are made available to us, they will also be posted here to watch
      without leaving the site, so that this page becomes a place you can come back to.</p>

      <!-- ===================================================================
           SERMON ARCHIVE

           To add a message, copy this block into the list below and fill it in.
           Keep the newest at the top. A plain <table> also works if you prefer,
           but the list below stays readable on a phone.

           Once a message has a video of its own (YouTube or Facebook), give it an
           <a href="...">Watch</a> link here, or replace the link with an embed:

           <li>
             <strong>Title of the message</strong>
             <span>Preached 4 January 2026 &middot; Pastor Anthony Williams &middot; John 3:16&ndash;21</span>
             <div class="video-embed">
               <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="Title of the message" loading="lazy" allowfullscreen></iframe>
             </div>
           </li>

           =================================================================== -->
      <div class="callout callout--quiet" id="archive">
        <p>The archive is being filled in. In the meantime, every message is on our
        <a href="%(fb)s">Facebook page</a>, and we are glad to point you to a particular one &mdash;
        just ask.</p>
      </div>

      <h2 class="spaced">Need a message you cannot find?</h2>
      <p class="prose">Call the church at <a href="%(tel)s">%(teld)s</a>, or email
      <a href="mailto:%(email)s">%(email)s</a>, and we will help you find it.</p>
    </div>
  </section>
""" % dict(fb=FB, tel=TEL, teld=TELD, email=EMAIL)

open(os.path.join(D, "sermons.html"), "w", encoding="utf-8").write(render(
    "sermons.html",
    "Sermons &mdash; East Side Free Will Baptist Church",
    "Listen to recent sermons and watch the Sunday livestream from East Side Free Will Baptist Church, Muldrow, Oklahoma.",
    sermons_body))
print("sermons.html written")


# ----------------------------------------------------------------- devotions
# The devotion blog: one page per devotion, generated from the list below.
#
# TO ADD A DEVOTION: copy one whole { ... } entry and fill in the fields. Order
# does not matter - pages are sorted by date, newest first. The Devotions index,
# each page and the sitemap are all rebuilt from this list.
#
#   slug       file name, no spaces:  devotions/<slug>.html
#   title      the devotion's title
#   date       ISO date, "2026-10-07" - used for ordering and the sitemap
#   label      how the date reads, "October 7, 2026"
#   author     the byline
#   scripture  the passage line shown under the title
#   summary    one or two sentences for the Devotions index
#   refs       the passages used, listed at the foot of the page
#   image      optional (file in assets/img, alt text)
#   video      optional YouTube video id, e.g. "aBcDeFgHiJk". Leave it out until
#              a devotion has been recorded and uploaded; the embed then appears
#              at the top of the article.
#   body       the article itself, as HTML

DEVOTIONS = [
    {
        "slug": "why-do-we-study-the-scriptures",
        "title": "Why Do We Study the Scriptures?",
        "date": "2026-10-07",
        "label": "October 7, 2026",
        "author": "Bro. Logan Williams",
        "scripture": "2 Timothy 3:14&ndash;17",
        "summary": "Before we begin reading together, it is worth asking why. Three reasons God gives us His Word: that many might be saved, that the saved might be made like His Son, and that He might be glorified in us.",
        "refs": [
            "2 Timothy 3:15, 16, 17", "2 Peter 1:21", "John 20:31", "Romans 10:17",
            "1 Peter 1:23", "1 Thessalonians 2:13", "Romans 8:29", "2 Corinthians 3:18",
            "John 17:17", "Psalm 119:11", "Psalm 119:18", "Hebrews 4:12",
            "James 1:22&ndash;24", "John 17:1, 5", "John 15:8", "Philippians 1:11",
            "2 Thessalonians 1:12", "1 Corinthians 10:31", "Acts 17:11",
        ],
        "image": ("open-bible.jpg", "An open Bible resting outdoors."),
        # "video": "YOUTUBE_VIDEO_ID",   # uncomment once the devotion is recorded
        "body": """<p class="lede">Why do we do it? Why will we be spending time together here, week by
      week, in the Scriptures? It is a fair question to ask at the start of anything new, and it
      deserves an honest answer.</p>

      <p>I will tell you plainly that I do not open my Bible because I am, by nature, a disciplined
      man. Left to myself I can find a dozen easier things to do with an evening. I open it because I
      have become convinced that the Bible is not a book like other books, and that God has said
      quite specifically what He intends it to do. So before we talk about how to study, let us begin
      where the Bible begins: with what God says His Word is for.</p>

      <p>There are three reasons, and they build on one another.</p>

      <h2>1. God gave us His Word so that many might be saved</h2>

      <p>Start with God&rsquo;s intention in giving it at all. Paul, writing near the end of his life
      to a young man he had trained in the faith, put it this way:</p>

      <blockquote>
        And that from a child thou hast known the holy scriptures, which are able to make thee wise
        unto salvation through faith which is in Christ Jesus.
        <cite>&mdash; 2 Timothy 3:15</cite>
      </blockquote>

      <p>Note the purpose. The Scriptures are <em>able to make a person wise unto salvation</em>. God
      did not give us a book to satisfy our curiosity, or to sharpen our arguing, or to make us look
      thoughtful on a Sunday. He gave us a book that saves &mdash; and He gave it that way on
      purpose, so that many would be saved and not a select few.</p>

      <p>That is why He did not leave the writing of it to men&rsquo;s own devices:</p>

      <blockquote>
        All scripture is given by inspiration of God, and is profitable for doctrine, for reproof,
        for correction, for instruction in righteousness.
        <cite>&mdash; 2 Timothy 3:16</cite>
      </blockquote>

      <blockquote>
        For the prophecy came not in old time by the will of man: but holy men of God spake as they
        were moved by the Holy Ghost.
        <cite>&mdash; 2 Peter 1:21</cite>
      </blockquote>

      <p>Moses and David, Isaiah and Jeremiah, Matthew and John, Peter and Paul &mdash; real men, in
      real places, writing in their own voices out of their own lives. And behind every one of them,
      the Spirit of God, carrying them along so that what they wrote was exactly what God meant to
      say. That is what <em>inspired</em> means: God-breathed. When we open the Bible, then, we are
      not reading men&rsquo;s opinions about God. We are listening to God.</p>

      <p>John tells us why he wrote his Gospel down at all:</p>

      <blockquote>
        But these are written, that ye might believe that Jesus is the Christ, the Son of God; and
        that believing ye might have life through his name.
        <cite>&mdash; John 20:31</cite>
      </blockquote>

      <p>And Paul tells us how that believing comes about:</p>

      <blockquote>
        So then faith cometh by hearing, and hearing by the word of God.
        <cite>&mdash; Romans 10:17</cite>
      </blockquote>

      <p>Peter says we are born again &ldquo;by the word of God, which liveth and abideth for
      ever&rdquo; (1 Peter 1:23). Paul thanked God that the Thessalonians received what he preached
      &ldquo;not as the word of men, but as it is in truth, the word of God, which effectually
      worketh also in you that believe&rdquo; (1 Thessalonians 2:13). <em>It effectually worketh.</em>
      The Word does something. It does not merely inform; it acts.</p>

      <p>That has a consequence for us as a church, and it is not a small one. If God saves people
      through His Word, then a church full of people who know their Bibles is a church full of people
      through whom God can work. The gospel you carry into a hospital room, into a nursing home, into
      a hard conversation at a kitchen table, is the same gospel that turned you around. Learning the
      Scriptures is not a private hobby for the unusually studious. It is how we come to have
      something worth giving away.</p>

      <h2>2. God desires that those who are saved become more like His Son</h2>

      <p>But salvation is not the end of God&rsquo;s purpose for us &mdash; it is the beginning. Paul
      says in Romans:</p>

      <blockquote>
        For whom he did foreknow, he also did predestinate to be conformed to the image of his Son,
        that he might be the firstborn among many brethren.
        <cite>&mdash; Romans 8:29</cite>
      </blockquote>

      <p><em>Conformed to the image of his Son.</em> That is the shape God intends your life and mine
      to take. Not merely forgiven and left as we were, but remade &mdash; until what we love, and
      how we spend our money, and how we speak to our families, and how we treat the person who can
      do nothing for us in return, begin to look like Jesus.</p>

      <p>So how does that happen? Paul answers that too:</p>

      <blockquote>
        But we all, with open face beholding as in a glass the glory of the Lord, are changed into
        the same image from glory to glory, even as by the Spirit of the Lord.
        <cite>&mdash; 2 Corinthians 3:18</cite>
      </blockquote>

      <p>Beholding, and changed. That is the order, and it never reverses. We do not become like
      Christ by gritting our teeth; we look at Him, and the Spirit does the changing. And where do we
      look at Him? In the Word. The Bible is the glass in which we see the glory of the Lord, and the
      one who keeps looking comes away different.</p>

      <p>This is why Jesus prayed for His own, &ldquo;Sanctify them through thy truth: thy word is
      truth&rdquo; (John 17:17). And it is why the psalmist wrote, &ldquo;Thy word have I hid in mine
      heart, that I might not sin against thee&rdquo; (Psalm 119:11) &mdash; not on the shelf, not
      only in a notebook, but in the heart, where it can do its work on an ordinary Tuesday
      afternoon.</p>

      <p>The Bible is honest about how much this can cost. It says of itself:</p>

      <blockquote>
        For the word of God is quick, and powerful, and sharper than any twoedged sword, piercing
        even to the dividing asunder of soul and spirit, and of the joints and marrow, and is a
        discerner of the thoughts and intents of the heart.
        <cite>&mdash; Hebrews 4:12</cite>
      </blockquote>

      <p>Which means our study will sometimes be uncomfortable. Scripture does not flatter us. Of the
      four things Paul says the Word is profitable for &mdash; doctrine, reproof, correction,
      instruction in righteousness &mdash; two of them are things we would rather not be told. But he
      gives the reason for all of it: &ldquo;That the man of God may be perfect, throughly furnished
      unto all good works&rdquo; (2 Timothy 3:17). God corrects what He loves.</p>

      <p>James warns us against a study that never reaches our hands:</p>

      <blockquote>
        But be ye doers of the word, and not hearers only, deceiving your own selves. For if any be a
        hearer of the word, and not a doer, he is like unto a man beholding his natural face in a
        glass: For he beholdeth himself, and goeth his way, and straightway forgetteth what manner of
        man he was.
        <cite>&mdash; James 1:22&ndash;24</cite>
      </blockquote>

      <p>So we do not read in order to collect information. We read in order to be made over &mdash;
      which means reading with a willingness to be told to change.</p>

      <h2>3. God seeks to be glorified, with His Son, through us</h2>

      <p>There is a third reason, and it takes us outside ourselves altogether. On the night He was
      betrayed, Jesus prayed:</p>

      <blockquote>
        Father, the hour is come; glorify thy Son, that thy Son also may glorify thee &hellip; And
        now, O Father, glorify thou me with thine own self with the glory which I had with thee
        before the world was.
        <cite>&mdash; John 17:1, 5</cite>
      </blockquote>

      <p>Father and Son, giving glory to one another from before the world was made. And by grace,
      that glory is meant to move through us. Jesus said, &ldquo;Herein is my Father glorified, that
      ye bear much fruit&rdquo; (John 15:8). Paul prayed that the Philippians would be
      &ldquo;filled with the fruits of righteousness, which are by Jesus Christ, unto the glory and
      praise of God&rdquo; (Philippians 1:11), and that &ldquo;the name of our Lord Jesus Christ may
      be glorified in you, and ye in him&rdquo; (2 Thessalonians 1:12).</p>

      <p>The end of all our studying, then, is not a well-informed congregation. It is a
      God-glorifying one &mdash; a people in whom the worth of Christ is visible in the ordinary
      business of a week: in patience with a difficult child, in honesty in a day&rsquo;s work, in
      the way a long illness is carried, in kindness to someone who will never be able to repay it.
      &ldquo;Whether therefore ye eat, or drink, or whatsoever ye do, do all to the glory of
      God&rdquo; (1 Corinthians 10:31).</p>

      <p>Put the three together and you have the answer to our opening question. God gave us His Word
      so that many might be saved. He gave it so that the saved might be made like His Son. And He
      gave it so that He and His Son might be glorified in us. Bible study is not an extra for the
      especially serious. It is where the Christian life is fed.</p>

      <h2>How, then, should we read?</h2>

      <p>A few plain things &mdash; not rules, but habits.</p>

      <div class="callout">
        <p><strong>Read a passage, not a fragment.</strong> A verse lifted out of its chapter can be
        made to say almost anything. Give yourself at least a paragraph, and ask what the writer is
        doing with it.</p>
        <p><strong>Ask two questions.</strong> What does this show me about God, and about Christ?
        And what does it ask of me? Answer those two and you have not wasted the time.</p>
        <p><strong>Pray before you begin.</strong> David&rsquo;s prayer is a good one to make your
        own: &ldquo;Open thou mine eyes, that I may behold wondrous things out of thy law&rdquo;
        (Psalm 119:18).</p>
        <p><strong>Small and steady beats long and rare.</strong> Fifteen minutes most days will do
        more in a year than a three-hour session in January.</p>
        <p><strong>Do not do it alone.</strong> Wednesday evening at 7:00 and Sunday school at 9:30
        are where we read together and ask one another what we are finding.</p>
      </div>

      <p>Scripture holds up the Bereans as an example for exactly this: &ldquo;they received the word
      with all readiness of mind, and searched the scriptures daily, whether those things were
      so&rdquo; (Acts 17:11). Ready to hear, and willing to check. That is the posture I hope we will
      keep here.</p>

      <p>So that is where I hope our time together in these devotions will go. Not a place to come
      and be impressive, and not a place to be lectured at &mdash; a place to open the Word, look at
      it carefully, and let it do what God said it would do. I am glad to have you reading along, and
      I am looking forward to it.</p>

      <p>May the Lord give us ears to hear.</p>""",
    },
]

DEV = sorted(DEVOTIONS, key=lambda d: d["date"], reverse=True)

DEVOTIONS_DIR = os.path.join(D, "devotions")
os.makedirs(DEVOTIONS_DIR, exist_ok=True)


def devotion_items():
    rows = []
    for d in DEV:
        href = "devotions/%s.html" % d["slug"]
        rows.append("""        <li class="devotion-item">
          <p class="devotion-meta">%(label)s &middot; %(author)s</p>
          <h3><a href="%(href)s">%(title)s</a></h3>
          <p class="devotion-scripture">%(scripture)s</p>
          <p>%(summary)s</p>
          <p><a href="%(href)s">Read the devotion &rarr;</a></p>
        </li>""" % dict(label=d["label"], author=d["author"], href=href,
                        title=d["title"], scripture=d["scripture"], summary=d["summary"]))
    return "\n".join(rows)


devotions_body = """  <section>
    <div class="wrap">
      <nav class="subnav" aria-label="Study Material">
        <p><a href="study-material.html">Study Material</a> <span aria-hidden="true">&rsaquo;</span> Devotions</p>
      </nav>

      <h1>Devotions</h1>
      <p class="prose lede">Devotional writing from East Side &mdash; a passage of Scripture opened
      up, and a thought to carry into the week. These are written to be read slowly, and read again.</p>

      <h2 class="spaced">All devotions</h2>
      <ul class="devotion-list">
%(items)s
      </ul>

      <div class="callout callout--quiet">
        <p>New devotions are added here as they are written.</p>
      </div>
    </div>
  </section>
""" % dict(items=devotion_items(), fb=FB)

open(os.path.join(D, "devotions.html"), "w", encoding="utf-8").write(render(
    "devotions.html",
    "Devotions &mdash; East Side Free Will Baptist Church",
    "Devotional writings from East Side Free Will Baptist Church, Muldrow, Oklahoma: a passage of Scripture opened up, and a thought to carry into the week.",
    devotions_body))
print("devotions.html written (%d devotion(s))" % len(DEV))


# One page per devotion, under devotions/. Those pages sit a level down, so every
# link and asset they carry is written with a ../ prefix.
def devotion_article(d):
    figure = ""
    if d.get("image"):
        f, alt = d["image"]
        figure = ("""      <figure class="figure devotion__figure">
        <img src="../assets/img/%(f)s" srcset="../assets/img/%(stem)s-640.jpg 640w, ../assets/img/%(f)s 1024w" sizes="(max-width: 46rem) 100vw, 40rem" alt="%(alt)s">
      </figure>
""" % dict(f=f, stem=f[:-4], alt=alt))

    video = ""
    if d.get("video"):
        video = ("""        <div class="video-embed">
          <iframe src="https://www.youtube-nocookie.com/embed/%(v)s" title="%(t)s" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
""" % dict(v=d["video"], t=d["title"].replace('"', "&quot;")))

    refs = "\n".join("        <li>%s</li>" % r for r in d["refs"])

    return """  <article class="devotion">
    <div class="wrap wrap--narrow">
      <nav class="subnav" aria-label="Study Material">
        <p><a href="../study-material.html">Study Material</a> <span aria-hidden="true">&rsaquo;</span> <a href="../devotions.html">Devotions</a> <span aria-hidden="true">&rsaquo;</span> %(title)s</p>
      </nav>

      <header class="devotion__head">
        <p class="meta">%(label)s &middot; %(author)s</p>
        <h1>%(title)s</h1>
        <p class="devotion__scripture">%(scripture)s</p>
      </header>

%(figure)s      <div class="prose devotion__body">
%(video)s%(text)s
      </div>

      <hr>

      <h2>Scriptures in this devotion</h2>
      <ul class="ref-list">
%(refs)s
      </ul>

      <p><a class="btn" href="../devotions.html">All devotions</a></p>
    </div>
  </article>
""" % dict(title=d["title"], label=d["label"], author=d["author"], scripture=d["scripture"],
           figure=figure, video=video, text=d["body"], refs=refs)


for d in DEV:
    open(os.path.join(DEVOTIONS_DIR, d["slug"] + ".html"), "w", encoding="utf-8").write(render(
        "devotions/%s.html" % d["slug"],
        "%s &mdash; Devotions &mdash; East Side Free Will Baptist Church" % d["title"],
        d["summary"],
        devotion_article(d),
        base="../"))
print("devotions/ written (%d page(s))" % len(DEV))


# ----------------------------------------------------------------- give
give_body = """  <section>
    <div class="wrap wrap--narrow prose">
      <h1>Give</h1>
      <p class="lede">Everything we do is funded by the willing generosity of this congregation &mdash;
      the preaching of the Word, the ministry to our children, and the care we carry to the sick, the
      shut-in, and the grieving.</p>

      <h2>Current fundraising goals</h2>

      <p class="lede">The Vision Fund and the Chair Fund are both moving forward. Here is where we stand
      and where we are headed.</p>

      <h3>Final Construction Phase Push</h3>
      <p class="callout">The Vision Fund is running through December 2026 as we push through the final
      construction phase of the new worship and ministry center. God is faithful to the promises He
      makes to those who trust in Him, and He is faithful to the hands that sow. Every dollar given is an
      act of faith in the work He is building.</p>

      <div class="give-goal">
        <div class="give-goal__figures">
          <div class="give-goal__item give-goal__item--total">
            <span class="give-goal__label">Goal</span>
            <span class="give-goal__amount">$200,000</span>
          </div>
          <div class="give-goal__item">
            <span class="give-goal__label">Raised so far</span>
            <span class="give-goal__amount">$75,892</span>
          </div>
        </div>
        <div class="give-goal__bar">
          <span class="give-goal__fill" style="width: 37.9%%"></span>
        </div>
        <p class="give-goal__pct">37.9%% of our $200,000 goal &mdash; through December 2026</p>
      </div>

      <p><a class="btn" href="%(vision_url)s">Give to the Vision Fund</a></p>

      <h3>Chair Fund</h3>
      <p>The Chair Fund is the fund we use for the needs the church sees first. Every dollar goes
      directly to the work it is given for, and we are grateful to everyone who has helped us get
      this far.</p>

      <div class="give-goal">
        <div class="give-goal__figures">
          <div class="give-goal__item give-goal__item--total">
            <span class="give-goal__label">Goal</span>
            <span class="give-goal__amount">$21,964.87</span>
          </div>
          <div class="give-goal__item">
            <span class="give-goal__label">Raised so far</span>
            <span class="give-goal__amount">$11,649.14</span>
          </div>
        </div>
        <div class="give-goal__bar">
          <span class="give-goal__fill" style="width: 53.0%%"></span>
        </div>
        <p class="give-goal__pct">53%% of our $21,964.87 goal</p>
      </div>

      <p><a class="btn" href="%(chair_url)s">Give to the Chair Fund</a></p>
    </div>
  </section>

  <section id="where-giving-goes">
    <div class="wrap wrap--narrow prose">
      <h2>Where your giving goes</h2>
      <p>Your giving supports the ministry of East Side here in Muldrow and helps carry the gospel
      beyond our own congregation. East Side gives through the Free Will Baptist Cooperative Plan
      (COOP), joining other churches to support ministry in Oklahoma, across North America, and around the world.</p>

      <h3>Here in Oklahoma</h3>
      <p>The Oklahoma Cooperative Plan supports the state Executive Board, Randall University,
      the Mission Board, and the Christian Education Board, and sends a portion to the National
      Association of Free Will Baptists.<sup><a href="#giving-source-1" aria-label="Source 1">[1]</a></sup>
      This includes Christian higher education at Randall and the Christian Education Board&rsquo;s
      work in training, education, fellowship, and evangelism.<sup><a href="#giving-source-2" aria-label="Source 2">[2]</a></sup></p>

      <h3>Across the nation and around the world</h3>
      <p>Through national cooperative giving, we also help support these Free Will Baptist ministries
      and programs.<sup><a href="#giving-source-3" aria-label="Source 3">[3]</a></sup><sup><a href="#giving-source-4" aria-label="Source 4">[4]</a></sup></p>
      <ul>
        <li><strong>International missions</strong> &mdash; IM, Inc., supporting cross-cultural gospel
        ministry, discipleship, church planting, and leadership training around the world.</li>
        <li><strong>North American Ministries</strong> &mdash; church planting, discipleship, and
        chaplain ministry, including service to members of the armed forces.</li>
        <li><strong>Christian education and family discipleship</strong> &mdash; Welch College and
        D6 Family Ministry, including curriculum, books, conferences, and youth programs such as Vertical Three.</li>
        <li><strong>Women&rsquo;s ministry</strong> &mdash; WNAC, equipping women to serve Christ
        at home and abroad.</li>
        <li><strong>Stewardship and retirement support</strong> &mdash; Free Will Baptist Foundation
        and Richland Ave Financial (the denomination&rsquo;s retirement ministry).</li>
        <li><strong>Shared denominational ministry</strong> &mdash; the Executive Office and the
        Commission for Theological Integrity, Historical Commission, Media Commission, and Music Commission.</li>
      </ul>
      <p>By giving together, our church shares in work that reaches far beyond what one congregation
      could do alone.</p>
      <div class="fine-print">
        <p><strong>Sources:</strong> Learn more from the official state and national ministry information:</p>
        <ul>
          <li id="giving-source-1">[1] <a href="https://www.okfwb.org/okfwb-boards">Oklahoma COOP allocations</a></li>
          <li id="giving-source-2">[2] <a href="https://www.okfwb.org/okfwb-links">Oklahoma ministry information</a></li>
          <li id="giving-source-3">[3] <a href="https://nafwb.org/site/wp-content/uploads/2025/06/25-TOG-Way-Flyer.pdf">The Together Way giving plan (PDF)</a></li>
          <li id="giving-source-4">[4] <a href="https://nafwb.org/site/links/departments-agencies/">National departments and commissions</a></li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap wrap--narrow prose">
      <blockquote>
        Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver.
        <cite>&mdash; 2 Corinthians 9:7</cite>
      </blockquote>

      <h2>Ways to give</h2>

      <h3>In person</h3>
      <p>Offering plates are passed during the Sunday morning service. Envelopes are available at the back
      of the sanctuary for those who would like their giving recorded for the year-end statement.</p>

      <h3>By mail</h3>
      <p>%(name)s<br>%(street)s<br>%(city)s</p>

      <h3>Online</h3>
      <!-- Online giving is handled by Church Center. The two fund buttons at the top of
           this page are the live giving links. -->
      <p>Online giving runs through Church Center. Use the fund buttons at the top of this page to give
      to the Vision Fund or the Chair Fund directly.</p>

      <h2>Questions about giving</h2>
      <p>Call the church at <a href="%(tel)s">%(teld)s</a> and someone will be glad to help.</p>
    </div>
  </section>

""" % dict(name=NAME, street=STREET, city=CITY, tel=TEL, teld=TELD, img=IMG,
           vision_url=VISION_URL, chair_url=CHAIR_URL)

open(os.path.join(D, "give.html"), "w", encoding="utf-8").write(render(
    "give.html",
    "Give &mdash; East Side Free Will Baptist Church",
    "Ways to give to the ministry of East Side Free Will Baptist Church, Muldrow, Oklahoma.",
    give_body))
print("give.html written")


# ----------------------------------------------------------------- contact
contact_body = """  <section>
    <div class="wrap">
      <h1>Contact &amp; Directions</h1>
      <p class="prose lede">We would be glad to hear from you &mdash; whether you have a question or need
      prayer.</p>

      <h2 class="spaced">How to reach us</h2>
      <div class="grid grid--loose">
        <article class="card">
          <h3>Address</h3>
          <p>%(name)s<br>%(street)s<br>%(city)s</p>
          <p><a href="%(mapdir)s">Get directions &rarr;</a></p>
        </article>
        <article class="card">
          <h3>Phone</h3>
          <p><a href="%(tel)s">%(teld)s</a></p>
          <p>The most reliable way to reach us. If no one answers, please leave a message.</p>
        </article>
        <article class="card">
          <h3>Email</h3>
          <p><a href="mailto:%(email)s">%(email)s</a></p>
          <p>For a question, a prayer request, or anything you would rather write than say.</p>
        </article>
        <article class="card">
          <h3>Facebook</h3>
          <p><a href="%(fb)s">East Side Free Will Baptist Church</a></p>
          <p>Service times, announcements, and the Sunday livestream are posted there each week.</p>
        </article>
        <article class="card">
          <h3>Pastoral Care</h3>
          <p>Associate Pastor Logan Williams leads our visits to hospitals, nursing homes, and members
          who are homebound.</p>
          <p>If you are part of the East Side family and would like a visit or a call, phone
          <a href="%(tel)s">%(teld)s</a>. Please do not wait to be asked.</p>
        </article>
        <article class="card">
          <h3>Find us</h3>
          <p>We are at %(street)s in Muldrow, in Sequoyah County. There is a map on our
          <a href="index.html#find-us">home page</a>.</p>
        </article>
      </div>

      <h2 class="spaced">Send us a message</h2>
      <div class="wrap--narrow prose">
        <p>Whether it is a question, a prayer request, or something you would like a pastor to know
        about, you are welcome to write to us here.</p>
      </div>

      <form class="form" id="contact-form" method="post"
            action="mailto:%(email)s" enctype="text/plain">
        <div class="form__row">
          <label for="cf-name">Your name</label>
          <input id="cf-name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="form__row">
          <label for="cf-contact">How we can reach you
            <span class="form__hint">email or phone &mdash; only if you would like a reply</span></label>
          <input id="cf-contact" name="contact" type="text" autocomplete="email">
        </div>
        <div class="form__row">
          <label for="cf-message">Your message or prayer request</label>
          <textarea id="cf-message" name="message" rows="6" required></textarea>
        </div>
        <div class="form__row form__row--check">
          <input id="cf-followup" name="followup" type="checkbox" value="Yes">
          <label for="cf-followup">I would like a pastor to follow up with me</label>
        </div>
        <p><button class="btn" type="submit">Send message</button></p>
      </form>

      <div class="callout callout--quiet" id="cf-sent" hidden>
        <p><strong>Thank you.</strong> Your email program should have opened with the message ready to
        send. If it did not, please write to <a href="mailto:%(email)s">%(email)s</a> or call
        <a href="%(tel)s">%(teld)s</a> &mdash; we would not want to miss you.</p>
      </div>

      <p class="fine-print">This form hands your message to your own email program; nothing is stored on
      this website. Anything you send to the church is read by the pastoral staff. If you would rather
      speak to a person, call <a href="%(tel)s">%(teld)s</a>.</p>

      <script>
      (function () {
        var form = document.getElementById('contact-form');
        if (!form) return;
        form.addEventListener('submit', function (event) {
          event.preventDefault();
          var val = function (id) {
            var el = document.getElementById(id);
            return el ? el.value.trim() : '';
          };
          var name = val('cf-name');
          var contact = val('cf-contact');
          var message = val('cf-message');
          var followup = document.getElementById('cf-followup').checked ? 'Yes' : 'No';
          var body = 'Name: ' + name + '\\n'
                   + 'Reach me at: ' + (contact || 'not given') + '\\n'
                   + 'Pastor follow-up requested: ' + followup + '\\n\\n'
                   + message + '\\n';
          var subject = 'Website message from ' + (name || 'the church website');
          window.location.href = 'mailto:%(email)s'
            + '?subject=' + encodeURIComponent(subject)
            + '&body=' + encodeURIComponent(body);
          var done = document.getElementById('cf-sent');
          if (done) done.hidden = false;
        });
      })();
      </script>

      <h2 class="spaced">Prayer</h2>
      <p class="prose">If you need prayer, please tell us &mdash; you do not need to explain more than
      you wish to. Call the church at <a href="%(tel)s">%(teld)s</a>, write to
      <a href="mailto:%(email)s">%(email)s</a>, or send a message through our
      <a href="%(fb)s">Facebook page</a>.</p>
    </div>
  </section>
""" % dict(name=NAME, street=STREET, city=CITY, tel=TEL, teld=TELD, fb=FB, email=EMAIL,
           mapdir=MAPDIR, mapemb=MAPEMB)

# Preserve the Pastoral Care draft without publishing its card.
SHOW_PASTORAL_CARE = False
if not SHOW_PASTORAL_CARE:
    contact_body = re.sub(r'\s*<article class="card">\s*<h3>Pastoral Care</h3>.*?</article>', '', contact_body, count=1, flags=re.S)

open(os.path.join(D, "contact.html"), "w", encoding="utf-8").write(render(
    "contact.html",
    "Contact &mdash; East Side Free Will Baptist Church",
    "Address, phone, email, directions, and a message form for East Side Free Will Baptist Church in Muldrow, Oklahoma.",
    contact_body))
print("contact.html written")


# ----------------------------------------------------------------- announcements
announcements_body = """  <section>
    <div class="wrap wrap--narrow prose">
      <h1>Announcements</h1>
      <p class="lede">Here is what we want you to know this week &mdash; services, classes, events, and life in the congregation.</p>

      <p class="meta">Updated October 4, 2026</p>

      <h2 class="spaced">Praise in the Park</h2>
      <p>Straight Street Ministries will host &ldquo;Praise in the Park&rdquo; on
      <strong>Saturday, October 10, from 1:00&ndash;4:00 PM</strong>. Enjoy good music, fellowship,
      and free food. See the flyer in the foyer.</p>

      <h2 class="spaced">Sunday Evening Service</h2>
      <p>We will have an evening service at <strong>6:00 PM on Sunday, October 11</strong>.</p>

      <h2 class="spaced">WAC Floral Arrangement Class</h2>
      <p>On <strong>Wednesday, October 21, at 7:00 PM</strong>, the WAC will hold a one-night
      instructional class on making a fall floral arrangement as a fundraiser. The cost is
      <strong>$30 per person</strong>, including supplies. The sign-up sheet is in the foyer;
      please sign up by <strong>October 14</strong>. Everyone will leave with a beautiful fall arrangement!</p>

      <h2 class="spaced">Family News</h2>
      <p>Jestina (formerly Jestina Cantrell) and Erik Garcia are expecting a baby boy, due
      <strong>October 17</strong>. We are collecting gifts for them in the foyer. If you would like
      to bless them with a gift or gift card, please leave it in the basket in the foyer. Thank you!</p>

      <h2 class="spaced">Vision Fund</h2>
      <p>Our &ldquo;Final Construction Phase Push&rdquo; for the Vision Fund continues through
      <strong>December 2026</strong>. Our goal is to raise <strong>$200,000</strong> through the end
      of the year. Please prayerfully consider what you can give toward this goal.</p>

      <h2 class="spaced">Fall Festival &amp; Camo Sunday</h2>
      <p>Our Annual Fall Festival will be held on <strong>Sunday, October 25, at 5:00 PM</strong>
      at <strong>Archer &amp; Tracy Ryan&rsquo;s barn</strong>. There will be live music and singing,
      delicious food, and fellowship. Bring your lawn chair and your favorite chili, soup, or dessert.</p>
      <p>October 25 is also <strong>Camo Sunday</strong>. Wear your camo that day!</p>

      <h2 class="spaced">Pastor Appreciation Month</h2>
      <p>October is Pastor Appreciation Month. We are so very blessed to have Bro. Anthony as our
      senior pastor and Bro. Logan as our associate pastor.</p>

      <h2 class="spaced">Giving Online</h2>
      <p>To pay your tithes online, download the <strong>Church Center App</strong>. Please see
      Sis. Myra if you have any questions or would like additional information.
      <a href="give.html">Visit our giving page</a> for the current fund links.</p>

      <div class="callout callout--quiet">
        <p><strong>Note:</strong> This page changes often. For the most current updates, check our Facebook page
        at <a href="%(fb)s">%(fb)s</a>.</p>
      </div>
    </div>
  </section>
""" % dict(fb=FB)

open(os.path.join(D, "announcements.html"), "w", encoding="utf-8").write(render(
    "announcements.html",
    "Announcements &mdash; East Side Free Will Baptist Church",
    "Current announcements at East Side Free Will Baptist Church: Praise in the Park, Sunday evening service, WAC class, Fall Festival, Vision Fund, and church family news.",
    announcements_body))
print("announcements.html written")

# ----------------------------------------------------------------- 404
# ----------------------------------------------------------------- 404
notfound = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found &mdash; %(name)s</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">East Side <small>Free Will Baptist Church</small></a>
  </div>
</header>
<main id="main">
  <section>
    <div class="wrap wrap--narrow prose">
      <h1>That page isn&rsquo;t here</h1>
      <p>Either the link is out of date or the address was mistyped. Sorry about that &mdash; here is
      the way back.</p>
      <ul class="notfound-links">
        <li><a href="index.html">Home</a> &mdash; service times, where we are, and what to expect</li>
        <li><a href="ministries.html">Ministries</a> &mdash; children, students, adults, and care
        ministries</li>
        <li><a href="study-material.html">Study Material</a> &mdash; sermons to watch and devotions to read</li>
        <li><a href="contact.html">Contact</a> &mdash; phone, email, directions, and prayer requests</li>
      </ul>
      <p><a class="btn" href="index.html">Back to the home page</a></p>
    </div>
  </section>
</main>
</body>
</html>
""" % dict(name=NAME)

open(os.path.join(D, "404.html"), "w", encoding="utf-8").write(notfound)
print("404.html written")


# --------------------------------------------------- sitemap + robots
# Generated here so both stay in step with the pages themselves.

SITEMAP_PAGES = [
    ("", "1.0"), ("about.html", "0.8"), ("beliefs.html", "0.8"),
    ("ministries.html", "0.8"), ("calendar.html", "0.7"), ("announcements.html", "0.7"),
    ("study-material.html", "0.8"), ("sermons.html", "0.7"), ("devotions.html", "0.7"),
    ("give.html", "0.6"), ("contact.html", "0.9"),
] + [("devotions/%s.html" % d["slug"], "0.6", d["date"]) for d in DEV]

today = datetime.date.today().isoformat()
rows = ['<?xml version="1.0" encoding="UTF-8"?>',
        '<!-- Generated by build_site.py - do not edit by hand. -->',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, prio, *rest in SITEMAP_PAGES:
    rows += ['  <url>',
             '    <loc>https://eastsidefwbc.org/%s</loc>' % path,
             '    <lastmod>%s</lastmod>' % (rest[0] if rest else today),
             '    <priority>%s</priority>' % prio,
             '  </url>']
rows.append('</urlset>')
open(os.path.join(D, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
print("sitemap.xml written (%d pages)" % len(SITEMAP_PAGES))

robots = """User-agent: *
Allow: /

Sitemap: https://eastsidefwbc.org/sitemap.xml
"""
open(os.path.join(D, "robots.txt"), "w", encoding="utf-8").write(robots)
print("robots.txt written")

print("ALL PAGES WRITTEN")
