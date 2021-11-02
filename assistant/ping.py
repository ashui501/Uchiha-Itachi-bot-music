import time
import shutil
import psutil
from datetime import datetime

Lastupdate = time.time()

@asst_cmd(pattern="ping$")
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"**█▀█ █ █▄░█ █▀▀ █ \n█▀▀ █ █░▀█ █▄█ ▄**\n\n ➲CɪᴘʜᴇʀX Ⲋⲉʀⳳⲉʀ Ⲣⲓⲛⳋ~`{ms} milliseconds`",
    )
