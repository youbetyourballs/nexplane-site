# nexplane-site — backlog

Deferred work for the public site (nexplane.ai). Not blocking; pick up as capacity allows.

## Analytics / measurement
- [ ] **Add Google Analytics to the public site.** Instrument all pages (homepage, `/enterprise`,
  `/licensing`, and every `/writing/<slug>` post + the `/writing` index). Since the site is
  generated static HTML, the GA snippet needs to land in the shared `<head>` — for the hand-written
  pages directly, and for the writing pages via the `page_head()` template in `_build_writing.py`
  (so regenerated posts keep the tag). Decide GA4 property + measurement ID, and whether a
  consent/cookie banner is needed before rollout.
  - **Blocked on:** setting up the `nexplane.ai` domain with Google Workspace (GSuite) first —
    needed before GA can be wired up properly (property ownership / domain verification).
