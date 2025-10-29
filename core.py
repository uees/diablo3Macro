import asyncio
import threading

BOT_SWITCH = threading.Event()
RING_SWITCH = threading.Event()


class BaseAsyncBot(threading.Thread):

    def run(self):
        self.run_loop()

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
