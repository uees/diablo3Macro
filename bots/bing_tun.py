import asyncio

import keyboard

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
        self.cdr = cdr

    # async def task_press_1(self):
    #    pass

    # async def task_press_2(self):
    #    pass

    async def task_press_3(self):
        """ 蓄势待发 - 集中心智"""
        cd = 45 * (100 - self.cdr) / 100  # cd 45s
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.1)
            keyboard.press_and_release('3')
            await asyncio.sleep(cd - 0.1)

        BOT_SWITCH.wait()
        await self.task_press_3()

    async def task_press_4(self):
        """ 复仇 - 黑暗之心 0.2s 按一次 维持buff"""
        while BOT_SWITCH.is_set():
            await asyncio.sleep(0.2)
            keyboard.press_and_release('4')

        BOT_SWITCH.wait()
        await self.task_press_4()

    async def task_press_left(self):
        """ 追踪箭 - 吞噬箭 4s 按一次 维持buff，使用shift+左键组合"""
        while BOT_SWITCH.is_set():
            try:
                # 按下shift键
                keyboard.press('shift')
                # 短暂延迟确保按键被正确识别
                await asyncio.sleep(0.05)
                # 按下左键
                keyboard.press('left')
                # 短暂延迟
                await asyncio.sleep(0.05)
                # 先释放左键
                keyboard.release('left')
                # 再释放shift键
                keyboard.release('shift')
            except Exception as e:
                print(f"Error in task_press_left: {e}")
            # 每4秒执行一次
            await asyncio.sleep(4)

        BOT_SWITCH.wait()
        await self.task_press_left()

    # async def task_press_right(self):
    #    pass
