from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
ROOT_DIR  = BASE_DIR.parent 
FONT_DIR = ROOT_DIR / "fonts"
FONT_EXT = {".ttf", ".otf"}

def _discover_fonts():
    fonts = {}
    for p in FONT_DIR.glob("*"):
        if p.suffix.lower() in FONT_EXT:
            fonts[p.stem] = p
    return fonts

FONTS = _discover_fonts()

