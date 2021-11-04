from . import *

REPOMSG = """
• **CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ** • 
"""

RP_BUTTONS = [
    [Button.url(get_string("bot_3"), "https://xhamsterlive.com")],
    [Button.url("Ⲋυⲣⲣⲟʀⲧ", "t.me/FutureTechnologyOfficial")],
]

BTS =[
    [
        Button.url("• Rⲉⲣⲟ •­", "https://xhamsterlive.com"), 
        Button.url("• Ⲋυⲣⲣⲟʀⲧ •­", "t.me/FutureTechnologyOfficial"),
    ], 
]
 

ULTSTRING = """🎇 **Thanks for Deploying CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    type=["official", "manager", "assistant"],
)
async def repify(e):
    await e.reply(REPOMSG, file=udB.get("STARTMEDIA"), buttons=BTS) 
    

@ultroid_cmd(pattern="cipher$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/167a0b85048b04129bd3b.jpg",
        buttons=button,
    )
    await eor(rs, f"**[Click Here]({msg.message_link})**")
