from pynput import mouse

from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """ 辅助猎魔人 python main.py -b dh_fz -c 30
    1. 烟幕弹 - 飘忽不定
    2. 战宠 - 恶狼战宠
    3. 多重射击 - 狂风冻结
    4. 死亡印记 - 死亡之谷
    left. 缠绕射击 - 连锁禁锢
    right. 扫射 - 暗影游移
    """

    async def task_press_2(self):
        """战宠"""
        await self.loop_press_with_cd('2', 30)

    async def task_press_left(self):
        """ 缠绕射击 - 连锁禁锢 4s 按一次 维持buff，使用shift+左键组合"""
        await self.loop_mouse_press(mouse.Button.left, 4)
