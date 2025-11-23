from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """武僧悟空套维持劲风煞效果"""

    async def task_press_3(self):
        """3键绑定劲凤煞"""
        await self.loop_press_with_cd('3', 6)

    async def task_press_2(self):
        """2键绑定幻身回内力"""
        await self.loop_press_with_cd('2', 5)
