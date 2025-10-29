import asyncio

import keyboard

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """武僧悟空套维持劲风煞效果"""

    def __init__(self, cdr):
        super().__init__()
        self.cdr = cdr

    async def task_press_3(self):
        """3键绑定劲凤煞"""
        while BOT_SWITCH.is_set():
            # logger.info("press key 3")
            keyboard.press_and_release('3')
            await asyncio.sleep(5.75)

        BOT_SWITCH.wait()
        await self.task_press_3()

    async def task_press_2(self):
        """2键绑定幻身回内力"""
        while BOT_SWITCH.is_set():
            # logger.info("press key 2")
            keyboard.press_and_release('2')
            await asyncio.sleep(5)

        BOT_SWITCH.wait()
        await self.task_press_2()
