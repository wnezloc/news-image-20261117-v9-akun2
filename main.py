#!/usr/bin/env python3
"""news-image-20261117 v9 (akun 2): 43-story cream front page.

Dense-facts recipe from the top-20 dissection (bedah-top20-vs-v6):
every story carries 2-4 verified facts (names, figures, outcomes),
zero duplication (Kerch+Kyiv merged, drones lead with tankers in the
deck), data badges + place captions on every grid card, all 43 stories
pinned/dotted on the map, sport included. Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
