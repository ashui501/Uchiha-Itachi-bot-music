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

@ultroid_cmd(pattern="(cmask|sosmas|toxic|anon|clown|krish|n95)$")
async def scan(event):
    match = event.pattern_match.group(1)
    ureply = await event.get_reply_message()
    xx = await event.eor("`...`")
    if not (ureply and (ureply.media)):
        await xx.edit(get_string("cvt_3"))
        return
    ultt = await event.client.download_media(ureply.media, "cipherx/")
    if ultt.endswith(".tgs"):
        xx = await xx.edit(get_string("sts_9"))
    file = await con.convert(ultt, convert_to="png", outname="ult")
    cascPath = "./resources/face.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    ult = cv2.imread(file)
    ultroid = cv2.cvtColor(ult, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(ultroid, 1.15)
    background = Image.open(ultt)
    if match == "cmask":
        for (x, y, w, h) in faces:
            mask = Image.open(ultt)
            mask = mask.resize((w, h), Image.ANTIALIAS)
            offset = (x, y)
            background.paste(mask, offset, mask=mask)
    elif match == "sosmas":
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
    file_name = "cipherx.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await ureply.reply(
        file=hehe,
        force_document=False,
    )
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
    await xx.delete()
