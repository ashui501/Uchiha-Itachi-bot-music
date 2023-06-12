#All credits belong to @CipherXBot/ToxygenX 
#Copy with credits else mf gay

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timezone, timedelta

from telethon import types  

from . import *

x = datetime.now(timezone.utc) - timedelta(seconds=30)

d = udB.get_key("ADMIN")
y = [int(m) for m in d.split()] 

demoted_admins = set()

async def revenge():
    for user_id in y:
        users = [
            p.id
            for p in await asst.get_participants(
                -1001888066860, filter=types.ChannelParticipantsKicked
            )
            if p.participant.kicked_by == user_id and p.participant.date >= x
        ]
        if len(users) >= 3 and user_id not in demoted_admins:
            await asst.edit_admin(
                -1001192530125,
                user_id,
                invite_users=False,
                ban_users=False,
                delete_messages=False,
                pin_messages=False,
                manage_call=False,
                change_info=False,
                post_messages=False, 
                edit_messages=False, 
                add_admins=False, 
            )
            LOGS.info(f"✨ demoted {user_id} at {datetime.now()} successfully")
            demoted_admins.add(user_id)
        elif len(users) == 0 and user_id in demoted_admins:
            demoted_admins.remove(user_id)

scheduler = AsyncIOScheduler(timezone=timezone.utc)

scheduler.add_job(revenge, "interval", seconds=30)

scheduler.start()