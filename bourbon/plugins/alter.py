import sys
sys.path.append('../..')
from tools import song_find, alter_add

from nonebot import on_command, CommandSession

@on_command('add')
async def add(session: CommandSession):
    user_id = session.ctx['user_id']
    text = session.current_arg_text.strip()
    if text.find('|||') == -1:
        await session.send('请正确输入命令，用法: /add 旧名字|||新别名')
    else:
        old, new = text.split('|||', 1)
        await session.send(alter_add(new, old, user_id))

@on_command('search')
async def search(session: CommandSession):
    text = session.current_arg_text.strip()
    song_info = song_find(text)
    if song_info == False:
        await session.send('歌曲未找到，请检查关键字或使用/add 添加别名')
    else:
        await session.send('你要找的是不是：' + song_info)