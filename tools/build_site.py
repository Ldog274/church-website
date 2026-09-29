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
  "description": "A Free Will Baptist congregation in Muldrow, Oklahoma. Sunday school 9:30 AM, morning worship 10:30 AM with children's church, Wednesday evening service 7:30 PM.",
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
       ("ministries.html", "Ministries"), ("calendar.html", "Calendar"), ("announcements.html", "Announcements"), ("sermons.html", "Sermons"),
       ("give.html", "Give"), ("contact.html", "Contact")]


def nav(page):
    rows = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ''
        rows.append('        <li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    return "\n".join(rows)


FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div>
      <h3>Service Times</h3>
      <ul>
        <li>Sunday School &mdash; 9:30 AM</li>
        <li>Morning Worship &mdash; 10:30 AM<span class="fine">Children&rsquo;s church at the same hour</span></li>
        <li>Wednesday &mdash; 7:30 PM<span class="fine">Youth meet at the Activities Center</span></li>
      </ul>
    </div>
    <div>
      <h3>Find Us</h3>
      <ul>
        <li>%(street)s</li>
        <li>%(city)s</li>
        <li><a href="%(tel)s">%(teld)s</a></li>
        <li><a href="mailto:%(email)s">%(email)s</a></li>
        <li><a href="contact.html">Directions &amp; contact</a></li>
      </ul>
    </div>
    <div>
      <h3>Connect</h3>
      <ul>
        <li><a href="%(fb)s">Facebook</a></li>
        <li><a href="calendar.html">Calendar</a></li>
        <li><a href="sermons.html">Sermons</a></li>
        <li><a href="give.html">Give</a></li>
      </ul>
    </div>
    <p class="legal">&copy; <span id="yr">2026</span> %(name)s</p>
  </div>
</footer>

<script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>""" % dict(street=STREET, city=CITY, tel=TEL, teld=TELD, fb=FB, name=NAME, email=EMAIL)


def render(page, title, desc, body, schema=""):
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
<link rel="stylesheet" href="css/styles.css">
%(schema)s
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">East Side <small>Free Will Baptist Church</small></a>
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
""" % dict(title=title, desc=desc, url=url, nav=nav(page), body=body, footer=FOOTER,
         ogimg=OG_IMG, schema=schema)


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
          <dd>7:30 PM<span>Youth meet at the Activities Center</span></dd>
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
          <p class="meta">Listen</p>
          <h3>Sermons &amp; livestream</h3>
          <p>Missed a Sunday, or want to hear a message again? Services are streamed on our Facebook page.</p>
          <p><a href="sermons.html">Watch a service &rarr;</a></p>
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

open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(render(
    "index.html",
    "East Side Free Will Baptist Church &mdash; Muldrow, Oklahoma",
    "A Free Will Baptist church family in Muldrow, Oklahoma. Sunday school 9:30 AM, morning worship 10:30 AM, Wednesday evening 7:30 PM. All are welcome.",
    index_body, schema=CHURCH_SCHEMA))
print("index.html written")


# ----------------------------------------------------------------- about
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
        <li><strong>Wednesday</strong> &mdash; the church gathers at <strong>7:30 PM</strong> for Bible study and prayer, and our youth meet at the same hour at the Activities Center, %(act)s.</li>
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
          <p>Our youth meet on <strong>Wednesday evening at 7:30 PM</strong> at the
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
          <p>The church gathers on <strong>Wednesday at 7:30 PM</strong> for Bible study and prayer.</p>
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

open(os.path.join(D, "ministries.html"), "w", encoding="utf-8").write(render(
    "ministries.html",
    "Ministries &mdash; East Side Free Will Baptist Church",
    "Sunday school, children's church, midweek service, youth worship, and the nursing home and shut-in ministry at East Side Free Will Baptist Church.",
    ministries_body))
print("ministries.html written")


# ----------------------------------------------------------------- calendar
# The church's own September-November 2026 calendar sheet, transcribed. Each
# month is a list of (day, [(time, title), ...]) in the order the sheet lists
# them. To update, edit this table and re-run the generator - never the HTML.
# Times the sheet left blank are recorded as None and simply omit the time.
MONTH_NUM = {"September": 9, "October": 10, "November": 11}

CHURCH_CALENDAR = [
    ("September 2026", [
        (2,  [("7:00 PM", "Bro. Trenton Forever devotion at the Activities Center"),
              ("7:00 PM", "WAC"),
              ("7:00 PM", "Men&rsquo;s Bible Study"),
              (None,    "Bro. Logan devotion"),
              (None,    "Bro. A out of office")]),
        (3,  [(None,    "Bro. A out of office")]),
        (4,  [(None,    "Bro. A out of office"),
              (None,    "East Side feeds the Needs Band (50)")]),
        (5,  [("8:00 AM", "5K Color Run &mdash; &ldquo;Faith in Motion&rdquo; fundraiser"),
              (None,    "Bro. A out of office")]),
        (6,  [(None,    "Vision Fund Sunday")]),
        (7,  [(None,    "Muldrow Schools &mdash; no school (Labor Day)")]),
        (8,  [("10:30 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (9,  [("10:30 AM", "Flanna Hills Nursing Home service"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (12, [("10:00 AM", "Semi-annual ARVA meeting at Mineral Springs FWB &mdash; speaker Lee Rogers")]),
        (13, [("6:00 PM",  "PM worship with Bro. Logan"),
              (None,      "Grandparents Day")]),
        (15, [("10:30 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (16, [("7:00 PM",  "WAC"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (20, [(None,      "&ldquo;Chair&rdquo; offering")]),
        (22, [("10:30 AM", "WWBS"),
              ("6:30 PM",  "BATTL")]),
        (23, [("7:00 PM",  "Men&rsquo;s Bible Study")]),
        (25, [(None,      "East Side feeds the football and cheer squads (75)")]),
        (27, [(None,      "WAC &ldquo;Dollar Days for Missions&rdquo; offering"),
              (None,      "Family &ldquo;All-in-One&rdquo; worship"),
              ("6:00 PM",  "Revival with Bro. Earl Roberts")]),
        (28, [("7:00 PM",  "Revival with Bro. Earl Roberts")]),
        (29, [("10:30 AM", "WWBS"),
              ("6:30 PM",  "BATTL"),
              ("7:00 PM",  "Revival with Bro. Earl Roberts")]),
        (30, [("7:00 PM",  "Revival with Bro. Earl Roberts"),
              ("7:00 PM",  "Men&rsquo;s Bible Study")]),
    ]),
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
        <strong>Wednesday</strong> &mdash; Midweek service 7:30 PM &middot; Youth worship 7:30 PM at the
        Activities Center, %(act)s</p>
      </div>

      <h2 class="spaced">September, October, and November 2026</h2>
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


# ----------------------------------------------------------------- sermons
sermons_body = """  <section>
    <div class="wrap">
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

      <!-- ===================================================================
           SERMON ARCHIVE

           To add a message, copy this block into the list below and fill it in.
           Keep the newest at the top. A plain <table> also works if you prefer,
           but the list below stays readable on a phone.

           <li>
             <strong>Title of the message</strong>
             <span>Preached 4 January 2026 &middot; Pastor Anthony Williams &middot; John 3:16&ndash;21</span>
             <a href="FACEBOOK_VIDEO_URL">Watch</a>
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

  <section class="feature feature--reverse">
    <div class="wrap feature__wrap">
      <figure class="figure">
        <img src="%(img)s/praying.jpg" srcset="%(img)s/praying-640.jpg 640w, %(img)s/praying.jpg 1024w" sizes="(max-width: 46rem) 100vw, 45vw" alt="Hands clasped in prayer resting on an open Bible.">
      </figure>
      <div class="feature__text">
        <h2>Where your giving goes</h2>
        <p>Alongside the ordinary costs of running a church, your giving supports our new worship and
        ministry center at 1302 South Main Street, our children&rsquo;s and youth work, and the practical
        care we extend to families in Muldrow who are having a hard time.</p>
        <p>A portion of what we receive also supports the wider work of our sister churches, missions, and
        camp ministry across the state.</p>
      </div>
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

open(os.path.join(D, "contact.html"), "w", encoding="utf-8").write(render(
    "contact.html",
    "Contact &mdash; East Side Free Will Baptist Church",
    "Address, phone, email, directions, a message form, and pastoral care contact for East Side Free Will Baptist Church in Muldrow, Oklahoma.",
    contact_body))
print("contact.html written")


# ----------------------------------------------------------------- announcements
announcements_body = """  <section>
    <div class="wrap wrap--narrow prose">
      <h1>Announcements</h1>
      <p class="lede">Here is what we want you to know this week &mdash; services, classes, events, and life in the congregation.</p>

      <h2 class="spaced">Worship &amp; Revival</h2>
      <p>Welcome to our &ldquo;All-in-One&rdquo; Family worship service this morning where we all come together in the
      sanctuary for worship including children&rsquo;s church and workers.</p>

      <p>The Revival Services start tonight through Wednesday! Bro. Earl Roberts will be preaching each night.
      Tonight&rsquo;s services will start at 6 PM and Monday through Wednesday nights will start at 7:00 PM.
      There will be singing too!</p>

      <p>We are having a &ldquo;Potluck Fellowship&rdquo; following tonight&rsquo;s services in the Fellowship Hall. Please
      bring your favorite dish or dessert. For Monday through Wednesday nights of the revival, we are
      serving dinner starting at 6:00 each night:</p>
      <ul>
        <li>Monday: Chicken dinner</li>
        <li>Tuesday: Hamburgers and hotdogs</li>
        <li>Wednesday: Pizza</li>
      </ul>

      <h2 class="spaced">WAC</h2>
      <p>The WAC will receive its &ldquo;Dollar Days for Missions&rdquo; offering today.</p>

      <p>On Wednesday, October 21st at 7:00, the WAC is doing a one-night instructional &ldquo;how to make a
      fall floral arrangement&rdquo; class as a fundraiser. Cost is <strong>$30 per person</strong>, which includes supplies
      that will be needed. Sign-up sheet in the foyer. Please sign up by <strong>Oct. 14</strong>. Everyone will leave
      with a beautiful fall arrangement!</p>

      <h2 class="spaced">Vision Fund</h2>
      <p>We are doing a &ldquo;Final Construction Phase Push&rdquo; for the Vision Fund through December 2026. Our
      goal is to raise <strong>$200,000</strong> thru the end of the year. Please prayerfully consider what you can give
      toward this goal.</p>

      <h2 class="spaced">Family News</h2>
      <p>Jestina (formerly Jestina Cantrell) and Erik Garcia are having a baby boy and are due in 4 weeks
      on <strong>Oct. 17th</strong>! We aren&rsquo;t doing a shower but want to do a gift drop-off for them in the foyer. If
      you would like to bless them with a gift or gift card, please bring your gifts by next Sunday,
      <strong>October 4th</strong>. They are registered with Amazon. Thank you!</p>

      <h2 class="spaced">Giving Online</h2>
      <p>If you would like to pay your tithes online, please download the &ldquo;Church Center App&rdquo; or scan the
      QR code for your convenience. Please see Sis. Myra if you have any questions or would like
      additional information.</p>

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
    "This week at East Side Free Will Baptist Church: worship services, revival, WAC events, Vision Fund, and family news.",
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
        <li><a href="sermons.html">Sermons</a> &mdash; watch a service, or find a message</li>
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
    ("ministries.html", "0.8"), ("calendar.html", "0.7"), ("announcements.html", "0.7"), ("sermons.html", "0.7"),
    ("give.html", "0.6"), ("contact.html", "0.9"),
]

today = datetime.date.today().isoformat()
rows = ['<?xml version="1.0" encoding="UTF-8"?>',
        '<!-- Generated by build_site.py - do not edit by hand. -->',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, prio in SITEMAP_PAGES:
    rows += ['  <url>',
             '    <loc>https://eastsidefwbc.org/%s</loc>' % path,
             '    <lastmod>%s</lastmod>' % today,
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
