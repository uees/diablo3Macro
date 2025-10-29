import asyncio
from pynput import keyboard

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):

    def __init__(self, cdr):
        super().__init__()
        self.keyboard = keyboard.Controller()
        self.cdr = cdr

    async def task_press_4(self):
        """黑人"""
        while BOT_SWITCH.is_set():
            self.keyboard.press('4')
            self.keyboard.release('4')
            await asyncio.sleep(1)

        BOT_SWITCH.wait()
        await self.task_press_4()

    async def task_press_2(self):
        """回精气"""
        while BOT_SWITCH.is_set():
            self.keyboard.press('2')
            self.keyboard.release('2')
            await asyncio.sleep(1.1)

        BOT_SWITCH.wait()
        await self.task_press_2()
