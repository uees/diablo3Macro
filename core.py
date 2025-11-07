import asyncio
import threading

from pynput import keyboard, mouse

BOT_SWITCH = threading.Event()
RING_SWITCH = threading.Event()


class BaseAsyncBot(threading.Thread):

    def __init__(self):
        super().__init__()
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        self.cdr = 5

    def run(self):
        self.run_loop()

    def set_cdr(self, cdr):
        self.cdr = cdr

    def get_tasks(self):
        tasks = []
        for attr in dir(self):
            if attr.startswith("task_"):
                # 获取协程函数
                coro_func = getattr(self, attr)
                # 调用协程函数获取协程对象
                coro = coro_func()
                tasks.append(coro)

        return tasks

    def run_loop(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            # 获取协程对象列表
            coroutines = self.get_tasks()
            # 将协程对象转换为任务对象
            tasks = [loop.create_task(coro) for coro in coroutines]
            # 等待所有任务完成
            loop.run_until_complete(asyncio.wait(
                tasks, return_when=asyncio.ALL_COMPLETED))
        except Exception as e:
            print(f"Error in run_loop: {e}")
        finally:
            loop.close()

    async def loop_press(self, key, interval):
        while True:
            if BOT_SWITCH.is_set():
                await asyncio.sleep(interval)
                self.keyboard.press(key)
                self.keyboard.release(key)
            else:
                # 等待启用信号，避免递归
                BOT_SWITCH.wait()

    async def loop_press_with_cd(self, key, interval):
        if interval <= 0.1:
            return await self.loop_press(key, interval)

        cd = interval * (100 - self.cdr) / 100
        while True:
            if BOT_SWITCH.is_set():
                await asyncio.sleep(0.1)
                self.keyboard.press(key)
                self.keyboard.release(key)
                await asyncio.sleep(cd - 0.1)
            else:
                # 等待启用信号，避免递归
                BOT_SWITCH.wait()

    async def loop_mouse_press(self, key: mouse.Button, interval: float):
        while True:
            if BOT_SWITCH.is_set():
                # 按下shift键 + 左键
                self.keyboard.press(keyboard.Key.shift)
                # 短暂延迟确保按键被正确识别
                await asyncio.sleep(0.05)
                # 按下左键
                self.mouse.press(key)
                # 短暂延迟
                await asyncio.sleep(0.05)
                # 先释放左键
                self.mouse.release(key)
                # 再释放shift键
                self.keyboard.release(keyboard.Key.shift)
                # 每4秒执行一次
                await asyncio.sleep(interval)
            else:
                # 等待启用信号，避免递归
                BOT_SWITCH.wait()

    async def loop_mouse_press_with_cd(self, key, interval):
        if interval <= 0.1:
            cd = 0.1
        else:
            cd = interval * (100 - self.cdr) / 100

        return await self.loop_mouse_press(key, cd)
