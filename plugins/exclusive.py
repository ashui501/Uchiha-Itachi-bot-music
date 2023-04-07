"""
✘ Commands Available
• `{i}hyper <telegram link>`
    Hyperlinks the link with its message id
    
• `{i}uglitch <reply to a image>`
    Creates glitch gif of given image
    
• Voices
    `{i}chtori`
    `{i}bnzm`
    `{i}momo`
    `{i}fy`
    `{i}shafa`
    
• `{i}cname`
    Change name with live time
    
• `{i}slash`
• `{i}para`
• `{i}fl`
• `{i}question`
• `{i}oof`
• `{i}motion`
• `{i}square`
• `{i}oop`
• `{i}round`
• `{i}cipherx`
• `{i}joon`
• `{i}bigoof`
• `{i}ok`
• `{i}meme`
• `{i}rmeme`
• `{i}think`
• `{i}snake`
• `{i}police`
• `{i}gangestar`
• `{i}flower`
• `{i}melow`
• `{i}cute`
• `{i}tlol`
• `{i}teeth`
• `{i}gym`
• `{i}run`
• `{i}candy`
• `{i}kiss`
• `{i}butterfly`
• `{i}box`
• `{i}clock`
• `{i}moon`
• `{i}earth`
• `{i}smile`
• `{i}laugh`
• `{i}cat`
• `{i}poker`
• `{i}wow`
• `{i}monkey`
• `{i}starheart`
• `{i}wink`
• `{i}lip`
• `{i}her`
• `{i}donce`
• `{i}cheart`
• `{i}finger`
• `{i}billy`
• `{i}agree`
• `{i}angry`
• `{i}sad`
• `{i}amaze`
• `{i}omg`
• `{i}tongue`
• `{i}sun`
• `{i}speaker`
• `{i}heart`
• `{i}sand`
• `{i}storm`
• `{i}floodwarn`
• `{i}rain`
• `{i}brain`
• `{i}dump`
• `{i}good`
• `{i}snake`
• `{i}human`
• `{i}solar`
• `{i}smoon`
• `{i}tmoon`
• `{i}lmoon`
• `{i}town`
• `{i}bombs`
• `{i}lalol`
• `{i}lit`
• `{i}love`
• `{i}my`
• `{i}hi`
• `{i}figcar`
• `{i}figkiller`
• `{i}tgm`
• `{i}emam`
• `{i}tgn`
• `{i}tnx`
• `{i}figgm`
• `{i}fighi`
• `{i}figgn`
• `{i}sponge`
• `{i}dick`
• `{i}figlol`
• `{i}figlmao`
• `{i}fighello`
• `{i}figno`
• `{i}figtrump`
• `{i}figputin`
• `{i}figchina`
• `{i}figthink`
• `{i}figdick`
• `{i}fighappyfrog`
• `{i}figdeadfrog`
• `{i}fuck`
• `{i}jagh`
• `{i}xmas`
• `{i}eem <text>`
• `{i}fhack`
• `{i}thack`
• `{i}whack`
""" 

import os
import time
import asyncio
from collections import deque
from glitch_this import ImageGlitcher

from telethon import events
from telethon.tl import functions
from telethon.tl.types import MessageMediaPhoto
from telethon.errors import FloodWaitError

from . import * 


glitcher = ImageGlitcher()
DURATION = 100  # Set this to however many centiseconds each frame should be visible for
LOOP = 0  # Set this to how many times the gif should loop
# LOOP = 0 means infinite loop

sedpath = "./cipherx/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

joonedel = "https://filetolinktelegrambot.herokuapp.com/97876907827512/jane%20janan.ogg"

bnzm ="https://filetolinktelegrambot.herokuapp.com/334068960705004/2021-04-08_15:31:04.oga" 

play = "https://filetolinktelegrambot.herokuapp.com/534283156175340/2021-04-15_18:06:27.oga" 

fuckyou = "http://dl.Zed-Bax.ml/w/wp_CqcKnwpc=/2021-05-15_12-29-04.oga"

shafa = "https://filetolinktelegram.herokuapp.com/245526/shafa.mp3" 
    
deltime = 60
namex = str(OWNER_NAME) if OWNER_NAME else "CɪᴘʜᴇʀX"

@ultroid_bot.on(events.NewMessage)
async def Dice(event):
    if event.dice and event.dice.emoticon == "🎲":
        await event.eor(f"Dice number is {event.dice.value}")


@ultroid_bot.on(events.NewMessage)
async def Dart(event):
    if event.dice and event.dice.emoticon == "🎯":
        await event.eor(f"Dart sybl number is {event.dice.value}")


@ultroid_cmd(pattern="hyper")
async def Hyperlink(event):
    url = event.text.split(" ", maxsplit=1)[1] 
    id = event.text.split("/",maxsplit=-1)[-1]
    if not "t.me" in event.text:
        await eod(event, "Lol, Send me a telegram link 🔗", timeout=5) 
    else:
        await event.eor(f"""<a href="{url}">›› {id}</a>""", parse_mode ="HTML", link_preview=False)
        
        
@ultroid_bot.on(events.NewMessage(incoming=True))
async def destructive(e):
    if not e.is_private:
        return
    if e.media and e.media.ttl_seconds != None:
        try:
            download = await e.client.download_media(e.media, "resources/")
            await e.client.send_message('me', '✨CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ✨', file=download)
            os.remove(download)
        except Exception as ex:
            await e.client.send_message(int(udB.get_key("PMLOGGROUP")), f"Error:\n\n{ex}")
            

@ultroid_cmd(pattern="uglitch")
async def glitch(event):
    sed = await event.get_reply_message()
    okbruh = await event.eor("Glitching...")
    if isinstance(sed.media, MessageMediaPhoto):
        photolove = await event.client.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        photolove = await event.client.download_media(sed.media, sedpath)
    else:
        await event.eor("Reply to Image`")
        return
    fmt = "gif"
    pathsn = f"./cipherx/cipherx.{fmt}"
    glitch_imgs = glitcher.glitch_image(photolove, 2, gif=True, color_offset=True)
    glitch_imgs[0].save(
        pathsn,
        format="GIF",
        append_images=glitch_imgs[1:],
        save_all=True,
        duration=DURATION,
        loop=LOOP,
    )
    await event.client.send_file(event.chat_id, pathsn)
    await okbruh.delete()
    for starky in (pathsn, photolove):
        if starky and os.path.exists(starky):
            os.remove(starky)
            

@ultroid_bot.on(events.NewMessage(pattern=r"\.chtori", outgoing=True))
async def _(event):
    reply = await event.get_reply_message()
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        joonedel,
        voice_note=True,
        reply_to=reply,
    )

@ultroid_bot.on(events.NewMessage(pattern=r"\.bnzm", outgoing=True))
async def _(event):
    reply = await event.get_reply_message()
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        bnzm,
        voice_note=True,
        reply_to=reply,
    )

@ultroid_bot.on(events.NewMessage(pattern=r"\.momo", outgoing=True))
async def _(event):
    reply = await event.get_reply_message()
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        play,
        voice_note=True,
        reply_to=reply,
    )

@ultroid_bot.on(events.NewMessage(pattern=r"\.fy", outgoing=True))
async def _(event):
    reply = await event.get_reply_message()
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        fuckyou,
        voice_note=True,
        reply_to=reply,
    )

@ultroid_bot.on(events.NewMessage(pattern=r"\.shafa", outgoing=True))
async def _(event):
    reply = await event.get_reply_message()
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        shafa,
        voice_note=True,
        reply_to=reply,
    )  
    

@ultroid_cmd(pattern="cname")
async def _(event):
    sed = await event.eor("sᴛᴀʀᴛɪɴɢ ᴀᴜᴛᴏɴᴀᴍᴇ. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    await sed.eor("CɪᴘʜᴇʀX ᴀᴜᴛᴏɴᴀᴍᴇ sᴛᴀʀᴛᴇᴅ")
    if event.fwd_from:
        return
    while True:
        dictionary = {
            "0": "₀",
            "1": "₁",
            "2": "₂",
            "3": "₃",
            "4": "₄",
            "5": "₅",
            "6": "₆",
            "7": "₇",
            "8": "₈",
            "9": "₉",
        }
        HM = time.strftime("%H . %M")
        for key, value in dictionary.items():
            HM = HM.replace(key, value)
        name = f"{namex} {HM}"
        try:
            await event.client(
                functions.account.UpdateProfileRequest(first_name=name)
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(deltime)
    await eod(sed, f"CɪᴘʜᴇʀX ᴀᴜᴛᴏ ɴᴀᴍᴇ ʜᴀs ʙᴇᴇɴ sᴛᴀʀᴛᴇᴅ", timeout=3)


@ultroid_bot.on(events.NewMessage(pattern=r"\.slash", outgoing=True))
async def kek(keks):
    if keks.fwd_from:
        return
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@ultroid_bot.on(events.NewMessage(pattern=r"\.para", outgoing=True))
async def kek(keks):
    if keks.fwd_from:
        return
    """ Check yourself ;)"""
    uio = [")", "("]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])

@ultroid_bot.on(events.NewMessage(pattern=r"\.fl", outgoing=True))
async def typewriter(typew):
    if typew.fwd_from:
        return
    typew.pattern_match.group(1)
    await typew.edit("`start loading...`")
    sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▊")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▉")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▎")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▍")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    number = number + 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    sleep(0.5)
    await typew.edit("`Done!`")

@ultroid_bot.on(events.NewMessage(pattern=r"\.question", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("?¿?¿?¿"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.oof", outgoing=True))
async def Oof(e):
    if e.fwd_from:
        return
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@ultroid_bot.on(events.NewMessage(pattern=r"\.motion", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["▮", "▯", "▬", "▭", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@ultroid_bot.on(events.NewMessage(pattern=r"\.square", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["◧", "◨", "◧", "◨", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@ultroid_bot.on(events.NewMessage(pattern=r"\.oop", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["╹", "╻", "╹", "╻", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@ultroid_bot.on(events.NewMessage(pattern=r"\.round", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["⚫", "⬤", "●", "∘", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@ultroid_bot.on(events.NewMessage(pattern=r"\.ultroid_bot", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    animation_chars = [
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 5.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.13GB\n    **🔹used:** 33.77GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 158.98GB\n    **🔹recv:** 146.27GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 159720314\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 20.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 7.18GB\n    **🔹used:** 28.26GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 146.27GB\n    **🔹recv:** 124.33GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 143565654\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 60.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 6.52GB\n    **🔹used:** 35.78GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 124.33GB\n    **🔹recv:** 162.48GB\n    **🔹sent_packets:** 25655655\n    **🔹recv_packets:** 165289456\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.81GB\n    **🔹used:** 30.11GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 162.48GB\n    **🔹recv:** 175.75GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 135345655\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 80.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.76GB\n    **🔹used:** 29.35GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 175.75GB\n    **🔹recv:** 118.55GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 185466554\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 62.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.23GB\n    **🔹used:** 33.32GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 118.55GB\n    **🔹recv:** 168.65GB\n    **🔹sent_packets:** 24786554\n    **🔹recv_packets:** 156745865\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 30.6%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.75GB\n    **🔹used:** 36.54GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 168.65GB\n    **🔹recv:** 128.35GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 1475823589\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 10.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 10.20GB\n    **🔹used:** 25.40GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 128.35GB\n    **🔹recv:** 108.31GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 157865426\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.25GB\n    **🔹used:** 31.14GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 108.31GB\n    **🔹recv:** 167.17GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 124575356\n\n\n**===================**\n",
        "**===================**\n      **CɪᴘʜᴇʀX Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 76.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.01GB\n    **🔹used:** 33.27GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 167.17GB\n    **🔹recv:** 158.98GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 165455856\n\n\n**===================**\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@ultroid_cmd(pattern="joon")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("J")
        await asyncio.sleep(0.2)
        await event.edit("Joo")
        await asyncio.sleep(0.2)
        await event.edit("Jooo")
        await asyncio.sleep(0.2)
        await event.edit("Joooo")
        await asyncio.sleep(0.2)
        await event.edit("Jooooo")
        await asyncio.sleep(0.2)
        await event.edit("Joooooo")
        await asyncio.sleep(0.2)
        await event.edit("Jooooooo")
        await asyncio.sleep(0.2)
        await event.edit("Joooooooo")
        await asyncio.sleep(0.2)
        await event.edit("Jooooooooo")
        await asyncio.sleep(0.2)
        await event.edit("Joooooooooo")
        await asyncio.sleep(0.2)
        await event.edit("Joooooooooon")


@ultroid_cmd(pattern="bigoof")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 40])


@ultroid_cmd(pattern="ok")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("ok")
        await asyncio.sleep(0.3)
        await event.edit("Ok")
        await asyncio.sleep(0.3)
        await event.edit("ok")
        await asyncio.sleep(0.3)
        await event.edit("Ok")
        await asyncio.sleep(0.3)
        await event.edit("ok")
        await asyncio.sleep(0.3)
        await event.edit("Ok")
        await asyncio.sleep(0.3)
        await event.edit("ok")
        await asyncio.sleep(0.3)
        await event.edit("Ok")
        await asyncio.sleep(0.3)
        await event.edit("ok")
        await asyncio.sleep(0.3)
        await event.edit("Ok")


@ultroid_bot.on(events.NewMessage(pattern=r"\.meme", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return
    memeVar = event.text
    sleepValue = 8
    memeVar = memeVar[6:]
    await event.edit("-------------" + memeVar)
    await event.edit("------------" + memeVar + "-")
    await event.edit("-----------" + memeVar + "--")
    await event.edit("----------" + memeVar + "---")
    await event.edit("---------" + memeVar + "----")
    await event.edit("--------" + memeVar + "-----")
    await event.edit("-------" + memeVar + "------")
    await event.edit("------" + memeVar + "-------")
    await event.edit("-----" + memeVar + "--------")
    await event.edit("----" + memeVar + "---------")
    await event.edit("---" + memeVar + "----------")
    await event.edit("--" + memeVar + "-----------")
    await event.edit("-" + memeVar + "------------")
    await event.edit(memeVar + "-------------")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)


@ultroid_bot.on(events.NewMessage(pattern=r"\.rmeme", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return
    memeVar = event.text
    sleepValue = 8
    memeVar = memeVar[6:]
    await event.edit("-------------" + memeVar)
    await event.edit("------------" + memeVar + "-")
    await event.edit("-----------" + memeVar + "--")
    await event.edit("----------" + memeVar + "---")
    await event.edit("---------" + memeVar + "----")
    await event.edit("--------" + memeVar + "-----")
    await event.edit("-------" + memeVar + "------")
    await event.edit("------" + memeVar + "-------")
    await event.edit("-----" + memeVar + "--------")
    await event.edit("----" + memeVar + "---------")
    await event.edit("---" + memeVar + "----------")
    await event.edit("--" + memeVar + "-----------")
    await event.edit("-" + memeVar + "------------")
    await event.edit(memeVar + "-------------")
    await event.edit("-" + memeVar + "------------")
    await event.edit("--" + memeVar + "-----------")
    await event.edit("---" + memeVar + "----------")
    await event.edit("----" + memeVar + "---------")
    await event.edit("-----" + memeVar + "--------")
    await event.edit("------" + memeVar + "-------")
    await event.edit("-------" + memeVar + "------")
    await event.edit("--------" + memeVar + "-----")
    await event.edit("---------" + memeVar + "----")
    await event.edit("----------" + memeVar + "---")
    await event.edit("-----------" + memeVar + "--")
    await event.edit("------------" + memeVar + "-")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)


@ultroid_cmd(pattern="think")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 288)
    await event.edit("thinking")
    animation_chars = [
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "Thinking... 🤔",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])


@ultroid_bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 27)
    input_str = event.pattern_match.group(1)
    if input_str == "snake":
        await event.edit(input_str)
        animation_chars = [
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
            "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 27])


@ultroid_cmd(pattern="police")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 64)
    await event.edit("Police")
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "[CɪᴘʜᴇʀX](https://t.me/Hackintush) **Police Service Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        animation_chars += [" "]*(64 - len(animation_chars))
        await event.edit(animation_chars[i % 64])


@ultroid_cmd(pattern="gangestar ?(.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Everybody")
        await asyncio.sleep(0.3)
        await event.edit("was")
        await asyncio.sleep(0.2)
        await event.edit("Gangestar")
        await asyncio.sleep(0.5)
        await event.edit("Until ")
        await asyncio.sleep(0.2)
        await event.edit("I")
        await asyncio.sleep(0.3)
        await event.edit("Arrived")
        await asyncio.sleep(0.3)
        await event.edit("🔥")
        await asyncio.sleep(0.3)
        await event.edit("Everybody was Gangestar Until I Arrived 🔥")


@ultroid_bot.on(events.NewMessage(pattern=r"\.flower", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return
    flower = " 🌹"
    sleepValue = 4

    await event.edit(flower + "        ")
    await event.edit(flower + flower + "       ")
    await event.edit(flower + flower + flower + "      ")
    await event.edit(flower + flower + flower + flower + "     ")
    await event.edit(flower + flower + flower + flower + flower + "    ")
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + "   "
    )
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + flower + "  "
    )
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + " "
    )
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
    )
    await asyncio.sleep(sleepValue)


@ultroid_bot.on(events.NewMessage(pattern=r"\.melow", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😀😃😄😀😃😄"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.cute", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🥺😢🥺😢🥺😢"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.tlol", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.teeth", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😐😬😐😬😐😬"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.gym", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.run", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🚶🏃🚶🏃🚶🏃🚶🏃"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.candy", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.kiss", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😗😚😘😗😚😘😗😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.butterfly", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.box", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.clock", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.earth", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.smile", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🙂🙃🙂🙃🙂🙃"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.laugh", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😄😁😄😁😄😁"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.cat", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😺😸😹😺😸😹😺😸😹"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.poker", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😐😑😐😑😐😑"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.wow", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😧😦😧😦😧😦"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.monkey", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🙉🙈🙉🙈🙉🙈"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.starheart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😍🤩😍🤩😍🤩"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.wink", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😶😉😶😉😶😉"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.lip", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🙁☹️🙁☹️🙁☹️"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="her ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 64)
    await event.edit("loveu")
    animation_chars = [
        "😀",
        "👩‍🎨",
        "😁",
        "😂",
        "🤣",
        "😃",
        "😄",
        "😅",
        "😊",
        "☺",
        "🙂",
        "🤔",
        "🤨",
        "😐",
        "😑",
        "😶",
        "😣",
        "😥",
        "😮",
        "🤐",
        "😯",
        "😴",
        "😔",
        "😕",
        "☹",
        "🙁",
        "😖",
        "😞",
        "😟",
        "😢",
        "😭",
        "🤯",
        "💔",
        "❤️",
        "I Love You ❤️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        animation_chars += [" "]*(64 - len(animation_chars))
        await event.edit(animation_chars[i % 64])


@ultroid_bot.on(events.NewMessage(pattern=r"\.donce", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    await event.edit("Connecting...")
    animation_chars = [
        "⠀⠀⠀⣶⣿⣶\n⠀⠀⠀⣿⣿⣿⣀\n⠀⣀⣿⣿⣿⣿⣿⣿\n⣶⣿⠛⣭⣿⣿⣿⣿\n⠛⠛⠛⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⣿⣿⣿\n⠀⠀⣀⣭⣿⣿⣿⣿⣀\n⠀⠤⣿⣿⣿⣿⣿⣿⠉\n⠀⣿⣿⣿⣿⣿⣿⠉\n⣿⣿⣿⣿⣿⣿\n⣿⣿⣶⣿⣿\n⠉⠛⣿⣿⣶⣤\n⠀⠀⠉⠿⣿⣿⣤\n⠀⠀⣀⣤⣿⣿⣿\n⠀⠒⠿⠛⠉⠿⣿\n⠀⠀⠀⠀⠀⣀⣿⣿\n⠀⠀⠀⠀⣶⠿⠿⠛\n",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿\n⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀\n⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀\n⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤\n⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉\n⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉\n⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀\n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛\n",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶\n⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶\n⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤\n⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀\n⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿\n⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶\n⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒\n⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉\n⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛\n⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤\n⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿\n⠀⠀⠀⠀⠀⠀⣿⠛\n⠀⠀⠀⠀⠀⠀⣭⣶\n",
        "⠀⠀⠀⠀⠀⠀⣶⣿⣶\n⠀⠀⠀⣤⣤⣤⣿⣿⣿\n⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿\n⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶\n⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤\n⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿\n⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉\n⠀⠀⠀⣿⣿⣿⣿⣿⣶\n⠀⠀⠀⠀⣿⠉⠿⣿⣿\n⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿\n⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉\n",
        "⠀⠀⠀⠀⠀⠀⣤⣶⣶\n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀\n⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿\n⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿\n⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿\n⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤\n⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿\n⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿\n⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛\n⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀\n⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿\n⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿\n⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿\n⠀⠀⠀⠀⠀⠀⣀⣿⣿\n⠀⠀⠀⠀⠤⣿⠿⠿⠿\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 100])


@ultroid_cmd(pattern="cheart ?(.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("❤️")
        await asyncio.sleep(0.3)
        await event.edit("💙")
        await asyncio.sleep(0.3)
        await event.edit("💛")
        await asyncio.sleep(0.3)
        await event.edit("💚")
        await asyncio.sleep(0.3)
        await event.edit("🧡")
        await asyncio.sleep(0.3)
        await event.edit("💜")
        await asyncio.sleep(0.3)
        await event.edit("🤎")
        await asyncio.sleep(0.3)
        await event.edit("🖤")
        await asyncio.sleep(0.3)
        await event.edit("🤍")
        await asyncio.sleep(0.3)
        await event.edit("💜")
        await asyncio.sleep(0.3)
        await event.edit("🤎")
        await asyncio.sleep(0.3)
        await event.edit("🤍")
        await asyncio.sleep(0.3)
        await event.edit("🧡")
        await asyncio.sleep(0.3)
        await event.edit("💚")
        await asyncio.sleep(0.3)
        await event.edit("💛")
        await asyncio.sleep(0.3)
        await event.edit("💙")
        await asyncio.sleep(0.3)
        await event.edit("❤️")
        await asyncio.sleep(0.3)
        await event.edit("💝")


@ultroid_cmd(pattern="finger ?(.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("🖕🏻")
        await asyncio.sleep(0.3)
        await event.edit("🖕")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏼")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏿")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏼")
        await asyncio.sleep(0.3)
        await event.edit("🖕")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏻")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏿")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏾")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏽")
        await asyncio.sleep(0.3)
        await event.edit("🖕")
        await asyncio.sleep(0.3)
        await event.edit("🖕🏼")


@ultroid_cmd(pattern="billy ?(.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("👍")
        await asyncio.sleep(0.6)
        await event.edit("👍🏻")
        await asyncio.sleep(0.6)
        await event.edit("👍🏼")
        await asyncio.sleep(0.6)
        await event.edit("👍🏽")
        await asyncio.sleep(0.6)
        await event.edit("👍🏾")
        await asyncio.sleep(0.6)
        await event.edit("👍🏿")
        await asyncio.sleep(0.6)
        await event.edit("👍🏾")
        await asyncio.sleep(0.6)
        await event.edit("👍🏽")
        await asyncio.sleep(0.6)
        await event.edit("👍🏼")
        await asyncio.sleep(0.6)
        await event.edit("👍🏻")


@ultroid_cmd(pattern="agree ?(.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("👌")
        await asyncio.sleep(0.6)
        await event.edit("👌🏻")
        await asyncio.sleep(0.6)
        await event.edit("👌🏼")
        await asyncio.sleep(0.6)
        await event.edit("👌🏽")
        await asyncio.sleep(0.6)
        await event.edit("👌🏾")
        await asyncio.sleep(0.6)
        await event.edit("👌🏿")
        await asyncio.sleep(0.6)
        await event.edit("👌🏾")
        await asyncio.sleep(0.6)
        await event.edit("👌🏽")
        await asyncio.sleep(0.6)
        await event.edit("👌🏼")
        await asyncio.sleep(0.6)
        await event.edit("👌🏻")


@ultroid_bot.on(events.NewMessage(pattern=r"\.angry", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😡🤬😡🤬😡🤬"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.sad", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😒😏😒😏😒😏"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.amaze", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😳😲😳😲😳😲"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.omg", outgoing=True))
async def _(event):

    if event.fwd_from:
        return
    deq = deque(list("🙄😳🙄😳🙄😳"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.tongue", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😛😝😛😝😛😝"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.sun", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🔅🔆🔅🔆🔅🔆"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.speaker", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🔈🔊🔈🔊🔈🔊"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.heart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("💖💝💖💝💖💝💖💝"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="heart$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.sand", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("⏳⌛️⏳⌛️⏳⌛️"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.storm", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌧⛈🌧⛈🌧⛈"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.floodwarn", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("💙💛💓💔💘💕💜💚💝💞💟"))
    for _ in range(64):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.rain", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("☁️⛈Ř/~\İŇ🌬⚡🌪"))
    for _ in range(64):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@ultroid_bot.on(events.NewMessage(pattern=r"\.brain", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 14)
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])


@ultroid_bot.on(events.NewMessage(pattern=r"\.dump", outgoing=True))
async def _(message):
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "🥞 🎂 🍫"
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await message.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@ultroid_cmd(pattern="good ?(.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            ".     😍😊😍😊😍😍\n 😊😍😍😍😍😊😍😊\n  😍😊                     😊😊\n 😍😍\n😍😊                😊😍😊😍\n😍😊                😍😊😊😊\n😍😊                        😊😍\n   😊😊                      😍😍\n     😍😊😍😍😍😊😊😍  \n          😊😊😊😍😍😊 "
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".           😍😊😊😊😍\n 😍😊😍😍😊😍😊\n   😍😊                   😊😍\n 😍😊                       😍😊\n😊😍                         😍😍\n😊😊                         😍😍\n 😊😊                       😍😍\n   😊😊                   😍😊\n      😍😍😍😍😍😍😊\n            😊😊😍😍😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".           😊😊😍😊😊\n     😊😍😍😍😊😍😊\n   😊😍                   😍😊\n 😊😊                       😍😊\n😍😍                         😍😊\n😍😍                         😊😊\n 😍😊                       😍😍\n   😊😍                   😊😊\n      😊😊😍😍😊😊😊\n            😍😊😊😊😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😍😊😍😊😍😊\n😍😍😍😊😍😍😍😊\n😍😊                      😊😊\n😊😊                         😊😊\n😍😊                         😊😍\n😍😍                         😊😊\n😍😊                         😊😊\n😊😍                      😍😊\n😊😍😍😍😊😊😊😊\n😊😊😊😍😍😊😍\n\n"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😍😊                              😍😍\n😊😍😊                      😍😊😊\n😍😊😍😊            😊😊😊😍\n😊😊    😊😊    😊😊    😊😊\n😊😊        😊😊😊        😍😍\n😊😊             😍             😍😊\n😍😊                              😍😊\n😊😍                              😊😊\n😍😍                              😊😊\n😊😊                              😍😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".           😍😊😊😊😍\n 😍😊😍😍😊😍😊\n   😍😊                   😊😍\n 😍😊                       😍😊\n😊😍                         😍😍\n😊😊                         😍😍\n 😊😊                       😍😍\n   😊😊                   😍😊\n      😍😍😍😍😍😍😊\n            😊😊😍😍😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😍😍😍😊😍😊😍\n😍😊😍😍😊😊😊😊\n😍😊                     😍😍\n😊😍                     😍😍\n😊😍😍😍😊😊😊😊\n😍😊😍😍😊😍😍\n😊😊    😍😊\n😍😍         😍😊\n😊😊              😊😊\n😊😊                  😍😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😍                           😍😍\n😍😍😊                       😊😍\n😊😊😍😍                 😍😊\n😍😍  😊😊               😍😊\n😍😊     😊😊            😊😊\n😊😍         😊😊        😍😊\n😊😍             😍😍    😍😍\n😊😍                 😊😍😊😊\n😍😊                     😊😍😊\n😍😊                          😊😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😊😊😍😊😍\n😊😍😊😍😍😍\n          😍😍\n          😍😍\n          😍😊\n          😍😊\n          😊😊\n          😊😊\n😍😊😍😊😊\n😊😍😍😊😊😊"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            "😊😍                           😍😍\n😍😍😊                       😊😍\n😊😊😍😍                 😍😊\n😍😍  😊😊               😍😊\n😍😊     😊😊            😊😊\n😊😍         😊😊        😍😊\n😊😍             😍😍    😍😍\n😊😍                 😊😍😊😊\n😍😊                     😊😍😊\n😍😊                          😊😍"
        )
        await asyncio.sleep(0.5)
        await event.edit(
            ".     😍😊😍😊😍😍\n 😊😍😍😍😍😊😍😊\n  😍😊                     😊😊\n 😍😍\n😍😊                😊😍😊😍\n😍😊                😍😊😊😊\n😍😊                        😊😍\n   😊😊                      😍😍\n     😍😊😍😍😍😊😊😍  \n          😊😊😊😍😍😊 "
        )
        await asyncio.sleep(0.5)
        await event.edit("GOOD MORNING ,HAVE A NICE DAY 😊")


@ultroid_bot.on(events.NewMessage(pattern=r"\.snake", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 64)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        animation_chars += [" "]*(64 - len(animation_chars))
        await event.edit(animation_chars[i % 64])


@ultroid_bot.on(events.NewMessage(pattern=r"\.human", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 27)
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🚗\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛🚗⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚗⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚗⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🚗⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛🚗⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n🚗⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛😊⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 27])


@ultroid_bot.on(events.NewMessage(pattern=r"\.mc", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 64)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        animation_chars += [" "]*(64 - len(animation_chars))
        await event.edit(animation_chars[i % 64])


@ultroid_bot.on(events.NewMessage(pattern=r"\.solar", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 64)
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        animation_chars += [" "]*(64 - len(animation_chars))
        await event.edit(animation_chars[i % 64])


@ultroid_bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 64)
    input_str = event.pattern_match.group(1)
    if input_str == "smoon":
        await event.edit(input_str)
        animation_chars = [
            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            animation_chars += [" "]*(64 - len(animation_chars))
            await event.edit(animation_chars[i % 64])


@ultroid_bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    input_str = event.pattern_match.group(1)
    if input_str == "tmoon":
        await event.edit(input_str)
        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 100])


@ultroid_cmd(pattern="lmoon")
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕"
    )


@ultroid_cmd(pattern="town")
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        """☁☁ 🌞     ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁         ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳 🚶           |   🚍            🚴🚴 
🌴/                    |                     \🌲"""
    )
    await asyncio.sleep(0.5)
    await event.edit(
        """☁☁  🌞    ☁           ☁
       ☁   ✈        ☁   🚁     ☁    ☁          ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/    l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖  🚘l                 \
   🌳 🚶          |    🚍          🚴🚴  
🌴/                    |                     \🌲"""
    )
    await asyncio.sleep(0.5)
    await event.edit(
        """☁☁   🌞   ☁           ☁
       ☁    ✈       ☁  🚁      ☁    ☁           ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/    l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖    l                \
   🌳 🚶        🚘|     🚍         🚴🚴   
🌴/                    |                     \🌲"""
    )
    await asyncio.sleep(0.5)
    await event.edit(
        """☁☁    🌞  ☁           ☁
       ☁     ✈      ☁ 🚁       ☁    ☁            ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/   l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖   l                 \
   🌳 🚶        🚘|      🚍        🚴🚴    
🌴/                    |                     \🌲"""
    )
    await asyncio.sleep(0.5)
    await event.edit(
        """☁☁     🌞 ☁           ☁
       ☁      ✈     ☁🚁        ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/    l   🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/         l               \
   🌳 🚶    🚖    |     🚍       🚴🚴      
🌴/             🚘     |                     \🌲"""
    )
    await asyncio.sleep(0.5)
    await event.edit(
        """☁☁      🌞☁           ☁
       ☁       ✈   ☁🚁         ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/    l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/         l               \
   🌳 🚶          |    🚍      🚴🚴    
🌴/         🚖  🚘     |                     \🌲"""
    )


@ultroid_bot.on(events.NewMessage(pattern=r"\.bombs", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("RIP...")


@ultroid_bot.on(events.NewMessage(pattern=r"\.plane", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("✈-------------")
    await asyncio.sleep(0.3)
    await event.edit("-✈------------")
    await asyncio.sleep(0.3)
    await event.edit("--✈-----------")
    await asyncio.sleep(0.3)
    await event.edit("---✈----------")
    await asyncio.sleep(0.3)
    await event.edit("----✈---------")
    await asyncio.sleep(0.3)
    await event.edit("-----✈--------")
    await asyncio.sleep(0.3)
    await event.edit("------✈-------")
    await asyncio.sleep(0.3)
    await event.edit("-------✈------")
    await asyncio.sleep(0.3)
    await event.edit("--------✈-----")
    await asyncio.sleep(0.3)
    await event.edit("---------✈----")
    await asyncio.sleep(0.3)
    await event.edit("----------✈---")
    await asyncio.sleep(0.3)
    await event.edit("-----------✈--")
    await asyncio.sleep(0.3)
    await event.edit("------------✈-")
    await asyncio.sleep(0.3)
    await event.edit("-------------✈")


@ultroid_cmd(pattern="lalol")
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "😂\n😂\n😂\n😂\n😂😂😂😂\n\n   😂😂😂\n 😂         😂\n😂           😂\n 😂         😂\n   😂😂😂\n\n😂\n😂\n😂\n😂\n😂😂😂😂"
    )


@ultroid_cmd(pattern="lit")
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    ) 
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    ) 
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    ) 
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    ) 
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    ) 
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    ) 
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    ) 
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    ) 
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    ) 
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    ) 
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    ) 
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    ) 
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    ) 
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    ) 
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@ultroid_cmd(pattern="my")
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")
        
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")

    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")

    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")

    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")

    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")

    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@ultroid_cmd(pattern="my")
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")

    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")

    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")

    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")

    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")

    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")

    
@ultroid_cmd(pattern="hi")
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")

    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")

    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")

    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")

    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")

    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")

    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")

    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")

    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")

    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")

    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")

    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")

    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")

    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")

    await event.edit("ʟᴏᴅɪɴɢ")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 ")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆") 

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍")

    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍")

    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💓💓")

    await event.edit("❤️❤️𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖❤️❤️")

    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💓💓")

    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💜💜")

    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💓💓")

    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💛💛")

    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💓💓")

    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💚💚")

    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💓💓")

    await event.edit("🧡🧡𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖🧡🧡")

    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💓💓")

    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💙💙")

    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💜💜")

    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💚💚")

    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💛💛")

    await event.edit("🖤🖤𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖🖤🖤")

    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💙💙")

    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💜💜")

    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💚💚")

    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💛💛")

    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💝💝")

    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💕💕")

    await event.edit("💖💖𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💖💖")

    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💕💕")

    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💝💝")

    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖💕💕")


@ultroid_cmd(pattern="figcar")
async def car(event):
    if event.fwd_from:
        return
    await event.edit(
        "┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈\n ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈\n▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈\n▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏\n▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲\n▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕\n▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱\n┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈"
    )


@ultroid_cmd(pattern="figkiller")
async def killer(event):
    if event.fwd_from:
        return
    await event.edit("_/﹋\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉ - -\n" "_/﹋\_\n")


@ultroid_cmd(pattern="tgm")
async def tgm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n"
            "╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n"
            "╔══╗────╔╗──────────╔╗\n"
            "║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n"
            "║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n"
            "╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n"
            "────────────────────────╚═╝\n"
            "╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n"
            "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･"
        )


@ultroid_cmd(pattern="emam")
async def emam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿\n"
            "⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿\n"
            "⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄\n"
            "⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸\n"
            "⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬\n"
            "⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴\n"
            "⣿⣿⣿⣿⠿⠍⣿⣿⣿⣿⣿⣿⣿⢇⠟⠁⠄⠄⠄⠄\n"
            "⠟⠛⠉⠄⠄⠄⡽⣿⣿⣿⣿⣿⣯⠏⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⢀⣾⣾⣿⣤⣯⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄\n"
        )


@ultroid_cmd(pattern="tgn")
async def tgn(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n"
            "╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n"
            "╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n"
            "║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n"
            "║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n"
            "╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n"
            "──────────────╚═╝\n"
            "╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n"
            "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･"
        )


@ultroid_cmd(pattern="tnx")
async def tnx(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            ".......🦋🦋........🦋🦋\n"
            "...🦋.........🦋🦋.......🦋\n"
            "...🦋............💙..........🦋\n"
            ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
            "....... 🦋.................🦋\n"
            "..............🦋......🦋\n"
            "...................💙\n"
        )


@ultroid_cmd(pattern="figgm")
async def gm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n"
            "╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n"
            "╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n"
            "┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n"
            "┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n"
            "╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n"
            "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･"
        )


@ultroid_cmd(pattern="fighi")
async def fighi(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "██╗░░██╗██╗\n"
            "██║░░██║██║\n"
            "███████║██║\n"
            "██╔══██║██║\n"
            "██║░░██║██║\n"
            "╚═╝░░╚═╝╚═╝\n"
        )


@ultroid_cmd(pattern="figgn")
async def gn(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥\n"
            "╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n"
            "╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n"
            "┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n"
            "┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n"
            "╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n"
            "｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･\n"
        )


@ultroid_cmd(pattern="sponge")
async def sponge(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
            "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
            "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
            "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
            "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n"
            "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
            "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
            "▕┈╰▏╰╯╰━━━━╯┈┈▏\n"
        )


# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# ===========================================


@ultroid_cmd(pattern="dick")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.edit(titid)


@ultroid_cmd(pattern="figlol")
async def figlol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `"
            "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"
            "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `"
            "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `"
        )


@ultroid_cmd(pattern="figlmao")
async def figlmao(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n┏┓┈╭━━╮╭━━╮╭━━╮`"
            "`\n┃┃┈┃┃┃┃┃╭╮┃┃╭╮┃`"
            "`\n┃┗┓┃┃┃┃┃┏┓┃┃╰╯┃`"
            "`\n┗━┛┗┻┻┛┗┛┗┛╰━━╯`"
        )


@ultroid_cmd(pattern="fighello")
async def fighello(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n╔┓┏╦━╦┓╔┓╔━━╗" "\n║┗┛║┗╣┃║┃║X X║" "\n║┏┓║┏╣┗╣┗╣╰╯║" "\n╚┛┗╩━╩━╩━╩━━╝"
        )


@ultroid_cmd(pattern="figno")
async def figno(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n███╗░░██╗░█████╗░"
            "\n████╗░██║██╔══██╗"
            "\n██╔██╗██║██║░░██║"
            "\n██║╚████║██║░░██║"
            "\n██║░╚███║╚█████╔╝"
            "\n╚═╝░░╚══╝░╚════╝░"
        )


@ultroid_cmd(pattern="figtrump")
async def figtrump(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿"
            "\n⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿"
            "\n⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿"
            "\n⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿"
            "\n⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿"
            "\n⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿"
            "\n⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿"
            "\n⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿"
            "\n⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿"
            "\n⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹"
            "\n⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄"
            "\n⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀"
            "\n⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿"
            "\n⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿"
            "\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘"
        )


@ultroid_cmd(pattern="figputin")
async def figputin(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n"
            "⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n"
            "⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n"
            "⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n"
            "⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n"
            "⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n"
            "⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n"
            "⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n"
            "⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n"
            "⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
        )


@ultroid_cmd(pattern=r"figchina")
async def figchina(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
            "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
            "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
            "⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
        )


@ultroid_cmd(pattern="figthink")
async def figthink(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠀⠀⠀⠀⢀⣀⣀⣀\n"
            "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
            "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
            "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
            "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
            "⠀\n"
            "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
            "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
            "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
            "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
            "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
            "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
            "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
            "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
        )


@ultroid_cmd(pattern="figdick")
async def figdick(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣿⣿⣿⣿⣯⠏⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⣴⣻⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⣼⣷⣿⣿⣿⣿⣿⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⢸⢿⣿⣿⣿⣿⣿⣿⣿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠸⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠹⣟⣿⣿⣿⣿⡿⣷⡿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠈⠛⠯⣿⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        )

@ultroid_cmd(pattern="fighappyfrog")
async def fighappyfrog(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
            "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
            "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
            "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
            "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
            "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
            "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
            "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
            "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
            "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
            "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
            "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
        )

@ultroid_cmd(pattern="figdeadfrog")
async def figdeadfrog(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
            "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
            "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
            "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
            "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
            "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
            "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
            "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        )


@ultroid_cmd(pattern="fuck")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n...................................../´¯/) "
            "\n...................................,/¯../ "
            "\n.................................../.../ "
            "\n................................../´.¯/"
            "\n................................./´¯./"
            "\n...............................,/¯../ "
            "\n.............................../.../ "
            "\n............................../´¯./"
            "\n............................./´¯./"
            "\n...........................,/¯../ "
            "\n.........................../.../ "
            "\n........................../´¯./"
            "\n........................./´¯./"
            "\n.......................,/¯../ "
            "\n......................./.../ "
            "\n....................../´¯./"
            "\n....................,/¯../ "
            "\n.................../..../ "
            "\n............./´¯/'...'/´¯¯`·¸ "
            "\n........../'/.../..../......./¨¯\ "
            "\n........('(...´...´.... ¯~/'...') "
            "\n.........\.................'...../ "
            "\n..........''...\.......... _.·´ "
            "\n............\..............( "
            "\n..............\.............\..."
        )


@ultroid_bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 60)
    input_str = event.pattern_match.group(1)
    if input_str == "jagh":
        await event.edit(input_str)
        animation_chars = [
            "8✊️===D",
            "8=✊️==D",
            "8==✊️=D",
            "8===✊️D",
            "8==✊️=D",
            "8=✊️==D",
            "8✊️===D",
            "8===✊️D💦",
            "8==✊️=D💦💦",
            "8=✊️==D💦💦💦",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])

@ultroid_bot.on(events.NewMessage(pattern=r"\.xmas", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,22)
    await event.edit("😊𝓜𝓔𝓡𝓡𝓨 𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢😁")
    animation_chars = ["""😀😀                              😀😀
😀😀😀                      😀😀😀
😀😀😀😀            😀😀😀😀
😀😀    😀😀    😀😀    😀😀
😀😀        😀😀😀        😀😀
😀😀             😀             😀😀
😀😀                              😀😀
😀😀                              😀😀
😀😀                              😀😀
😀😀                              😀😀""",
"""🤩🤩🤩🤩🤩🤩🤩🤩
🤩🤩🤩🤩🤩🤩🤩🤩
🤩🤩
🤩🤩
🤩🤩🤩🤩🤩🤩
🤩🤩🤩🤩🤩🤩
🤩🤩
🤩🤩
🤩🤩🤩🤩🤩🤩🤩🤩
🤩🤩🤩🤩🤩🤩🤩🤩""",
"""😉😉😉😉😉😉😉
😉😉😉😉😉😉😉😉
😉😉                     😉😉
😉😉                     😉😉
😉😉😉😉😉😉😉😉
😉😉😉😉😉😉😉
😉😉    😉😉
😉😉         😉😉
😉😉              😉😉
😉😉                  😉😉""",
"""⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️                     ⭐️⭐️
⭐️⭐️                     ⭐️⭐️
⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️    ⭐️⭐️
⭐️⭐️         ⭐️⭐️
⭐️⭐️              ⭐️⭐️
⭐️⭐️                  ⭐️⭐️""",
"""💥💥                    💥💥
   💥💥              💥💥
      💥💥        💥💥
         💥💥  💥💥
            💥💥💥
              💥💥
              💥💥
              💥💥
              💥💥
              💥💥""","""
     🧣🧣🧣🧣🧣🧣
     🧣🧣🧣🧣🧣🧣🧣🧣
   🧣🧣                      🧣🧣
 🧣🧣
🧣🧣
🧣🧣
 🧣🧣
   🧣🧣                      🧣🧣
     🧣🧣🧣🧣🧣🧣🧣🧣
         🧣🧣🧣🧣🧣🧣""",
"""🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟🌟🌟🌟🌟🌟🌟🌟
🌟🌟🌟🌟🌟🌟🌟🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟""",
"""💝💝💝💝💝💝💝
💝💝💝💝💝💝💝💝
💝💝                     💝💝
💝💝                     💝💝
💝💝💝💝💝💝💝💝
💝💝💝💝💝💝💝
💝💝    💝💝
💝💝         💝💝
💝💝              💝💝
💝💝                  💝💝""",
"""🎅🎅🎅🎅🎅🎅
🎅🎅🎅🎅🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
🎅🎅🎅🎅🎅🎅
🎅🎅🎅🎅🎅🎅""",
"""       💫💫💫💫💫
  💫💫💫💫💫💫💫
  💫💫                 💫💫
💫💫
  💫💫💫💫💫💫
      💫💫💫💫💫💫
                            💫💫
💫💫                 💫💫
  💫💫💫💫💫💫💫
       💫💫💫💫💫""",
"""✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨""",
"""☄️☄️                              ☄️☄️
☄️☄️☄️                      ☄️☄️☄️
☄️☄️☄️☄️            ☄️☄️☄️☄️
☄️☄️    ☄️☄️    ☄️☄️    ☄️☄️
☄️☄️        ☄️☄️☄️        ☄️☄️
☄️☄️             ☄️             ☄️☄️
☄️☄️                              ☄️☄️
☄️☄️                              ☄️☄️
☄️☄️                              ☄️☄️
☄️☄️                              ☄️☄️""",
"""⁭
                    🌎
                  🌎🌎
               🌎🌎🌎
            🌎🌎 🌎🌎
          🌎🌎    🌎🌎
        🌎🌎       🌎🌎
      🌎🌎🌎🌎🌎🌎
     🌎🌎🌎🌎🌎🌎🌎
   🌎🌎                 🌎🌎
  🌎🌎                    🌎🌎
🌎🌎                       🌎🌎""",
"""       🪐🪐🪐🪐🪐
  🪐🪐🪐🪐🪐🪐🪐
  🪐🪐                 🪐🪐
🪐🪐
  🪐🪐🪐🪐🪐🪐
      🪐🪐🪐🪐🪐🪐
                            🪐🪐
🪐🪐                 🪐🪐
  🪐🪐🪐🪐🪐🪐🪐
       🪐🪐🪐🪐🪐"""]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])

main = [
    "⁭\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n",
    "⁭\n          💛💛💛💛💛💛\n     💛💛💛💛💛💛💛💛\n   💛💛                      💛💛\n 💛💛\n💛💛\n💛💛\n 💛💛\n   💛💛                      💛💛\n     💛💛💛💛💛💛💛💛\n         💛💛💛💛💛💛\n",
    "⁭\n💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                      💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                      💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n",
    "⁭\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟\n💟💟💟💟💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n",
    "⁭\n💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚\n💚💚\n💚💚\n💚💚💚💚💚💚\n💚💚💚💚💚💚\n💚💚\n💚💚\n💚💚\n💚💚\n",
    "⁭\n          💜💜💜💜💜💜\n     💜💜💜💜💜💜💜💜\n   💜💜                     💜💜\n 💜💜\n💜💜                💜💜💜💜\n💜💜                💜💜💜💜\n 💜💜                        💜💜\n   💜💜                      💜💜\n     💜💜💜💜💜💜💜💜\n          💜💜💜💜💜💜\n",
    "⁭\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n",
    "⁭\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n",
    "⁭\n         💛💛💛💛💛💛\n         💛💛💛💛💛💛\n                  💛💛\n                  💛💛\n                  💛💛\n                  💛💛\n💛💛          💛💛\n  💛💛       💛💛\n   💛💛💛💛💛\n      💛💛💛💛\n",
    "⁭\n💙💙                  💙💙\n💙💙             💙💙\n💙💙        💙💙\n💙💙   💙💙\n💙💙💙💙\n💙💙 💙💙\n💙💙     💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                   💙💙\n",
    "⁭\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n",
    "⁭\n💚💚                              💚💚\n💚💚💚                      💚💚💚\n💚💚💚💚            💚💚💚💚\n💚💚    💚💚    💚💚    💚💚\n💚💚        💚💚💚        💚💚\n💚💚             💚             💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n",
    "⁭\n💜💜                           💜💜\n💜💜💜                       💜💜\n💜💜💜💜                 💜💜\n💜💜  💜💜               💜💜\n💜💜     💜💜            💜💜\n💜💜         💜💜        💜💜\n💜💜             💜💜    💜💜\n💜💜                 💜💜💜💜\n💜💜                     💜💜💜\n💜💜                          💜💜\n",
    "⁭\n           💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n",
    "⁭\n           💛💛💛💛💛\n      💛💛💛💛💛💛💛\n   💛💛                    💛💛\n 💛💛                        💛💛\n💛💛                           💛💛\n💛💛              💛💛     💛💛\n 💛💛               💛💛 💛💛\n   💛💛                   💛💛\n      💛💛💛💛💛💛💛💛\n           💛💛💛💛💛   💛💛\n",
    "⁭\n💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                     💙💙\n💙💙                     💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n💙💙    💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                  💙💙\n",
    "⁭\n       💟💟💟💟💟\n  💟💟💟💟💟💟💟\n  💟💟                 💟💟\n💟💟\n  💟💟💟💟💟💟\n      💟💟💟💟💟💟\n                            💟💟\n💟💟                 💟💟\n  💟💟💟💟💟💟💟\n       💟💟💟💟💟\n",
    "⁭\n💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n",
    "⁭\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n  💜💜                  💜💜\n      💜💜💜💜💜💜\n            💜💜💜💜\n",
    "⁭\n💖💖                              💖💖\n  💖💖                          💖💖\n    💖💖                      💖💖\n      💖💖                  💖💖\n         💖💖              💖💖\n           💖💖         💖💖\n             💖💖     💖💖\n               💖💖 💖💖\n                  💖💖💖\n                       💖\n",
    "⁭\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗              💗            💗💗\n 💗💗           💗💗          💗💗\n 💗💗        💗💗💗       💗💗\n  💗💗   💗💗  💗💗   💗💗\n   💗💗💗💗      💗💗💗💗\n    💗💗💗             💗💗💗\n",
    "⁭\n💛💛                    💛💛\n   💛💛              💛💛\n      💛💛        💛💛\n         💛💛  💛💛\n            💛💛💛\n            💛💛💛\n         💛💛 💛💛\n      💛💛       💛💛\n   💛💛             💛💛\n💛💛                   💛💛\n",
    "⁭\n💙💙                    💙💙\n   💙💙              💙💙\n      💙💙        💙💙\n         💙💙  💙💙\n            💙💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n",
    "⁭\n 💟💟💟💟💟💟💟\n 💟💟💟💟💟💟💟\n                       💟💟\n                   💟💟\n               💟💟\n           💟💟\n       💟💟\n   💟💟\n💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟\n",
    "⁭\n       💗💗💗💗\n   💗💗💗💗💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n   💗💗💗💗💗💗\n        💗💗💗💗\n",
    "⁭\n          💙💙\n     💙💙💙\n💙💙 💙💙\n          💙💙\n          💙💙\n          💙💙\n          💙💙\n          💙💙\n     💙💙💙💙\n     💙💙💙💙\n",
    "⁭\n    💟💟💟💟💟\n  💟💟💟💟💟💟\n💟💟          💟💟\n                💟💟\n             💟💟\n          💟💟\n       💟💟\n    💟💟\n  💟💟💟💟💟💟\n  💟💟💟💟💟💟\n",
    "⁭\n     💛💛💛💛\n  💛💛💛💛💛\n💛💛         💛💛\n                   💛💛\n            💛💛💛\n            💛💛💛\n                   💛💛\n💛💛         💛💛\n  💛💛💛💛💛\n     💛💛💛💛\n",
    "⁭\n                         💖💖\n                    💖💖💖\n              💖💖 💖💖\n          💖💖     💖💖\n     💖💖          💖💖\n💖💖               💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n                         💖💖\n                         💖💖\n",
    "⁭\n💚💚💚💚💚💚\n💚💚💚💚💚💚\n💚💚\n 💚💚💚💚💚\n   💚💚💚💚💚\n                    💚💚\n                    💚💚\n💚💚          💚💚\n  💚💚💚💚💚\n     💚💚💚💚\n",
    "⁭\n        💜💜💜💜\n    💜💜💜💜💜\n💜💜\n\n💜💜\n💜💜💜💜💜💜\n💜💜💜💜💜💜💜\n💜💜               💜💜\n💜💜               💜💜\n    💜💜💜💜💜💜\n        💜💜💜💜\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n                      💗💗\n                     💗💗\n                   💗💗\n                 💗💗\n               💗💗\n             💗💗\n           💗💗\n         💗💗\n",
    "⁭\n        💙💙💙💙\n   💙💙💙💙💙💙\n💙💙               💙💙\n💙💙               💙💙\n   💙💙💙💙💙💙\n   💙💙💙💙💙💙\n💙💙               💙💙\n💙💙               💙💙\n   💙💙💙💙💙💙\n        💙💙💙💙\n",
    "⁭\n        💟💟💟💟\n   💟💟💟💟💟💟\n💟💟               💟💟\n💟💟               💟💟\n 💟💟💟💟💟💟💟\n      💟💟💟💟💟💟\n                         💟💟\n                        💟💟\n  💟💟💟💟💟💟\n       💟💟💟💟\n",
]
letter = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


@ultroid_cmd(pattern="eem(?: |$)(.*)")
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit(
             "`Give me some text...`"
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in letter:
            char = main[letter.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)


SHUTDOWN = "https://filetolinktelegrambot.herokuapp.com/41750275203384/voice.ogg"
STARTUP = "https://filetolinktelegrambot.herokuapp.com/41767455072568/funny.gif.mp4"


@ultroid_bot.on(events.NewMessage(pattern=r"\.fhack", outgoing=True))
async def _(event):
    await event.client.send_file(
        event.chat_id,
        STARTUP,
        caption="`You will be Hacked in a Moment by CɪᴘʜᴇʀX Bot.`",
        voice_note=True,
    ),
    await event.client.send_file(
        event.chat_id, SHUTDOWN, caption="`Hacking in progress...`", voice_note=True
    )
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    animation_chars = [
        "`Connecting To CɪᴘʜᴇʀX Server...`",
        "`Target Selected.`",
        "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Looking for Telegram Data...`\nETA: 0m, 20s",
        "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Found SD Directory...`\n`Looking for Telegram Data : ✅`\nETA: 0m, 10s",
        "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Searching for Databases....`\n`Looking for Telegram Data : ✅`\n`Found Telegram Database Directory : ✅ `\nETA: 0m, 15s",
        "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`\n`Found msgstore.db.crypt12...`\n`Looking for Telegram Data : ✅`\n`Found Telegram Database Directory : ✅ `\n`Searching for Databases : ✅ `\nETA: 0m, 09s",
        "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Trying to Decrypt...`\n`Looking for Telegram Data : ✅`\n`Found Telegram Database Directory : ✅\n`Searching for Databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\n`⚠️ error occurred ..`\nETA: 0m, 25s",
        "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Decryption successful!`\n`Looking for Telegram Data : ✅`\n`⚠️ error occurred ..`\n`Found Telegram Database Directory : ✅`\n`⚠️ Error Occurred ...`\n`Searching for Databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\nETA: 0m, 25s",
        "`Hacking... 84%\n█████████████████████▒▒▒▒ `\n`Scanning file...`\n`Looking for Telegram Data : ✅`\n`⚠️ error occurred ..`\n`Found Telegram Database Directory : ✅`\n`⚠️ Error Occurred ..`\n`⚠️ Error Occurred ...`\n`Searching for Databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\n`Scanning File :  ✅`\nETA: 0m, 16s",
        "`Hacking... 100%\n` 98% HACKED`",
        "`Targeted Account Hacked By CɪᴘʜᴇʀX`\n\n`_______________________`\n`result ... :)`\n\n`Chatlist : ✅`\n`Calls : ✅`\n`groups : ✅`\n `Contacts : ✅`\n`Channel : ✅`\n`Deleted Messages : ❌`\n`Edited Messages : ❌`\n`All API Tokens : ✅`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])

@ultroid_cmd(pattern="thack")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    await event.edit("Starting CɪᴘʜᴇʀX Servers")
    animation_chars = [
        "`Connecting To T-800 At 149.154.167.51 - IPV4 - TELEGRAM // DC-4/1`",
        "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
        "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
        "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",
        "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'",
        "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
        "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
        "`Hacking... 84%\n█████████████████████▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**",
        "`Hacking... 100%\n█████████HACKED███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹Output: Generating.....",
        "`Hacked...\n\nYour account has been hacked by CɪᴘʜᴇʀX...`\n\nTERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked this Account From Telegram Database**\n\n\n🔹**Output:** Successful",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@ultroid_bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 15)
    input_str = event.pattern_match.group(1)
    if input_str == "whack":
        await event.edit(input_str)
        animation_chars = [
            "Looking for WhatsApp databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s",
            "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s",
            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",
            "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",
            "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s",
            "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",
            "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",
            "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s",
            "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s",
            "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s",
            "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s",
            "Hacking complete!\nUploading file...",
            "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to CɪᴘʜᴇʀX server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 15])
