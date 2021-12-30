import asyncio
import keyboard

from core import BaseAsyncBot, BOT_SWITCH
from logger import logger


class PressKey(BaseAsyncBot):

    async def task_press_3(self):
        """持续劲凤煞"""
        while BOT_SWITCH.is_set():
            logger.info("press key 3")
            keyboard.press_and_release('3')
            await asyncio.sleep(5.78)

        BOT_SWITCH.wait()
        await self.task_press_3()

    async def task_press_2(self):
        while BOT_SWITCH.is_set():
            logger.info("press key 2")
            keyboard.press_and_release('2')
            await asyncio.sleep(5)

        BOT_SWITCH.wait()
        await self.task_press_2()
