import requests
from googletrans import Translator


from . import *

@asst_cmd("tr") 
async def _(event):
    if len(event.text) > 3:
        if not event.text[3] == " ":
            return
    input = event.text[4:6]
    txt = event.text[7:]
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    elif input:
        text = txt
        lan = input or "en"
    else:
        return await event.reply("1⃣ /tr [Language Code](https://telegra.ph/CɪᴘʜᴇʀX-03-10) as reply to a message\n2⃣ /tr <target LangCode> <text> ~ Ex: /tr ko hello", link_preview=False)
    translator = Translator()
    try:
        tt = translator.translate(text, dest=lan)
        output_str = f"""**Ⲧʀⲁⲛⲋⳑⲁⲧⲉⲇ ⲃⲩ CɪᴘʜᴇʀX Ⲃⲟⲧ**\n\n**Ⲋⲟυʀⲥⲉ ({tt.src})**:\n`{text}`\n\n**Ⲧʀⲁⲛⲋⳑⲁⲧⲓⲟⲛ (lan})**:\n`{{tt.text}`"""
        #if len(output_str) >= 4096:
            #url = "https://del.dog/documents"
            #r = requests.post(url, data=output_str.encode("UTF-8")).json()
            #url2 = f"https://del.dog/{r['key']}"
            #output_str = (
            #    f"Translated text was too big, so I've pasted it [Here]({url2})"
            #)
        await event.reply(output_str)
    except Exception:
        await asst.send_message(event.chat_id, "Something went wrong 🤔\nSee [Language Codes](https://telegra.ph/CɪᴘʜᴇʀX-03-10) and try again.", link_preview=False)
        
        
        
