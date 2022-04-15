from os import path

import nonebot

if __name__ == '__main__':
    nonebot.init()
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'bourbon', 'plugins'),
        'bourbon.plugins'
    )
    nonebot.run(host='127.0.0.1', port=8080)