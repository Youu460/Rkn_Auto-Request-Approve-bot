# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To (https://github.com/JayMahakal98)
# Update Channel @Digital_Botz & @DigitalBotz_Support

"""
Apache License 2.0
Copyright (c) 2022 @RknDeveloper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/RknDeveloper
Repo Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot
License Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot/blob/main/LICENSE
"""

# pyrogram imports
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant, PeerIdInvalid, UserIsBlocked

# bots imports
from RknDeveloper.database import rkn_botz
from RknDeveloper.fs import force_sub
from configs import rkn1
import random, asyncio, os


# Main Process _ _ _ _ _ Users Send Massage 🥀__🥀 Please 😢 Give Credit

@Client.on_chat_join_request()#filters.group | filters.channel & filters.private)
async def approve_request(bot, m):
    try:
        await rkn_botz.add_chat(bot, m)
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
        img = random.choice(rkn1.SURPRICE)
        await bot.send_video(m.from_user.id, img, "**Hey, {}!\nWelcome To {}\n\n__Pᴏᴡᴇʀᴅ Bʏ : @RknDeveloper__**".format(m.from_user.mention, m.chat.title), reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("📍𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
        ],[
        InlineKeyboardButton("📍𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")]]))
        await rkn_botz.add_user(bot, m)
    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid as err:
        print(f"user isn't start bot (means group) Error- {err}")
    except Exception as err:
        print(f"Error\n{str(err)}")
        
   
# Start Massage _____ # Please 😢 Give Credit 

@Client.on_message(filters.command("start"))
async def start_commond(bot, m :Message):
    if m.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await rkn_botz.add_chat(bot, m)
        return await m.reply_text("**❣️ Hᴇʟʟᴏ {}!\n\nWʀɪᴛᴇ Mᴇ Pʀɪᴠᴀᴛᴇ Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs.**".format(m.from_user.first_name), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pʀɪᴠᴀᴛᴇ", url=f"https://t.me/{bot.username}?start=start")
                    ]
                ]
            ))
            
    await rkn_botz.add_user(bot, m)
    await force_sub(bot, m, rkn1.FORCE_SUB)
    await m.reply_photo(photo=rkn1.RKN_PIC, caption="**Hᴇy, {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @Leomc_bot__**".format(m.from_user.mention, "https://i.ibb.co/jPHBQMmv/x.jpg"), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("🪝 𝘼𝘽𝙊𝙐𝙏", callback_data = "about")
                    ],[
                InlineKeyboardButton("📺 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/+3f1-fix2NrVmNTc0"),
                InlineKeyboardButton("⚓️ 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝙂𝙍𝙊𝙐𝙋⚓️", url="https://t.me/+3f1-fix2NrVmNTc0")
                ],[
                InlineKeyboardButton("📍𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("📍𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]]))
            
 
@Client.on_callback_query(filters.regex("start"))
async def start_query(bot, cb : CallbackQuery):
    await cb.message.edit("**Hᴇy, {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @Leomc_bot__**".format(cb.from_user.mention, "https://i.ibb.co/jPHBQMmv/x.jpg"), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("🪝 𝘼𝘽𝙊𝙐𝙏", callback_data = "about")
                    ],[
                InlineKeyboardButton("📺 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/+3f1-fix2NrVmNTc0"),
                InlineKeyboardButton("⚓️ 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝙂𝙍𝙊𝙐𝙋⚓️", url="https://t.me/+3f1-fix2NrVmNTc0")
                ],[
                InlineKeyboardButton("📍𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("📍𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]]), disable_web_page_preview=True)
    
#🔥 Please Don't Remove Credit 💳 # ❣️ 
@Client.on_callback_query(filters.regex('about'))
async def about_query(bot, update):
	await update.message.edit_text(
	    #⚠️ don't change source code & source link ⚠️ #
	    text = """<b>» Mʏ Nᴀᴍᴇ: <a href='https://t.me/Rkn_AutoRequestApprovebot'>Aᴜᴛᴏ Jᴏɪɴ Rᴇǫᴜᴇsᴛ Bᴏᴛ</a>
‣ Cʀᴇᴀᴛᴏʀ : <a href='tg://settings'>ᴛʜɪs Pᴇʀsᴏɴ</a>
‣ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Leomc_bot'>🖥️Dᴇᴠᴇʟᴏᴘᴇʀ</a>
‣ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org'>Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3</a>
‣ Dᴀᴛᴀ Bᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
‣ Bᴏᴛ Sᴇʀᴠᴇʀ : ‣[Vᴘs]‣<a href='https://app.koyeb.com/'>[Kᴏʏᴇʙ]</a>
‣ Sᴏᴜʀᴄᴇ : <a href='https://t.me/Leomc_bot'> PRIVATE 🔒</a>
‣ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ2.1.1 [sᴛᴀʙʟᴇ]</b>""",
	    reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ ❣️", url="https://t.me/Leomc_bot")],[
               InlineKeyboardButton("→ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
    )
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
