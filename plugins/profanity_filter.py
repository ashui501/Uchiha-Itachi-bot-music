"""
✘ Commands Available -

•`{i}addprofanity`
   If someone sends bad word in a chat, Then bot will delete that message.

•`{i}remprofanity`
   From chat from Profanity list.

"""

from ProfanityDetector import detector
from cython.dB.nsfw_db import is_profan, profan_chat, rem_profan

from . import eor, events, get_string, ultroid_bot, ultroid_cmd


@ultroid_cmd(pattern="addprofanity$", admins_only=True)
async def addp(e):
    profan_chat(e.chat_id, "mute")
    await eor(e, get_string("prof_1"), time=10)


@ultroid_cmd(pattern="remprofanity", admins_only=True)
async def remp(e):
    rem_profan(e.chat_id)
    await eor(e, get_string("prof_2"), time=10)


@ultroid_bot.on(events.NewMessage(incoming=True))
async def checkprofan(e):
    chat = e.chat_id
    if is_profan(chat) and e.text:
        x, y = detector(e.text)
        if y:
            await e.delete()
