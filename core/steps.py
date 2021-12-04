# (c) @Judson-web

import os
import json
import inflect as __inflect
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from core.fix import FixEnvData

inflect = __inflect.engine()
ikeyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("𝙲𝚊𝚗𝚌𝚎𝚕 𝙿𝚛𝚘𝚌𝚎𝚜𝚜", callback_data="cancelProcess")]]
)


async def StartSteps(bot: Client, editable: Message):
    heroku_app = {
        "name": "",
        "logo": "",
        "description": "",
        "keywords": list(),
        "repository": "",
        "website": "",
        "success_url": "",
        "env": dict(),
        "stack": "",
        "buildpacks": list(),
        "formation": dict(),
    }
    ## --- Step 1 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟷:**\n" "𝚂𝚎𝚗𝚍 𝚖𝚎 𝚢𝚘𝚞𝚛 𝙷𝚎𝚛𝚘𝚔𝚞 𝙰𝚙𝚙 𝙽𝚊𝚖𝚎!!", reply_markup=ikeyboard
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    if input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    heroku_app["name"] = input_m.text
    await input_m.delete(True)
    ## --- Step 2 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 2:**\n"
        "𝙽𝚘𝚠 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚢𝚘𝚞𝚛 𝙷𝚎𝚛𝚘𝚔𝚞 𝙰𝚙𝚙 𝙳𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗.\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝚂𝚎𝚗𝚍 `/skip`",
        reply_markup=ikeyboard,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    heroku_app["description"] = input_m.text
    if input_m.text.startswith("/skip"):
        del heroku_app["description"]
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    await input_m.delete(True)
    ## --- Step 3 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟹:**\n"
        "𝙽𝚘𝚠 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚢𝚘𝚞𝚛 𝙷𝚎𝚛𝚘𝚔𝚞 𝙰𝚙𝚙 𝙺𝚎𝚢𝚠𝚘𝚛𝚍𝚜.\n"
        "𝚂𝚎𝚙𝚊𝚛𝚊𝚝𝚎 𝚞𝚜𝚒𝚗𝚐 𝚌𝚘𝚖𝚖𝚊(`,`)\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝚂𝚎𝚗𝚍 `/skip`",
        reply_markup=ikeyboard,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    heroku_app["keywords"] = input_m.text.replace(" ", "").split(",")
    if input_m.text.startswith("/skip"):
        del heroku_app["keywords"]
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    await input_m.delete(True)
    ## --- Step 4 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 4:**\n" "𝙽𝚘𝚠 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚢𝚘𝚞𝚛 𝙶𝚒𝚝𝙷𝚞𝚋 𝚁𝚎𝚙𝚘𝚜𝚒𝚝𝚘𝚛𝚢 𝙻𝚒𝚗𝚔.",
        reply_markup=ikeyboard,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    heroku_app["repository"] = input_m.text
    if input_m.text.startswith("/skip"):
        del heroku_app["repository"]
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    await input_m.delete(True)
    ## --- Step 5 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟻:**\n"
        "𝙽𝚘𝚠 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚢𝚘𝚞𝚛 𝚆𝚎𝚋𝚜𝚒𝚝𝚎 𝙻𝚒𝚗𝚔.\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝚂𝚎𝚗𝚍 `/skip`",
        reply_markup=ikeyboard,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    heroku_app["website"] = input_m.text
    if input_m.text.startswith("/skip"):
        del heroku_app["website"]
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    await input_m.delete(True)
    ## --- Step 6 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 6:**\n"
        "𝙽𝚘𝚠 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚢𝚘𝚞𝚛 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝚄𝚁𝙻.\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝚂𝚎𝚗𝚍 `/skip`",
        reply_markup=ikeyboard,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    heroku_app["success_url"] = input_m.text
    if input_m.text.startswith("/skip"):
        del heroku_app["success_url"]
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    await input_m.delete(True)
    ## --- Step 7 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 7:**\n"
        "𝙽𝚘𝚠 𝚝𝚒𝚖𝚎 𝚏𝚘𝚛 𝙴𝙽𝚅 𝚌𝚘𝚗𝚏𝚒𝚐𝚜!\n\n"
        "𝚆𝚑𝚎𝚗 𝚍𝚘𝚗𝚎 𝚂𝚎𝚗𝚍 `/done`\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝚂𝚎𝚗𝚍 `/skip`",
        reply_markup=ikeyboard,
    )
    env_inputs_running = True
    env_count = 1
    while env_inputs_running:
        _cache_m = await editable.reply_text(
            f"𝚂𝚎𝚗𝚍 𝚖𝚎 {inflect.ordinal(env_count)} 𝙴𝙽𝚅 𝚗𝚊𝚖𝚎 & 𝚟𝚊𝚕𝚞𝚎.\n\n"
            "**𝙽𝚘𝚝𝚎:** __𝙴𝙽𝚅 𝚗𝚊𝚖𝚎 𝚠𝚒𝚝𝚑𝚘𝚞𝚝 𝚜𝚙𝚊𝚌𝚎 𝚊𝚗𝚍\n"
            "𝚞𝚜𝚎 (__`:`__) 𝚝𝚘 𝚍𝚎𝚏𝚒𝚗𝚎 𝚍𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗, 𝚟𝚊𝚕𝚞𝚎, 𝚛𝚎𝚚𝚞𝚒𝚛𝚎𝚍, 𝚐𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛 𝚛𝚎𝚜𝚙𝚎𝚌𝚝𝚒𝚟𝚎𝚕𝚢.__"
        )
        input_m: Message = await bot.listen(editable.chat.id, timeout=600)
        if input_m.text.startswith("/skip"):
            del heroku_app["env"]
            env_inputs_running = False
            await _cache_m.delete(True)
            continue
        elif input_m.text.startswith("/done"):
            env_inputs_running = False
            await _cache_m.delete(True)
            continue
        elif input_m.text.startswith("/"):
            return await input_m.continue_propagation()
        input_str = input_m.text.split(":", 5)
        env_count += 1
        if len(input_str) < 5:
            while len(input_str) < 5:
                input_str.append("")
        input_str = await FixEnvData(input_str)
        heroku_app["env"][f"{input_str[0].upper()}"] = {
            "description": f"{input_str[1]}",
            "required": f"{input_str[3]}",
        }
        if input_str[2] != "":
            heroku_app["env"][f"{input_str[0].upper()}"]["value"] = f"{input_str[2]}"
        if input_str[4] != "":
            heroku_app["env"][f"{input_str[0].upper()}"][
                "generator"
            ] = f"{input_str[4]}"
        await input_m.delete(True)
        await _cache_m.delete(True)
    ## --- Step 8 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟾:**\n"
        "𝙽𝚘𝚠 𝚜𝚎𝚗𝚍 𝙷𝚎𝚛𝚘𝚔𝚞 𝙰𝚙𝚙 [𝙱𝚞𝚒𝚕𝚍𝚙𝚊𝚌𝚔𝚜](https://telegra.ph/Heroku-Default-Buildpacks-09-27) 𝚕𝚒𝚜𝚝.\n"
        "𝚂𝚎𝚙𝚊𝚛𝚊𝚝𝚎 𝚠𝚒𝚝𝚑 (`|`)\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝙿𝚛𝚎𝚜𝚜 `/skip`",
        reply_markup=ikeyboard,
        disable_web_page_preview=True,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    input_buildpacks = input_m.text.split("|")
    for i in range(len(input_buildpacks)):
        heroku_app["buildpacks"].append({"url": f"{input_buildpacks[i]}"})
    if input_m.text.startswith("/skip"):
        del heroku_app["buildpacks"]
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    await input_m.delete(True)
    ## --- Step 9 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟿:**\n"
        "𝚆𝚑𝚊𝚝 𝚝𝚢𝚙𝚎 𝚘𝚏 𝚙𝚛𝚘𝚌𝚎𝚜𝚜?\n"
        "𝚂𝚎𝚗𝚍 [`web`] 𝚘𝚛 [`worker`]\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝙿𝚛𝚎𝚜𝚜 `/skip`",
        reply_markup=ikeyboard,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    if input_m.text.startswith("/skip"):
        pass
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    process_type = input_m.text.lower().strip()
    if process_type not in ["web", "worker"]:
        process_type = "worker"
    heroku_app["formation"][f"{process_type}"] = {}
    await input_m.delete(True)
    ## --- Step 10 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟷𝟶:**\n"
        "𝚆𝚑𝚊𝚝 𝚠𝚒𝚕𝚕 𝚋𝚎 𝙳𝚢𝚗𝚘 𝚃𝚢𝚙𝚎?\n"
        "𝚂𝚎𝚗𝚍 [`free`] 𝚘𝚛 [`hobby`] 𝚘𝚛 [`standard-1x`] 𝚘𝚛 "
        "[`standard-2x`] 𝚘𝚛 [`performance-m`] 𝚘𝚛 [`performance-l`]\n\n"
        "[𝙾𝚏𝚏𝚒𝚌𝚒𝚊𝚕 𝙳𝚘𝚌𝚞𝚖𝚎𝚗𝚝𝚊𝚝𝚒𝚘𝚗](https://devcenter.heroku.com/articles/dyno-types)\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝙿𝚛𝚎𝚜𝚜 `/skip`",
        reply_markup=ikeyboard,
        disable_web_page_preview=True,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    if input_m.text.startswith("/skip"):
        pass
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    dyno_type = input_m.text.lower()
    if dyno_type not in [
        "free",
        "hobby",
        "standard-1x",
        "standard-2x",
        "performance-m",
        "performance-l",
    ]:
        dyno_type = "free"
    heroku_app["formation"][f"{process_type}"] = {"quantity": 1, "size": f"{dyno_type}"}
    await input_m.delete(True)
    ## --- Step 11 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟷𝟷:**\n"
        "𝚂𝚎𝚗𝚍 𝚖𝚎 𝙻𝚘𝚐𝚘 𝚒𝚗 𝙹𝙿𝙶 𝚏𝚘𝚛𝚖𝚊𝚝 𝚏𝚘𝚛 𝚢𝚘𝚞𝚛 𝙷𝚎𝚛𝚘𝚔𝚞 𝙰𝚙𝚙.\n\n"
        "𝚃𝚘 𝚂𝚔𝚒𝚙 𝚝𝚑𝚒𝚜 𝚂𝚝𝚎𝚙 𝙿𝚛𝚎𝚜𝚜 `/skip`",
        reply_markup=ikeyboard,
        disable_web_page_preview=True,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    if input_m.text and input_m.text.startswith("/skip"):
        del heroku_app["logo"]
    elif input_m.text and input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    elif input_m.photo:
        await editable.edit("𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝙻𝚘𝚐𝚘 ...")
        logo_jpg = await bot.download_media(
            input_m,
            file_name=f"./downloads/logo/{str(editable.chat.id)}/{str(editable.message_id)}/",
        )
        resp = upload_file(logo_jpg)
        logo_jpg = f"https://telegra.ph/{resp[0]}"
        heroku_app["logo"] = logo_jpg
    else:
        del heroku_app["logo"]
    await input_m.delete(True)
    ## --- Step 11 --- ##
    await editable.edit(
        "**𝚂𝚝𝚎𝚙 𝟷𝟸:**\n"
        "𝚂𝚎𝚗𝚍 𝚖𝚎 [𝙷𝚎𝚛𝚘𝚔𝚞 𝚂𝚝𝚊𝚌𝚔](https://devcenter.heroku.com/articles/stack) 𝚕𝚎𝚟𝚎𝚕.\n"
        "𝙵𝚛𝚘𝚖 𝚑𝚎𝚛𝚎 [`container`, `heroku-20`, `heroku-18`, `heroku-16`]",
        reply_markup=ikeyboard,
        disable_web_page_preview=True,
    )
    input_m: Message = await bot.listen(editable.chat.id, timeout=600)
    if input_m.text.startswith("/skip"):
        del heroku_app["stack"]
    elif input_m.text.startswith("/"):
        return await input_m.continue_propagation()
    else:
        heroku_stack_level = input_m.text.lower().strip()
        if heroku_stack_level not in [
            "container",
            "heroku-20",
            "heroku-18",
            "heroku-16",
        ]:
            heroku_stack_level = "heroku-20"
        heroku_app["stack"] = heroku_stack_level
    await input_m.delete(True)
    ## --- Make --- ##
    await editable.edit("𝙼𝚊𝚔𝚒𝚗𝚐 `𝚊𝚙𝚙.𝚓𝚜𝚘𝚗` ...")
    app_json_f = os.path.join("downloads", str(editable.chat.id), str(editable.message_id))
    if not os.path.exists(app_json_f):
        os.makedirs(app_json_f)
    app_json = os.path.join(app_json_f, "app.json")
    js = json.dumps(heroku_app, indent=4, separators=(",", ": "))
    with open(app_json, "w+") as f:
        f.write(js)
    return app_json
