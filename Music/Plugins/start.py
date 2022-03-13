import asyncio
from time import time
from datetime import datetime
from Music import BOT_USERNAME
from Music.config import ZAID_SUPPORT
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ad2aa6ee030e378adafe6.jpg",
        caption=f"""**Mongodb Berbasis Bot Musik Telegram.
  Tambahkan Saya Ke Obrolan Anda Untuk dan Bantuan dan Dukungan Klik Tombol ...
 💓 Fitur-Fitur Ini Berbasis A.I
 Dipersembahkan oleh [Oukeen?](t.me/bukanyesus) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", url=f"https://t.me/OukeenUpdates/6"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/bukanyesus"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🇲🇨", url=f"https://t.me/{ZAID_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ad2aa6ee030e378adafe6.jpg",
        caption=f"""Terima Kasih Telah Menambahkan Saya Ke Obrolan Anda, Untuk Setiap Pertanyaan Anda Dapat Bergabung dengan Grup Dukungan Kami 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ 💞", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ad2aa6ee030e378adafe6.jpg",
        caption=f"""Cie Nyari Reponya Hahaha ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Pencet Ini ⚒️", url=f"https://t.me/bukanyesus")
                ]
            ]
        ),
    )
