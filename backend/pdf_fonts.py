# How to read, all file name from a folder and store it in a dictionary. 

"""
Utility to discover every .ttf / .otf in ./fonts and expose:

    FONT_DIR  – absolute Path object
    FONTS     – dict { "PlayfairDisplay-Bold": Path("/.../fonts/PlayfairDisplay-Bold.ttf"), ... }
"""

from pathlib import Path

# ───────────────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
FONT_DIR = BASE_DIR / "fonts"          # ✅ keep all static TTF/OTF files here
FONT_EXT = {".ttf", ".otf"}            # what we consider a font
# ───────────────────────────────────────────────────────────────────────────────

def _discover_fonts():
    """Return dict {stem:str -> Path} for every file in FONT_DIR with wanted ext."""
    fonts = {}
    for p in FONT_DIR.glob("*"):
        if p.suffix.lower() in FONT_EXT:
            fonts[p.stem] = p
    return fonts

FONTS = _discover_fonts()

# # debug
# if __name__ == "__main__":
#     print(f"Found {len(FONTS)} fonts:")
#     for name, path in FONTS.items():
#         print(" •", name, "→", path.name)
