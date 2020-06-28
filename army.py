import asyncio
from pynput.keyboard import Controller

from core import BaseAsyncBot


keyboard = Controller()


class ZhuDongSanGuang(BaseAsyncBot):
    """主动三光"""

    async def task_press_2(self):
        while self.is_run:
            await asyncio.sleep(0.11)
            keyboard.press('2')
            await asyncio.sleep(0.172)
            keyboard.release('2')

    async def task_press_4(self):
        while self.is_run:
            await asyncio.sleep(0.12)
            keyboard.press('4')
            await asyncio.sleep(0.212)
            keyboard.release('4')
