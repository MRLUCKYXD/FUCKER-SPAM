import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import anon, anon2, anon3, anon4, anon5, anon6, anon7, anon8, anon9, anon10, ALIVE_PIC, OWNER_ID
from SpamRobo.plugins.help import *


ANON_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/7bd111132fce009e4605e.jpg"

Anon_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/terayaarhoomai")
        ],
        [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
        ]
        ]
               
AnonX_Button = [
        [
        Button.url("• ғᴜᴄᴋᴇʀ •", "https://t.me/cute_boy701"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/terayaarhoomai")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://telegra.ph/file/b2a4f66615d038f77bb46.mp4")
        ]
        ]
        
        
#USERS 


@anon.on(events.NewMessage(pattern="/start"))
@anon2.on(events.NewMessage(pattern="/start"))
@anon3.on(events.NewMessage(pattern="/start"))
@anon4.on(events.NewMessage(pattern="/start"))
@anon5.on(events.NewMessage(pattern="/start"))
@anon6.on(events.NewMessage(pattern="/start"))
@anon7.on(events.NewMessage(pattern="/start"))
@anon7.on(events.NewMessage(pattern="/start"))
@anon8.on(events.NewMessage(pattern="/start"))
@anon9.on(events.NewMessage(pattern="/start"))
@anon10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       AnonBot = await event.client.get_me()
       bot_id = AnonBot.first_name
       bot_username = AnonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAnon = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**ʜᴇʏ ʙᴀʙʏ,\n      ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴀɴᴏɴʏᴍᴏᴜs ʏᴏᴜ ᴀʀᴇ ᴍʏ ᴏᴡɴᴇʀ sᴏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ᴄʜᴀᴛs ᴛᴏ sᴩᴀᴍ, ʀᴀɪᴅ, ʜᴀɴɢ ᴀɴᴅ ᴅᴏɪɴɢ ᴍᴀɴʏ ᴍᴏʀᴇ ᴅɪsᴛᴜʀʙɪɴɢ ᴛʜɪɴɢs.** \n\n©️ @terayaarhoomai"
       usermsg = f"**ʜᴇʏ {firstname},\n\nʟᴇᴛ ᴍᴇ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ ʙᴀʙʏ.\n\nɪ ᴀᴍ {bot_id} ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ-ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ ʙʏ sᴏᴍᴇᴏɴᴇ.\nɪ ᴀᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇsᴛʀᴏʏ ᴍʏ ᴏᴡɴᴇʀ's ᴇɴᴇᴍʏ,\nɪ ᴡɪʟʟ ғᴜ*ᴋ ʏᴏᴜ ᴜᴘ ɪғ ʏᴏᴜ ᴇᴠᴇʀ ᴛʀɪᴇᴅ ᴛᴏ ᴍᴇss ᴡɪᴛʜ ᴍʏ ᴏᴡɴᴇʀ !** \n\n█▓▒­░⡷⠂𝗙𝗨𝗖𝗞𝝣𝗥⠂⢾░▒▓█\n[『 𝐋𝐔𝐂𝐊𝐘 』](tg://user?id=1729094176) \n\n\n©️ @terayaarhoomai"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheAnon,
                  ANON_IMG,
                  caption=ownermsg, 
                  buttons=Anon_Button)
       else:
            await event.client.send_file(TheAnon,
                  ANON_IMG,
                  caption=usermsg, 
                  buttons=AnonX_Button)
                

