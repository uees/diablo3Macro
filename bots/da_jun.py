from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """王者大军
    4: 号令骸骨 - 死寒之握

    被动:
    """

    async def task_press_4(self):
        """ 号令骸骨 - 死寒之握 """
        await self.loop_press('4', 0.2)
