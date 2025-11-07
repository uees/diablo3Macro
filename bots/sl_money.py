from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """万箭归宗
    3: 吞噬 - 吞血食肉
    4: 号令骸骨 - 死寒之握

    被动:
    """

    async def task_press_3(self):
        """ 吞噬 - 吞血食肉 """
        await self.loop_press('3', 0.3)

    async def task_press_4(self):
        """ 号令骸骨 - 死寒之握 """
        await self.loop_press('4', 0.3)
