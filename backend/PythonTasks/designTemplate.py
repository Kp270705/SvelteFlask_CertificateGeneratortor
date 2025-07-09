

# from PIL import Image, ImageEnhance


# def expandListArgstoVar(args):
#   mediaDict = {
#   "backgroundImagePath" : "",
#   "logo1Path"           : "",
#   "logo2Path"           : "",
#   "linepath"            : "",
#   "auth1Path"           : "",
#   "auth2Path"           : "",
#   }
#   mediaList = ["backgroundImagePath", "logo1Path", "logo2Path", "linepath", "auth1Path", "auth2Path"]
#   for i in range(0, len(mediaList)):
#     mediaDict[mediaList[i]] = args[i]
#   return mediaDict


# def openImage(imagePath):
#   imgObj = Image.open(f"{imagePath}").convert('RGBA')
#   return imgObj

# # -----------------------------------------------------------------------------


# def templatedesign1_2_3(args):
#   # print(f"\nIn templatedesign_1_2_3()")
#   paths = expandListArgstoVar(args)
#   background_image = Image.open(paths["backgroundImagePath"]).convert('RGBA')
#   a4_width = 3508
#   a4_height = 2480
#   background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)

#   logo_image1 = Image.open(paths["logo1Path"]).convert('RGBA')  # Ensure RGBA mode
#   logo_width, logo_height = logo_image1.size
#   if logo_height == logo_width:
#     logo1_new_width = int(a4_width/8)
#     logo1_new_height = int(a4_height/6)

#   else:
#     logo1_new_width = int(a4_width/4)
#     logo1_new_height = int(a4_height/8)

#   logo1_position = (90, 120) 
#   logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
#   mask = logo_image1.getchannel('A')
#   background_image.paste(logo_image1, logo1_position, mask)


#   if not (paths["logo2Path"] == None):
#     logo_image2 = Image.open(f"{paths["logo2Path"]}").convert('RGBA')  # Ensure RGBA mode
#     logo2_width, logo2_height = logo_image2.size
#     if logo2_height == logo2_width:
#       logo2_new_width = int(a4_width/8)
#       logo2_new_height = int(a4_height/6)

#     else:
#       logo2_new_width = int(a4_width/3)
#       logo2_new_height = int(a4_height/5)

#     logo2_position = (2800, 1950) 
#     logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
#     mask2 = logo_image2.getchannel('A')
#     background_image.paste(logo_image2, logo2_position, mask2)



#   auth1_sign = Image.open(f"{paths["auth1Path"]}").convert('RGBA')  # Ensure RGBA mode
#   auth1_sign_width = int(a4_width/9)
#   auth1_sign_height = int(a4_height/10)
#   position3 = (1000, 1900)
#   auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)
#   mask3 = auth1_sign.getchannel('A')
#   background_image.paste(auth1_sign, position3, mask3)



#   auth2_sign = Image.open(f"{paths["auth2Path"]}").convert('RGBA')  # Ensure RGBA mode
#   auth2_sign_width = int(a4_width/9)
#   auth2_sign_height = int(a4_height/10)
#   position4 = (2050, 1900)
#   auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)
#   mask4 = auth2_sign.getchannel('A')
#   background_image.paste(auth2_sign, position4, mask4)



#   line1 = Image.open(f"{paths["linepath"]}").convert('RGBA')  # Ensure RGBA mode
#   line1_width = int(a4_width/5)
#   line1_height = int(a4_height/5)
#   position5 = (850, 1900)
#   line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
#   mask5 = line1.getchannel('A')
#   background_image.paste(line1, position5, mask5)



#   line2 = Image.open(f"{paths["linepath"]}").convert('RGBA')  # Ensure RGBA mode
#   line2_width = int(a4_width/5)
#   line2_height = int(a4_height/5)
#   position6 = (1850, 1900)
#   line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
#   mask6 = line2.getchannel('A')
#   background_image.paste(line2, position6, mask6)


#   # Paste the logo image with transparency mask

#   # Save the resulting image as PNG
#   output_image_path = f"./static/Images/Home/FinalTemplate/finalTemplate.png"
#   background_image.save(output_image_path, quality=75)
#   background_image.save(output_image_path, format='PNG')
#   # print(f"\nTemplate created...")
#   return output_image_path


# # -----------------------------------------------------------------------------


# def templatedesign4(args):
#   print(f"\nIn templatedesign4()")
#   paths = expandListArgstoVar(args)
#   print(f"line1 path: {paths["linepath"]}")
#   background_image = openImage(paths["backgroundImagePath"])
#   a4_width = 3508
#   a4_height = 2480
#   background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)


#   logo_image1 = openImage(paths["logo1Path"])
#   logo_width, logo_height = logo_image1.size
#   if logo_height == logo_width:
#     logo1_new_width = int(a4_width/8)
#     logo1_new_height = int(a4_height/6)

#   else:
#     logo1_new_width = int(a4_width/4)
#     logo1_new_height = int(a4_height/8)

#   logo1_position = (30, 2050) 
#   logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
#   mask = logo_image1.getchannel('A')
#   background_image.paste(logo_image1, logo1_position, mask)


#   if not(paths["logo2Path"] == None):
#     logo_image2 = openImage(paths["logo2Path"])  # Ensure RGBA mode
#     logo2_width, logo2_height = logo_image2.size
#     if logo2_height == logo2_width:
#       logo2_new_width = int(a4_width/8)
#       logo2_new_height = int(a4_height/6)

#     else:
#       logo2_new_width = int(a4_width/3)
#       logo2_new_height = int(a4_height/5)

#     logo2_position = (3100, 3) 
#     logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
#     mask2 = logo_image2.getchannel('A')
#     background_image.paste(logo_image2, logo2_position, mask2)



#   auth1_sign = openImage(paths["auth1Path"])
#   auth1_sign_width = int(a4_width/9)
#   auth1_sign_height = int(a4_height/12)
#   position3 = (1000, 1950)
#   auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)
#   mask3 = auth1_sign.getchannel('A')
#   background_image.paste(auth1_sign, position3, mask3)
  



#   auth2_sign = openImage(paths["auth2Path"])
#   auth2_sign_width = int(a4_width/9)
#   auth2_sign_height = int(a4_height/10)
#   position4 = (2050, 1900)
#   auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)
#   mask4 = auth2_sign.getchannel('A')
#   background_image.paste(auth2_sign, position4, mask4)



#   line1 = openImage(paths["linepath"])
#   line1_width = int(a4_width/5)
#   line1_height = int(a4_height/5)
#   position5 = (950, 1900)
#   line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
#   mask5 = line1.getchannel('A')
#   background_image.paste(line1, position5, mask5)



#   line2 = openImage(paths["linepath"])
#   line2_width = int(a4_width/5)
#   line2_height = int(a4_height/5)
#   position6 = (1860, 1900)
#   line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
#   mask6 = line2.getchannel('A')
#   background_image.paste(line2, position6, mask6)


#   # Save the resulting image as PNG
#   output_image_path = f"./static/Images/Home/FinalTemplate/finalTemplate.png"
#   background_image.save(output_image_path, quality=75)
#   background_image.save(output_image_path, format='PNG')
#   return output_image_path


# # ------------------------------------------------------------------------------------------------------------


# def templatedesign5(args):
#   print(f"\nIn templatedesign5()")
#   paths = expandListArgstoVar(args)
#   background_image = openImage(paths["backgroundImagePath"])
#   a4_width = 3508
#   a4_height = 2480
#   background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)
#   print(f"Final Bg image resolution is: {background_image.size}")

#   logo_image1 = openImage(paths["logo1Path"])
#   logo_width, logo_height = logo_image1.size
#   if logo_height == logo_width:
#     logo1_new_width = int(a4_width/12)
#     logo1_new_height = int(a4_height/8)

#   else:
#     logo1_new_width = int(a4_width/4)
#     logo1_new_height = int(a4_height/8)

#   logo1_position = (1609, 518) 
#   logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
#   print(f"Logo image resolution is: {logo_image1.size}")
#   mask = logo_image1.getchannel('A')
#   background_image.paste(logo_image1, logo1_position, mask)



#   if not (paths["logo2Path"] == None):
#     logo_image2 = openImage(paths["logo2Path"])  # Ensure RGBA mode
#     logo2_width, logo2_height = logo_image2.size
#     print(f"Logo2 image resolution is: {logo_image2.size}")

#     if logo2_height == logo2_width:
#       logo2_new_width = int(a4_width/10)
#       logo2_new_height = int(a4_height/8)

#     else:
#       logo2_new_width = int(a4_width/3)
#       logo2_new_height = int(a4_height/5)

#     logo2_position = (550, 2000) 
#     logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
#     mask2 = logo_image2.getchannel('A')
#     background_image.paste(logo_image2, logo2_position, mask2)



#   auth1_sign = openImage(paths["auth1Path"])
#   auth1_sign_width = int(a4_width/9)
#   auth1_sign_height = int(a4_height/12)
#   position3 = (1150, 1900)
#   auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)
#   mask3 = auth1_sign.getchannel('A')
#   background_image.paste(auth1_sign, position3, mask3)



#   auth2_sign = openImage(paths["auth2Path"])
#   auth2_sign_width = int(a4_width/9)
#   auth2_sign_height = int(a4_height/12)
#   position4 = (2050, 1900)
#   auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)
#   mask4 = auth2_sign.getchannel('A')
#   background_image.paste(auth2_sign, position4, mask4)


#   line1 = openImage(paths["linepath"])
#   line1_width = int(a4_width/5)
#   line1_height = int(a4_height/5)
#   position5 = (1050, 1900)
#   line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
#   mask5 = line1.getchannel('A')
#   background_image.paste(line1, position5, mask5)



#   line2 = openImage(paths["linepath"])
#   line2_width = int(a4_width/5)
#   line2_height = int(a4_height/5)
#   position6 = (1900, 1900)
#   line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
#   mask6 = line2.getchannel('A')
#   background_image.paste(line2, position6, mask6)


#   # Paste the logo image with transparency mask

#   # Save the resulting image as PNG
#   output_image_path = f"./static/Images/Home/FinalTemplate/finalTemplate.png"
#   background_image.save(output_image_path, quality=75)
#   background_image.save(output_image_path, format='PNG')
#   return output_image_path

# # ------------------------------------------------------------------------------------------------------------


# def templatedesign2b(backgroundImagePath, logo1Path, auth1Path, auth2Path):

#     # Open the images:
#     background_image = Image.open(backgroundImagePath).convert('RGBA')


#     auth1_sign = Image.open(f"{auth1Path}").convert('RGBA')  # Ensure RGBA mode
#     auth1_sign_width = 700
#     auth1_sign_height = 200
#     position3 = (950, 1950)
#     auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)

#     auth2_sign = Image.open(f"{auth2Path}").convert('RGBA')  # Ensure RGBA mode
#     auth2_sign_width = 800
#     auth2_sign_height = 200
#     position4 = (1900, 1950)
#     auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)

#     # Get a mask from the alpha channel
#     mask3 = auth1_sign.getchannel('A')
#     mask4 = auth2_sign.getchannel('A')

#     # Paste the images with transparency mask:
#     background_image.paste(auth1_sign, position3, mask3)
#     background_image.paste(auth2_sign, position4, mask4)

#     # Save the resulting image as PNG
#     output_image_path = "./static/Images/finalTemplate.png"
#     background_image.save(output_image_path, quality=75)
#     background_image.save(output_image_path, format='PNG')

#     # print(f"Image created suauth1essfully! Saved as: {output_image_path}")

#     return output_image_path

# # -----------------------------------------------------------------------------


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
    out_path = "./randomStaticContent/finalTemplate.png"
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
