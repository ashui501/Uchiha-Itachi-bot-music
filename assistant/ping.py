# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import time
import shutil
import psutil
from datetime import datetime

Lastupdate = time.time()

@asst_cmd("ping$")
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"**█▀█ █ █▄░█ █▀▀ █ \n█▀▀ █ █░▀█ █▄█ ▄**\n\n ➲CɪᴘʜᴇʀX Ⲋⲉʀⳳⲉʀ Ⲣⲓⲛⳋ~`{ms} milliseconds`",
    )
