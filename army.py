import asyncio

from core import BaseAsyncBot


class ZhuDongSanGuang(BaseAsyncBot):
    """主动三光"""

    async def task_press_1(self):
        while self.is_run:
            await asyncio.sleep(0.1)
            print("按下了1")
            await asyncio.sleep(0.112)
            print("提起了1")
            await asyncio.sleep(0.3)

    async def task_press_2(self):
        while self.is_run:
            await asyncio.sleep(0.2)
            print("按下了2")
            await asyncio.sleep(0.112)
            print("提起了2")
            await asyncio.sleep(0.7)
