import re

from telethon import Button
from telethon.errors.rpcerrorlist import (
    BotInlineDisabledError,
    BotResponseTimeoutError,
    MessageNotModifiedError,
)
from telethon.tl import types
from telethon.tl.functions.users import GetFullUserRequest as gu

from . import (
    HNDLR,
    LOGS,
    asst,
    callback,
    get_string,
    in_pattern,
    inline_mention,
    ultroid_bot,
    ultroid_cmd,
)

buddhhu = {}


@ultroid_cmd(
    pattern="wspr( (.*)|$)",
)
async def _(e):
    if e.reply_to_msg_id:
        okk = await e.get_reply_message()
        put = f"@{okk.sender.username}" if okk.sender.username else okk.sender_id
    else:
        put = e.pattern_match.group(1).strip()
    if put:
        try:
            results = await e.client.inline_query(asst.me.username, f"msg {put}")
        except BotResponseTimeoutError:
            return await e.eor(
                get_string("help_2").format(HNDLR),
            )
        except BotInlineDisabledError:
            return await e.eor(get_string("help_3"))
        await results[0].click(e.chat_id, reply_to=e.reply_to_msg_id, hide_via=True)
        return await e.delete()
    await e.eor(get_string("wspr_3"))


@in_pattern("wspr")
async def _(e):
    iuser = e.query.user_id
    zzz = e.text.split(maxsplit=2)
    try:
        query = zzz[1]
        if query.isdigit():
            query = int(query)
        logi = await ultroid_bot.get_entity(query)
        if not isinstance(logi, types.User):
            raise ValueError("Invalid Username.")
    except IndexError:
        sur = await e.builder.article(
            title="Give Username",
            description="You Didn't Type Username or id.",
            text="You Didn't Type Username or id.",
        )
        return await e.answer([sur])
    except ValueError as er:
        LOGS.exception(er)
        sur = await e.builder.article(
            title="User Not Found",
            description="Make sure username or id is correct.",
            text="Make sure username or id is correct.",
        )
        return await e.answer([sur])
    try:
        desc = zzz[2]
    except IndexError:
        sur = await e.builder.article(
            title="ᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ", text="ᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ"
        )
        return await e.answer([sur])
    button = [
        [
            Button.inline("Sᴇᴄrᴇᴛ Mᴇssᴀgᴇ", data=f"dd_{e.id}"),
            Button.inline("Dᴇlᴇᴛᴇ Mᴇssᴀgᴇ", data=f"del_{e.id}"),
        ],
        [
            Button.switch_inline(
                "New", query=f"wspr {logi.username or logi.id}", same_peer=True
            )
        ],
    ]
    us = logi.username or logi.first_name
    sur = await e.builder.article(
        title=logi.first_name,
        description=desc,
        text=get_string("wspr_1").format(us),
        buttons=button,
    )
    buddhhu.update({e.id: [logi.id, iuser, desc]})
    await e.answer([sur])


@in_pattern("msg")
async def _(e):
    zzz = e.text.split(maxsplit=1)
    desc = "Touch me"
    try:
        query = zzz[1]
        if query.isdigit():
            query = int(query)
        logi = await ultroid_bot(gu(id=query))
        user = logi.users[0]
        mention = inline_mention(user)
        x = user.status
        if isinstance(x, types.UserStatusOnline):
            status = "Online"
        elif isinstance(x, types.UserStatusOffline):
            status = "Offline"
        elif isinstance(x, types.UserStatusRecently):
            status = "Last Seen Recently"
        elif isinstance(x, types.UserStatusLastMonth):
            status = "Last seen months ago"
        elif isinstance(x, types.UserStatusLastWeek):
            status = "Last seen weeks ago"
        else:
            status = "Can't Tell"
        text = f"**Ⲛⲁⲙⲉ:**    `{user.first_name}`\n"
        text += f"**ⲒⲆ:**    `{user.id}`\n"
        if user.username:
            text += f"**Ⳙⲋⲉʀⲛⲁⲙⲉ:**    `{user.username}`\n"
            url = f"https://t.me/{user.username}"
        else:
            text += f"**Mention:**    `{mention}`\n"
            url = f"tg://user?id={user.id}"
        text += f"**Ⲋⲧⲁⲧυⲋ:**    `{status}`\n"
        text += f"**Ⲁⲃⲟυⲧ:**    `{logi.full_user.about}`"
        button = [
            Button.url("Privᴀᴛᴇ", url=url),
            Button.switch_inline(
                "Sᴇᴄrᴇᴛ Mᴇssᴀgᴇ",
                query=f"wspr {query} پیامتو اینجا بنویس",
                same_peer=True,
            ),
        ]
        sur = e.builder.article(
            title=user.first_name,
            description=desc,
            text=text,
            buttons=button,
        )
    except IndexError:
        sur = e.builder.article(
            title="Give Username",
            description="You Didn't Type Username or id.",
            text="You Didn't Type Username or id.",
        )
    except BaseException as er:
        LOGS.exception(er)
        name = get_string("wspr_4").format(query)
        sur = e.builder.article(
            title=name,
            text=name,
        )

    await e.answer([sur])


@callback(
    re.compile(
        "dd_(.*)",
    ),
)
async def _(e):
    ids = int(e.pattern_match.group(1).strip().decode("UTF-8"))
    if buddhhu.get(ids):
        if e.sender_id in buddhhu[ids]:
            await e.answer(buddhhu[ids][-1], alert=True)
        else:
            await e.answer("Don't spy at my secret message bitch 😒", alert=True)
    else:
        await e.answer(get_string("wspr_2"), alert=True)


@callback(re.compile("del_(.*)"))
async def _(e):
    ids = int(e.pattern_match.group(1).strip().decode("UTF-8"))
    if buddhhu.get(ids):
        if e.sender_id in buddhhu[ids]:
            buddhhu.pop(ids)
            try:
                await e.edit(get_string("wspr_2"))
            except MessageNotModifiedError:
                pass
        else:
            await e.answer(get_string("wspr_5"), alert=True)
