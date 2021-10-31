from cython import *
from cython.functions.helper import *
from cython.misc import owner_and_sudos
from cython.misc._assistant import asst_cmd, callback, in_pattern
from telethon import Button, custom

from plugins import ATRA_COL
from strings import get_languages, get_string, language

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
