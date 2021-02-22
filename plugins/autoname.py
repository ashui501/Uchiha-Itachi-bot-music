"""
✘ Commands Available -
• `{i}autoname`
    Turn on auto profile name.
"""

from telethon.errors import FloodWaitError
from telethon.tl import functions

from . import *

DEL_TIME_OUT = 60
DEFAULTUSER = str(OWNER_NAME) if OWNER_NAME else "CɪᴘʜᴇʀX"

@ultroid_cmd(
    pattern="autoname ?(.*)",
) 
async def _(event):
    sed = await edit_or_reply(event, "`sᴛᴀʀᴛɪɴɢ ᴀᴜᴛᴏɴᴀᴍᴇ. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...`")
    await sed.edit(event, "`CɪᴘʜᴇʀX ᴀᴜᴛᴏɴᴀᴍᴇ sᴛᴀʀᴛᴇᴅ`")
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

        name = f"{DEFAULTUSER} {HM}"

        logger.info(name)

        try:

            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    first_name=name
                )
            )

        except FloodWaitError as ex:

            logger.warning(str(e))

            await asyncio.sleep(ex.seconds)
 


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
