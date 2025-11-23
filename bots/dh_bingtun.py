from pynput import mouse

from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """恐惧冰吞 python main.py -b dh_bingtun -c 30
    1: 烟幕弹 - 飘忽不定
    2: 战宠 - 恶狼战宠
    3: 蓄势待发 - 集中心智
    4: 复仇 - 黑暗之心
    left: 追踪箭 - 吞噬箭
    right: 扫射 - 飞弹风暴

    被动: 战术优势、追猎快感、伏击、恃强凌弱
    """

    # async def task_press_1(self):
    #    pass

    async def task_press_2(self):
        """战宠"""
        await self.loop_press_with_cd('2', 30)

    async def task_press_3(self):
        """ 蓄势待发 - 集中心智"""
        await self.loop_press_with_cd('3', 45)

    async def task_press_4(self):
        """ 复仇 - 黑暗之心 0.2s 按一次 维持buff"""
        await self.loop_press('4', 0.5)

    async def task_press_left(self):
        """ 追踪箭 - 吞噬箭 4s 按一次 维持buff，使用shift+左键组合"""
        await self.loop_mouse_press(mouse.Button.left, 4)

    # async def task_press_right(self):
    #    pass
