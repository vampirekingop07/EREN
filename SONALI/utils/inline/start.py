from pyrogram.types import InlineKeyboardButton

import config
from SONALI import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                "🕸ᴛᴀᴘ ᴛᴏ sᴇᴇ ᴍᴀɢɪᴄ🕸",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton("♡︎ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs ♡︎", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton("🌷ᴄʜᴀɴɴᴇʟ🌷", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton("❄️sᴜᴘᴘᴏʀᴛ❄️", url=config.SUPPORT_CHANNEL),
        ],
        [InlineKeyboardButton("🥀ᴏᴡɴᴇʀ🥀", user_id=config.OWNER_ID)],
    ]
    return buttons
