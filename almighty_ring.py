from collections.abc import Callable
from typing import Iterable, Mapping
import pygame
import asyncio

from core import BaseAsyncBot, RING_SWITCH
from settings import BASE_DIR

# 初始化pygame mixer
pygame.mixer.init()


class AlmightyRing(BaseAsyncBot):
    """
    全能法戒 4s x 4 = 16s

    用声音提示什么时候有法戒加成
    """

    def __init__(self, ring12: bool) -> None:
        super().__init__()
        self.ring12 = ring12

    async def task_ring_sound(self):
        duration = 3.5
        cycle = 12 if self.ring12 else 16
        while RING_SWITCH.is_set():
            # 使用pygame播放声音
            sound = pygame.mixer.Sound(f"{BASE_DIR}/resources/ring_start.mp3")
            sound.play()
            await asyncio.sleep(duration)

            sound = pygame.mixer.Sound(f"{BASE_DIR}/resources/ring_end.mp3")
            sound.play()
            await asyncio.sleep(cycle - duration)

        RING_SWITCH.wait()
        await self.task_ring_sound()
