from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """武僧尹娜套维持飓风转5秒效果"""

    async def task_press_3(self):
        """释放飓风转5秒内获得增益效果"""
        await self.loop_press('3', 4.9)
