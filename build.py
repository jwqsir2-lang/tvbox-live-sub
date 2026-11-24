#!/usr/bin/env python3
"""Merge upstream live.txt into the base TVBox config (musebox / TVBoxQ edition).

- base.json is the FIXED template: VOD sites / parses / flags / original live
  groups never change.
- Pulls live.txt (standard "#genre#" text format), parses groups, filters out
  non-playable junk (.php interfaces, ad rows, non-m3u8 pages), dedupes, and
  rewrites TVBoxv3xg.json. Runs on a schedule via GitHub Actions.
"""
import json
import re
import sys
import urllib.request
from collections import OrderedDict

LIVE_TXT_URL = "https://raw.githubusercontent.com/Supprise0901/TVBox_live/main/live.txt"
BASE_FILE = "base.json"
OUT_FILE = "TVBoxv3xg.json"
DEFAULT_EPG = "http://epg.112114.xyz/?ch={name}&date={date}"

# A live URL must look like a real stream: m3u8 / ts / flv / rtsp over http(s).
STREAM_RE = re.compile(r"^https?://[^\s]+\.(m3u8|ts|flv)(\?|$)", re.I)
# Junk: php interfaces (often dynamic redirect pages), placeholder/test domains,
# promo/ad rows that are not real channels.
JUNK_RE = re.compile(r"(\.php(\?|$))|(测试\.)|( nxog\.top)|(716888)|(711888)", re.I)


def usable(url):
    return bool(STREAM_RE.match(url)) and not JUNK_RE.search(url)


def parse_live_txt(text):
    groups, cur, idx = [], None, {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if "#genre#" in line:
            cur = {"group": line.split(",")[0].strip(), "channels": []}
            groups.append(cur)
            idx = {}
            continue
        parts = line.split(",", 1)
        if len(parts) != 2:
            continue
        name, url = parts[0].strip(), parts[1].strip()
        if not name or not usable(url):
            continue
        if name in idx:
            if url not in idx[name]["urls"]:
                idx[name]["urls"].append(url)
        else:
            ch = {"name": name, "urls": [url]}
            idx[name] = ch
            if cur is not None:
                cur["channels"].append(ch)
    # drop groups that ended up empty (e.g. the promo-only groups)
    return [g for g in groups if g["channels"]]


def main():
    with open(BASE_FILE, encoding="utf-8") as f:
        base = json.load(f, object_pairs_hook=OrderedDict)

    req = urllib.request.Request(LIVE_TXT_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        text = r.read().decode("utf-8", errors="ignore")

    live_groups = parse_live_txt(text)
    if not live_groups:
        print("WARNING: no live groups parsed from upstream; keeping existing output")
        sys.exit(0)

    # lives are fully REPLACED by the upstream live.txt groups — the base
    # template's own live groups (央/卫/新闻/体育/其他) are intentionally dropped
    # so the config only carries whatever upstream live.txt ships.
    epg = DEFAULT_EPG
    if base.get("lives"):
        epg = base["lives"][0].get("epg", DEFAULT_EPG)

    seen = set()
    new_lives = []
    for g in live_groups:
        name = g["group"]
        suffix = 2
        while name in seen:
            name = f"{g['group']}{suffix}"
            suffix += 1
        seen.add(name)
        ng = OrderedDict()
        ng["group"] = name
        ng["epg"] = epg
        ng["channels"] = [
            OrderedDict(
                [
                    ("name", c["name"]),
                    (
                        "urls",
                        [
                            f"{u}$线路{i + 1}" if "$" not in u else u
                            for i, u in enumerate(c["urls"])
                        ],
                    ),
                ]
            )
            for c in g["channels"]
        ]
        new_lives.append(ng)

    out = OrderedDict()
    for k in base:
        out[k] = new_lives if k == "lives" else base[k]

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

    nch = sum(len(g["channels"]) for g in live_groups)
    nurl = sum(len(c["urls"]) for g in live_groups for c in g["channels"])
    print(f"OK: appended {len(live_groups)} groups / {nch} channels / {nurl} urls -> {OUT_FILE}")


if __name__ == "__main__":
    main()
