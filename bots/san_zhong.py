import asyncio
import keyboard

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):

    def __init__(self, cdr):
        super().__init__()
        self.cdr = cdr

    async def task_press_4(self):
        """黑人"""
        while BOT_SWITCH.is_set():
            keyboard.press_and_release('4')
            await asyncio.sleep(1)

        BOT_SWITCH.wait()
        await self.task_press_4()

    async def task_press_2(self):
        """回精气"""
        while BOT_SWITCH.is_set():
            keyboard.press_and_release('2')
            await asyncio.sleep(1.1)

        BOT_SWITCH.wait()
        await self.task_press_2()
