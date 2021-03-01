from googletrans import Translator
import emoji
from . import *

@asst_cmd("tr")
async def _(event):
    input = event.text[4:6]
    txt = event.text[7:]
    xx = await eor(event, "`Translating...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    elif input:
        text = txt
        lan = input or "en"
    else:
        return await eod(xx, f"`/tr LanguageCode` as reply to a message", time=5)
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        tt = translator.translate(text, dest=lan)
        output_str = f"**Trᴀnslᴀᴛᴇd** Frᴏʍ {tt.src} Tᴏ {lan} By CɪᴘʜᴇʀX Bᴏᴛ\n{tt.text}"
        await eod(xx, output_str)
    except Exception as exc:
        await eod(xx, str(exc), time=10)
