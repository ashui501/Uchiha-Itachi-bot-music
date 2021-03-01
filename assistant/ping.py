# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import time
from datetime import datetime


@asst_cmd("ping")
@owner
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - start_time))
    await asst.send_message(
        event.chat_id,
        f"**█▀█ █ █▄░█ █▀▀ █ \n█▀▀ █ █░▀█ █▄█ ▄**\n ➲CɪᴘʜᴇʀX Ⲋⲉʀⳳⲉʀ Ⲣⲓⲛⳋ : `{ms}ms`\n ➲ CɪᴘʜᴇʀX bot uptime : `{uptime}`",
    )
