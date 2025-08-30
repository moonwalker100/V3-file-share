#(©) PythonBotz 

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b><blockquote>╭───────────⍟
├➤ ᴏᴡɴᴇʀ : <a href='https://t.me/Black_walker_id'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
├➤ ʟɪʙʀᴀʀy : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
├➤ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a>
├➤ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/PythonBotz>ᴏᴜᴛʟᴀᴡ ʙᴏᴛs</a>
├➤ ᴘᴀɪᴅ ʙᴏᴛ : <a href=https://t.me/seiao>ᯓ ɪɴᴠᴀʟɪᴅ ᡣ𐭩</a>
├➤ ᴅᴇᴠʟᴏᴘᴇʀ : <a href=https://t.me/metaui>ᯓ ʜᴀᴛᴇ ғʀᴇᴇ ᡣ𐭩</a>
╰───────────────⍟</blockquote></b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data ="source"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , callback_data = "main")],
                 [InlineKeyboardButton("ᴡᴀᴛᴄʜ sʜᴏʀᴛs 𝟷𝟾+ ᴠɪᴅᴇᴏs", url = "https://t.me/UnseenRobot/shorts")],
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
