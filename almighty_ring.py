import asyncio

from playsound import playsound
from core import BaseAsyncBot, RING_SWITCH
from settings import BASE_DIR


class AlmightyRing(BaseAsyncBot):
    """
    全能法戒 4s x 4 = 16s

    用声音提示什么时候有法戒加成
    """

    async def task_ring_sound(self):
        duration = 3.5
        cycle = 16
        while RING_SWITCH.is_set():
            await asyncio.to_thread(playsound, f"{BASE_DIR}/resources/ring_start.mp3")
            await asyncio.sleep(duration)
            await asyncio.to_thread(playsound, f"{BASE_DIR}/resources/ring_end.mp3")
            await asyncio.sleep(cycle - duration)

        RING_SWITCH.wait()
        await self.task_ring_sound()
