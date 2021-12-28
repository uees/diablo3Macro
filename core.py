import asyncio
import threading

BOT_SWITCH = threading.Event()


class BaseAsyncBot(threading.Thread):

    def run(self):
        self.run_loop()

    def get_tasks(self):
        tasks = []
        for attr in dir(self):
            if attr.startswith("task_"):
                tasks.append(getattr(self, attr)())

        return tasks

    def run_loop(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = self.get_tasks()
        loop.run_until_complete(asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED))
        loop.close()
