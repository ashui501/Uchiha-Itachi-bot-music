import requests
from googletrans import Translator


from . import *

@asst_cmd("tr") 
async def _(event):
    input = event.text[4:6]
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    elif "|" in input:
        lan, text = input.split("|")
    else:
        await asst.send_message(
            event.chat_id, "`/tr LanguageCode` as reply to a message"
        )
        return
    translator = Translator()
    try:
        tt = translator.translate(text, dest=lan)
        output_str = f"""**Ⲧʀⲁⲛⲋⳑⲁⲧⲉⲇ ⲃⲩ CɪᴘʜᴇʀX Ⲃⲟⲧ**
    **Ⲋⲟυʀⲥⲉ ({tt.src})**:
    `{text}`

    **Ⲧʀⲁⲛⲋⳑⲁⲧⲓⲟⲛ ({transl_lan})**:
    `{lan}`"""
        if len(output_str) >= 4096:
            url = "https://del.dog/documents"
            r = requests.post(url, data=output_str.encode("UTF-8")).json()
            url2 = f"https://del.dog/{r['key']}"
            output_str = (
                f"Translated text was too big, so I've pasted it [Here]({url2})"
            )
        await asst.send_message(event.chat_id, output_str)
    except Exception:
        await asst.send_message(event.chat_id, "Something went wrong 🤔\nSee [Language Codes](https://telegra.ph/CɪᴘʜᴇʀX-03-10) and try again.")
        
        
        
