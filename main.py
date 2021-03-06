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
        "π·ππ, πΈ π°π π·πππππ πππ.ππππ πΆππππππππ π±ππ.\n\n"
        "ππ πππππ πΌπππππ πππ.ππππ π΅ππ ππππ π·πππππ π°ππ,\n"
        "ππππ `/f`",
        quote=True,
        disable_web_page_preview=True,
    )


@app.on_message(filters.command("f") & ~filters.edited & filters.private)
async def f_command(bot: Client, m: Message):
    editable = await m.reply_text(
        "π±πππ πΏπππππ π πππ ...",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("α΄α΄Ι΄α΄α΄Κ α΄Κα΄α΄α΄κ±κ±", callback_data="cancelProcess")]]
        ),
    )
    try:
        app_json = await StartSteps(bot, editable)
        if os.path.exists(app_json):
            await bot.send_document(
                chat_id=m.chat.id,
                document=app_json,
                caption="`πΌπππ π±π’ @STMbOTsUPPORTgROUP`",
            )
            await editable.edit("ππππ `πππ.ππππ` !!")
            os.remove(app_json)
        else:
            await editable.edit("π΅πππππ ππ πΌπππ `πππ.ππππ` !!\n\n" "πππ’ πππππ!!")
    except TimeoutError:
        pass


@app.on_callback_query()
async def cb_handler(_, cb: CallbackQuery):
    if "cancelProcess" in cb.data:
        await cb.message.edit("πΏππππππ π²ππππππππ ππππππππππππ’!")


app.start()
print("Bot Started!")
idle()
app.stop()
print("Bot Stopped!")
