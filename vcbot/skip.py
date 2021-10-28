"""
✘ Commands Available -

• `{i}skip`
   Skip the current song and play the next in queue, if any.
"""

from . import *


@vc_asst("skip")
async def skipper(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat, event)
    await ultSongs.play_from_queue()
