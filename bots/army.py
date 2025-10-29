import asyncio

import keyboard

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """主动三光"""

    def __init__(self, cdr):
        super().__init__()
        self.cdr = cdr

    async def task_press_2(self):
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.11)
            keyboard.press_and_release('2')

        BOT_SWITCH.wait()
        await self.task_press_2()

    async def task_press_4(self):
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.12)
            keyboard.press_and_release('4')

        BOT_SWITCH.wait()
        await self.task_press_4()
