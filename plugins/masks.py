"""
✘ Commands Available -
  Filters Available:
  •`{i}cmask`
  •`{i}sosmas`
  •`{i}toxic`
  •`{i}anon`
  •`{i}clown`
  •`{i}krish`
  •`{i}n95`
  •`{i}momo`
  •`{i}neon`
  •`{i}skelet`
  •`{i}golden`
  •`{i}zoro`
  •`{i}zombie`

"""

import os

if not os.path.isdir("./cipherx/"):
    os.makedirs("./cipherx/")
    
try:
    import cv2
except ImportError:
    LOGS.error(f"{__file__}: OpenCv not Installed.")
    
try:
    from PIL import Image
except ImportError:
    Image = None
    LOGS.info(f"{__file__}: PIL  not Installed.")
    
from . import *

@ultroid_cmd(pattern="(cmask|sosmas|toxic|anon|clown|krish|n95|momo|neon|skelet|golden|zoro|zombie)$")
async def scan(event):
    match = event.pattern_match.group(1)
    ureply = await event.get_reply_message()
    xx = await event.eor("`...`")
    if not (ureply and (ureply.media)):
        await xx.edit(get_string("cvt_3"))
        return
    ultt = await event.client.download_media(ureply.media, "./cipherx/")
    if ultt.endswith(".tgs"):
        xx = await xx.edit(get_string("sts_9"))
        ultt = await con.convert(ultt, convert_to="png", outname="ult")
    cascPath = "./resources/face.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    ult = cv2.imread(ultt)
    ultroid = cv2.cvtColor(ult, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(ultroid, 1.15)
    background = Image.open(ultt)
    if match == "sosmas":
        os.system("wget https://telegra.ph/file/f061c861ba85fbb23a51e.png")
        maskPath = "f061c861ba85fbb23a51e.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "toxic":
        os.system("wget https://telegra.ph/file/df2d739544595ae337642.png")
        maskPath = "df2d739544595ae337642.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "anon":
        os.system("wget https://telegra.ph/file/4cc40d1e0846667488341.png")
        maskPath = "4cc40d1e0846667488341.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "clown":
        os.system("wget https://telegra.ph/file/55fcb205c6f8f4790585e.png")
        maskPath = "55fcb205c6f8f4790585e.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "krish":
        os.system("wget https://telegra.ph/file/54d2a267d411951b41a20.png")
        maskPath = "54d2a267d411951b41a20.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "n95":
        os.system("wget https://telegra.ph/file/b934a713abb321bd1a9fe.png")
        maskPath = "b934a713abb321bd1a9fe.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "momo":
        os.system("wget https://graph.org/file/5ebbf5298f6c46b84883a.jpg")
        maskPath = "5ebbf5298f6c46b84883a.jpg"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "neon":
        os.system("wget https://graph.org/file/27d21d43df7b60e385371.jpg")
        maskPath = "27d21d43df7b60e385371.jpg"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "skelet":
        os.system("wget https://graph.org/file/48b12c7d2a79475be0daf.png")
        maskPath = "48b12c7d2a79475be0daf.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "golden":
        os.system("wget https://graph.org/file/11fff712ae37da38c8c87.png")
        maskPath = "11fff712ae37da38c8c87.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "zoro":
        os.system("wget https://graph.org/file/a71bfbc5f86cb094161eb.png")
        maskPath = "a71bfbc5f86cb094161eb.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "zombie":
        os.system("wget https://graph.org/file/8908cd2b3595a1be14726.png")
        maskPath = "8908cd2b3595a1be14726.png"
        for (x, y, w, h) in faces:
            mask = Image.open(maskPath)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    file_name = "cipherx.png"
    path = "./cipherx"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await ureply.reply(
        file=hehe,
        force_document=False,
    )
    for files in (hehe, ultt):
        if files and os.path.exists(files):
            os.remove(files)
    await xx.delete()
