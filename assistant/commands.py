import time
from datetime import datetime
import requests
from google_trans_new import google_translator

from telethon import events, Button 
from telethon.utils import pack_bot_file_id
 
from strings.strings import get_string
from . import *
from plugins import * 

@asst_cmd(pattern="tr$") 
async def _(event):
    if len(event.text) > 3 and event.text[3] != " ":
        return
    input = event.text[4:6]
    txt = event.text[7:]
    if txt:
        text = txt
        lan = input or "en"
    elif event.is_reply:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    else:
        return await event.edit(event.chat_id, "1⃣ /tr [Language Code](https://telegra.ph/CɪᴘʜᴇʀX-03-10) as reply to a message\n2⃣ /tr <target LangCode> <text> ~ Ex: /tr ko hello", link_preview=False)
    translator = google_translator()
    try:
        tt = translator.translate(text, lang_tgt=lan)
        fr = translator.detect(text)
        output_str = f"**Ⲧʀⲁⲛⲋⳑⲁⲧⲉⲇ ⲃⲩ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ**\n\n**Ⲋⲟυʀⲥⲉ ({fr})**:\n`{text}`\n\n**Ⲧʀⲁⲛⲋⳑⲁⲧⲓⲟⲛ ({lan})**:\n`{tt.text}`"
        if len(output_str) >= 4096:
            url = "https://del.dog/documents"
            r = requests.post(url, data=output_str.encode("UTF-8")).json()
            url2 = f"https://del.dog/{r['key']}"
            output_str = (
                f"Translated text was too big, so I've pasted it [Here]({url2})"
            )
        await event.reply(output_str)
    except Exception:
        await event.reply("Something went wrong 🤔\nSee [Language Codes](https://telegra.ph/CɪᴘʜᴇʀX-03-10) and try again.", link_preview=False)
       
       
@asst_cmd(pattern="id")
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await asst.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id), bot_api_file_id
                ),
            )
        else:
            await asst.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)
                ),
            )
    else:
        await asst.send_message(
            event.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id))
        )


@asst_cmd(pattern="ping")
async def _(event):
    start = time.time()
    x = await event.respond("𝙿𝙸𝙽𝙶")
    end = round((time.time() - start) * 1000)
    uptime = time_formatter((time.time() - start_time) * 1000)
    await x.edit(get_string("ping").format(end, uptime))


@asst_cmd(pattern="repo")
async def repify(e):
    await e.reply(REPOMSG, file=udB.get("STARTMEDIA"), buttons=BTS) 
    
