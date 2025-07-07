

from PIL import Image, ImageEnhance


def expandListArgstoVar(args):
  mediaDict = {
  "backgroundImagePath" : "",
  "logo1Path"           : "",
  "logo2Path"           : "",
  "linepath"            : "",
  "auth1Path"           : "",
  "auth2Path"           : "",
  }
  mediaList = ["backgroundImagePath", "logo1Path", "logo2Path", "linepath", "auth1Path", "auth2Path"]
  for i in range(0, len(mediaList)):
    mediaDict[mediaList[i]] = args[i]
  return mediaDict


def openImage(imagePath):
  imgObj = Image.open(f"{imagePath}").convert('RGBA')
  return imgObj

# -----------------------------------------------------------------------------


def templatedesign1_2_3(args):
  # print(f"\nIn templatedesign_1_2_3()")
  paths = expandListArgstoVar(args)
  background_image = Image.open(paths["backgroundImagePath"]).convert('RGBA')
  a4_width = 3508
  a4_height = 2480
  background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)

  logo_image1 = Image.open(paths["logo1Path"]).convert('RGBA')  # Ensure RGBA mode
  logo_width, logo_height = logo_image1.size
  if logo_height == logo_width:
    logo1_new_width = int(a4_width/8)
    logo1_new_height = int(a4_height/6)

  else:
    logo1_new_width = int(a4_width/4)
    logo1_new_height = int(a4_height/8)

  logo1_position = (90, 120) 
  logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
  mask = logo_image1.getchannel('A')
  background_image.paste(logo_image1, logo1_position, mask)


  if not (paths["logo2Path"] == None):
    logo_image2 = Image.open(f"{paths["logo2Path"]}").convert('RGBA')  # Ensure RGBA mode
    logo2_width, logo2_height = logo_image2.size
    if logo2_height == logo2_width:
      logo2_new_width = int(a4_width/8)
      logo2_new_height = int(a4_height/6)

    else:
      logo2_new_width = int(a4_width/3)
      logo2_new_height = int(a4_height/5)

    logo2_position = (2800, 1950) 
    logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
    mask2 = logo_image2.getchannel('A')
    background_image.paste(logo_image2, logo2_position, mask2)



  auth1_sign = Image.open(f"{paths["auth1Path"]}").convert('RGBA')  # Ensure RGBA mode
  auth1_sign_width = int(a4_width/9)
  auth1_sign_height = int(a4_height/10)
  position3 = (1000, 1900)
  auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)
  mask3 = auth1_sign.getchannel('A')
  background_image.paste(auth1_sign, position3, mask3)



  auth2_sign = Image.open(f"{paths["auth2Path"]}").convert('RGBA')  # Ensure RGBA mode
  auth2_sign_width = int(a4_width/9)
  auth2_sign_height = int(a4_height/10)
  position4 = (2050, 1900)
  auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)
  mask4 = auth2_sign.getchannel('A')
  background_image.paste(auth2_sign, position4, mask4)



  line1 = Image.open(f"{paths["linepath"]}").convert('RGBA')  # Ensure RGBA mode
  line1_width = int(a4_width/5)
  line1_height = int(a4_height/5)
  position5 = (850, 1900)
  line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
  mask5 = line1.getchannel('A')
  background_image.paste(line1, position5, mask5)



  line2 = Image.open(f"{paths["linepath"]}").convert('RGBA')  # Ensure RGBA mode
  line2_width = int(a4_width/5)
  line2_height = int(a4_height/5)
  position6 = (1850, 1900)
  line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
  mask6 = line2.getchannel('A')
  background_image.paste(line2, position6, mask6)


  # Paste the logo image with transparency mask

  # Save the resulting image as PNG
  output_image_path = f"./static/Images/Home/FinalTemplate/finalTemplate.png"
  background_image.save(output_image_path, quality=75)
  background_image.save(output_image_path, format='PNG')
  # print(f"\nTemplate created...")
  return output_image_path


# -----------------------------------------------------------------------------


def templatedesign4(args):
  print(f"\nIn templatedesign4()")
  paths = expandListArgstoVar(args)
  print(f"line1 path: {paths["linepath"]}")
  background_image = openImage(paths["backgroundImagePath"])
  a4_width = 3508
  a4_height = 2480
  background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)


  logo_image1 = openImage(paths["logo1Path"])
  logo_width, logo_height = logo_image1.size
  if logo_height == logo_width:
    logo1_new_width = int(a4_width/8)
    logo1_new_height = int(a4_height/6)

  else:
    logo1_new_width = int(a4_width/4)
    logo1_new_height = int(a4_height/8)

  logo1_position = (30, 2050) 
  logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
  mask = logo_image1.getchannel('A')
  background_image.paste(logo_image1, logo1_position, mask)


  if not(paths["logo2Path"] == None):
    logo_image2 = openImage(paths["logo2Path"])  # Ensure RGBA mode
    logo2_width, logo2_height = logo_image2.size
    if logo2_height == logo2_width:
      logo2_new_width = int(a4_width/8)
      logo2_new_height = int(a4_height/6)

    else:
      logo2_new_width = int(a4_width/3)
      logo2_new_height = int(a4_height/5)

    logo2_position = (3100, 3) 
    logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
    mask2 = logo_image2.getchannel('A')
    background_image.paste(logo_image2, logo2_position, mask2)



  auth1_sign = openImage(paths["auth1Path"])
  auth1_sign_width = int(a4_width/9)
  auth1_sign_height = int(a4_height/12)
  position3 = (1000, 1950)
  auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)
  mask3 = auth1_sign.getchannel('A')
  background_image.paste(auth1_sign, position3, mask3)
  



  auth2_sign = openImage(paths["auth2Path"])
  auth2_sign_width = int(a4_width/9)
  auth2_sign_height = int(a4_height/10)
  position4 = (2050, 1900)
  auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)
  mask4 = auth2_sign.getchannel('A')
  background_image.paste(auth2_sign, position4, mask4)



  line1 = openImage(paths["linepath"])
  line1_width = int(a4_width/5)
  line1_height = int(a4_height/5)
  position5 = (950, 1900)
  line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
  mask5 = line1.getchannel('A')
  background_image.paste(line1, position5, mask5)



  line2 = openImage(paths["linepath"])
  line2_width = int(a4_width/5)
  line2_height = int(a4_height/5)
  position6 = (1860, 1900)
  line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
  mask6 = line2.getchannel('A')
  background_image.paste(line2, position6, mask6)


  # Save the resulting image as PNG
  output_image_path = f"./static/Images/Home/FinalTemplate/finalTemplate.png"
  background_image.save(output_image_path, quality=75)
  background_image.save(output_image_path, format='PNG')
  return output_image_path


# ------------------------------------------------------------------------------------------------------------


def templatedesign5(args):
  print(f"\nIn templatedesign5()")
  paths = expandListArgstoVar(args)
  background_image = openImage(paths["backgroundImagePath"])
  a4_width = 3508
  a4_height = 2480
  background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)
  print(f"Final Bg image resolution is: {background_image.size}")

  logo_image1 = openImage(paths["logo1Path"])
  logo_width, logo_height = logo_image1.size
  if logo_height == logo_width:
    logo1_new_width = int(a4_width/12)
    logo1_new_height = int(a4_height/8)

  else:
    logo1_new_width = int(a4_width/4)
    logo1_new_height = int(a4_height/8)

  logo1_position = (1609, 518) 
  logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
  print(f"Logo image resolution is: {logo_image1.size}")
  mask = logo_image1.getchannel('A')
  background_image.paste(logo_image1, logo1_position, mask)



  if not (paths["logo2Path"] == None):
    logo_image2 = openImage(paths["logo2Path"])  # Ensure RGBA mode
    logo2_width, logo2_height = logo_image2.size
    print(f"Logo2 image resolution is: {logo_image2.size}")

    if logo2_height == logo2_width:
      logo2_new_width = int(a4_width/10)
      logo2_new_height = int(a4_height/8)

    else:
      logo2_new_width = int(a4_width/3)
      logo2_new_height = int(a4_height/5)

    logo2_position = (550, 2000) 
    logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
    mask2 = logo_image2.getchannel('A')
    background_image.paste(logo_image2, logo2_position, mask2)



  auth1_sign = openImage(paths["auth1Path"])
  auth1_sign_width = int(a4_width/9)
  auth1_sign_height = int(a4_height/12)
  position3 = (1150, 1900)
  auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)
  mask3 = auth1_sign.getchannel('A')
  background_image.paste(auth1_sign, position3, mask3)



  auth2_sign = openImage(paths["auth2Path"])
  auth2_sign_width = int(a4_width/9)
  auth2_sign_height = int(a4_height/12)
  position4 = (2050, 1900)
  auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)
  mask4 = auth2_sign.getchannel('A')
  background_image.paste(auth2_sign, position4, mask4)


  line1 = openImage(paths["linepath"])
  line1_width = int(a4_width/5)
  line1_height = int(a4_height/5)
  position5 = (1050, 1900)
  line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
  mask5 = line1.getchannel('A')
  background_image.paste(line1, position5, mask5)



  line2 = openImage(paths["linepath"])
  line2_width = int(a4_width/5)
  line2_height = int(a4_height/5)
  position6 = (1900, 1900)
  line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
  mask6 = line2.getchannel('A')
  background_image.paste(line2, position6, mask6)


  # Paste the logo image with transparency mask

  # Save the resulting image as PNG
  output_image_path = f"./static/Images/Home/FinalTemplate/finalTemplate.png"
  background_image.save(output_image_path, quality=75)
  background_image.save(output_image_path, format='PNG')
  return output_image_path

# ------------------------------------------------------------------------------------------------------------


def templatedesign2b(backgroundImagePath, logo1Path, auth1Path, auth2Path):

    # Open the images:
    background_image = Image.open(backgroundImagePath).convert('RGBA')


    auth1_sign = Image.open(f"{auth1Path}").convert('RGBA')  # Ensure RGBA mode
    auth1_sign_width = 700
    auth1_sign_height = 200
    position3 = (950, 1950)
    auth1_sign = auth1_sign.resize((auth1_sign_width, auth1_sign_height), Image.LANCZOS)

    auth2_sign = Image.open(f"{auth2Path}").convert('RGBA')  # Ensure RGBA mode
    auth2_sign_width = 800
    auth2_sign_height = 200
    position4 = (1900, 1950)
    auth2_sign = auth2_sign.resize((auth2_sign_width, auth2_sign_height), Image.LANCZOS)

    # Get a mask from the alpha channel
    mask3 = auth1_sign.getchannel('A')
    mask4 = auth2_sign.getchannel('A')

    # Paste the images with transparency mask:
    background_image.paste(auth1_sign, position3, mask3)
    background_image.paste(auth2_sign, position4, mask4)

    # Save the resulting image as PNG
    output_image_path = "./static/Images/finalTemplate.png"
    background_image.save(output_image_path, quality=75)
    background_image.save(output_image_path, format='PNG')

    # print(f"Image created suauth1essfully! Saved as: {output_image_path}")

    return output_image_path

# -----------------------------------------------------------------------------