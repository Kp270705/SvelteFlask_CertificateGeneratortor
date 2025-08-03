#########################################################################################################################

from __future__ import annotations
from pathlib import Path
from typing import List

from PIL import Image, ImageOps, ImageEnhance, ImageStat, ImageChops
import numpy as np


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def _open_rgba(path: str | Path) -> Image.Image:
    """Open an image and force RGBA."""
    return Image.open(path).convert("RGBA")


def _is_fully_opaque(img: Image.Image) -> bool:
    """
    Return True if the alpha channel is 255 everywhere
    (i.e. no transparency at all).
    """
    if img.mode != "RGBA":
        return True
    alpha = img.getchannel("A")
    lo, hi = alpha.getextrema()
    return hi == 255 and lo == 255


def _strip_white_edges(img: Image.Image, thresh: int = 245) -> Image.Image:
    """
    Flood‑fill from edges to make nearly‑white pixels transparent.
    Keeps interior white shapes (letters) untouched.
    """
    img = img.convert("RGBA")
    data = np.array(img)
    # mask of bright pixels
    white = (data[..., :3] > thresh).all(axis=-1)

    h, w = white.shape
    stack = [(x, 0)   for x in range(w)] + \
            [(x, h-1) for x in range(w)] + \
            [(0, y)   for y in range(h)] + \
            [(w-1, y) for y in range(h)]

    while stack:
        x, y = stack.pop()
        if 0 <= x < w and 0 <= y < h and white[y, x]:
            white[y, x] = False
            data[y, x, 3] = 0          # alpha -> 0
            stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

    return Image.fromarray(data, "RGBA")


def _resize_keep_ratio(img: Image.Image, max_w: int, max_h: int) -> Image.Image:
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    return img


# ---------------------------------------------------------------------------
# Template constructor
# ---------------------------------------------------------------------------

def templatedesign1_2_3(paths: List[str | Path]) -> str:

    bg_path, logo1_path, logo2_path, line_path, sig1_path, sig2_path = paths

    # --- Background --------------------------------------------------------
    A4_W, A4_H = 3508, 2480  # landscape 300 dpi
    bg = _open_rgba(bg_path).resize((A4_W, A4_H), Image.LANCZOS)

    # --- Logo 1 : top‑left --------------------------------------------------
    if logo1_path:
        logo1 = _open_rgba(logo1_path)
        if _is_fully_opaque(logo1):
            logo1 = _strip_white_edges(logo1)

        _resize_keep_ratio(logo1, A4_W // 4, A4_H // 5)
        bg.paste(logo1, (80, 120), logo1)

    # --- Logo 2 : bottom‑right ---------------------------------------------
    if logo2_path:
        logo2 = _open_rgba(logo2_path)
        if _is_fully_opaque(logo2):
            logo2 = _strip_white_edges(logo2)

        _resize_keep_ratio(logo2, A4_W // 4, A4_H // 5)
        margin = 120
        x = A4_W - margin - logo2.width + 40
        y = A4_H - margin - logo2.height
        print(f"x,y: {x},{y}")
        bg.paste(logo2, (x, y), logo2)

    # --- Signature images ---------------------------------------------------
    if sig1_path:
        sig1 = _open_rgba(sig1_path)
        _resize_keep_ratio(sig1, A4_W // 9, A4_H // 10)
        bg.paste(sig1, (1000, 1900), sig1)

    if sig2_path:
        sig2 = _open_rgba(sig2_path)
        _resize_keep_ratio(sig2, A4_W // 9, A4_H // 10)
        bg.paste(sig2, (2050, 1900), sig2)

    # --- Lines under signatures --------------------------------------------
    if line_path:
        line = _open_rgba(line_path)
        _resize_keep_ratio(line, A4_W // 5, A4_H // 5)
        bg.paste(line, (850, 1900), line)
        bg.paste(line, (1850, 1900), line)

    # --- Save final ---------------------------------------------------------
    out_path = "./static/Images/finalCertTemplate/finalTemplate.png"
    bg.save(out_path, format="PNG", optimize=True, quality=85)
    print("✅ Template created:", out_path)
    return out_path



# ---------------------------------------------------------------------------
# TEMPLATE 4  –  “Green/Black” layout
# ---------------------------------------------------------------------------
def templatedesign4(paths: List[str | Path]) -> str:
    bg_path, logo_bl_path, logo_tr_path, line_path, sig1_path, sig2_path = paths

    # --- Constants --------------------------------------------------------
    A4_W, A4_H = 3508, 2480          # landscape 300 dpi
    SIDE_MARGIN   = 60               # used for top‑right logo
    TOP_MARGIN    = 60
    BOTTOM_MARGIN = 60               # for bottom‑left logo

    # --- Background -------------------------------------------------------
    bg = _open_rgba(bg_path).resize((A4_W, A4_H), Image.LANCZOS)

    # --- Logo • bottom‑left (organisation) --------------------------------
    if logo_bl_path:
        logo_bl = _open_rgba(logo_bl_path)
        if _is_fully_opaque(logo_bl):
            logo_bl = _strip_white_edges(logo_bl)

        # keep aspect
        if logo_bl.height == logo_bl.width:
            max_w, max_h = A4_W // 8, A4_H // 6
        else:
            max_w, max_h = A4_W // 4, A4_H // 8
        _resize_keep_ratio(logo_bl, max_w, max_h)

        x_bl = SIDE_MARGIN
        y_bl = A4_H - BOTTOM_MARGIN - logo_bl.height
        bg.paste(logo_bl, (x_bl, y_bl), logo_bl)

    # --- Logo • top‑right (event) -----------------------------------------
    if logo_tr_path:
        logo_tr = _open_rgba(logo_tr_path)
        if _is_fully_opaque(logo_tr):
            logo_tr = _strip_white_edges(logo_tr)

        if logo_tr.height == logo_tr.width:
            max_w, max_h = A4_W // 8, A4_H // 6
        else:
            max_w, max_h = A4_W // 3, A4_H // 5
        _resize_keep_ratio(logo_tr, max_w, max_h)

        x_tr = A4_W - SIDE_MARGIN - logo_tr.width
        y_tr = TOP_MARGIN
        bg.paste(logo_tr, (x_tr, y_tr), logo_tr)

    # --- Signatures -------------------------------------------------------
    if sig1_path:
        sig1 = _open_rgba(sig1_path)
        _resize_keep_ratio(sig1, A4_W // 9, A4_H // 12)
        bg.paste(sig1, (1000, 1950), sig1)

    if sig2_path:
        sig2 = _open_rgba(sig2_path)
        _resize_keep_ratio(sig2, A4_W // 9, A4_H // 10)
        bg.paste(sig2, (2050, 1900), sig2)

    # --- Lines under signatures ------------------------------------------
    if line_path:
        line = _open_rgba(line_path)
        _resize_keep_ratio(line, A4_W // 5, A4_H // 5)
        bg.paste(line, (950, 1900), line)     # under sig1
        bg.paste(line, (1860, 1900), line)    # under sig2

    # --- Save -------------------------------------------------------------
    out_path = "./randomStaticContent/finalTemplate.png"
    bg.save(out_path, format="PNG", optimize=True, quality=85)
    print("✅ Template‑4 created:", out_path)
    return out_path
