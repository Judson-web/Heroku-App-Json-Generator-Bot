# (c) @Judson-web

import os
from configs import Configs
from pyromod import listen
from asyncio import TimeoutError
from core.steps import StartSteps
from pyrogram import Client, filters, idle
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)

app = Client(
    session_name=Configs.SESSION_NAME,
    api_id=Configs.API_ID,
    api_hash=Configs.API_HASH,
    bot_token=Configs.BOT_TOKEN,
)


@app.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_command(_, m: Message):
    await m.reply_text(
        "𝙷𝚕𝚘, 𝙸 𝙰𝚖 𝙷𝚎𝚛𝚘𝚔𝚞 𝚊𝚙𝚙.𝚓𝚜𝚘𝚗 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛 𝙱𝚘𝚝.\n\n"
        "𝚃𝚘 𝚂𝚝𝚊𝚛𝚝 𝙼𝚊𝚔𝚒𝚗𝚐 𝚊𝚙𝚙.𝚓𝚜𝚘𝚗 𝙵𝚘𝚛 𝚈𝚘𝚞𝚛 𝙷𝚎𝚛𝚘𝚔𝚞 𝙰𝚙𝚙,\n"
        "𝚂𝚎𝚗𝚍 `/f`",
        quote=True,
        disable_web_page_preview=True,
    )


@app.on_message(filters.command("f") & ~filters.edited & filters.private)
async def f_command(bot: Client, m: Message):
    editable = await m.reply_text(
        "𝙱𝚛𝚞𝚑 𝙿𝚕𝚎𝚊𝚜𝚎 𝚠𝚊𝚒𝚝 ...",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ᴄᴀɴᴄᴇʟ ᴘʀᴏᴄᴇꜱꜱ", callback_data="cancelProcess")]]
        ),
    )
    try:
        app_json = await StartSteps(bot, editable)
        if os.path.exists(app_json):
            await bot.send_document(
                chat_id=m.chat.id,
                document=app_json,
                caption="`𝙼𝚊𝚍𝚎 𝙱𝚢 [𝙼𝚒𝚌𝚔𝚎𝚢](https://t.me/STMbOTsUPPORTgROUP)`",
            )
            await editable.edit("𝚂𝚎𝚗𝚝 `𝚊𝚙𝚙.𝚓𝚜𝚘𝚗` !!")
            os.remove(app_json)
        else:
            await editable.edit("𝙵𝚊𝚒𝚕𝚎𝚍 𝚝𝚘 𝙼𝚊𝚔𝚎 `𝚊𝚙𝚙.𝚓𝚜𝚘𝚗` !!\n\n" "𝚃𝚛𝚢 𝚊𝚐𝚊𝚒𝚗!!")
    except TimeoutError:
        pass


@app.on_callback_query()
async def cb_handler(_, cb: CallbackQuery):
    if "cancelProcess" in cb.data:
        await cb.message.edit("𝙿𝚛𝚘𝚌𝚎𝚜𝚜 𝙲𝚊𝚗𝚌𝚎𝚕𝚕𝚎𝚍 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢!")


app.start()
print("Bot Started!")
idle()
app.stop()
print("Bot Stopped!")
