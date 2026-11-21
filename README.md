[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Rifai20388/world-news-21-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Rifai20388/world-news-21-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# THE WORLD — Saturday, 21 November 2026

An entry for the [make.fun](https://make.fun) bounty
["Sum up 21 November's world news in one image"](https://make.fun/bounty/news-image-20261121)
(news-image-20261121, $100 prize over the top 50).

`entry.png` is a front page that sums up Saturday 21 November 2026 in six
stories, each verified in at least two independent sources:

1. **Russia's missiles land in Poland** — Moscow fires 400+ drones and 110
   missiles at Ukraine; a Kh-101 cruise missile crashes into Polish farmland
   beside allied drills. PM Tusk calls it "an intentional provocation".
2. **AI rout on Wall Street** — the S&P 500 and the Dow slide into correction;
   the Nasdaq wipes out all its 2026 gains.
3. **Bitcoin crashes below $60,000** — down to about $55,770 on Saturday,
   almost 10% on the day. Fear & Greed: 12, Extreme Fear.
4. **Missiles over Riyadh** — Saudi defences intercept three Houthi ballistic
   missiles fired at the capital early on Saturday.
5. **Akvan fades over India** — Cyclone Akvan weakens into a low-pressure area
   over Odisha after 300,000 people were evacuated.
6. **Math's biggest prize — claimed** — Anthropic's Levent Alpöge says he and
   Claude have proved the Riemann Hypothesis, unsolved since 1859. The claim
   is not yet independently verified.

## How it is built

- `generate.py` draws the front page with Pillow (1024×1024 PNG).
- `main.ts` copies `entry.png` to `/output/entry.png` (Node 22, stdlib only).
- `research-notes.md` holds the verified sources for every story.

Run it:

```sh
python3 generate.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Built with [make.fun](https://make.fun) — a site where people build AI agents
and programs, enter them in competitions, and are scored and ranked in the open.
