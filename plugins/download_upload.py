# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}ul <path/to/file>`
    Upload file to telegram chat.

• `{i}dl <filename(optional)>`
    Reply to file to download.

• `{i}save <filename.ext>`
    Reply to a text msg to save it in a file.

"""

import asyncio
import os
import time
from datetime import datetime as dt

from . import *

opn = []


@ultroid_cmd(
    pattern="dl ?(.*)",
)
async def download(event):
    if not event.is_reply:
        return await eor(event, "`Reply to a Media Message`")
    xx = await eor(event, get_string("com_1"))
    kk = event.pattern_match.group(1)
    s = dt.now()
    k = time.time()
    if event.reply_to_msg_id:
        ok = await event.get_reply_message()
        if not ok.media:
            return await eod(xx, get_string("udl_1"), time=5)
        else:
            if not kk:
                d = "resources/downloads/"
                o = await event.client.download_media(
                    ok,
                    d,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(
                            d,
                            t,
                            xx,
                            k,
                            "Downloading...",
                        ),
                    ),
                )
            else:
                d = f"resources/downloads/{kk}"
                o = await event.client.download_media(
                    ok,
                    d,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(
                            d,
                            t,
                            xx,
                            k,
                            "Downloading...",
                            file_name=d,
                        )
                    ),
                )
    e = datetime.now()
    t = time_formatter(((e - s).seconds) * 1000)
    if t:
        await eod(xx, get_string("udl_2").format(o, t))
    else:
        await eod(xx, f"Downloaded `{o}` in `0 second(s)`")


@ultroid_cmd(
    pattern="ul ?(.*)",
)
async def download(event):
    xx = await eor(event, get_string("com_1"))
    kk = event.pattern_match.group(1)
    s = dt.now()
    tt = time.time()
    if not kk:
        return await eod(xx, get_string("udl_3"))
    else:
        try:
            x = await event.client.send_file(
                event.chat_id,
                kk,
                caption=kk,
                force_document=True,
                thumb="resources/extras/cipherx.jpg",
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d,
                        t,
                        xx,
                        tt,
                        "Uploading...",
                        file_name=kk,
                    ),
                ),
            )
        except ValueError as ve:
            return await eod(xx, str(ve))
        except BaseException:
            try:
                await ultroid_bot.send_message(event.chat_id, kk)
                return await kk.delete()
            except BaseException:
                pass
    e = datetime.now()
    t = time_formatter(((e - s).seconds) * 1000)
    try:
        await x.edit(f"`{kk}`\nTime Taken: `{t}`")
    except BaseException:
        pass
    await eod(xx, f"Uploaded `{kk}` in `{t}`", time=5)


@ultroid_cmd(
    pattern="save",
)
async def _(event):
    input_str = event.text[6:]
    xx = await eor(event, get_string("com_1"))
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        if not a.message:
            return await xx.edit("`Reply to a message`")
        else:
            b = open(input_str, "w")
            b.write(str(a.message))
            b.close()
            await xx.edit(f"**Packing into** `{input_str}`")
            await asyncio.sleep(2)
            await xx.edit(f"**Uploading** `{input_str}`")
            await asyncio.sleep(2)
            await event.client.send_file(event.chat_id, input_str)
            await xx.delete()
            os.remove(input_str)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
