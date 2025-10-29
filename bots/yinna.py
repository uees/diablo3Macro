import asyncio

import keyboard

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """武僧尹娜套维持飓风转5秒效果"""

    def __init__(self, cdr):
        super().__init__()
        self.cdr = cdr

    async def task_press_3(self):
        """释放飓风转5秒内获得增益效果"""
        while BOT_SWITCH.is_set():
            keyboard.press_and_release('3')
            await asyncio.sleep(4.9)

        BOT_SWITCH.wait()
        await self.task_press_3()
