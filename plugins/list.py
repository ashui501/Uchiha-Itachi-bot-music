# Credits belong to CɪᴘʜᴇʀX(@Hackintush)
# Written for Ultroid Userbot 

"""
✘ Commands Available

• `{i}lid idtext`
    Get users id of a chat in txt format.

• `{i}lid idcsv`
    Get users id of a chat in csv format.

• `{i}lid usertext`
    Get users username of a chat in txt format.

• `{i}lid usercsv`
    Get users username of a chat in csv format.
""" 

from telethon.errors import ChatAdminRequiredError

from . import * 


@ultroid_cmd(pattern="lid")
async def listtotal(event):
    x = await eor(event, get_string("com_1"))
    try:
        t = event.text.split(" ", maxsplit=1)[1]
    except Exception as e:
        return await eor(x, f"Type `{HNDLR}help list` to see the commands", time=10)
    if t == "idtext":
        return await id_text(x)
    elif t == "idcsv":
        return await id_csv(x)
    elif t == "usertext":
        return await user_text(x)
    elif t == "usercsv":
        return await user_csv(x)
    else:
        await eor(x, "`Lol, What are you doing?`", time=5)


async def id_text(x):
    if not x.text[0].isalpha() and x.text[0] not in ("/", "#", "@", "!"):
        if not x.is_group:
            await x.edit("Do the command in groups only.")
            return
        reply = await x.get_reply_message()
        info = await x.client.get_entity(x.chat_id)
        title = info.title if info.title else "this chat"
        group_id = x.to_id.channel_id
        mentions = "Ⳙⲋⲉʀⲋ Ⲓⲇ ⲓⲛ -100{}\n".format(group_id)
        try:
            async for user in x.client.iter_participants(x.chat_id):
                if not user.deleted:
                    mentions += f"\n{user.id}"
                else:
                    mentions += f"\n{user.id}"
            else:
                async for user in x.client.iter_participants(
                    x.chat_id,
                ):
                    if not user.deleted:
                        mentions += f"\n{user.id}"
                    else:
                        mentions += f"\n{user.id}"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            file = open("IdList.txt", "w+")
            file.write(mentions)
            file.close()
            await x.client.send_file(
                x.chat_id,
                "IdList.txt",
                caption="Ⳙⲋⲉʀⲋ Ⲓⲇ ⲓⲛ {}".format(title),
                reply_to=reply,
            )
            os.remove("IdList.txt")
        except:
            print("sed")
    await eod(x, "Done", time=5)


async def id_csv(x):
    if not x.text[0].isalpha() and x.text[0] not in ("/", "#", "@", "!"):
        if not x.is_group:
            await x.edit("Do the command in groups only.")
            return
        reply = await x.get_reply_message()
        info = await x.client.get_entity(x.chat_id)
        title = info.title if info.title else "this chat"
        group_id = x.to_id.channel_id
        mentions = "Ⳙⲋⲉʀⲋ Ⲓⲇ ⲓⲛ -100{}\n".format(group_id)
        try:
            async for user in x.client.iter_participants(x.chat_id):
                if not user.deleted:
                    mentions += f"\n{user.id}"
                else:
                    mentions += f"\n{user.id}"
            else:
                async for user in x.client.iter_participants(
                    x.chat_id,
                ):
                    if not user.deleted:
                        mentions += f"\n{user.id}"
                    else:
                        mentions += f"\n{user.id}"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            file = open("IdList.csv", "w+")
            file.write(mentions)
            file.close()
            await x.client.send_file(
                x.chat_id,
                "IdList.csv",
                caption="Ⳙⲋⲉʀⲋ Ⲓⲇ ⲓⲛ {}".format(title),
                reply_to=reply,
            )
            os.remove("IdList.csv")
        except:
            print("sed")
    await eod(x, "Done", time=5)


async def user_text(x):
    if not x.text[0].isalpha() and x.text[0] not in ("/", "#", "@", "!"):
        if not x.is_group:
            await x.edit("Do the command in groups only.")
            return
        reply = await x.get_reply_message()
        info = await x.client.get_entity(x.chat_id)
        title = info.title if info.title else "this chat"
        mentions = "Ⳙⲋⲉʀⲋ ⲓⲛ {}: \n".format(title)
        try:
            async for user in x.client.iter_participants(x.chat_id):
                if not user.deleted:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    )
                else:
                    mentions += f"\nⲆⲉⳑⲉⲧⲉⲇ Ⲁⲥⲥⲟυⲛⲧ `{user.id}`"
            else:
                async for user in x.client.iter_participants(
                    x.chat_id,
                ):
                    if not user.deleted:
                        mentions += (
                            f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                        )
                    else:
                        mentions += f"\nⲆⲉⳑⲉⲧⲉⲇ Ⲁⲥⲥⲟυⲛⲧ `{user.id}`"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            file = open("UserList.txt", "w+")
            file.write(mentions)
            file.close()
            await x.client.send_file(
                x.chat_id,
                "UserList.txt",
                caption="Ⳙⲋⲉʀⲋ ⲓⲛ {}".format(title),
                reply_to=reply,
            )
            os.remove("UserList.txt")
        except:
            print("sed")
    await eod(x, "Done", time=5)


async def user_csv(x):
    if not x.text[0].isalpha() and x.text[0] not in ("/", "#", "@", "!"):
        if not x.is_group:
            await x.edit("Do the command in groups only.")
            return
        reply = await x.get_reply_message()
        info = await x.client.get_entity(x.chat_id)
        title = info.title if info.title else "this chat"
        mentions = "Ⳙⲋⲉʀⲋ ⲓⲛ {}: \n".format(title)
        try:
            async for user in x.client.iter_participants(x.chat_id):
                if not user.deleted:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    )
                else:
                    mentions += f"\nⲆⲉⳑⲉⲧⲉⲇ Ⲁⲥⲥⲟυⲛⲧ `{user.id}`"
            else:
                async for user in x.client.iter_participants(
                    x.chat_id,
                ):
                    if not user.deleted:
                        mentions += (
                            f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                        )
                    else:
                        mentions += f"\nⲆⲉⳑⲉⲧⲉⲇ Ⲁⲥⲥⲟυⲛⲧ `{user.id}`"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            file = open("UserList.csv", "w+")
            file.write(mentions)
            file.close()
            await x.client.send_file(
                x.chat_id,
                "UserList.csv",
                caption="Ⳙⲋⲉʀⲋ ⲓⲛ {}".format(title),
                reply_to=reply,
            )
            os.remove("UserList.csv")
        except:
            print("sed")
    await eod(x, "Done", time=5)
    

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
