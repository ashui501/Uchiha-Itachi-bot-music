import asyncio

from telethon.tl.types import ChannelParticipantsAdmins

from . import *

keywords = ["vmess", "trojan", "vless", "proxy", "ss", "ssr"]

async def apolo(event):
    if udB.get_key("MEGANET")!= "True":
        return
    else:
        if not event.chat_id==-1001667884656:
            return
        if event.is_private:
            return
        if event.chat_id==-1001667884656:
            adkins = [-1001667884656]
            participants = await event.client.get_participants(-1001667884656, filter=ChannelParticipantsAdmins())
            for i in participants:
                adkins.append(i.id)
            if event.sender_id in adkins:
                return
            else:
                x = event.message.text.lower()
                if not any(keyword in x for keyword in keywords):
                    await event.message.delete()


@asst_cmd()
async def _(event):
    await apolo(event)

