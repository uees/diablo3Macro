from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """主动三光"""

    async def task_press_2(self):
        await self.loop_press('2', 0.11)

    async def task_press_4(self):
        await self.loop_press('4', 0.12)
