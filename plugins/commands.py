# imports
import os
import logging
import random
from pyrogram import Client, filters
from script import Script
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from utils import Media, get_file_details
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

# -- constants ---
STICKERS = (
    "CAACAgIAAxkBAAFIRn5hKSOKb3njAAHvRKwD80OkF0tLkAwAAl4AA6_GURqPIlssOJ_8NyAE",
    "CAACAgIAAxkBAAFIRn9hKSOKjcr8VLQefLOf_6LWBuoJJAACXQADr8ZRGjk1L1YLigsVIAQ",
    "CAACAgIAAxkBAAFIRoBhKSOLC1KHf3oOEku7lsvC7CHmDgACYQADr8ZRGq70R9934jY7IAQ",
    "CAACAgIAAxkBAAFIRoFhKSOMj1_kTx-dKVIbeIN9XnX2kwACXwADr8ZRGpFB8WXiSOloIAQ",
    "CAACAgIAAxkBAAFIRoJhKSOM9N-nx8sj6RIPPfYPv39CiQACZQADr8ZRGn2-GO6trucHIAQ",
    "CAACAgIAAxkBAAFIRoNhKSOOUmKqdcRpti9sQqsqZ_7e3gACVwADr8ZRGi4O74AW-2UxIAQ",
    "CAACAgIAAxkBAAFIRoRhKSOOAvbAsgzONssG-uZUS0H7kgACZgADr8ZRGsQ2jQXZMcpzIAQ",
    "CAACAgIAAxkBAAFIRoVhKSOPxxkK26MUfzJfNy0RxjkYWwACWAADr8ZRGs5s1MJUTM72IAQ",
    "CAACAgIAAxkBAAFIRoZhKSOQUWvFdj2ie2hkxEcF-AhnIQACWQADr8ZRGozJIAQs0RWxIAQ",
    "CAACAgIAAxkBAAFIRohhKSORLwOMcUbBLtyuTDdyfKmhawACYgADr8ZRGrF6sYqYtZ2WIAQ",
    "CAACAgIAAxkBAAFIRolhKSOTDIDxelzoh5GLisXC0gGUNAACYAADr8ZRGjufkDKyxauoIAQ",
    "CAACAgIAAxkBAAFIRolhKSOTDIDxelzoh5GLisXC0gGUNAACYAADr8ZRGjufkDKyxauoIAQ",
    "CAACAgIAAxkBAAFIRophKSOTSxsTMeewMnpoRhekvZR7kQACWgADr8ZRGnfyVwkiVE6CIAQ",
    "CAACAgIAAxkBAAFIRothKSOUfHH2pZvv_Zmd2Cx-J97WuAACWwADr8ZRGkv_pdGBt_pPIAQ",
    "CAACAgIAAxkBAAFIRo1hKSOUHQqCLbRHlDCJKTcjM5QznwACXAADr8ZRGhmnzvSkaMQkIAQ",
    "CAACAgIAAxkBAAFIRo5hKSOVoyBJod1cmVXLLz4pnPL1BwACZAADr8ZRGt1OQaIPwAkhIAQ",
    "CAACAgIAAxkBAAFIRo9hKSOWwVjiVgk2746eGEH6q7NKnwACZwADr8ZRGsmQice9AYoCIAQ",
    "CAACAgIAAxkBAAFIRpBhKSOXr7nCXRJxPeh7sQ0woV3hBwACaAADr8ZRGmKWjxfFaPfQIAQ",
    "CAACAgIAAxkBAAFIRpFhKSOX1nStU7pmPuxJ0ByNIJqw7QACaQADr8ZRGrZyHv618OjQIAQ",
    "CAACAgIAAxkBAAFIRpJhKSOYyrFNC4Lu_3ie6_3IJbabDwACagADr8ZRGuiCGKEfyBPBIAQ",
    "CAACAgIAAxkBAAFIRpNhKSOZtkij_JQWcQfdDm0fTVugjQACawADr8ZRGhWONteHdHrbIAQ",
    "CAACAgIAAxkBAAFIRpRhKSOavdKOIP3ZdKtEcEvKbbYX6QACbAADr8ZRGrWxwiCZlayYIAQ",
    "CAACAgIAAxkBAAFIRpVhKSOazYfqMvpG0npDDgNDkVSm8QACbQADr8ZRGu2loo9F1U5qIAQ",
    "CAACAgIAAxkBAAFIRpZhKSObHxK_ginJvhYLNhs9INuoNgACbgADr8ZRGjNF2IaG56c3IAQ",
    "CAACAgIAAxkBAAFIRpdhKSObORUdt6e6dTCBXBDx-YpbEgACbwADr8ZRGjGYrB7l2M5CIAQ",
    "CAACAgIAAxkBAAFIRphhKSOcd9uXrAiWjQABy1wp3gHWXZUAAnAAA6_GURr1rq3xgoZ54CAE"
)

@Client.on_message(filters.command("start"))
async def start(bot, cmd):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start albin_binu"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="**Please Join My Updates Channel to use this Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton(" 🔄 Try Again", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        try:
            ident, file_id = cmd.text.split("_-_-_-_")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [
                    [
                        InlineKeyboardButton('Search again', switch_inline_query_current_chat=''),
                        InlineKeyboardButton('More Bots', url='https://t.me/subin_works/122')
                    ]
                    ]
                await bot.send_cached_media(
                    chat_id=cmd.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
    elif len(cmd.command) > 1 and cmd.command[1] == 'subscribe':
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        await bot.send_photo(
            chat_id=cmd.from_user.id,
            photo="https://telegra.ph/file/b05760409061092dc139b.jpg",
            caption="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                    ]
                ]
            )
        )
    else:
        await cmd.reply_sticker(random.choice(STICKERS))
             reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❔How to use me❓", callback_data="howto")
                    ],
                    [
                        InlineKeyboardButton("🔍Serach here🔎", switch_inline_query_current_chat=''),
                        InlineKeyboardButton("💁Help", callback_data="helpz")
                    ],
                    [
                        InlineKeyboardButton("👻My dev", url="https://t.me/albin_binu"),
                        InlineKeyboardButton("🎯About", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("♻️Add me in your Chat", url="https://t.me/albin_binu")
                    ]
                ]
            )
        )
            
@Client.on_message(filters.command('help') & filters.private)
async def help(bot, cmd):
    await cmd.reply_photo(
            photo="https://telegra.ph/file/b05760409061092dc139b.jpg",
            caption=Script.HELP_MSG,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url="t.me/albin_binu")
                    ]
                ]
            )
        )
        
@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
@Client.on_message(filters.command('about'))
async def bot_info(bot, message):
    buttons = [
        [
            InlineKeyboardButton('Update Channel', url='https://t.me/subin_works'),
            InlineKeyboardButton('Source Code', url='https://github.com/subinps/Media-Search-bot')
        ]
        ]
    await message.reply(text="<b>Developer : <a href='https://t.me/subinps_bot'>SUBIN</a>\nLanguage : <code>Python3</code>\nLibrary : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\nSource Code : <a href='https://github.com/subinps/Media-Search-bot'>Click here</a>\nUpdate Channel : <a href='https://t.me/subin_works'>XTZ Bots</a> </b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
