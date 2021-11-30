from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from Config import MUST_JOIN


@Client.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"You must join [this channel]({link}) to use me. After joining try again !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ Join Channel ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")


if not await is_served_chat(chat_id):
        await message.reply_text(
            f"**__𝐌𝐚'𝐚𝐟 𝐠𝐫𝐨𝐮𝐩 𝐢𝐧𝐢 𝐛𝐞𝐥𝐮𝐦 𝐭𝐞𝐫𝐝𝐚𝐟𝐭𝐚𝐫.__**\n\n𝐌𝐔𝐒𝐈𝐊 𝐊𝐔 𝐇𝐚𝐧𝐲𝐚 𝐮𝐧𝐭𝐮𝐤 𝐠𝐫𝐨𝐮𝐩 𝐲𝐚𝐧𝐠 𝐭𝐞𝐫𝐝𝐚𝐟𝐭𝐚𝐫 𝐬𝐚𝐣𝐚. 𝐒𝐢𝐥𝐚𝐡𝐤𝐚𝐧 𝐡𝐮𝐛𝐮𝐧𝐠𝐢 𝐀𝐝𝐦𝐢𝐧 𝐛𝐨𝐭 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐝𝐚𝐟𝐭𝐚𝐫.\n𝐏𝐞𝐫𝐢𝐤𝐬𝐚 𝐝𝐚𝐟𝐭𝐚𝐫 𝐚𝐝𝐦𝐢𝐧 𝐛𝐨𝐭 [𝐊𝐋𝐈𝐊 𝐃𝐈𝐒𝐈𝐍𝐈](https://t.me/{BOT_USERNAME}?start=sudolist)"
        )
        return await app.leave_chat(chat_id)
    out = start_pannel()
    await message.reply_text(
        f"𝐓𝐞𝐫𝐢𝐦𝐚𝐤𝐚𝐬𝐢𝐡 𝐭𝐞𝐥𝐚𝐡 𝐦𝐞𝐧𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐬𝐚𝐲𝐚 𝐝𝐢 𝐠𝐫𝐨𝐮𝐩 𝐀𝐧𝐝𝐚 {message.chat.title}.\n𝐁𝐨𝐭 𝐬𝐢𝐚𝐩 𝐝𝐢 𝐠𝐮𝐧𝐚𝐤𝐚𝐧.\n\n𝐉𝐢𝐤𝐚 𝐛𝐮𝐭𝐮𝐡 𝐛𝐚𝐧𝐭𝐮𝐚𝐧 𝐬𝐢𝐥𝐚𝐡𝐤𝐚𝐧 𝐛𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠 𝐝𝐢 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐤𝐚𝐦𝐢.",
        reply_markup=InlineKeyboardMarkup(out[1]),
    )
    return


@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def play(_, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, message.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await message.reply(
                    f"**Hay {rpk} Untuk menghindari penggunaan yang berlebihan bot ini di khususkan untuk yang sudah join di group kami!**",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("✨ Join Channel ✨", url=link)]]
                    ),
                )
                await message.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Saya bukan admin di chat MUST_JOIN chat : {MUST_JOIN} !")
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        await app.send_photo(
            message.chat.id,
            photo=KEN,
            caption=f"𝐇𝐚𝐥𝐨 {rpk}!\n\n𝐈𝐧𝐢 𝐚𝐝𝐚𝐥𝐚𝐡 𝐛𝐨𝐭 𝐦𝐮𝐬𝐢𝐤 𝐌𝐔𝐒𝐈𝐊 𝐊𝐔.\n𝐁𝐨𝐭 𝐢𝐧𝐢 𝐦𝐚𝐦𝐩𝐮 𝐦𝐞𝐦𝐮𝐭𝐚𝐫 𝐦𝐮𝐬𝐢𝐤 𝐝𝐢 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐯𝐢𝐝𝐞𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.\n\n𝐓𝐚𝐩𝐢 𝐡𝐚𝐧𝐲𝐚 𝐮𝐧𝐭𝐮𝐤 𝐠𝐫𝐨𝐮𝐩 𝐭𝐞𝐫𝐭𝐞𝐧𝐭𝐮 𝐬𝐚𝐣𝐚.",
            parse_mode="markdown",
            reply_markup=pstart_markup,
            reply_to_message_id=message.message_id,
        )
    elif len(message.command) == 2:
        query = message.text.split(None, 1)[1]
        f1 = query[0]
        f2 = query[1]
        f3 = query[2]
        finxx = f"{f1}{f2}{f3}"
        if str(finxx) == "inf":
            query = (str(query)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                x = ytdl.extract_info(query, download=False)
            thumbnail = x["thumbnail"]
            searched_text = f"""
🔍__**Video Track Information**__

❇️**Title:** {x["title"]}
   
⏳**Duration:** {round(x["duration"] / 60)} Mins
👀**Views:** {x["view_count"]}
👍**Likes:** {x["like_count"]}
⭐️**Average Ratings:** {x["average_rating"]}
🎥**Channel Name:** {x["uploader"]}
📎**Channel Link:** [Visit From Here]({x["channel_url"]})
🔗**Link:** [Link]({x["webpage_url"]})

⚡️ Searched Powered By MUSIKKU"""
            link = x["webpage_url"]
