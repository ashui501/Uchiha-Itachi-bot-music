#Ported from Friday Userbot by @Hackintush 

import logging 

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy import Column, String, create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from telethon import functions
from telethon.tl.types import ChatBannedRights

from . import * 

from cython.dB.database import Var
from cython.misc._supporter import Config 

"""
✘ Commands Available -
• `{i}nighton`
    Enables Night Mode from Database. (from 3-7 AM) 
• `{i}nightoff`
    Disables Night Mode from Database. (from 3-7 AM) 
"""

##########SQL Support##########

class Nightmode(BASE):
    __tablename__ = "nightmode"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Nightmode.__table__.create(checkfirst=True)


def add_nightmode(chat_id: str):
    nightmoddy = Nightmode(str(chat_id))
    SESSION.add(nightmoddy)
    SESSION.commit()


def rmnightmode(chat_id: str):
    rmnightmoddy = SESSION.query(Nightmode).get(str(chat_id))
    if rmnightmoddy:
        SESSION.delete(rmnightmoddy)
        SESSION.commit()


def get_all_chat_id():
    stark = SESSION.query(Nightmode).all()
    SESSION.close()
    return stark


def is_nightmode_indb(chat_id: str):
    try:
        s__ = SESSION.query(Nightmode).get(str(chat_id))
        if s__:
            return str(s__.chat_id)
    finally:
        SESSION.close()

databased = logging.getLogger("DATABASE")


def start() -> scoped_session:
    engine = create_engine(Var.REDIS_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    databased.warning(
        "REDIS_URI is not configured. Features depending on the database might have issues."
    )
    databased.warning(str(e))

##########SQL Support##########

hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)

async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        if sed.is_admin:
            is_mod = True
        else:
            is_mod = False
    except:
        is_mod = False
    return is_mod

@ultroid_cmd(pattern="nighton$")
async def close_ws(event):
    if not event.is_group:
        await event.edit("You Can Only Enable Night Mode in Groups!")
        return
    if not await is_admin(event, bot.uid):
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if is_nightmode_indb(str(event.chat_id)):
        await event.edit("This Chat is Has Already Enabled Night Mode.")
        return
    add_nightmode(str(event.chat_id))
    await event.edit(
        f"**Added Chat {event.chat.title} with id {event.chat_id} To CɪᴘʜᴇʀX Bot Database. This Group Will Be Closed on 3 Am And Will Opened On 7 Am**"
    )


@ultroid_cmd(pattern="nightoff$")
async def disable_ws(event):
    if not event.is_group:
        await event.edit("You Can Only Disable Night Mode in Groups!")
        return
    if not await is_admin(event, bot.uid):
        await event.edit("`You Should Be Admin to Do This!`")
        return
    if not is_nightmode_indb(str(event.chat_id)):
        await event.edit("This Chat Has Not Enabled Night Mode.")
        return
    rmnightmode(str(event.chat_id))
    await event.edit(
        f"**Removed Chat {event.chat.title} With id {event.chat_id} from CɪᴘʜᴇʀX Bot Database.**"
    )


async def job_close():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await ultroid_bot.send_message(
                int(warner.chat_id),
                "`3:00 Am, Group is Closing Till 7 Am. Night Mode Started !` \n**✨Powered by CɪᴘʜᴇʀX✨**",
            )
            await ultroid_bot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(warner.chat_id), banned_rights=hehes
                )
            )
            if Config.CLEAN_GROUPS:
                async for user in ultroid_bot.iter_participants(int(warner.chat_id)):
                    if user.deleted:
                        await ultroid_bot.edit_permissions(
                            int(warner.chat_id), user.id, view_messages=False
                        )
        except Exception as e:
            logger.info(f"Unable to Close Group {warner} - {e}")


scheduler = AsyncIOScheduler(timezone="Asia/Tehran")
scheduler.add_job(job_close, trigger="cron", hour=2, minute=55)
scheduler.start()


async def job_open():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await ultroid_bot.send_message(
                int(warner.chat_id),
                "`7:00 Am, Group is Opening.`\n**✨Powered By CɪᴘʜᴇʀX✨**",
            )
            await ultroid_bot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(warner.chat_id), banned_rights=openhehe
                )
            )
        except Exception as e:
            logger.info(f"Unable to Open Group {warner.chat_id} - {e}")


# Run everyday at 06
scheduler = AsyncIOScheduler(timezone="Asia/Tehran")
scheduler.add_job(job_open, trigger="cron", hour=7, minute=10)
scheduler.start()

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
