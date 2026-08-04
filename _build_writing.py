#!/usr/bin/env python3
import re, os, html, pathlib

CANON = "F:/Nexplane/nexplane-canon/"
NX    = "F:/Nexplane/nexplane/"
OUT   = pathlib.Path("F:/Nexplane/nexplane-site/public")
WRITE = OUT / "writing"
WRITE.mkdir(parents=True, exist_ok=True)
BASE  = "https://nexplane.ai"

# Grouped post structure — (slug, source_path)
GROUPS = [
  ("Essays", [
    ("anchor-the-rollback-nobody-built",            CANON+"content/posts/A1-the-rollback-nobody-built.md"),
    ("anchor-the-organizational-memory-problem",    CANON+"content/posts/A2-the-organizational-memory-problem.md"),
    ("anchor-why-ai-needs-a-change-process",        CANON+"content/posts/A3-why-ai-needs-a-change-process.md"),
  ]),
  ("Nexplane", [
    ("the-system-produces-bad-outcomes",            CANON+"content/posts/01-the-system-produces-bad-outcomes.md"),
    ("the-incentive-mismatch",                      CANON+"content/posts/02-the-incentive-mismatch.md"),
    ("the-execution-gap",                           CANON+"content/posts/03-the-execution-gap.md"),
    ("the-same-bet-twice",                          CANON+"content/posts/04-the-same-bet-twice.md"),
    ("someone-told-me-they-had-rollbacks",          CANON+"content/posts/05-someone-told-me-they-had-rollbacks.md"),
    ("soar-itsm-consultants",                       CANON+"content/posts/06-soar-itsm-consultants.md"),
    ("fit-over-correctness",                        CANON+"content/posts/07-fit-over-correctness.md"),
    ("resilience-is-the-right-frame",               CANON+"content/posts/08-resilience-is-the-right-frame.md"),
    ("the-rollback-nobody-built",                   NX+"blog/04-the-missing-rollback.md"),
    ("the-rollback-guarantee",                      CANON+"content/posts/09-the-rollback-guarantee.md"),
    ("chestertons-fence",                           CANON+"content/posts/10-chestertons-fence.md"),
    ("the-asset-inventory-problem",                 CANON+"content/posts/11-the-asset-inventory-problem.md"),
    ("the-ai-safety-harness-the-incidents",         CANON+"content/posts/12-ai-safety-harness-1-incidents.md"),
    ("the-ai-safety-harness-the-mechanism",         CANON+"content/posts/13-ai-safety-harness-2-mechanism.md"),
  ]),
  ("Back to Basics", [
    ("back-to-basics-microsegmentation",            CANON+"content/posts/B1-back-to-basics-network-microsegmentation.md"),
    ("back-to-basics-kernel-upgrades",              CANON+"content/posts/B2-back-to-basics-os-kernel-upgrades.md"),
    ("back-to-basics-seccomp",                      CANON+"content/posts/B3-back-to-basics-application-seccomp.md"),
    ("back-to-basics-least-privilege",              CANON+"content/posts/B4-back-to-basics-identity-least-privilege.md"),
    ("back-to-basics-secrets-rotation",             CANON+"content/posts/B5-back-to-basics-secrets-rotation.md"),
    ("back-to-basics-log-agent",                    CANON+"content/posts/B6-back-to-basics-observability-log-agent.md"),
    ("back-to-basics-security-groups",              CANON+"content/posts/B7-back-to-basics-cloud-security-groups.md"),
  ]),
  ("Founder", [
    ("why-i-built-nexplane",                        NX+"blog/05-founder-story.md"),
    ("we-gave-an-ai-agent-infrastructure-access",   NX+"blog/02-ai-agent-safety.md"),
    ("why-security-creates-work-for-engineering",   NX+"blog/03-org-alignment.md"),
    ("recovering-an-ad-forest-after-ransomware",    NX+"blog/01-ad-forest-recovery.md"),
  ]),
  ("Short form", [
    ("ai-shouldnt-have-root",                       CANON+"content/blog/001-ai-shouldnt-have-root.md"),
    ("reasoning-is-the-new-source-code",            CANON+"content/blog/002-reasoning-is-the-new-source-code.md"),
    ("ai-doesnt-need-more-permissions",             CANON+"content/blog/003-ai-doesnt-need-more-permissions-it-needs-a-better-change-process.md"),
    ("architecture-is-a-record-of-assumptions",     CANON+"content/blog/004-your-architecture-is-a-record-of-your-assumptions.md"),
    ("stop-measuring-lines-of-code",                CANON+"content/blog/005-stop-measuring-lines-of-code-start-measuring-engineering-judgment.md"),
    ("postmortems-should-measure-reasoning",        CANON+"content/blog/006-postmortems-should-measure-the-quality-of-the-reasoning-not-the-outcome.md"),
    ("adrs-missing-the-most-important-section",     CANON+"content/blog/007-architecture-decision-records-are-missing-the-most-important-section.md"),
    ("every-production-change-is-an-experiment",    CANON+"content/blog/008-every-production-change-is-a-scientific-experiment.md"),
    ("the-most-important-engineering-metric",       CANON+"content/blog/009-the-most-important-engineering-metric-doesnt-exist-yet.md"),
    ("engineering-org-has-a-memory-leak",           CANON+"content/blog/010-your-engineering-org-has-a-memory-leak.md"),
    ("best-engineers-arent-bottlenecks",            CANON+"content/blog/011-your-best-engineers-arent-bottlenecks-theyre-uncompiled-knowledge.md"),
    ("production-changes-should-begin-with-prediction", CANON+"content/blog/012-why-every-production-change-should-begin-with-a-prediction.md"),
    ("real-productivity-killer-is-decision-reconstruction", CANON+"content/blog/013-the-real-productivity-killer-is-decision-reconstruction.md"),
    ("best-architecture-review-starts-with-one-question", CANON+"content/blog/014-the-best-architecture-review-starts-with-one-question.md"),
    ("ai-needs-chain-of-evidence",                  CANON+"content/blog/015-ai-doesnt-need-chain-of-thought-it-needs-chain-of-evidence.md"),
    ("engineering-org-chart-missing-a-role",        CANON+"content/blog/016-the-engineering-org-chart-is-missing-a-role-the-organizational-memory-engineer.md"),
    ("future-of-devops-is-decisionops",             CANON+"content/blog/017-the-future-of-devops-is-decisionops.md"),
    ("stop-treating-ai-as-an-operator",             CANON+"content/blog/018-stop-treating-ai-as-an-operator.md"),
    ("most-dangerous-words-in-engineering",         CANON+"content/blog/022-the-most-dangerous-words-in-engineering-weve-always-done-it-this-way.md"),
    ("engineering-teams-build-time-machines",       CANON+"content/blog/023-the-best-engineering-teams-build-time-machines.md"),
    ("complexity-is-interest-on-decisions",         CANON+"content/blog/024-complexity-is-interest-on-yesterdays-decisions.md"),
    ("highest-leverage-engineering-work",           CANON+"content/blog/025-the-highest-leverage-engineering-work-is-often-invisible.md"),
    ("change-management-optimizing-wrong-thing",    CANON+"content/blog/026-your-change-management-process-is-probably-optimizing-the-wrong-thing.md"),
    ("infrastructure-teams-reinvent-a-control-plane", CANON+"content/blog/027-why-every-infrastructure-team-eventually-reinvents-a-control-plane.md"),
    ("every-outage-is-a-broken-mental-model",       CANON+"content/blog/028-every-outage-is-a-broken-mental-model.md"),
    ("documentation-is-dead",                       CANON+"content/blog/029-documentation-is-dead-long-live-context.md"),
    ("engineering-organizations-have-a-context-budget", CANON+"content/blog/030-engineering-organizations-have-a-context-budget.md"),
    ("last-known-good-state",                       CANON+"content/blog/031-the-last-known-good-state-may-be-the-most-valuable-object-in-infrastructure.md"),
    ("infrastructure-should-remember-more",         CANON+"content/blog/032-infrastructure-should-remember-more-than-configuration.md"),
    ("engineering-organizations-optimize-for-regret", CANON+"content/blog/033-the-best-engineering-organizations-optimize-for-regret.md"),
    ("platform-teams-become-product-companies",     CANON+"content/blog/034-why-most-platform-engineering-teams-eventually-become-internal-product-companies.md"),
    ("engineering-debt-is-cognitive",               CANON+"content/blog/035-engineering-debt-isnt-technical-its-cognitive.md"),
    ("ai-needs-better-organizations",               CANON+"content/blog/036-ai-doesnt-need-better-models-it-needs-better-organizations.md"),
    ("next-competitive-advantage-is-organizational-intelligence", CANON+"content/blog/037-the-next-competitive-advantage-is-organizational-intelligence.md"),
    ("architecture-diagrams-missing-time",          CANON+"content/blog/038-every-architecture-diagram-is-missing-time.md"),
    ("engineering-is-becoming-information-science", CANON+"content/blog/039-engineering-is-becoming-an-information-science.md"),
    ("future-cto-will-manage-organizational-intelligence", CANON+"content/blog/040-the-future-cto-will-manage-organizational-intelligence.md"),
    ("what-is-an-engineering-control-plane",        CANON+"content/blog/041-what-is-an-engineering-control-plane.md"),
    ("infrastructure-needs-version-control-for-decisions", CANON+"content/blog/042-why-infrastructure-needs-version-control-for-decisions.md"),
    ("future-infrastructure-stack",                 CANON+"content/blog/043-the-future-infrastructure-stack.md"),
    ("ai-should-review-infrastructure",             CANON+"content/blog/044-why-ai-should-review-infrastructure-before-it-changes-infrastructure.md"),
    ("missing-feedback-loop-in-infrastructure",     CANON+"content/blog/045-the-missing-feedback-loop-in-infrastructure.md"),
    ("infrastructure-should-explain-itself",        CANON+"content/blog/046-infrastructure-should-explain-itself.md"),
    ("engineering-needs-a-memory-layer",            CANON+"content/blog/047-why-engineering-needs-a-memory-layer.md"),
    ("reversibility-is-the-ultimate-safety-feature", CANON+"content/blog/048-reversibility-is-the-ultimate-safety-feature.md"),
    ("building-an-ai-native-organization",          CANON+"content/blog/049-building-an-ai-native-engineering-organization.md"),
    ("next-decade-of-engineering",                  CANON+"content/blog/050-the-next-decade-of-engineering.md"),
  ]),
]

# Flat list for individual page generation (preserves all existing URLs)
POSTS = [(s, p) for _, grp in GROUPS for s, p in grp]

def parse(path):
    raw = pathlib.Path(path).read_text(encoding="utf-8")
    title = None
    body = raw
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    if m:
        fm, body = m.group(1), m.group(2)
        tm = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M)
        if tm: title = tm.group(1).strip()
    # first markdown H1 as fallback title, then strip it from body
    if title is None:
        h = re.search(r'^#\s+(.*)$', body, re.M)
        if h: title = h.group(1).strip()
    body = re.sub(r'^#\s+.*$', '', body, count=1, flags=re.M)   # drop leading H1
    # drop standalone [JOHN: ...] paragraphs; strip any stray inline brackets
    body = re.sub(r'^\s*\[JOHN:[^\]]*\]\s*$', '', body, flags=re.M)
    body = re.sub(r'\[JOHN:[^\]]*\]', '', body)
    return title, body.strip()

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'(?<!\w)_([^_]+)_(?!\w)', r'<em>\1</em>', t)
    return t

def md2html(body):
    out, para, lst, ltype = [], [], [], None
    def flush_para():
        if para:
            txt = " ".join(para).strip()
            if txt:
                cls = ' class="cta-line"' if (txt.startswith("*") and txt.endswith("*")) else ""
                out.append(f"<p{cls}>{inline(txt)}</p>")
            para.clear()
    def flush_list():
        nonlocal ltype
        if lst:
            out.append(f"<{ltype}>" + "".join(f"<li>{inline(x)}</li>" for x in lst) + f"</{ltype}>")
            lst.clear(); ltype=None
    for line in body.split("\n"):
        s = line.strip()
        if not s:
            flush_para(); flush_list(); continue
        if s == "---":
            flush_para(); flush_list(); continue
        h = re.match(r'^(#{2,4})\s+(.*)$', s)
        if h:
            flush_para(); flush_list()
            lvl = {2:"h3",3:"h4",4:"h5"}[len(h.group(1))]
            out.append(f"<{lvl}>{inline(h.group(2))}</{lvl}>"); continue
        ul = re.match(r'^[-*]\s+(.*)$', s)
        ol = re.match(r'^\d+\.\s+(.*)$', s)
        if ul:
            flush_para()
            if ltype not in (None,"ul"): flush_list()
            ltype="ul"; lst.append(ul.group(1)); continue
        if ol:
            flush_para()
            if ltype not in (None,"ol"): flush_list()
            ltype="ol"; lst.append(ol.group(1)); continue
        flush_list(); para.append(s)
    flush_para(); flush_list()
    return "\n      ".join(out)

def desc_of(body):
    for line in body.split("\n"):
        s = line.strip()
        if s and not s.startswith(("#","-","*","1.",">")):
            s = re.sub(r'[*`_]', '', s)
            return (s[:152] + "…") if len(s) > 153 else s
    return "Writing from John Terrill on infrastructure change, security, and AI."

HEAD_FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

NAV = '''<nav>
  <div class="nav-inner">
    <a href="/" class="logo">Nexplane</a>
    <div class="nav-links">
      <a href="/#platform">Platform</a>
      <a href="/#use-cases">Use cases</a>
      <a href="/enterprise">Enterprise</a>
      <a href="/#integrations">Integrations</a>
      <a href="https://docs.nexplane.ai" target="_blank" rel="noopener">Docs</a>
      <a href="/writing">Writing</a>
      <a href="/#request-demo" class="btn-nav">Request demo</a>
    </div>
  </div>
</nav>'''

FOOTER = '''<footer>
  <div class="footer-inner">
    <div class="footer-logo">Nexplane</div>
    <p class="footer-tagline">The control plane for infrastructure change.</p>
    <div class="footer-links">
      <a href="/writing">Writing</a>
      <a href="/enterprise">Enterprise</a>
      <a href="/licensing">Licensing</a>
      <a href="https://docs.nexplane.ai" target="_blank" rel="noopener">Docs</a>
      <a href="mailto:hello@nexplane.ai">hello@nexplane.ai</a>
    </div>
    <p class="footer-copy">&copy; 2026 Nexplane. All rights reserved.</p>
  </div>
</footer>'''

def page_head(title, desc, canonical, article=False):
    og = f'''<meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:type" content="{'article' if article else 'website'}">
  <meta property="og:url" content="{canonical}">
  {'<meta property="article:author" content="John Terrill">' if article else ''}
  <meta name="twitter:card" content="summary_large_image">'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}" />
  <link rel="canonical" href="{canonical}" />
  {og}
  <link rel="stylesheet" href="/style.css" />
  {HEAD_FONTS}
</head>
<body>
{NAV}'''

built = []
for slug, src in POSTS:
    title, body = parse(src)
    desc = desc_of(body)
    canonical = f"{BASE}/writing/{slug}"
    body_html = md2html(body)
    doc = page_head(title, desc, canonical, article=True) + f'''

<section>
  <div class="container article-head">
    <div class="section-eyebrow"><a href="/writing" style="color:var(--brand-light)">John · Writing</a></div>
    <h2 class="article-title">{html.escape(title)}</h2>
    <div class="byline"><b>John Terrill</b> · <a href="https://www.linkedin.com/in/johnterrill" target="_blank" rel="noopener">LinkedIn</a> · <span class="permalink">/writing/{slug}</span></div>
    <div class="prose">
      {body_html}
    </div>
    <div class="github-cta">
      <div class="github-cta-text">
        <strong>Nexplane is open source.</strong> If this resonated, star the repo — it helps others find it.
      </div>
      <a href="https://github.com/youbetyourballs/nexplane" target="_blank" rel="noopener" class="btn-github">⭐ Star on GitHub</a>
    </div>
    <div class="ref-row">
      <span>Reference:</span>
      <a href="https://www.linkedin.com/in/johnterrill" target="_blank" rel="noopener">Share on LinkedIn</a>
      <a href="/writing">← All writing</a>
    </div>
  </div>
</section>

{FOOTER}
</body>
</html>
'''
    (WRITE / f"{slug}.html").write_text(doc, encoding="utf-8", newline="\n")
    built.append((slug, title, desc))
    print("wrote writing/%s.html  (%s)" % (slug, title))

# ---- index ----
# Build slug->title lookup from built list
slug_to_meta = {s: (t, d) for s, t, d in built}

# Anchor shortcuts (Essays group)
anchor_slugs = [s for s, _ in GROUPS[0][1]]
anchor_links = "\n".join(
    f'      <a class="anchor-link" href="/writing/{s}">{html.escape(slug_to_meta[s][0])}</a>'
    for s in anchor_slugs if s in slug_to_meta)

# Grouped sections (skip Essays group — shown above as anchors)
group_sections = ""
for group_name, group_posts in GROUPS:
    items = "\n".join(
        f'        <a class="post-item" href="/writing/{s}"><span class="pt">{html.escape(slug_to_meta[s][0])}</span><span class="pd">{html.escape(slug_to_meta[s][1])[:70]}</span></a>'
        for s, _ in group_posts if s in slug_to_meta)
    group_sections += f'''
    <div class="post-group">
      <div class="post-group-label">{html.escape(group_name)}</div>
      <div class="post-list">
{items}
      </div>
    </div>'''

idx = page_head("Writing — John Terrill · Nexplane",
    "Writing from John Terrill on why the platform works the way it does and how to use it — the reasoning behind Nexplane.",
    f"{BASE}/writing") + f'''

<section>
  <div class="container article-head">
    <div class="section-eyebrow">John · Writing</div>
    <h2 class="article-title">Why it works this way, <em>and how to use it.</em></h2>
    <div class="byline"><b>John Terrill</b> — 4× CISO, founder of Nexplane. <a href="https://www.linkedin.com/in/johnterrill" target="_blank" rel="noopener">LinkedIn →</a></div>
    <p class="section-sub">The reasoning behind Nexplane and how to apply it — a reference library, not a feed. The docs tell you what each button does; this is why it exists and when to reach for it.</p>
    <div class="anchor-essays">
      <div class="anchor-essays-label">Start here</div>
{anchor_links}
    </div>
{group_sections}
  </div>
</section>

{FOOTER}
</body>
</html>
'''
(WRITE / "index.html").write_text(idx, encoding="utf-8", newline="\n")
print("wrote writing/index.html")

# ---- sitemap.xml ----
urls = [f"{BASE}/", f"{BASE}/enterprise", f"{BASE}/licensing", f"{BASE}/writing"] + [f"{BASE}/writing/{s}" for s,_,_ in built]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n"
(OUT / "sitemap.xml").write_text(sm, encoding="utf-8", newline="\n")
print("wrote sitemap.xml (%d urls)" % len(urls))

# ---- robots.txt ----
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8", newline="\n")
print("wrote robots.txt")
print("DONE:", len(built), "posts")
