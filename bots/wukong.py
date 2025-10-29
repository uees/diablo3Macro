import asyncio

from pynput import keyboard

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """武僧悟空套维持劲风煞效果"""

    def __init__(self, cdr):
        super().__init__()
        self.keyboard = keyboard.Controller()
        self.cdr = cdr

    async def task_press_3(self):
        """3键绑定劲凤煞"""
        while BOT_SWITCH.is_set():
            # logger.info("press key 3")
            self.keyboard.press('3')
            self.keyboard.release('3')
            await asyncio.sleep(5.75)

        BOT_SWITCH.wait()
        await self.task_press_3()

    async def task_press_2(self):
        """2键绑定幻身回内力"""
        while BOT_SWITCH.is_set():
            self.keyboard.press('2')
            self.keyboard.release('2')
            await asyncio.sleep(5)

        BOT_SWITCH.wait()
        await self.task_press_2()
