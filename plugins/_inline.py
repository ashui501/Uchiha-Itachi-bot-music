# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import os
import random
import re
import time
from datetime import datetime
from math import ceil
from platform import python_version as pyver

from git import Repo
from support import *
from telethon import Button, __version__
from telethon.tl.types import InputWebDocument
from cython.dB.database import Var
from . import *

PMPIC = os.environ.get("PMPIC", None)
if PMPIC is None:
    WARN_PIC = "https://telegra.ph/file/82c595986872349e5ba1a.jpg"
else:
    WARN_PIC = PMPIC

# ================================================#
notmine = "This bot is for {}".format(OWNER_NAME)
ULTROID_PIC = "https://telegra.ph/file/167a0b85048b04129bd3b.jpg"
helps = """
**✨{} Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ Hᴇʟᴘ Mᴇɴᴜ✨

✵ Pʟᴜɢɪɴs ~ {}**
"""


if Var.ADDONS:
    zhelps = """
**✨{} Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ Hᴇʟᴘ Mᴇɴᴜ✨

✵ Aᴅᴅᴏɴs ~ {}**
"""
else:
    zhelps = """
**✨{} Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ Hᴇʟᴘ Mᴇɴᴜ✨

✵ Aᴅᴅᴏɴs ~ {}

Gᴏ Aɴᴅ Aᴅᴅ ADDON Vᴀʀ Wɪᴛʜ Vᴀʟᴜᴇ Tʀᴜᴇ**
"""
# ============================================#

@inline
async def inline_handler(event):
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id == bot.uid and query.startswith("**PMSecurity"):
        result = builder.photo(
            file=WARN_PIC,
            text=query,
            buttons=[
                [
                    custom.Button.inline(
                        "✘ I'm Here for Spamming ✘", data="dontspamnigga"
                    )
                ],
                [
                    custom.Button.inline(
                        "✓ I'm Here for Talking with CɪᴘʜᴇʀX ✓",
                        data="whattalk",
                    )
                ],
                [
                    custom.Button.inline(
                        "✓ I'm Here for Asking Something ✓", data="askme"
                    )
                ],
                [custom.Button.inline("≼≼≼Close Menu≽≽≽", data="sendclose")],
            ],
        )
        await event.answer([result])

@inline
@callback("dontspamnigga")
async def rip(event):
    if event.query.user_id == bot.uid:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    text1 = "You Have Chosed A Prohibited Option. Therefore, You Have Been Blocked and Reported to Telegram Agency.\n(C) CɪᴘʜᴇʀX"
    await event.edit("⨵ Choice not Accepted ⨵")
    await ultroid_bot.send_message(event.query.user_id, text1)
    await ultroid_bot(functions.contacts.BlockRequest(event.query.user_id))
    await ultroid_bot.send_message(
        Var.LOG_CHANNEL,
        f"Hello, [This](tg://user?id={him_id}) Selected Prohibited Option, Therefore Blocked.\n(C) CɪᴘʜᴇʀX",
    )

@inline
@callback("whattalk")
async def rip(event):
    if event.query.user_id == bot.uid:
        sedok = "Master, you don't need to use this."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Choice Accepted ✓\n(C) CɪᴘʜᴇʀX")
    text2 = "Ok. Please Wait until CɪᴘʜᴇʀX Approves you. Don't Spam or Try Anything Stupid. \nThanks for Contacting me."
    await ultroid_bot.send_message(event.query.user_id, text2)
    await ultroid_bot.send_message(
        Var.LOG_CHANNEL,
        message=f"Hello, [New User](tg://user?id={him_id}) Wants to Talk with tou.\n(C) CɪᴘʜᴇʀX",
        buttons=[Button.url("Contact Him", f"tg://user?id={him_id}")],
    )

@inline
@callback("askme")
async def rip(event):
    if event.query.user_id == bot.uid:
        sedok = "Master, you don't need to use this."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Choice Accepted ✓")
    text3 = (
        "Ok, Wait. You can Ask after CɪᴘʜᴇʀX Approves you. Kindly, Wait.\n(C) CɪᴘʜᴇʀX"
    )
    await ultroid_bot.send_message(event.query.user_id, text3)
    await ultroid_bot.send_message(
        Var.LOG_CHANNEL,
        message=f"Hello, [New User](tg://user?id={him_id}) Wants to Ask you Something.\n(C) CɪᴘʜᴇʀX",
        buttons=[Button.url("Contact Him", f"tg://user?id={him_id}")],
    )


@inline
@callback("sendclose")
async def users(event):
    await event.edit(
        "⨵CɪᴘʜᴇʀX Bot Pm-Security Closed⨵",
        buttons=[(custom.Button.inline("≼≼≼Leave Me≽≽≽"))],
    )

@inline
@in_owner
async def e(o):
    if len(o.text) == 0:
        b = o.builder
        uptime = grt((time.time() - start_time))
        ALIVEMSG = """
**CɪᴘʜᴇʀX Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ**\n\n
✵ **Ⲟⲱⲛⲉʀ** - `{}`
✵ **Ⳳⲉʀⲋⲓⲟⲛ** - `{}`
✵ **Ⳙⲣⲧⲓⲙⲉ** - `{}`
✵ **Ⲣⲩⲧⲏⲟⲛ** - `{}`
✵ **Ⲧⲉⳑⲉⲧⲏⲟⲛ** - `{}`
✵ **Ⲃʀⲁⲛⲥⲏ** - `{}`
✵ ✨ [CɪᴘʜᴇʀX](t.me/hackintush) is ᴛhᴇ Bᴇsᴛ ✨
""".format(
            OWNER_NAME,
            ultroid_version,
            uptime,
            pyver(),
            __version__,
            Repo().active_branch,
        )
        res = [
            b.article(
                title="✵ CɪᴘʜᴇʀX Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ ✵",
                url="https://t.me/Hackintush",
                description=" (c) CɪᴘʜᴇʀX ",
                text=ALIVEMSG,
                thumb=InputWebDocument(ULTROID_PIC, 0, "image/jpeg", []),
            )
        ]
        await o.answer(res, switch_pm=f"👥 CɪᴘʜᴇʀX Ⲣⲟʀⲧⲁⳑ", switch_pm_param="start")


if Var.BOT_USERNAME is not None and asst is not None:

    @inline
    @in_owner
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id in sed and query.startswith("ultd"):
            result = builder.article(
                title="Help Menu",
                description="✵ Help Menu of CɪᴘʜᴇʀX Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ ✵ | (c) CɪᴘʜᴇʀX",
                url="https://t.me/Hackintush",
                thumb=InputWebDocument(ULTROID_PIC, 0, "image/jpeg", []),
                text=f"**✨{OWNER_NAME} Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ✨ \n\n✵ Mᴀɪɴ Mᴇɴᴜ\n\n✵ Pʟᴜɢɪɴs ~ {len(PLUGINS) - 4}\n✵ Aᴅᴅᴏɴs ~ {len(ADDONS)}**",
                buttons=[
                    [
                        Button.inline("• Pʟᴜɢɪɴs", data="hrrrr"),
                        Button.inline("• Aᴅᴅᴏɴs", data="frrr"),
                    ],
                    [Button.inline("Oᴡɴᴇʀ•ᴛᴏᴏʟꜱ", data="ownr")],
                    [Button.inline("Iɴʟɪɴᴇ•Pʟᴜɢɪɴs", data="inlone")],
                    [Button.inline("••Cʟᴏꜱᴇ••", data="close")],
                ],
            )
            await event.answer([result] if result else None)
        elif event.query.user_id in sed and query.startswith("paste"):
            ok = query.split("-")[1]
            link = f"https://nekobin.com/{ok}"
            link_raw = f"https://nekobin.com/raw/{ok}"
            result = builder.article(
                title="Paste",
                text="Pᴀsᴛᴇᴅ Tᴏ Nᴇᴋᴏʙɪɴ!",
                buttons=[
                    [
                        Button.url("✵NekoBin✵", url=f"{link}"),
                        Button.url("✵Raw✵", url=f"{link_raw}"),
                    ]
                ],
            )
            await event.answer([result] if result else None)

    @inline
    @in_owner
    @callback("ownr")
    @owner
    async def setting(event):
        await event.edit(
            buttons=[
                [
                    Button.inline("•Pɪɴɢ•", data="pkng"),
                    Button.inline("•Uᴘᴛɪᴍᴇ•", data="upp"),
                ],
                [Button.inline("•Rᴇsᴛᴀʀᴛ•", data="rstrt")],
                [Button.inline("<- Bᴀᴄᴋ", data="open")],
            ],
        )

    @callback("pkng")
    async def _(event):
        start = datetime.now()
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        pin = f"🌋Pɪɴɢ = {ms}ms"
        await event.answer(pin, cache_time=0, alert=True)

    @callback("upp")
    async def _(event):
        uptime = grt((time.time() - start_time))
        pin = f"✵ Uᴘᴛɪᴍᴇ = {uptime}"
        await event.answer(pin, cache_time=0, alert=True)

    @callback("inlone")
    @owner
    async def _(e):
        button = [
            [
                Button.switch_inline(
                    "✵ Sᴇɴᴅ Oғғɪᴄɪᴀʟ Pʟᴜɢɪɴs",
                    query="send ",
                    same_peer=True,
                )
            ],
            [
                Button.switch_inline(
                    "✵ Pʟᴀʏ Sᴛᴏʀᴇ Aᴘᴘs",
                    query="app ",
                    same_peer=True,
                )
            ],
            [
                Button.switch_inline(
                    "✵ Mᴏᴅᴅᴇᴅ Aᴘᴘs",
                    query="mods ",
                    same_peer=True,
                )
            ],
            [
                Button.switch_inline(
                    "✵ Sᴇᴀʀᴄʜ Oɴ Gᴏᴏɢʟᴇ",
                    query="google ",
                    same_peer=True,
                )
            ],
            [
                Button.switch_inline(
                    "✵ Sᴇᴀʀᴄʜ Oɴ Yᴀʜᴏᴏ",
                    query="yahoo ",
                    same_peer=True,
                )
            ],
            [
                Button.switch_inline(
                    "✵ YᴏᴜTᴜʙᴇ Dᴏᴡɴʟᴏᴀᴅᴇʀ",
                    query="yt ",
                    same_peer=True,
                )
            ],
            [
                Button.switch_inline(
                    "✵ CʟɪᴘAʀᴛ Sᴇᴀʀᴄʜ",
                    query="clipart ",
                    same_peer=True,
                )
            ],
            [
                Button.inline(
                    "<- Bᴀᴄᴋ",
                    data="open",
                )
            ],
        ]
        await e.edit(buttons=button, link_preview=False)

    @callback("hrrrr")
    @owner
    async def on_plug_in_callback_query_handler(event):
        xhelps = helps.format(OWNER_NAME, len(PLUGINS) - 4)
        buttons = paginate_help(0, PLUGINS, "helpme")
        await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)

    @callback("frrr")
    @owner
    async def addon(event):
        halp = zhelps.format(OWNER_NAME, len(ADDONS))
        if len(ADDONS) > 0:
            buttons = paginate_addon(0, ADDONS, "addon")
            await event.edit(f"{halp}", buttons=buttons, link_preview=False)
        else:
            await event.answer(
                "• Iɴsᴛᴀʟʟ A Pʟᴜɢɪɴ Mᴀɴᴜᴀʟʟʏ Oʀ Aᴅᴅ Vᴀʀ ADDON Wɪᴛʜ Vᴀʟᴜᴇ Tʀᴜᴇ",
                cache_time=0,
                alert=True,
            )

    @callback("rstrt")
    @owner
    async def rrst(ult):
        await restart(ult)

    @callback(
        re.compile(
            rb"helpme_next\((.+?)\)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page_number + 1, PLUGINS, "helpme")
        await event.edit(buttons=buttons, link_preview=False)

    @callback(
        re.compile(
            rb"helpme_prev\((.+?)\)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page_number - 1, PLUGINS, "helpme")
        await event.edit(buttons=buttons, link_preview=False)

    @callback(
        re.compile(
            rb"addon_next\((.+?)\)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_addon(current_page_number + 1, ADDONS, "addon")
        await event.edit(buttons=buttons, link_preview=False)

    @callback(
        re.compile(
            rb"addon_prev\((.+?)\)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_addon(current_page_number - 1, ADDONS, "addon")
        await event.edit(buttons=buttons, link_preview=False)

    @callback("back")
    @owner
    async def backr(event):
        xhelps = helps.format(OWNER_NAME, len(PLUGINS) - 4)
        current_page_number = int(upage) 
        buttons = paginate_help(current_page_number, PLUGINS, "helpme")
        await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)

    @callback("buck")
    @owner
    async def backr(event):
        xhelps = zhelps.format(OWNER_NAME, len(ADDONS))
        current_page_number = int(addpage) 
        buttons = paginate_addon(current_page_number, ADDONS, "addon")
        await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)

    @callback("open")
    @owner
    async def opner(event):
        buttons = [
            [
                Button.inline("• Pʟᴜɢɪɴs ", data="hrrrr"),
                Button.inline("• Aᴅᴅᴏɴs", data="frrr"),
            ],
            [Button.inline("Oᴡɴᴇʀ•Tᴏᴏʟꜱ", data="ownr")],
            [Button.inline("Iɴʟɪɴᴇ•Pʟᴜɢɪɴs", data="inlone")],
            [Button.inline("••Cʟᴏꜱᴇ••", data="close")],
        ]
        await event.edit(
            f"✨ **{OWNER_NAME}** Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ Hᴇʟᴘ Mᴇɴᴜ✨\n\n✵ Mᴀɪɴ Mᴇɴᴜ\n\n✵ Oꜰꜰɪᴄɪᴀʟ Pʟᴜɢɪɴs ~ {len(PLUGINS) - 4}\n✵ Uɴᴏꜰꜰɪᴄɪᴀʟ Pʟᴜɢɪɴs ~ {len(ADDONS)}**",
            buttons=buttons,
            link_preview=False,
        )

    @callback("close")
    @owner
    async def on_plug_in_callback_query_handler(event):
        await event.edit(
            "**≼≼≼Mᴇɴᴜ Hᴀs Bᴇᴇɴ Cʟᴏsᴇᴅ≽≽≽**",
            buttons=Button.inline("≼≼≼Oᴘᴇɴ Mᴀɪɴ Mᴇɴᴜ Aɢᴀɪɴ≽≽≽", data="open"),
        )

    @callback(
        re.compile(
            b"us_plugin_(.*)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = f"Plugin Name - `{plugin_name}`\n"
        try:
            for i in HELP[plugin_name]:
                help_string += i
        except BaseException:
            pass
        if help_string == "":
            reply_pop_up_alert = "{} has no detailed help...".format(plugin_name)
        else:
            reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n© CɪᴘʜᴇʀX"
        try:
            if event.query.user_id in sed:
                await event.edit(
                    reply_pop_up_alert,
                    buttons=[
                        Button.inline("<- Bᴀᴄᴋ", data="back"),
                        Button.inline("••Cʟᴏꜱᴇ••", data="close"),
                    ],
                )
            else:
                reply_pop_up_alert = notmine
                await event.answer(reply_pop_up_alert, cache_time=0)
        except BaseException:
            halps = "Do .help {} to get the list of commands.".format(plugin_name)
            await event.edit(halps)

    @callback(
        re.compile(
            b"add_plugin_(.*)",
        ),
    )
    @owner
    async def on_plug_in_callback_query_handler(event):
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = ""
        try:
            for i in HELP[plugin_name]:
                help_string += i
        except BaseException:
            try:
                for u in CMD_HELP[plugin_name]:
                    help_string = (
                        f"Plugin Name-{plugin_name}\n\n✘ Commands Available-\n\n"
                    )
                    help_string += str(CMD_HELP[plugin_name])
            except BaseException:
                try:
                    if plugin_name in LIST:
                        help_string = (
                            f"Plugin Name-{plugin_name}\n\n✘ Commands Available-\n\n"
                        )
                        for d in LIST[plugin_name]:
                            help_string += Var.HNDLR + d
                            help_string += "\n"
                except BaseException:
                    pass
        if help_string == "":
            reply_pop_up_alert = "{} has no detailed help...".format(plugin_name)
        else:
            reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n© CɪᴘʜᴇʀX"
        try:
            if event.query.user_id in sed:
                await event.edit(
                    reply_pop_up_alert,
                    buttons=[
                        Button.inline("<- Bᴀᴄᴋ", data="buck"),
                        Button.inline("••Cʟᴏꜱᴇ••", data="close"),
                    ],
                )
            else:
                reply_pop_up_alert = notmine
                await event.answer(reply_pop_up_alert, cache_time=0)
        except BaseException:
            halps = "Do .help {} to get the list of commands.".format(plugin_name)
            await event.edit(halps)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 6
    number_of_cols = 2
    multi = os.environ.get("EMOJI_TO_DESPLAY_IN_HELP", "✵")
    mult2i = os.environ.get("EMOJI2_TO_DESPLAY_IN_HELP", "✵")
    helpable_plugins = []
    global upage
    upage = page_number
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        Button.inline(
            "{} {} {}".format(
                random.choice(list(multi)), x, random.choice(list(mult2i))
            ),
            data="us_plugin_{}".format(x),
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline(
                    "<- Pʀᴇᴠɪᴏᴜs", data="{}_prev({})".format(prefix, modulo_page)
                ),
                Button.inline("-Bᴀᴄᴋ-", data="open"),
                Button.inline(
                    "Nᴇxᴛ ->", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    else:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline("-Bᴀᴄᴋ-", data="open"),
            )
        ]
    return pairs


def paginate_addon(page_number, loaded_plugins, prefix):
    number_of_rows = 6
    number_of_cols = 2
    multi = os.environ.get("EMOJI_TO_DESPLAY_IN_HELP", "✵")
    mult2i = os.environ.get("EMOJI2_TO_DESPLAY_IN_HELP", "✵")
    helpable_plugins = []
    global addpage
    addpage = page_number
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        Button.inline(
            "{} {} {}".format(
                random.choice(list(multi)), x, random.choice(list(mult2i))
            ),
            data="add_plugin_{}".format(x),
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline(
                    "<- Pʀᴇᴠɪᴏᴜs", data="{}_prev({})".format(prefix, modulo_page)
                ),
                Button.inline("-Bᴀᴄᴋ-", data="open"),
                Button.inline(
                    "Nᴇxᴛ ->", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    else:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline("-Bᴀᴄᴋ-", data="open"),
            )
        ]
    return pairs
