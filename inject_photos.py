#!/usr/bin/env python3
"""
inject_photos.py — Burla Mac Digitali photo injector
Drop photos in /photos, run this script, push to GitHub.
"""

import os
import re
from pathlib import Path

PHOTOS_DIR = Path(__file__).parent / "photos"
INDEX_FILE = Path(__file__).parent / "index.html"

MEMBERS = [
    "gabriel", "benji", "beny", "elias", "alesandra",
    "helena", "mike", "sarah", "camila", "isaac_hamui"
]
SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}
GALLERY_SLOTS = 15


def find_photos(prefix):
    """Return sorted list of photo paths for a given member prefix."""
    if not PHOTOS_DIR.exists():
        return []
    return sorted([
        f for f in PHOTOS_DIR.iterdir()
        if f.stem.lower().startswith(prefix + "_") and f.suffix.lower() in SUPPORTED
    ])


def find_gallery_photos():
    if not PHOTOS_DIR.exists():
        return []
    return sorted([
        f for f in PHOTOS_DIR.iterdir()
        if f.stem.lower().startswith("gallery_") and f.suffix.lower() in SUPPORTED
    ])


def inject():
    if not INDEX_FILE.exists():
        print("❌ index.html not found. Run this from the project root.")
        return

    html = INDEX_FILE.read_text(encoding="utf-8")
    injected = 0
    placeholders_remaining = 0

    # --- MUGSHOT INJECTION ---
    for member in MEMBERS:
        photos = find_photos(member)
        photo_id = f"photo-{member.replace('_', '_')}"
        placeholder_id = f"placeholder-{member.replace('_', '_')}"

        if photos:
            src = f"photos/{photos[0].name}"
            # Show the img tag
            html = re.sub(
                rf'(<img id="{photo_id}" src=")[^"]*(" alt="[^"]*") style="display:none"',
                rf'\g<1>{src}\2 style="display:block"',
                html
            )
            # Hide the placeholder div
            html = re.sub(
                rf'(<div class="mugshot-placeholder" id="{placeholder_id}">)',
                rf'<div class="mugshot-placeholder" id="{placeholder_id}" style="display:none">',
                html
            )
            injected += 1
            print(f"  ✅ {member}: mugshot → {photos[0].name}")
        else:
            # Ensure img stays hidden and placeholder visible
            html = re.sub(
                rf'(<img id="{photo_id}" src=")[^"]*(" alt="[^"]*") style="display:block"',
                rf'\g<1>\2 style="display:none"',
                html
            )
            html = re.sub(
                rf'(<div class="mugshot-placeholder" id="{placeholder_id}") style="display:none"',
                rf'\1',
                html
            )
            placeholders_remaining += 1
            print(f"  ⬜ {member}: sin foto")

    # --- GALLERY INJECTION ---
    # Collect extra member photos + dedicated gallery photos
    gallery_queue = []

    for member in MEMBERS:
        photos = find_photos(member)
        if len(photos) > 1:
            for extra in photos[1:]:
                gallery_queue.append((extra, f"Evidencia adicional: {member.replace('_', ' ').title()}"))

    for gphoto in find_gallery_photos():
        gallery_queue.append((gphoto, f"Archivo general — {gphoto.stem}"))

    gallery_injected = 0
    for slot_idx in range(GALLERY_SLOTS):
        photo_id = f"gallery-photo-{slot_idx}"
        if slot_idx < len(gallery_queue):
            photo_path, caption = gallery_queue[slot_idx]
            src = f"photos/{photo_path.name}"
            html = re.sub(
                rf'(<img id="{photo_id}" src=")[^"]*(" alt="") style="display:none"',
                rf'\g<1>{src}\2 style="display:block;position:absolute;inset:0;width:100%;height:100%;object-fit:cover"',
                html
            )
            gallery_injected += 1
        else:
            # Reset to hidden if re-running with fewer photos
            html = re.sub(
                rf'(<img id="{photo_id}" src=")[^"]*(" alt="") style="display:block[^"]*"',
                rf'\g<1>\2 style="display:none"',
                html
            )

    INDEX_FILE.write_text(html, encoding="utf-8")

    print()
    print(f"✅ {injected} mugshots inyectados")
    print(f"✅ {gallery_injected} fotos de galería inyectadas")
    print(f"⬜ {placeholders_remaining} mugshots pendientes (sin foto)")
    print()
    print("Siguiente paso:")
    print('  git add . && git commit -m "📸 Fotos agregadas" && git push')


if __name__ == "__main__":
    print("🚨 Burla Mac Digitali — Photo Injector\n")
    inject()
