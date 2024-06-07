import math
import asyncio
from pyrogram import Client

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#from pyrogram import InlineKeyboardButton, 
from pyrogram.types import CallbackQuery
from AnonXMusic.utils.formatters import time_to_seconds
app = Client("my_bot")

def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "◉—————————"
    elif 10 < umm < 20:
        bar = "—◉————————"
    elif 20 <= umm < 30:
        bar = "——◉———————"
    elif 30 <= umm < 40:
        bar = "———◉——————"
    elif 40 <= umm < 50:
        bar = "————◉—————"
    elif 50 <= umm < 60:
        bar = "—————◉————"
    elif 60 <= umm < 70:
        bar = "——————◉———"
    elif 70 <= umm < 80:
        bar = "———————◉——"
    elif 80 <= umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"
    buttons = [
        [
            InlineKeyboardButton(text="Skip Song", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="Stop Stream", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="Pause Music", callback_data=f"ADMIN Pause|{chat_id}"),
            InlinekeyboardButton(text="Resume Music", callback_data=f"ADMIN Resume|{chat_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="audio",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="video",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons



def stream_markup(chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="🎛️ Control", callback_data="CTRL"),
            InlineKeyboardButton(text="Close ❌", callback_data="close"),
        ]
    ]
    return InlineKeyboardMarkup(buttons)

@app.on_callback_query(filters.regex("CTRL"))
async def handle_control_callback(client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    buttons = [
        [
            InlineKeyboardButton(text="Skip", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="Stop", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="Pause", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="Resume", callback_data=f"ADMIN Resume|{chat_id}"),
        ],
        [InlineKeyboardButton(text="Close ❌", callback_data="close")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_reply_markup(reply_markup=reply_markup)
    
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="audio",
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="video",
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text="audio",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="video",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔙",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⏭️",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

