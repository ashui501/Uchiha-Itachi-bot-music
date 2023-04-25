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
  •`{i}batman`
  •`{i}neon`
  •`{i}golden`
  •`{i}zoro`
  •`{i}zombie`

"""

import os
import numpy as np

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


@ultroid_cmd(pattern="(cmask|sosmas|toxic|anon|clown|krish|n95|batman|neon|golden|zoro|zombie)$")
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
    input_image = cv2.imread(ultt).astype(np.uint8)
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("./resources/face.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if match == "sosmas":
        os.system("wget https://telegra.ph/file/f061c861ba85fbb23a51e.png")
        maskPath = "f061c861ba85fbb23a51e.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "toxic":
        os.system("wget https://telegra.ph/file/df2d739544595ae337642.png")
        maskPath = "df2d739544595ae337642.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "anon":
        os.system("wget https://telegra.ph/file/4cc40d1e0846667488341.png")
        maskPath = "4cc40d1e0846667488341.png"
        mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
        for (x, y, w, h) in faces:
            resized_mask = cv2.resize(mask, (w, h))
        mask_image = np.zeros((input_image.shape[0], input_image.shape[1], resized_mask.shape[2]), dtype=resized_mask.dtype)
        mask_image[y:y+h, x:x+w, :] = cv2.resize(resized_mask, (w, h))
        resized_input_image = cv2.resize(input_image, (w, h)).astype(resized_mask.dtype)
        masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
        masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], cv2.resize(resized_mask, (w, h)))
        output_path = "cipherx/cipherx.jpg"
        cv2.imwrite(output_path, masked_image)
    elif match == "clown":
        os.system("wget https://telegra.ph/file/55fcb205c6f8f4790585e.png")
        maskPath = "55fcb205c6f8f4790585e.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "krish":
        os.system("wget https://telegra.ph/file/54d2a267d411951b41a20.png")
        maskPath = "54d2a267d411951b41a20.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "n95":
        os.system("wget https://telegra.ph/file/b934a713abb321bd1a9fe.png")
        maskPath = "b934a713abb321bd1a9fe.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "batman":
        os.system("wget https://graph.org/file/438b017f522e92e292207.png")
        maskPath = "438b017f522e92e292207.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "neon":
        os.system("wget https://graph.org/file/f1c6109df4e3389379501.png")
        maskPath = "f1c6109df4e3389379501.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "golden":
        os.system("wget https://graph.org/file/11fff712ae37da38c8c87.png")
        maskPath = "11fff712ae37da38c8c87.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "zoro":
        os.system("wget https://graph.org/file/a71bfbc5f86cb094161eb.png")
        maskPath = "a71bfbc5f86cb094161eb.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    elif match == "zombie":
        os.system("wget https://graph.org/file/e61967306ec8802534e74.png")
        maskPath = "e61967306ec8802534e74.png"
        for (x, y, w, h) in faces:
            mask = cv2.imread(maskPath, cv2.IMREAD_UNCHANGED)
            resized_mask = cv2.resize(mask, (w, h))
            mask_image = np.zeros(input_image.shape[:2], dtype=np.uint8)
            mask_image[y:y+h, x:x+w] = 255
            resized_input_image = cv2.resize(input_image, (w, h))
            masked_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=mask_image)
            masked_image[y:y+h, x:x+w] = cv2.add(masked_image[y:y+h, x:x+w], resized_mask)
            output_path = "cipherx/cipherx.jpg"
            cv2.imwrite(output_path, masked_image)
    await ureply.reply(
        file=output_path,
        force_document=False,
    )
    os.remove(maskPath)
    os.remove(ultt)
    os.remove(output_path)
    await xx.delete()
