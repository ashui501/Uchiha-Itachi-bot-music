# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from datetime import datetime

from pytz import timezone as tz
from cython.functions.asst_fns import *
from cython.misc import owner_and_sudos
from telethon import events
from telethon.utils import get_display_name

from plugins import *

from . import *


_settings = [
    [
        Button.inline("API Kᴇʏs", data="apiset"),
        Button.inline("Pᴍ Bᴏᴛ", data="chatbot"),
    ],
    [
        Button.inline("Aʟɪᴠᴇ", data="alvcstm"),
        Button.inline("PᴍPᴇʀᴍɪᴛ", data="ppmset"),
    ],
    [Button.inline("Fᴇᴀᴛᴜʀᴇs", data="otvars")],
    [Button.inline("VC Sᴏɴɢ Bᴏᴛ", data="vcb")],
    [Button.inline("« Bᴀᴄᴋ", data="mainmenu")],
]

_start = [
    [
        Button.inline("Lᴀɴɢᴜᴀɢᴇ 🌐", data="lang"),
        Button.inline("Sᴇᴛᴛɪɴɢs ⚙️", data="setter"),
    ],
    [
        Button.inline("Sᴛᴀᴛs ✨", data="stat"),
        Button.inline("Bʀᴏᴀᴅᴄᴀsᴛ 📻", data="bcast"),
    ],
    [Button.inline("TɪᴍᴇZᴏɴᴇ 🌎", data="tz")],
]

@asst_cmd("start ?(.*)")
async def ultroid(event):
    if event.is_group:
        return
    else:
        if (
            not is_added(event.sender_id)
            and str(event.sender_id) not in owner_and_sudos()
        ):
            add_user(event.sender_id)
            await asst.send_message(
                1601105531,
                f"Bot started by [{event.sender_id}](tg://user?id={event.sender_id})",
            )
        if str(event.sender_id) not in owner_and_sudos():
            ok = ""
            u = await event.client.get_entity(event.chat_id)
            if not udB.get("STARTMSG"):
                if udB.get("PMBOT") == "True":
                    ok = "✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵"
                await event.reply(
                    f"Ⲏⲉⲩ [{get_display_name(u)}](tg://user?id={u.id}), ⲧⲏⲓⲋ ⲓⲋ Ⲋυⲣⲉʀ Ⲧⲉⲥⲏⲛⲟⳑⲟⳋⲩ Ⲁⲋⲋⲓⲋⲧⲁⲛⲧ ⲟϝ {ultroid_bot.me.first_name}!\n\n{ok}",
                    file=udB.get("STARTMEDIA"),
                    buttons=[
                        [
                            Button.url("✵Jᴏin Chᴀnnᴇl✵", url="https://t.me/FutureTechnologyOfficial"),
                        ],
                        [
                            Button.inline("✵Chᴀᴛ wiᴛh CɪᴘʜᴇʀX✵", data="chat"),
                        ],
                        [
                            Button.inline("✵Grᴏuᴩ/Chᴀnnᴇl ʍᴀnᴀgᴇr Hᴇlᴩ✵", data="group"),
                        ],
                        [
                            Button.inline("✵CɪᴘʜᴇʀX Sᴇrvᴇr Ping✵", data="ping"),
                        ],
                        [
                            Button.inline("✵Tᴇxᴛ Trᴀnslᴀᴛᴏr✵", data="tlans"),
                        ],
                        [
                            Button.inline("✵CɪᴘʜᴇʀX Bᴏᴛs Lisᴛ✵", data="list"),
                        ],
                    ],
                )
            else:
                me = f"[{ultroid_bot.me.first_name}](tg://user?id={ultroid_bot.uid})"
                mention = f"[{get_display_name(u)}](tg://user?id={u.id})"
                await event.reply(
                    Redis("STARTMSG").format(me=me, mention=mention),
                    file=udB.get("STARTMEDIA"),
                    buttons=[
                        [
                            Button.url("✵Jᴏin Chᴀnnᴇl✵", url="https://t.me/FutureTechnologyOfficial"),
                        ],
                        [
                            Button.inline("✵Chᴀᴛ wiᴛh CɪᴘʜᴇʀX✵", data="chat"),
                        ],
                        [
                            Button.inline("✵Grᴏuᴩ/Chᴀnnᴇl ʍᴀnᴀgᴇr Hᴇlᴩ✵", data="group"),
                        ],
                        [
                            Button.inline("✵CɪᴘʜᴇʀX Sᴇrvᴇr Ping✵", data="ping"),
                        ],
                        [
                            Button.inline("✵Tᴇxᴛ Trᴀnslᴀᴛᴏr✵", data="tlans"),
                        ],
                        [
                            Button.inline("✵CɪᴘʜᴇʀX Bᴏᴛs Lisᴛ✵", data="list"),
                        ],
                    ],
                )
        else:
            name = get_display_name(event.sender_id)
            if event.pattern_match.group(1) == "set":
                await event.reply(
                    "Choose from the below options -",
                    buttons=_settings,
                )
            else:
                await event.reply(
                    get_string("ast_3").format(name),
                    buttons=_start,
                )


@callback("tlans")
async def tlans(event):
    await asst.send_message(event.chat_id, "✨ How to use:\n1⃣ `/tr LangaugeCode text` \n2⃣ `/tr Language Code` as reply to a message \n\nHere is the list of [Language Codes](https://telegra.ph/CɪᴘʜᴇʀX-03-10)", link_preview=False)

@callback("list")
async def list(event):
    await asst.send_message(event.chat_id, "⚜️ Here is the list of bots made by CɪᴘʜᴇʀX ⚜️\n\n🎆CɪᴘʜᴇʀX Assistant ~ [Bot Link](https://t.me/CipherXBot)\n\n🎆File to Link Generator ~ [Bot Link](https://t.me/FiletoLinkTelegramBot)\n\n🎆Rename with Custom Thumbnail ~ [Bot Link](https://t.me/RenameTelegramBot)\n\n🎆LynX Group Manager ~ [Bot Link](https://t.me/LynXGroupManagerRobot)\n\n🎆Future Technology Chat Bot ~ [Bot Link](https://t.me/FutureTechnologyChatBot)", link_preview=False)

@callback("chat")
async def chat(event):
    await asst.send_message(event.chat_id, "Send your message please. I'll see and answer you whenever get online\n\n✨ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ✨")

Lastupdate = time.time()

@callback("ping")
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"**█▀█ █ █▄░█ █▀▀ █ \n█▀▀ █ █░▀█ █▄█ ▄**\n\n ➲CɪᴘʜᴇʀX Ⲋⲉʀⳳⲉʀ Ⲣⲓⲛⳋ~`{ms}ms`",
    )

@callback("group")
async def users(event):
    await event.delete()
    grabon = "🎆 Here Are Some Commands for group/channel management\n➤ /start ~ Check if I'm Alive \n➤ /ping ~ Ping CɪᴘʜᴇʀX Server Response Time\n➤ /tr <lang-code>\n➤ /id ~ Shows ID of User/Media/Chat\n➤ /ban ~ Works in Group , Bans a User \n➤ /unban ~ Works in Group , Unbans a User\n➤ /promote ~ Promotes A User \n➤ /demote ~ Demotes A User \n➤ /gpin ~ Pins a Message\n(c)✨ CɪᴘʜᴇʀX Ⲃⲟⲧ Ⲉⲭⲥⳑυⲋⲓⳳⲉ ✨"
    await asst.send_message(event.chat_id, grabon)




@callback("mainmenu")
@owner
async def ultroid(event):
    if event.is_group:
        return
    await event.edit(
        get_string("ast_3").format(OWNER_NAME),
        buttons=_start,
    )


@callback("stat")
@owner
async def botstat(event):
    ok = len(get_all_users())
    msg = """CɪᴘʜᴇʀX Assistant - Stats
Total Users - {}""".format(
        ok,
    )
    await event.answer(msg, cache_time=0, alert=True)


@callback("bcast")
@owner
async def bdcast(event):
    ok = get_all_users()
    await event.edit(f"Broadcast to {len(ok)} users.")
    async with event.client.conversation(OWNER_ID) as conv:
        await conv.send_message(
            "Enter your broadcast message.\nUse /cancel to stop the broadcast.",
        )
        response = conv.wait_event(events.NewMessage(chats=OWNER_ID))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message("Cancelled!!")
        else:
            success = 0
            fail = 0
            await conv.send_message(f"Starting a broadcast to {len(ok)} users...")
            start = datetime.now()
            for i in ok:
                try:
                    await asst.send_message(int(i), f"{themssg}")
                    success += 1
                except BaseException:
                    fail += 1
            end = datetime.now()
            time_taken = (end - start).seconds
            await conv.send_message(
                f"""
Broadcast completed in {time_taken} seconds.
Total Users in Bot - {len(ok)}
Sent to {success} users.
Failed for {fail} user(s).""",
            )


@callback("setter")
@owner
async def setting(event):
    await event.edit(
        "Choose from the below options -",
        buttons=_settings,
    )


@callback("tz")
@owner
async def timezone_(event):
    await event.delete()
    pru = event.sender_id
    var = "TIMEZONE"
    name = "Timezone"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            "Send Your TimeZone From This List [Check From Here](http://www.timezoneconverter.com/cgi-bin/findzone.tzc)"
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("mainmenu"),
            )
        else:
            try:
                tz(themssg)
                await setit(event, var, themssg)
                await conv.send_message(
                    f"{name} changed to {themssg}\n",
                    buttons=get_back_button("mainmenu"),
                )
            except BaseException:
                await conv.send_message(
                    "Wrong TimeZone, Try again",
                    buttons=get_back_button("mainmenu"),
                )
