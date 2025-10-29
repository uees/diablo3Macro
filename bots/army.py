import asyncio

from pynput import keyboard

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """主动三光"""

    def __init__(self, cdr):
        super().__init__()
        self.keyboard = keyboard.Controller()
        self.cdr = cdr

    async def task_press_2(self):
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.11)
            self.keyboard.press('2')
            self.keyboard.release('2')

        BOT_SWITCH.wait()
        await self.task_press_2()

    async def task_press_4(self):
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.12)
            self.keyboard.press('4')
            self.keyboard.release('4')

        BOT_SWITCH.wait()
        await self.task_press_4()
