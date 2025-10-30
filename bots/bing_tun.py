import asyncio

from pynput import keyboard, mouse

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """恐惧冰吞
    1: 烟幕弹 - 飘忽不定
    2: 战宠 - 恶狼战宠
    3: 蓄势待发 - 集中心智
    4: 复仇 - 黑暗之心
    left: 追踪箭 - 吞噬箭
    right: 扫射 - 飞弹风暴

    被动: 战术优势、追猎快感、伏击、恃强凌弱
    """

    def __init__(self, cdr):
        super().__init__()
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        self.cdr = cdr

    # async def task_press_1(self):
    #    pass

    async def task_press_2(self):
        """战宠"""
        cd = 30 * (100 - self.cdr) / 100  # cd 45s
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.1)
            self.keyboard.press('2')
            self.keyboard.release('2')
            await asyncio.sleep(cd - 0.1)

        BOT_SWITCH.wait()
        await self.task_press_2()

    async def task_press_3(self):
        """ 蓄势待发 - 集中心智"""
        cd = 45 * (100 - self.cdr) / 100  # cd 45s
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.1)
            self.keyboard.press('3')
            self.keyboard.release('3')
            await asyncio.sleep(cd - 0.1)

        BOT_SWITCH.wait()
        await self.task_press_3()

    async def task_press_4(self):
        """ 复仇 - 黑暗之心 0.2s 按一次 维持buff"""
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.2)
            self.keyboard.press('4')
            self.keyboard.release('4')

        BOT_SWITCH.wait()
        await self.task_press_4()

    async def task_press_left(self):
        """ 追踪箭 - 吞噬箭 4s 按一次 维持buff，使用shift+左键组合"""
        while BOT_SWITCH.is_set():
            # 按下shift键 + 左键
            with self.keyboard.pressed(keyboard.Key.shift):
                self.mouse.press(mouse.Button.left)
                self.mouse.release(mouse.Button.left)

            # 每4秒执行一次
            await asyncio.sleep(4)

        BOT_SWITCH.wait()
        await self.task_press_left()

    # async def task_press_right(self):
    #    pass
