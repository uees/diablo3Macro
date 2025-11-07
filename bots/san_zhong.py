from core import BaseAsyncBot


class PressKey(BaseAsyncBot):

    async def task_press_4(self):
        """黑人"""
        await self.loop_press('4', 1)

    async def task_press_2(self):
        """回精气"""
        await self.loop_press('2', 1.1)
