# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import base64
from random import choice
from re import compile as re_compile
from re import findall

import requests
import json
from bs4 import BeautifulSoup
from play_scraper import search
from search_engine_parser import GoogleSearch, YahooSearch
from telethon import Button
from telethon.tl.types import InputWebDocument as wb

from . import *
from . import humanbytes as hb

binpic = "https://telegra.ph/file/be4dd7375ef2313a43c41.jpg"
ippic = "https://telegra.ph/file/807e012dbe2789c0648ee.jpg"
gugirl = "https://telegra.ph/file/0df54ae4541abca96aa11.jpg"
yeah = "https://telegra.ph/file/e3c67885e16a194937516.jpg"
ps = "https://telegra.ph/file/de0b8d9c858c62fae3b6e.jpg"
ultpic = "https://telegra.ph/file/b2da137de76fc5cd85ffa.jpg"
xkcdpic = "https://telegra.ph/file/040b5ab6e50e438fc215e.jpg"

api1 = base64.b64decode("QUl6YVN5QXlEQnNZM1dSdEI1WVBDNmFCX3c4SkF5NlpkWE5jNkZV").decode(
    "ascii"
)
api2 = base64.b64decode("QUl6YVN5QkYwenhMbFlsUE1wOXh3TVFxVktDUVJxOERnZHJMWHNn").decode(
    "ascii"
)
api3 = base64.b64decode("QUl6YVN5RGRPS253blB3VklRX2xiSDVzWUU0Rm9YakFLSVFWMERR").decode(
    "ascii"
)

@in_pattern("xkcd")
@in_owner
async def _(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="xkcd",
            description="Random Meme",
            thumb=wb(xkcdpic, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ X𐌺𑀝𑀥**\n\nYou didn't search any query",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="xkcd ", same_peer=True),
        )
        await e.answer([kkkk])
        return
    xkcd_id = None
    if quer:
        if quer.isdigit():
            xkcd_id = quer
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url, params={"action": "xkcd", "query": quote(quer)}
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        data.get("title")
        output_str = """
[XKCD]({})
Title: {}
Alt: {}
Day: {}
Month: {}
Year: {}""".format(
            xkcd_link, safe_title, alt, day, month, year
        )
        lul_k = builder.photo(file=img, text=output_str)
        await e.answer([lul_k])
    else:
        resultm = builder.article(
            title="- No Results :/ -", text=f"No Results Found.\n(C) CɪᴘʜᴇʀX"
        )
        await e.answer([resultm])

@in_pattern("bin")
@in_owner
async def _(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Bin Checker",
            description="Give me your bin number",
            thumb=wb(binpic, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Ⲃⲓⲛ Ⲥⲏⲉⲥⲕⲉʀ**\n\nYou didn't search any bin number",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="bin ", same_peer=True),
        )
        await e.answer([kkkk])
    url = f"https://bins-su-api.vercel.app/api/{quer}"
    data = json.loads(requests.get(url).text) 
    search(quer)
    results = data["result"]
    messages = data["message"]
    types = data["data"]["type"]
    bins = data["data"]["bin"]
    vendors = data["data"]["vendor"]
    levels = data["data"]["level"]
    banks = data["data"]["bank"]
    countrys = data["data"]["country"]
    text = """
**Ⳳⲁⳑⲓⲇⲓⲧⲩ**:- `{}`
**Ⲋⲧⲁⲧυⲋ**:- `{}`
**Ⲃⲓⲛ Ⲛυⲙⲃⲉʀ**:- `{}`
**Ⳳⲉⲛⲇⲟʀ**:- `{}`
**Ⳑⲉⳳⲉⳑ**:- `{}`
**Ⲧⲩⲣⲉ**:- `{}`
**Ⲃⲁⲛⲕ**:- `{}`
**Ⲥⲟυⲛⲧʀⲩ**:- `{}`
**✨ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ ✨**
""".format(
            results,
            messages,
            bins,
            vendors,
            levels,
            types,
            banks,
            countrys,
        )
    but = [
        await e.builder.article(
            title=f"Bin Nuʍʙᴇr Sᴇᴀrᴄh Rᴇsulᴛ",
            description=f"{results}\n{messages}",
            text=text,
            thumb=wb(binpic, 0, "image/jpeg", []),
            link_preview=False,
            buttons=[
                [
                    Button.switch_inline(
                        "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                        query="bin ",
                        same_peer=True,
                    ),
                    Button.switch_inline(
                        "Sʜᴀʀᴇ",
                        query=f"bin {quer}",
                        same_peer=False,
                    ),
                ],
            ],
        ),
    ] 
    await e.answer(but)
    
    

@in_pattern("ip")
async def _(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        kkkk = e.builder.article(
            title="Ip Info",
            description="Give me an ip address",
            thumb=wb(ippic, 0, "image/jpeg", []),
            text="**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ ⲒⲢ Ⲓⲛϝⲟ**\n\nYou didn't search any ip address",
            buttons=Button.switch_inline("Sᴇᴀʀᴄʜ Aɢᴀɪɴ", query="ip ", same_peer=True),
        )
        await e.answer([kkkk])
    url = f"http://ip-api.com/json/{quer}"
    data = json.loads(requests.get(url).text) 
    search(quer)
    stat = data["status"]
    count = data["country"]
    countc = data["countryCode"]
    reg = data["region"]
    regn = data["regionName"]
    cit = data["city"]
    zp = data["zip"]
    lt = data["lat"]
    ln = data["lon"]
    tz = data["timezone"]
    isps = data["isp"]
    orgs = data["org"]
    ass = data["as"]
    que = data["query"]
    linkk = f"https://maps.google.com/?q={lt},{ln}"
    text = """
**IP Aɗɗrᥱss**:- `{}`
**𐍃ᴛᥲᴛᥙs**:- `{}`
**𑀝᧐ᥙᥒᴛry**:- `{}`
**𑀝᧐ᥙᥒᴛry 𑀝᧐ɗᥱ**:- `{}`
**Rᥱgi᧐ᥒ**:- `{}`
**Rᥱgi᧐ᥒ 𐌽ᥲⲙᥱ**:- `{}`
**𑀝iᴛy**:- `{}`
**Ziρ**:- `{}`
**𑀉ᥲᴛiᴛᥙɗᥱ**:- `{}`
**𑀉᧐ᥒgiᴛᥙɗᥱ**:- `{}`
**Tiⲙᥱ Z᧐ᥒᥱ**:- `{}`
**I𐍃P**:- `{}`
**𐌏RᏵ**:- `{}`
**A𐍃**:- `{}`
**𑀉᧐ᥴᥲᴛi᧐ᥒ 𑀉iᥒκ**:- [Link]({})

**✨ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ ✨**
""".format(
            que,
            stat,
            count,
            countc,
            reg,
            regn,
            cit,
            zp,
            lt,
            ln,
            tz,
            isps,
            orgs,
            ass,
            linkk,
        )
    but = [
        await e.builder.article(
            title=f"IP Iᥒf᧐rⲙᥲᴛi᧐ᥒ Rᥱsᥙᥣᴛ",
            description=f"{stat}\n{count}",
            text=text,
            thumb=wb(ippic, 0, "image/jpeg", []),
            link_preview=False,
            buttons=[
                [
                    Button.switch_inline(
                        "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                        query="ip ",
                        same_peer=True,
                    ),
                    Button.switch_inline(
                        "Sʜᴀʀᴇ",
                        query=f"ip {quer}",
                        same_peer=False,
                    ),
                ],
            ],
        ),
    ] 
    await e.answer(but)


@in_pattern("file ?(.*)")
@in_owner
async def _(e):
    file_path = e.pattern_match.group(1)
    file_name = file_path.split("/")[-1]
    bitton = [
        [
            Button.inline("anonfiles", data=f"flanonfiles//{file_path}"),
            Button.inline("transfer", data=f"fltransfer//{file_path}"),
        ],
        [
            Button.inline("bayfiles", data=f"flbayfiles//{file_path}"),
            Button.inline("x0", data=f"flx0//{file_path}"),
        ],
        [
            Button.inline("file.io", data=f"flfile.io//{file_path}"),
            Button.inline("siasky", data=f"flsiasky//{file_path}"),
        ],
    ]
    try:
        lnk = e.builder.article(
            title="file",
            text=f"**File:**\n{file_name}",
            buttons=bitton,
        )
    except BaseException:
        lnk = e.builder.article(
            title="file",
            text="File not found",
        )
    await e.answer([lnk], switch_pm="File to Link", switch_pm_param="start")


@callback(
    re_compile(
        "fl(.*)",
    ),
)
@owner
async def _(e):
    t = (e.data).decode("UTF-8")
    data = t[2:]
    host = data.split("//")[0]
    file = data.split("//")[1]
    file_name = file.split("/")[-1]
    await e.edit(f"Uploading... `{file_name}` on {host}")
    await dloader(e, host, file)

@in_pattern("cipherx")
@in_owner
async def repo(e):
    res = [
        await e.builder.article(
            title="CɪᴘʜᴇʀX Bᴏᴛ",
            description="CɪᴘʜᴇʀX Bᴏᴛ | Telethon",
            thumb=wb(ultpic, 0, "image/jpeg", []),
            text="• **CɪᴘʜᴇʀX Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ** •",
            buttons=[
                [Button.url("•CɪᴘʜᴇʀX Bᴏᴛ•", url="t.me/CipherXBot")],
                [Button.url("•Sᴜᴘᴘᴏʀᴛ Chᴀnnᴇl•", url="t.me/FutureTechnologyOfficial")],
            ],
        ),
    ]
    await e.answer(res, switch_pm="CɪᴘʜᴇʀX Suᴩᴇr Tᴇᴄhnᴏlᴏgy Bᴏᴛ", switch_pm_param="start")
    
    
@in_pattern("go")
@in_owner
async def gsearch(q_event):
    try:
        match = q_event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await q_event.answer(
            [], switch_pm="Google Search. Enter a query!", switch_pm_param="start"
        )
        await q_event.answer([kkkk])
    searcher = []
    page = findall(r"page=\d+", match)
    cache = False
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page), bool(cache))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
            searcher.append(
                await q_event.builder.article(
                    title=title,
                    description=desc,
                    thumb=wb(gugirl, 0, "image/jpeg", []),
                    text=f"**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Gᴏᴏɢʟᴇ Sᴇᴀʀᴄʜ**\n\n**••Tɪᴛʟᴇ••**\n`{title}`\n\n**••Dᴇsᴄʀɪᴘᴛɪᴏɴ••**\n`{desc}`",
                    link_preview=False,
                    buttons=[
                        [Button.url("Lɪɴᴋ", url=f"{link}")],
                        [
                            Button.switch_inline(
                                "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                                query="go ",
                                same_peer=True,
                            ),
                            Button.switch_inline(
                                "Sʜᴀʀᴇ",
                                query=f"go {match}",
                                same_peer=False,
                            ),
                        ],
                    ],
                ),
            )
        except IndexError:
            break
    await q_event.answer(searcher, switch_pm="Google Search", switch_pm_param="start")

@in_pattern("yahoo")
@in_owner
async def yahoosearch(q_event):
    try:
        match = q_event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await q_event.answer(
            [], switch_pm="Yahoo Search. Enter a query!", switch_pm_param="start"
        )
        await q_event.answer([kkkk])
    searcher = []
    page = findall(r"page=\d+", match)
    cache = False
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page), bool(cache))
    gsearch = YahooSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
            searcher.append(
                await q_event.builder.article(
                    title=title,
                    description=desc,
                    thumb=wb(yeah, 0, "image/jpeg", []),
                    text=f"**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ Yᴀʜᴏᴏ Sᴇᴀʀᴄʜ**\n\n**••Tɪᴛʟᴇ••**\n`{title}`\n\n**••Dᴇsᴄʀɪᴘᴛɪᴏɴ••**\n`{desc}`",
                    link_preview=False,
                    buttons=[
                        [Button.url("Lɪɴᴋ", url=f"{link}")],
                        [
                            Button.switch_inline(
                                "Sᴇᴀʀᴄʜ Aɢᴀɪɴ",
                                query="yahoo ",
                                same_peer=True,
                            ),
                            Button.switch_inline(
                                "Sʜᴀʀᴇ",
                                query=f"yahoo {match}",
                                same_peer=False,
                            ),
                        ],
                    ],
                ),
            )
        except IndexError:
            break
    await q_event.answer(searcher, switch_pm="Yahoo Search", switch_pm_param="start")


@in_pattern("app")
@in_owner
async def _(e):
    try:
        f = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await e.answer(
            [], switch_pm="App search. Enter app name!", switch_pm_param="start"
        )
        await e.answer([kkkk])
    foles = []
    aap = search(f)
    for z in aap:
        name = z["title"]
        desc = z["description"]
        price = z["price"]
        dev = z["developer"]
        icon = z["icon"]
        url = z["url"]
        ids = z["app_id"]
        text = f"**••Aᴘᴘ Nᴀᴍᴇ••** [{name}]({icon})\n"
        text += f"**••Dᴇᴠᴇʟᴏᴘᴇʀ••** `{dev}`\n"
        text += f"**••Pʀɪᴄᴇ••** `{price}`\n\n"
        text += f"**••Dᴇsᴄʀɪᴘᴛɪᴏɴ••**\n`{desc}`"
        foles.append(
            await e.builder.article(
                title=name,
                description=ids,
                thumb=wb(ps, 0, "image/jpeg", []),
                text=text,
                link_preview=True,
                buttons=[
                    [Button.url("Lɪɴᴋ", url=f"https://play.google.com{url}")],
                    [
                        Button.switch_inline(
                            "Mᴏʀᴇ Aᴘᴘs",
                            query="app ",
                            same_peer=True,
                        ),
                        Button.switch_inline(
                            "Sʜᴀʀᴇ",
                            query=f"app {f}",
                            same_peer=False,
                        ),
                    ],
                ],
            ),
        )
    await e.answer(foles, switch_pm="Application Searcher", switch_pm_param="start")


@in_pattern("mods")
@in_owner
async def _(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await e.answer(
            [], switch_pm="Mod Apps Search. Enter app name!", switch_pm_param="start"
        )
    page = 1
    start = (page - 1) * 3 + 1
    da = choice([api1, api2, api3])
    url = f"https://www.googleapis.com/customsearch/v1?key={da}&cx=25b3b50edb928435b&q={quer}&start={start}"
    url = f"https://www.googleapis.com/customsearch/v1?key={da}&cx=25b3b50edb928435b&q={quer}&start={start}"
    data = requests.get(url).json()
    search_items = data.get("items")
    search(quer)
    modss = []
    for a in search_items:
        title = a.get("title")
        desc = a.get("snippet")
        link = a.get("link")
        text = f"**••Tɪᴛʟᴇ••** `{title}`\n\n"
        text += f"**Dᴇsᴄʀɪᴘᴛɪᴏɴ** `{desc}`"
        modss.append(
            await e.builder.article(
                title=title,
                description=desc,
                text=text,
                link_preview=True,
                buttons=[
                    [Button.url("Dᴏᴡɴʟᴏᴀᴅ", url=f"{link}")],
                    [
                        Button.switch_inline(
                            "Mᴏʀᴇ Mᴏᴅs",
                            query="mods ",
                            same_peer=True,
                        ),
                        Button.switch_inline(
                            "Sʜᴀʀᴇ",
                            query=f"mods {quer}",
                            same_peer=False,
                        ),
                    ],
                ],
            ),
        )
    await e.answer(modss, switch_pm="Search Mod Applications", switch_pm_param="start")


@in_pattern("clipart")
@in_owner
async def clip(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await e.answer([], switch_pm="ClipArt Search", switch_pm_param="start")
    quer = quer.replace(" ", "+")
    sear = f"https://clipartix.com/search/{quer}"
    html = urlopen(sear)
    bs = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    resul = bs.find_all("img", "attachment-full size-full")
    buil = e.builder
    hm = []
    for res in resul:
        hm += [buil.photo(include_media=True, file=res["src"])]
    await e.answer(
        hm, gallery=True, switch_pm="Clipart Searcher", switch_pm_param="start"
    )



@in_pattern("ebooks")
@in_owner
async def clip(e):
    try:
        quer = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await e.answer(
            [], switch_pm="Enter Query to Look for EBook", switch_pm_param="start"
        )
        return
    quer = quer.replace(" ", "+")
    sear = f"http://www.gutenberg.org/ebooks/search/?query={quer}&submit_search=Go%21"
    magma = requests.get(sear).content
    bs = BeautifulSoup(magma, "html.parser", from_encoding="utf-8")
    out = bs.find_all("img")
    Alink = bs.find_all("a", "link")
    if len(out) == 0:
        return await e.answer(
            [], switch_pm="No Results Found !", switch_pm_param="start"
        )
    buil = e.builder
    dont_take = [
        "Authors",
        "Did you mean",
        "Sort Alpha",
        "Sort by",
        "Subjects",
        "Bookshelves",
    ]
    hm = []
    titles = []
    for num in Alink:
        try:
            rt = num.find("span", "title").text
            if not rt.startswith(tuple(dont_take)):
                titles.append(rt)
        except BaseException:
            pass
    for rs in range(len(out)):
        if "/cache/epub" in out[rs]["src"]:
            link = out[rs]["src"]
            num = link.split("/")[3]
            link = "https://gutenberg.org" + link.replace("small", "medium")
            file = wb(link, 0, "image/jpeg", [])
            hm.append(
                buil.article(
                    title=titles[rs],
                    type="photo",
                    description="GutenBerg Search",
                    thumb=file,
                    content=file,
                    include_media=True,
                    text=f"**• CɪᴘʜᴇʀX ᴇxᴄlusivᴇ ʙᴏᴛ Ebook Search**\n\n->> `{titles[rs]}`",
                    buttons=Button.inline("Get as Doc", data=f"ebk_{num}"),
                )
            )
    await e.answer(hm, switch_pm="Ebooks Search", switch_pm_param="start")
