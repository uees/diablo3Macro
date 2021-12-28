import asyncio
import keyboard

from core import BaseAsyncBot, BOT_SWITCH
from logger import logger


class PressKey(BaseAsyncBot):

    async def task_press_3(self):
        """持续劲凤煞"""
        while BOT_SWITCH.is_set():
            await asyncio.sleep(5.9)
            keyboard.press_and_release('3')
            logger.info("press key 3")

        BOT_SWITCH.wait()  # 调用该方法的线程会被阻塞
        await self.task_press_3()
