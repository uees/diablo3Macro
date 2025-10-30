import asyncio

from pynput import keyboard, mouse

from core import BaseAsyncBot, BOT_SWITCH


class PressKey(BaseAsyncBot):
    """ 辅助猎魔人
    1. 烟幕弹 - 飘忽不定
    2. 战宠 - 恶狼战宠
    3. 多重射击 - 狂风冻结
    4. 死亡印记 - 死亡之谷
    left. 缠绕射击 - 连锁禁锢
    right. 扫射 - 暗影游移
    """

    def __init__(self, cdr: float) -> None:
        super().__init__()
        self.cdr = cdr
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()

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

    async def task_press_left(self):
        """ 缠绕射击 - 连锁禁锢 4s 按一次 维持buff，使用shift+左键组合"""
        while BOT_SWITCH.is_set():
            # 按下shift键 + 左键
            self.keyboard.press(keyboard.Key.shift)
            # 短暂延迟确保按键被正确识别
            await asyncio.sleep(0.05)
            # 按下左键
            self.mouse.press(mouse.Button.left)
            # 短暂延迟
            await asyncio.sleep(0.05)
            # 先释放左键
            self.mouse.release(mouse.Button.left)
            # 再释放shift键
            self.keyboard.release(keyboard.Key.shift)
            # 每4秒执行一次
            await asyncio.sleep(4)

        BOT_SWITCH.wait()
        await self.task_press_left()
