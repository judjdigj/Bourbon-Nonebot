from webbrowser import get
import nonebot
from nonebot.message import MessageSegment
import sys
sys.path.append('../..')
from tools import song_find, alter_add

from nonebot import on_command, CommandSession

@on_command('add')
async def add(session: CommandSession):
    user_id = session.ctx['user_id']

    alter_add()
    await session.send('Hello' + str(user_id))