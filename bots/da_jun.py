import asyncio

from pynput import keyboard, mouse

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """王者大军
    4: 号令骸骨 - 死寒之握

    被动:
    """

    def __init__(self, cdr):
        super().__init__()
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        self.cdr = cdr

    async def task_press_4(self):
        """ 号令骸骨 - 死寒之握 """
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.2)
            self.keyboard.press('4')
            self.keyboard.release('4')

        BOT_SWITCH.wait()
        await self.task_press_4()
